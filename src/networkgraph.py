import csv
from itertools import combinations
import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite
from sknetwork.data import from_edge_list
from sknetwork.clustering import Louvain
from nxviz import CircosPlot, BasePlot
import nxviz as nv
import math
import json

G = nx.Graph()

with open('./data/doi_joined.json') as terms:
    graph = json.load(terms)

graph = [i for i in graph if i['doi'] != '']

dois = [i['doi'] for i in graph]

resources = set()

for i in graph:
    for j in i['resources']:
        resources.add(j)

G.add_nodes_from(dois, bipartite = 0)
G.add_nodes_from(resources, bipartite = 1)

for i in graph:
    for j in i['resources']:
        G.add_edges_from([(i['doi'], j)])

# We have a bipartite graph.
nx.is_connected(G)

edge_list=[(e[0],e[1], 1) for e in G.edges(data=True)]
bgraph = from_edge_list(edge_list, bipartite=True)

names = bgraph.names
names_row = bgraph.names_row
names_col = bgraph.names_col
biadjacency=bgraph.biadjacency

#Louvain with Barber modularity
louvain = Louvain()
louvain.fit(biadjacency,force_bipartite=True)
labels_row = louvain.labels_row_
labels_col = louvain.labels_col_

#Add the label to the graph
partition={}
for i,n_r in enumerate(names_row):
    partition[n_r]=labels_row[i]
for i,n_c in enumerate(names_col):
    partition[n_c]=labels_col[i]
    
nx.set_node_attributes(G, partition, 'community_louvain')

resource_nodes = [node for node in G.nodes() if G._node[node]['bipartite'] == 1]
paper_nodes = [node for node in G.nodes() if G._node[node]['bipartite'] == 0]

resource_centrality = [node for node in nx.bipartite.degree_centrality(G, resource_nodes).items() if not node[0].startswith("1")]

sorted(resource_centrality, key=lambda x: x[1], reverse=True)[:5]

resource_graph = nx.bipartite.projection.projected_graph(G, resource_nodes)

for n, d in resource_graph.nodes(data=True):
    resource_graph._node[n]['neighbors_count'] = len(list(resource_graph.neighbors(n)))

options = {"edgecolors": "tab:gray", "node_size": 700, "alpha": 0.7}
label_options = {"ec": "k", "fc": "white", "alpha": 0.7}

pos = nx.spring_layout(resource_graph, seed=3113794652)  # positions for all nodes

fig = plt.figure(figsize=(6, 9))

nx.draw_networkx_edges(resource_graph, pos, alpha = 0.1)
nx.draw_networkx_nodes(resource_graph, pos, **options)
nx.draw_networkx_labels(resource_graph, pos, font_size=14, bbox=label_options)
plt.show()


# function to create node colour list
def create_community_node_colors(graph, communities):
    number_of_colors = len(communities)
    colors = ["#D4FCB1", "#CDC5FC", "#FFC2C4", "#F2D140", "#BCC6C8"][:number_of_colors]
    node_colors = []
    for node in graph:
        current_community_index = 0
        for community in communities:
            if node in community:
                node_colors.append(colors[current_community_index])
                break
            current_community_index += 1
    return node_colors


# function to plot graph with node colouring based on communities
def visualize_communities(graph, communities, i):
    node_colors = create_community_node_colors(graph, communities)
    modularity = round(nx.community.modularity(graph, communities), 6)
    title = f"Community Visualization of {len(communities)} communities with modularity of {modularity}"
    pos = nx.spring_layout(graph, k=0.3, iterations=50, seed=2)
    plt.subplot(3, 1, i)
    plt.title(title)
    nx.draw(
        graph,
        pos=pos,
        node_size=1000,
        node_color=node_colors,
        with_labels=True,
        font_size=20,
        font_color="black",
    )


communities = list(nx.algorithms.community.girvan_newman(resource_graph))

# Plot graph with colouring based on communities
visualize_communities(resource_graph, communities[0], 1)
visualize_communities(resource_graph, communities[3], 2)
plt.show()