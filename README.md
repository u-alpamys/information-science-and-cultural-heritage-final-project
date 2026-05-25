# Information Science and Cultural Heritage — Final Project

**Alpamys Ualbekov · DHDK 2025–26**

This project takes the English Wikipedia article on *Pulp Fiction* (1994) as its primary source and documents the full pipeline from plain text to structured linked data.

## Structure

```
├── index.html                          — project website
├── knowledge-organisation/
│   ├── theoretical_model.png           — entity mind map
│   ├── theoretical_model.graphml
│   ├── conceptual_model.png            — Graffoo ontology diagram
│   └── conceptual_model.graphml
└── knowledge-representation/
    ├── tei/
    │   └── pulp_fiction.xml            — XML/TEI encoding of the article
    ├── html/
    │   └── pulp_fiction.html           — HTML rendering of the TEI document
    ├── rdf/
    │   └── pulp_fiction.ttl            — RDF dataset (Turtle)
    ├── graph/
    │   └── knowledge_graph.png         — knowledge graph visualization
    └── scripts/
        ├── xml2html.py                 — TEI to HTML transformation
        ├── style.xslt                  — XSLT stylesheet
        ├── tei2rdf.py                  — TEI to RDF conversion
        └── graph_visualizer.py         — graph rendering
```

## Overview

**Domain study** — Nineteen named entities were identified across six categories (persons, places, organizations, events, concepts, bibliographic resources) and reconciled to authority files (Wikidata, VIAF).

**Knowledge organisation** — A theoretical model maps entity relations in natural language. A conceptual model formalizes those relations using Schema.org, Dublin Core Terms, and SKOS, represented in Graffoo notation.

**Knowledge representation** — The article is encoded in XML/TEI with inline entity markup. An XSLT stylesheet transforms the document to HTML. A Python script derives an RDF dataset from the TEI header, serialized as Turtle. The dataset is rendered as a network graph.

## Dependencies

```
pip install lxml rdflib networkx matplotlib
```
