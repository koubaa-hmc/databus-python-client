"""Download Tests"""
import databusclient.client as cl

DEFAULT_ENDPOINT = "https://databus.openenergyplatform.org/sparql"
TEST_QUERY = """
PREFIX dcat: <http://www.w3.org/ns/dcat#>
SELECT ?x WHERE {
  ?sub dcat:downloadURL ?x .
} LIMIT 10
"""
TEST_COLLECTION = "https://databus.openenergyplatform.org/koubaa-hmc/collections/sandbox"
TEST_ARTEFACT = "https://databus.openenergyplatform.org/koubaa-hmc/active_photovoltaic/01-2022"


def test_with_query():
    cl.download("tmp", DEFAULT_ENDPOINT, [TEST_QUERY])


def test_with_collection():
    cl.download("tmp", DEFAULT_ENDPOINT, [TEST_COLLECTION])


def test_with_artefact():
    cl.download("tmp", DEFAULT_ENDPOINT, [TEST_ARTEFACT])
