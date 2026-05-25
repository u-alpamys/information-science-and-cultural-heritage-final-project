from rdflib import Graph
from rdflib.namespace import RDF
import networkx as nx
import matplotlib.pyplot as plt

graph = Graph()
graph.parse("pulp_fiction.ttl", format="turtle")

nx_graph = nx.DiGraph()

def get_label(uri):
    uri = str(uri)
    if "#" in uri:
        return uri.split("#")[-1]
    return uri.split("/")[-1]

labels = {
    "Q104123": "Pulp Fiction",
    "37054403": "Quentin Tarantino",
    "85099020": "Roger Avary",
    "117713609": "John Travolta",
    "14970417": "Uma Thurman",
    "84357496": "Samuel L. Jackson",
    "85362156": "Bruce Willis",
    "1066569": "Lawrence Bender",
    "249149066546665601337": "Sally Menke",
    "69138003": "Andrzej Sekuła",
    "131570070": "Miramax Films",
    "Q300323": "A Band Apart",
    "153908908": "Jersey Films",
    "151962300": "Library of Congress",
    "Q65": "Los Angeles",
    "Q39984": "Cannes",
    "Q961852": "1994 Cannes Film Festival",
    "Q857001": "67th Academy Awards",
    "Q8740": "Vietnam War",
    "Q2894685": "Nonlinear narrative",
    "Q7234396": "Postmodern film",
    "Q53094": "Black comedy",
    "Q459290": "Independent film",
    "Q865585": "Pulp magazine",
    "Q1607955": "Soundtrack",
}

for subject, predicate, obj in graph:
    if predicate == RDF.type:
        continue

    subject_label = get_label(subject)
    predicate_label = get_label(predicate)
    obj_label = get_label(obj)

    nx_graph.add_edge(subject_label, obj_label, label=predicate_label)

plt.figure(figsize=(20, 15))

pos = nx.spring_layout(nx_graph, k=2, seed=42)

nx.draw_networkx_nodes(nx_graph, pos, node_color="#C8FF00", node_size=2000)

nx.draw_networkx_edges(nx_graph, pos, arrows=True, arrowsize=20, edge_color="#E7E8E0", node_size=2000, arrowstyle="-|>")

nx.draw_networkx_labels(nx_graph, pos, labels=labels, font_size=8, font_color="#0E0E0E")

edge_labels = nx.get_edge_attributes(nx_graph, "label")
nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels, font_size=6, font_color="#666666")

plt.axis("off")
plt.tight_layout()
plt.savefig("knowledge_graph.png", dpi=150, bbox_inches="tight")
plt.close()

print("Done!")