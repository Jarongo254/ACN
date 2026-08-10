### Introduction

- Biological systems => Multiple interacting components
- Components:
    - Are not isolated
    - levels are affected by interactions
    - Form cohesive subsystems that perform specific tasks
    - Are spatially organized(cellular structures)
    - Their spatio-temporal interactions result in biological system features.

- Function of a component can be inferred from its interactions.
- Network theory and mathamatical modeling are used to analyze interactions.

### Network theory

Graph: abstract representation of a set of components(nodes/vertices) where some components are connected by edges.

Formal definition: Graph is a pair G = (V,E) such that E ⊆ {{u,v}|u,v ∈ V}.  V is the set of nodes and E is the set of edges.


In context of biology:
- nodes: genes, proteins, metabolites, regulatory elements, cells, species, etc.
- edges: interactions, relations, dependencies, etc.

Network can be:
- directed or undirected
- weighted or unweighted
- simple or multigraph
- etc.

Number of nodes n = |V(G)|
Number of edges m = |E(G)|

Parallel edges: two edges connect same pair of vertices. - paralel edges form a multi-edge
Loops: an edge connect a vertex to itself.
Simple graph: graph with no parallel edges and no loops.
Multigraph: graph with parallel edges and loops.

* Weighted directed hypergraph - Nodes connected to subset of nodes

#### Graph representation on computers
* Adjacency matrix - constant time to check for an edge between two nodes
  - A[u,v] = 1 if {u,v} ∈ E(G)
  - A[u,v] = 0 if {u,v} ∉ E(G)
  - Matrix is symmetric for a non directed graph but not for directed
* Incidence matrix
  - A[u,e] = 1 if u ∈ E(G)
  - A[u,e] = 0 if u ∉ E
* Adjacency list - To each node, a list of neighbors/connected nodes

#### Walk
Alternating sequence of nodes and edges
**Formally**: Let G = (V,E) be a simple graph. A sequence W = (v_1, e_1, v_2, ..e_k-1, v_k) with v_i ∈
V(G), 1 \leq i \leq k and e_i = {v_i, v_i+1} ∈ E(G), 1 \leq i \leq k-1 is called a walk
