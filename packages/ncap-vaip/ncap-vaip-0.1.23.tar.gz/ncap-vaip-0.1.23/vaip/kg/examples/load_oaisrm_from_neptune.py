from vaip.kg.model.oaisrm import Oaisrm
from vaip.kg.client.neptune import NeptuneClient

oais = Oaisrm()

query="""
SELECT ?s ?p ?o
WHERE {
    GRAPH <http://ncei.noaa.gov/vaip/0.3.0>
    { ?s ?p ?o }
}
"""
client = NeptuneClient()
client.load_into_oaisrm(oais, query)

rdf_text = oais.save_rdf_text(format="application/rdf+xml")
print(rdf_text)