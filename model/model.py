import networkx as nx
from database.DAO import DAO
from operator import itemgetter


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def buildGraph(self, country, year):
        self._grafo.clear()
        getRetailersCountry = DAO.getRetailersCountry(country)
        allNodes = DAO.getAllNodes()
        self._grafo.add_nodes_from(getRetailersCountry)
        for r in allNodes:
            self._idMap[r.Retailer_code] = r
        self.getAllEdges2(year)

    def getAllEdges(self, year):
        allConnessioni = DAO.getAllConnessioni(year, self._idMap)
        for c in allConnessioni:
            if c.rc1 in self._grafo and c.rc2 in self._grafo:
                self._grafo.add_edge(c.rc1, c.rc2, weight=c.n)

    def getAllEdges2(self, year):
        for r1 in self._grafo.nodes:
            for r2 in self._grafo.nodes:
                if r1 != r2:
                    peso = DAO.getAllConnessioni2(r1, r2, year)
                    if peso > 0:
                        self._grafo.add_edge(r1, r2, weight=peso)


    def getAllCountries(self):
        allCountries = DAO.getAllCountries()
        nazioni = []
        for paese in allCountries:
            nazioni.append(paese)
        return nazioni

    def getVolumiVendita(self):
        volumi = {}
        for r1 in self._grafo.nodes:
            count = 0
            for r2 in self._grafo.nodes:
                if r1 != r2:
                    if self._grafo.has_edge(r1, r2):
                        count += self._grafo[r1][r2]['weight']
            if r1 not in volumi:
                volumi[r1.Retailer_name] = count
            volumi = dict(sorted(volumi.items(), key=itemgetter(1), reverse=True))
        return volumi
