"""
topo_indices.py

This module contains functions to calculate Topological Indices
of chemical molecule.

Author: Anthuvan Joseph Benjamin
Copyright (c) 2025 Anthuvan Joseph Benjamin
Free for academic/research use under MIT license
Commercial use requires paid license
"""

import networkx as nx

def first_zagreb(G: nx.Graph) -> float:
    """
    First Zagreb index: sum of squared degrees of all nodes.

    Parameters:
        G (nx.Graph): A NetworkX graph representing the molecule.

    Returns:
        float: First Zagreb index.
    """
    return sum(deg**2 for _, deg in G.degree())


def randic(G: nx.Graph) -> float:
    """
    Randić index: sum over edges of 1/sqrt(d(u) * d(v)).

    Parameters:
        G (nx.Graph): A NetworkX graph representing the molecule.

    Returns:
        float: Randić index.
    """
    return sum(1.0 / (G.degree(u) * G.degree(v))**0.5 for u, v in G.edges())
