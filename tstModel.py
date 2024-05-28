from model.model import Model

mymodel = Model()
mymodel.buildGraph("United States", 2017)
print(f"Num nodi: {len(mymodel._grafo.nodes)}")
print(f"Num archi: {len(mymodel._grafo.edges)}")
