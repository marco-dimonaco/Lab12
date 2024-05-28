import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, country, year):
        getRetailersCountry = DAO.getRetailersCountry(country)
        allNodes = DAO.getAllNodes()
        self._grafo.add_nodes_from(getRetailersCountry)
        for r in allNodes:
            self._idMap[r.Retailer_code] = r
        self.getAllEdges(year)

    def getAllEdges(self, year):
        allConnessioni = DAO.getAllConnessioni(year, self._idMap)
        for c in allConnessioni:
            if c.rc1 in self._grafo and c.rc2 in self._grafo:
                self._grafo.add_edge(c.rc1, c.rc2, weight=c.n)

    def getAllCountries(self):
        allCountries = DAO.getAllCountries()
        nazioni = []
        for paese in allCountries:
            nazioni.append(paese)
        return nazioni
