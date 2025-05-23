from _typeshed import Incomplete
from networkx.classes.graph import Graph

class MultiGraph(Graph):
    edge_key_dict_factory: Incomplete
    def to_directed_class(self): ...
    def to_undirected_class(self): ...
    def __init__(self, incoming_graph_data: Incomplete | None = ..., multigraph_input: Incomplete | None = ..., **attr) -> None: ...
    def adj(self): ...
    def new_edge_key(self, u, v): ...
    def add_edge(self, u_for_edge, v_for_edge, key: Incomplete | None = ..., **attr): # type: ignore[override]
        ...
    def add_edges_from(self, ebunch_to_add, **attr): ...
    def remove_edge(self, u, v, key: Incomplete | None = ...) -> None: ...
    def remove_edges_from(self, ebunch) -> None: ...
    def has_edge(self, u, v, key: Incomplete | None = ...): ...
    def edges(self): ...
    def get_edge_data(self, u, v, key: Incomplete | None = ..., default: Incomplete | None = ...): # type: ignore[override]
        ...
    def degree(self): ...
    def is_multigraph(self): ...
    def is_directed(self): ...
    def copy(self, as_view: bool = ...): ...
    def to_directed(self, as_view: bool = ...): ...
    def to_undirected(self, as_view: bool = ...): # type: ignore[override]
        ...
    def number_of_edges(self, u: Incomplete | None = ..., v: Incomplete | None = ...): ...
