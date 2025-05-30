-- This file contains only "core" UGW functions and does not consider the problem of parallelizing pairwise across many problems.
module unbalanced_gw_core (M: real) = {
  import "common"
  import "scaling_unbalanced"
  import "gw"

  open common M
  module sinkhorn = scaling_unbalanced M
  module gw = gromov_wasserstein M
  type t = M.t

  -- Definition 1 in section 2.1
 def L rho1 rho2 X mu Y nu P =
    (gw.GW_cost X Y P) M.+
    (let P1  = map M.sum P in
     rho1 M.* (KL2 (tensor P1 P1) (tensor mu mu))) M.+
    (let P2  = map M.sum (transpose P) in
     rho2 M.* (KL2 (tensor P2 P2) (tensor nu nu)))

  def F [n][m] (A : [n][n]t) (B :[m][m]t) pi gamma mu nu rho1 rho2 =
    gw.GW_cost' A B pi gamma M.+
    rho1 M.* KL2 (tensor (map M.sum pi)
			  (map M.sum gamma)) (tensor mu mu) M.+
    rho2 M.* KL2 (tensor (map M.sum (transpose pi))
			  (map M.sum (transpose gamma))) (tensor nu nu)
  -- An algebraic theorem (that we should test for correctness in the implementation!) is that
  -- D_phi rho1 (\pi1 \otimes \gamma1 ) (\mu\otimes\mu) ==
  -- rho1 * [ (KLu pi1 mu) * (m gamma) + (KLu gamma1 mu) * (m pi) - (m pi) * (m gamma) + (m mu)*(m mu)
  -- where m is the mass function.
  -- Of course we have the same for
  -- D_phi rho1 (\pi2 \otimes \gamma2 ) (\nu\otimes\nu).

  -- This is the thing we are trying to optimize.
  def Feps (r : sinkhorn.otp[][]) A B pi gamma  =
    F A B pi gamma r.mu r.nu r.rho1 r.rho2
      M.+ r.eps M.* KL4 pi gamma r.mu r.nu

  -- This should agree with Feps when pi = gamma.
  def UGW_eps (r : sinkhorn.otp[][]) X Y =
    let a =  (L r.rho1 r.rho2 X r.mu Y r.nu r.C) in
    let b =  ((KL4 r.C r.C r.mu r.nu)) in
    M.fma b r.eps a

  -- See UGW_eps_1 below.
  def compensate  [m][n] (r : sinkhorn.otp[m][n]) =
    let m_mu = (M.sum r.mu) in
    let m_nu = (M.sum r.nu) in
    let m_mu_nu = m_mu M.* m_nu in
    M.(r.rho1 * m_mu * m_mu +
       r.rho2 * m_nu * m_nu
        + r.eps * m_mu_nu * m_mu_nu
      )

  -- This breaks UGW into a sum of a variable and a constant depending only on mu and nu.
  -- It should be the same as UGW_eps.
  -- We should test this.
  def UGW_eps_1 [m][n] (r: sinkhorn.otp[m][n]) (X: [m][m]M.t) (Y: [n][n]M.t) =
    let gw_cost = (gw.GW_cost X Y r.C) in
    let pi_X = map M.sum r.C in
    let mP = M.sum pi_X in
    let pi_Y = map M.sum (transpose r.C) in
    let c_eps = r.eps M.* KLu2 r.C r.mu r.nu in
    let c_rho1 = r.rho1 M.* KLu pi_X r.mu in
    let c_rho2 = r.rho2 M.* KLu pi_Y r.nu in
    let x =
      M.(gw_cost + (i64 2 * (c_eps +
			    c_rho1 + c_rho2) * mP) - ((mP * mP) * (r.eps +
							  r.rho1 + r.rho2)))
    in
    x M.+ compensate r

  -- The UGW cost together with the constituent costs.
  def UGW_cost_arr (r : sinkhorn.otp[][]) X Y =
    [gw.GW_cost X Y r.C,
     let P1 = map M.sum r.C in KL2 (tensor P1 P1) (tensor r.mu r.mu),
     let P2 = map M.sum (transpose r.C) in KL2 (tensor P2 P2) (tensor r.nu r.nu),
     KL4 r.C r.C r.mu r.nu,
     UGW_eps r X Y]

  -- Feps <= UGW_eps
  -- Local linearization of the UGW gradient descent, cost matrix part
  -- X is a distance matrix, mu is a positive measure
  -- Y is a distance matrix, nu is a positive measure
  -- gamma is a measure on the product space.
  -- This is the expression c^\varepsilon_\gamma from Proposition 4.
  def ll_cost_matrix (r : sinkhorn.otp[][]) X Y =
    let c1 = gw.L2_otimes_T X Y r.C in
    let a1 = r.rho1 M.* KLu (map M.sum r.C) r.mu in
    let a2 = r.rho2 M.* KLu (map M.sum (transpose r.C)) r.nu in
    let a3 = r.eps M.* KLu2 r.C r.mu r.nu in
    map (\v -> add_vs v (a1 M.+ a2 M.+ a3)) c1

  -- Because of a convention change between the unbalanced Gromov-Wasserstein paper and
  -- the sinkhorn scaling paper, we need to modify the cost matrix slightly.
  -- This is the cost matrix which we actually want to use in the UGW descent loop.
  def ll_cost_matrix' (r: sinkhorn.otp[][]) X Y =
    let mass_gamma = map M.sum r.C |> M.sum in
    let epslgmu = map M.log r.mu |> map (M.* (r.eps M.* mass_gamma)) in
    let epslgnu = map M.log r.nu |> map (M.* (r.eps M.* mass_gamma)) in
    ll_cost_matrix r X Y |>
    (\a -> map2 sub_vs a epslgmu) |> transpose |> (\a -> map2 sub_vs a epslgnu) |> transpose

  -- This term describes the difference between the loss of the local linearization problem
  -- generated by ll_cost_matrix', and the value of
  -- F(P,Q) +\varepsilon KL(P\otimes Q | (\mu\otimes\nu)^2 ).
  -- Note that although p contains a field "C", the cost matrix,
  -- this does not play any role in the computation.
  def ll_error_term [n][m] Q (p :sinkhorn.otp[n][m]) =
    let m_mu = M.sum p.mu in
    let m_nu = M.sum p.nu in

    let t1 = (map M.sum Q |> M.sum |> M.neg) M.*
	     (p.rho1 M.* m_mu M.+ p.rho2 M.* m_nu) in
    let m_mu2 = m_mu M.* m_mu in
    let m_nu2 = m_nu M.* m_nu in
    let t2 = p.rho1 M.* m_mu2 M.+ p.rho2 M.* m_nu2 M.+ p.eps M.* m_mu2 M.* m_nu2 in
    t1 M.+ t2

  -- This function is not used but is provided as a form of documentation
  -- which explains the meaning of ll_error_term Q p.
  -- If the implementation is correct, this function should return
  -- the same answer as Feps (and as UGW_eps when P = Q)
  -- so it demonstrates how the quadratic problem of minimizing UGW cost
  -- is reduced to the "local linearization" which can be solved using
  -- the technique from the scaling_unbalanced paper.
  -- Note that Q is understood to be the "current" plan (it is needed
  -- to determine the linear cost matrix) and P is the plan "to be optimized"

  def alternate_ugw_cost [n][m] rho1 rho2 eps X (mu : [n]t) Y (nu : [m]t) P Q =
  -- let otp = {rho1, rho2, eps, mu, nu, C=P} in
  --let massp = map f64.sum P |> f64.sum in
  let massq = map M.sum Q |> M.sum in
  let p = { rho1, rho2, eps, mu, nu, C = Q} in
  let c_eps_gamma = ll_cost_matrix' p X Y
  in
  massq M.* M.(frobenius (map (map (/ massq)) c_eps_gamma) P +
	   (rho1 * (KL (map sum P) mu ) +
	   (rho2 * (KL (map sum (transpose P)) nu)) +
	   (eps * H P)))
  M.+ ll_error_term Q p

  -- We define the first iteration of the unbalanced GW
  -- distance slightly differently,
  -- the primary difference between this and the other function is
  -- that in the initial step we assume that
  def unbalanced_gw_init_step [n][m] (a : sinkhorn.otp[][]) X Y params =
    let c_eps_gamma = ll_cost_matrix' a X Y in
    let mass_gamma = map M.sum a.C |> M.sum in
    --Cost matrix for the unbalanced linear OT problem
    let C = map (map (M./ mass_gamma)) c_eps_gamma in
    -- let _ = #[trace] map count_nan C in
    let (r : sinkhorn.otp [n][m]) = (a with C = C) in
    let (u1, v1, C') = sinkhorn.algo3 r params in

    let sumC' = map M.sum C' |> M.sum in
    (u1, v1, map (map (M.* (M.sqrt (mass_gamma M./ sumC')))) C')

  def unbalanced_gw_descent_step [n][m] (a : sinkhorn.otp[][]) X Y u v
    params =
    let c_eps_gamma = ll_cost_matrix' a X Y in
    let mass_gamma = (map M.sum a.C |> M.sum)
    -- Cost matrix for the unbalanced linear OT problem
    let C = map (map (M./ mass_gamma)) c_eps_gamma in
    let (r : sinkhorn.otp [n][m]) =
      { rho1 = a.rho1, rho2 = a.rho2, eps = a.eps, mu = a.mu, nu = a.nu, C = C }
    in
    let (u1, v1, C') =
      sinkhorn.algo4 r (replicate n one) u (replicate m one) v params in
    let sumC' = map M.sum C' |> M.sum in
    if sumC' M.> zero then (u1, v1, map (map (M.* (M.sqrt (mass_gamma M./ sumC')))) C')
    else (map (\_ -> zero) u1, map (\_ -> zero) v1, map (map (\_ -> zero)) C')

  type problem_data [n][m] = {
      X : [n][n]t,
      mu : [n]t,
      Y : [m][m]t,
      nu : [m]t,
      rho1 : t,
      rho2 : t,
      eps : t
  }

  -- def ugw_loop_structure [m][n]
  -- (initialization_function : (sinkhorn.otp[m][n]) -> [m][n]M.t -> [m][n]M.t -> params -> [m]M.t * [n]M.t * [m][n]M.t)
  -- (update : (sinkhorn.otp[m][n]) -> [m][n]M.t -> [m][n]M.t -> params -> [m]M.t * [n]M.t * [m][n]M.t))

  def unbalanced_gw_init [n][m] (r : sinkhorn.otp[][]) X Y params tol_outerloop =
    let (u0, v0, p0) =
       unbalanced_gw_init_step r X Y params in
    let update (u: [n]t) (v:[m]t) (p: [n][m]t) : ([n]t, [m]t, [n][m]t) =
      unbalanced_gw_descent_step ((r with C = p) : sinkhorn.otp[][]) X Y u v params
    in
    loop (c0 : [n][m]t, u :[n]t, v:[m]t, c1:[n][m]t) = (r.C, u0, v0, p0)
    while sinkhorn.any2 (sinkhorn.any2 (\x y -> not (sinkhorn.ratio_err_ok tol_outerloop x y))) c0 c1
    -- while any (M.>= tol_outerloop) ((map2 err c0 c1)) -- && ((any (any (M.> zero))) c1)
    do
    let (u', v', c2) = update u v c1 in
    (c1, u', v', c2)

  def unbalanced_gw rho1 rho2 eps X mu Y nu =
    unbalanced_gw_init {rho1, rho2, eps, mu, nu, C = (tensor mu nu) } X Y

  -- This module implements a naive gradient descent along L, using armijo line search.
  -- It does not take the approach of attempting to optimize for each variable simultaneously.
  module gradient_descent = {

  -- The gradient of the marginal components
  def nabla_marginal [m][n] (distr :[m]t) (P: [m][n]t) : [m][n]t =
    let massP = map M.sum P |> M.sum in
    let pi_X = (map M.sum P) in
    let a = M.((i64 2) * massP) in
    map M.(\b -> fma a b (i64 2 * (KLu pi_X distr - massP))) (map2 klu' pi_X distr)
    |> map (replicate n)

  def nabla_L [m][n] rho1 rho2 (A: [m][m]t) (mu :[m]t) (B: [n][n]t) (nu: [n]t) (P: [m][n]t) =
    let nabla_G = gw.nabla_G A B P in
    let marginal_1 = nabla_marginal mu P in
    let marginal_2 = nabla_marginal nu (transpose P) |> transpose in
    map2 (map2 (\a c -> M.fma a rho1 c)) marginal_1 nabla_G |>
    map2 (map2 (\a c -> M.fma a rho2 c)) marginal_2

  def nabla_UGW_eps [m][n] (r: sinkhorn.otp[][])
      (A: [m][m]t) (B: [n][n]t) (P: [m][n]t)
      : [m][n]t =
    -- \nabla UGW_eps = \nabla_L + eps * \nabla KL4.
    map2 (map2 (\c a -> M.fma a r.eps c)) (nabla_L r.rho1 r.rho2 A r.mu B r.nu P) (nabla_KL4 P r.mu r.nu)
    |> map (map M.(\a -> max (neg (f64 1e100)) a))

  def nabla_UGW_eps_debug [m][n] rho1 rho2 epsilon
      (A: [m][m]t) (mu :[m]t) (B: [n][n]t) (nu: [n]t) (P: [m][n]t) (diff: [m][n]t)
      : t =
    let mytrace a b = if a M.< M.inf then b else M.inf
    in
    let P' =  (map2 (map2 (M.+)) P diff) in
    let gw_cost =
      let current_gw_loss = trace (gw.GW_cost A B P) in
      let new_gw_loss = trace (gw.GW_cost A B P') in
      let linear_loss_diff = trace (frobenius (gw.nabla_G A B P) diff) in
      let guess_ratio_gw =
	M.( (new_gw_loss - current_gw_loss)/linear_loss_diff) in
      let guess_ratio_gw = #[trace] guess_ratio_gw in
      mytrace guess_ratio_gw new_gw_loss
    in

    let margin_A =
      let current_marginal_loss_A = KL2 (tensor (map M.sum P) (map M.sum P)) (tensor mu mu) in
      let new_marginal_loss_A = KL2 (tensor (map M.sum P') (map M.sum P')) (tensor mu mu) in
      let linear_loss_diff = frobenius (nabla_marginal mu P) diff in
      let guess_ratio_margin =
	M.((new_marginal_loss_A - current_marginal_loss_A)/linear_loss_diff) in
      let guess_ratio_margin = #[trace] guess_ratio_margin in
      mytrace guess_ratio_margin (rho1 M.* new_marginal_loss_A )
    in

    let margin_B =
      -- let current_marginal_loss_B = KL (map M.sum (transpose P)) nu in
      let current_marginal_loss_B = KL2 (tensor (map M.sum (transpose P)) (map M.sum (transpose P))) (tensor nu nu) in
      let new_marginal_loss_B = KL2 (tensor (map M.sum (transpose P')) (map M.sum (transpose P'))) (tensor nu nu) in
      -- let new_marginal_loss_B = KL (map2 (M.+) (map M.sum (transpose P)) (map M.sum (transpose diff))) nu in
      let linear_loss_diff = frobenius (nabla_marginal nu (transpose P)) (transpose diff) in
      let guess_ratio_margin =
	M.((new_marginal_loss_B - current_marginal_loss_B)/linear_loss_diff) in
      let guess_ratio_margin = #[trace] guess_ratio_margin in
      mytrace guess_ratio_margin (rho2 M.* new_marginal_loss_B)
    in

    let KL4_div =
      let current_loss_KL4 = (KL4 P P mu nu) in

      let new_loss_KL4 = (KL4 P' P' mu nu) in
      let gradient = (nabla_KL4 P mu nu) in
      let linear_loss_diff = frobenius gradient diff in
      let guess_ratio = M.((new_loss_KL4 - current_loss_KL4)/linear_loss_diff) in
      mytrace (#[trace] guess_ratio) (epsilon M.* new_loss_KL4)
    in

    let x = gw_cost M.+ margin_A M.+ margin_B M.+ KL4_div in
    let other_val = UGW_eps {rho1, rho2, eps=epsilon, mu, nu, C = (map2 (map2 (M.+)) P diff) } A B in
    mytrace
    (#[trace] other_val)
    (#[trace] x)

  def safe_starting_diff [m][n] (point: [m][n]M.t) (step: [m][n]M.t) : [m][n]M.t =
      if M.(map2 (map2 (+)) point step) |> map (all (M.i64 0 M.<)) |> reduce (&&) true then step else
      let ratios = map2 M.(map2 (\a b -> if b >= i64 0 then i64 1 else neg a / b)) point step in
      let min_ratio = map M.minimum ratios |> M.minimum in
      map M.(map (\b -> (min_ratio * b/(i64 2)))) step

    let safe_starting_diff' [m][n] (point: [m][n]M.t) (step: [m][n]M.t) : [m][n]M.t =
      let f x dx = M.(
		     if x + dx >= i64 0 then dx else
		       neg x / (i64 2)
		   )
      in
      map2 (map2 f) point step

  type armijo_params = { tau: M.t, c: M.t }

  -- A, B: metric spaces
  -- mu, nu: measures
  -- tol_outerloop: stopping criterion expressed as a distance between successive matrices
    def naive_descent_init [m][n] rho1 rho2 eps
       (A: [m][m]t) (mu :[m]t) (B: [n][n]t) (nu: [n]t) (P: [m][n]M.t) (params: armijo_params)
    (tol_outerloop: M.t)
    =
--      let loss_fn P = main_loss_function {rho1, rho2, eps, mu, nu, C = P} A B in
      let loss_fn P = UGW_eps_1 {rho1, rho2, eps, mu, nu, C = P} A B in
      -- let loss_fn = nabla_UGW_eps_debug rho1 rho2 eps A mu B nu in
      let gradient_fn = nabla_UGW_eps {rho1, rho2, eps, mu, nu, C = P} A B in
      let descent_direction P =
  	let diff =
	  let gradient = gradient_fn P in
	  let diff_0 = (map (map M.neg) gradient) in
	  let scaling_const = M.(i64 n) M./ (M.sum (map max_abs gradient)) in
	  -- let gradient = (map (map (M.* c)) a) in
	  safe_starting_diff' P (map (map (M.* scaling_const)) diff_0)
	in
	assert (all M.(all (\a -> a > i64 0)) (map2 M.(map2 (+)) diff P)) diff
      in
      let diff_of P current_loss =
	      armijo_line_search loss_fn
	      current_loss P (descent_direction P)
			   (\A B -> frobenius (gradient_fn A) B)
			   params.tau params.c
      in
      let (_, final_loss, _) =
	loop (diff, current_loss, P) =
	  let l = (UGW_eps {C = P, rho1, rho2, eps, mu, nu} A B) in
	  let (diff, l, _) = (diff_of P l) in
	  (diff, l, P)
	while
	  any (M.> tol_outerloop) (map (M.maximum) (map (map M.abs) diff))
	do
  	let P' = (map2 (map2 (M.+)) P diff) in
  	-- let min = M.(f64 1e30 * minimum (map M.minimum P')) in
	-- let mass = M.sum (map M.sum P') in
	let small_count = P' |> (map (map (\a -> if a M.< M.f64 1e-10 then 1 else 0)))
			  |> map i32.sum |> i32. sum
	in
  	let current_loss = if (M.i32 small_count)
			      M.> M.(neg (i64 1)) then current_loss else (M.i64 0) in
  	let (diff, l, _) = diff_of P' current_loss in
	(diff, l, P')
      in
      final_loss -- M.+ compensate {rho1, rho2, eps, mu, nu, C = P}

    def naive_descent [m][n] rho1 rho2 eps
       (A: [m][m]t) (mu :[m]t) (B: [n][n]t) (nu: [n]t) (params: armijo_params) tol_outerloop =
      naive_descent_init rho1 rho2 eps A mu B nu (tensor mu nu) params tol_outerloop
  }

  module armijo = {

    def descent [n][m] (a : sinkhorn.otp[][]) X Y u v params initial_loss =
      let c_eps_gamma = ll_cost_matrix' a X Y in
      let mass_gamma = (map M.sum a.C |> M.sum) in
      -- Cost matrix for the unbalanced linear OT problem
      let C = map (map (M./ mass_gamma)) c_eps_gamma in
      let (r : sinkhorn.otp [n][m]) =
	{ rho1 = a.rho1, rho2 = a.rho2, eps = a.eps, mu = a.mu, nu = a.nu, C = C }
      in
      let (u1, v1, C') =
	sinkhorn.algo4 r (replicate n one) u (replicate m one) v params in
      let sumC' = map M.sum C' |> M.sum in
      if sumC' M.> zero then
      let x = map (map (M.* (M.sqrt (mass_gamma M./ sumC')))) C' in
      let (diff, loss, _) =
	let loss_fn = (\P -> (UGW_eps_1 (a with C = P) X Y) ) in
	let gradient_fn = gradient_descent.nabla_UGW_eps a X Y in
      	let diff = (map2 (map2 (M.-)) x a.C) in
      	armijo_line_search loss_fn (initial_loss) a.C diff
      			   (\A B -> gradient_fn A |> frobenius B) (M.f64 0.5) (M.f64 0.5)
      in
      (u1, v1, map2 (map2 (M.+)) a.C diff, loss)
    else
      (map (\_ -> zero) u1, map (\_ -> zero) v1, map (map (\_ -> zero)) C' , M.i64 0)

    def ratio_err_ok tol a b =
      M.(a * (one + tol) >= b && b * (one + tol) >= a)

    def init [n][m] (r : sinkhorn.otp[][]) X Y params tol_outerloop =
      let (u0, v0, p0) =
	      unbalanced_gw_init_step r X Y params in
       let initial_loss = UGW_eps_1 r X Y in
      let update (u: [n]t) (v:[m]t) (p: [n][m]t) (loss: t): ([n]t, [m]t, [n][m]t, t)  =
	      descent ((r with C = p) : sinkhorn.otp[][]) X Y u v params loss
      in
      let (_, _,_, final_plan, _) =
        loop (c0 : [n][m]t, u :[n]t, v:[m]t, c1:[n][m]t, loss) = (r.C, u0, v0, p0, initial_loss)
        while (sinkhorn.any2 (sinkhorn.any2 (\x y -> not (ratio_err_ok tol_outerloop x y)))) c0 c1 && ((any (any (M.> zero))) c1) do
        let (u', v', c2, loss) = update u v c1 loss in (c1, u', v', c2, loss)
      in UGW_cost_arr (r with C = final_plan) X Y

    def main rho1 rho2 eps X mu Y nu =
      init {rho1, rho2, eps, mu, nu, C = (tensor mu nu) } X Y
  }
}
