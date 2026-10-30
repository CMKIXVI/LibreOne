from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class GraphNode:
    id: str
    capability: str

@dataclass(frozen=True, slots=True)
class GraphEdge:
    source: str
    target: str

@dataclass(frozen=True, slots=True)
class ExecutionGraph:
    nodes: tuple[GraphNode, ...]
    edges: tuple[GraphEdge, ...]
