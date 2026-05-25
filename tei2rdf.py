from lxml import etree
from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS

SCHEMA = Namespace("https://schema.org/")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
DCTERMS = Namespace("http://purl.org/dc/terms/")

graph = Graph()

graph.bind("schema", SCHEMA)
graph.bind("skos", SKOS)
graph.bind("dcterms", DCTERMS)

PulpFiction = URIRef("https://www.wikidata.org/wiki/Q104123")
Tarantino = URIRef("https://viaf.org/viaf/37054403")
Avary = URIRef("https://viaf.org/viaf/85099020")
Travolta = URIRef("https://viaf.org/viaf/117713609")
Thurman = URIRef("https://viaf.org/viaf/14970417")
Jackson = URIRef("https://viaf.org/viaf/84357496")
Willis = URIRef("https://viaf.org/viaf/85362156")
Bender = URIRef("https://viaf.org/viaf/1066569")
Menke = URIRef("https://viaf.org/viaf/249149066546665601337")
Sekula = URIRef("https://viaf.org/viaf/69138003")
Miramax = URIRef("https://viaf.org/viaf/131570070")
ABandApart = URIRef("https://www.wikidata.org/wiki/Q300323")
JerseyFilms = URIRef("https://viaf.org/viaf/153908908")
LibraryOfCongress = URIRef("https://viaf.org/viaf/151962300")
LosAngeles = URIRef("https://www.wikidata.org/wiki/Q65")
Cannes = URIRef("https://www.wikidata.org/wiki/Q39984")
Cannes1994 = URIRef("https://www.wikidata.org/wiki/Q961852")
Oscars = URIRef("https://www.wikidata.org/wiki/Q857001")
Vietnam = URIRef("https://www.wikidata.org/wiki/Q8740")
NonlinearNarrative = URIRef("https://www.wikidata.org/wiki/Q2894685")
PostmodernFilm = URIRef("https://www.wikidata.org/wiki/Q7234396")
BlackComedy = URIRef("https://www.wikidata.org/wiki/Q53094")
IndependentFilm = URIRef("https://www.wikidata.org/wiki/Q459290")
PulpMagazine = URIRef("https://www.wikidata.org/wiki/Q865585")
Soundtrack = URIRef("https://www.wikidata.org/wiki/Q1607955")

graph.add((PulpFiction, RDF.type, SCHEMA.Movie))

graph.add((Tarantino, RDF.type, SCHEMA.Person))
graph.add((Avary, RDF.type, SCHEMA.Person))
graph.add((Travolta, RDF.type, SCHEMA.Person))
graph.add((Thurman, RDF.type, SCHEMA.Person))
graph.add((Jackson, RDF.type, SCHEMA.Person))
graph.add((Willis, RDF.type, SCHEMA.Person))
graph.add((Bender, RDF.type, SCHEMA.Person))
graph.add((Menke, RDF.type, SCHEMA.Person))
graph.add((Sekula, RDF.type, SCHEMA.Person))

graph.add((Miramax, RDF.type, SCHEMA.Organization))
graph.add((ABandApart, RDF.type, SCHEMA.Organization))
graph.add((JerseyFilms, RDF.type, SCHEMA.Organization))
graph.add((LibraryOfCongress, RDF.type, SCHEMA.Organization))

graph.add((LosAngeles, RDF.type, SCHEMA.Place))
graph.add((Cannes, RDF.type, SCHEMA.Place))

graph.add((Cannes1994, RDF.type, SCHEMA.Event))
graph.add((Oscars, RDF.type, SCHEMA.Event))
graph.add((Vietnam, RDF.type, SCHEMA.Event))

graph.add((NonlinearNarrative, RDF.type, SKOS.Concept))
graph.add((PostmodernFilm, RDF.type, SKOS.Concept))
graph.add((BlackComedy, RDF.type, SKOS.Concept))
graph.add((IndependentFilm, RDF.type, SKOS.Concept))
graph.add((PulpMagazine, RDF.type, SKOS.Concept))

graph.add((Soundtrack, RDF.type, SCHEMA.MusicAlbum))

graph.add((PulpFiction, SCHEMA.director, Tarantino))
graph.add((PulpFiction, SCHEMA.contributor, Avary))
graph.add((PulpFiction, SCHEMA.actor, Travolta))
graph.add((PulpFiction, SCHEMA.actor, Thurman))
graph.add((PulpFiction, SCHEMA.actor, Jackson))
graph.add((PulpFiction, SCHEMA.actor, Willis))
graph.add((PulpFiction, SCHEMA.producer, Bender))
graph.add((PulpFiction, SCHEMA.editor, Menke))
graph.add((PulpFiction, DCTERMS.contributor, Sekula))

graph.add((PulpFiction, SCHEMA.publisher, Miramax))
graph.add((PulpFiction, SCHEMA.producer, ABandApart))
graph.add((PulpFiction, SCHEMA.producer, JerseyFilms))
graph.add((PulpFiction, SCHEMA.sponsor, LibraryOfCongress))

graph.add((PulpFiction, SCHEMA.contentLocation, LosAngeles))
graph.add((PulpFiction, SCHEMA.locationCreated, Cannes))

graph.add((PulpFiction, SCHEMA.award, Cannes1994))
graph.add((PulpFiction, DCTERMS.references, Vietnam))

graph.add((PulpFiction, SCHEMA.genre, NonlinearNarrative))
graph.add((PulpFiction, SCHEMA.genre, PostmodernFilm))
graph.add((PulpFiction, SCHEMA.genre, BlackComedy))
graph.add((PulpFiction, SCHEMA.genre, IndependentFilm))
graph.add((PulpFiction, DCTERMS.source, PulpMagazine))

graph.add((PulpFiction, SCHEMA.isRelatedTo, Soundtrack))

graph.add((Tarantino, SCHEMA.contributor, Avary))
graph.add((Tarantino, SCHEMA.founder, ABandApart))
graph.add((Cannes1994, SCHEMA.contentLocation, Cannes))
graph.add((Oscars, SCHEMA.award, Travolta))
graph.add((Oscars, SCHEMA.award, Thurman))
graph.add((Oscars, SCHEMA.award, Jackson))
graph.add((Oscars, SCHEMA.contentLocation, LosAngeles))
graph.add((Miramax, SCHEMA.location, LosAngeles))
graph.add((Vietnam, DCTERMS.references, Willis))
graph.add((Soundtrack, SCHEMA.publisher, Miramax))

graph.serialize(destination="pulp_fiction.ttl", format="turtle")

print("Conversion is done")