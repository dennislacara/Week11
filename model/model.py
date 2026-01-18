import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self.oggetti = []
        self.map_oggetti = {}
        self.relazioni = []
        self.G = None

    def get_all_objects(self):
        self.oggetti = DAO.read_all_objects()

        if self.oggetti:
            for oggetti in self.oggetti:
                self.map_oggetti[oggetti.object_id] = oggetti
        else:
            print('lista oggetti vuota')

    def get_all_relations(self):
        self.relazioni = DAO.read_all_relations()

    def crea_grafo(self):
        if self.G is None:
            self.G = nx.Graph()
        else:
            self.G.clear()

        self.get_all_objects()
        self.get_all_relations()
        print(self.oggetti)
        print(self.relazioni)

        if self.oggetti and self.relazioni:
            #implemento nodi
            for ogg in self.oggetti:
                self.G.add_node(ogg.object_id)
            #implemento archi
            for arco in self.relazioni:
                self.G.add_edge(arco[0], arco[1], peso = arco[2])

        print(self.G)

    def calcola_componente_conn(self, id):
        componente_conn = nx.node_connected_component(self.G, id)
        print(componente_conn)
        ris = [(self.map_oggetti[id_arrivo],self.G[id][id_arrivo]['peso']) for id_arrivo in componente_conn if id != id_arrivo]
        print(len(ris))
        return ris



