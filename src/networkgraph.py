import networkx as nx
import csv
from itertools import combinations
import matplotlib.pyplot as plt
import math

G = nx.Graph()

papers = []
dbs = []

with open('./data/merged_records.csv', 'r', encoding='UTF-8') as terms:
    reader = csv.reader(terms)
    for i in reader:
        dbs.append([j.strip() for j in i])

with open('./data/repohits.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    for i in reader:
        db = [j[0] for j in dbs].index(i[3])
        papers.append({'doi': i[0],
                       'snippet': i[1],
                       'title': i[2],
                       'database': dbs[db][1]})

# Remove all papers without a DOI:
papers = [i for i in papers if i.get('doi') or '' != '']
doi_list = [i.get('doi') for i in papers]
doi_set = set(doi_list)
doi_count = {i: doi_list.count(i) for i in doi_set if doi_list.count(i) > 1}
clean_dois = set(doi_count.keys())

clean_papers = [i for i in papers if i.get('doi') in clean_dois]

dataresources = set([i.get('database') for i in papers])

G.add_nodes_from(dataresources)
dois = []

j = 0

for i in clean_papers:
    j = j + 1
    if i.get('doi') not in [i.get('doi') or '' for i in dois]:
        dois.append({'doi': i.get('doi'), 'resource': set(i.get('database'))})
    else:
        doi_loc = [j.get('doi') for j in dois].index(i.get('doi'))
        dois[doi_loc]['resource'].add(i.get('database'))
    if j % 1000 == 0:
        print(j)

for i in dois:
    if len(i.get('resource')) > 1:
        combs = list(combinations(i.get('resource'), 2))
        for j in combs:
            if j[0] != j[1]:
                if j in G.edges:
                    G.edges[j[0], j[1]]['weight'] = G.edges[j]['weight'] + 1
                else:
                    G.add_edge(j[0], j[1], weight = 1)

weights = [math.sqrt(G[u][v]['weight']) for u,v in G.edges()]

subax1 = plt.subplot(111)
nx.draw(G, nx.kamada_kawai_layout(G), with_labels=True, edge_color="tab:red", font_weight='bold')
plt.show()

# Betweenness
# remove randomly selected nodes (to make example fast)
# largest connected component
components = nx.connected_components(G)
largest_component = max(components, key=len)
H = G.subgraph(largest_component)

# compute centrality
centrality = nx.betweenness_centrality(G, endpoints=True, weight = 'weight')

# compute community structure
lpc = nx.community.label_propagation_communities(G)
community_index = {n: i for i, com in enumerate(lpc) for n in com}

#### draw graph ####
fig, ax = plt.subplots(figsize=(20, 15))
pos = nx.spring_layout(G, k=0.15, seed=4572321)
node_color = [community_index[n] for n in G]
node_size = [v * 20000 for v in centrality.values()]
nx.draw_networkx(
    G,
    pos=pos,
    with_labels=False,
    node_color=node_color,
    node_size=node_size,
    edge_color="gainsboro",
    alpha=0.4,
)

# Title/legend
font = {"color": "k", "fontweight": "bold", "fontsize": 20}
ax.set_title("Gene functional association network (C. elegans)", font)
# Change font color for legend
font["color"] = "r"

ax.text(
    0.80,
    0.10,
    "node color = community structure",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)
ax.text(
    0.80,
    0.06,
    "node size = betweenness centrality",
    horizontalalignment="center",
    transform=ax.transAxes,
    fontdict=font,
)

# Resize figure for label readability
ax.margins(0.1, 0.05)
fig.tight_layout()
plt.axis("off")
plt.show()