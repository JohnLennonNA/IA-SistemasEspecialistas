from pyknow import *
from app.facts.Produto import Produto


class Logistica(KnowledgeEngine):
    @Rule(Produto(perfil='Sofisticado'), Produto(fome='Pouca'), Produto(horario='Jantar'))
    def sugere_frances(self):
        print('Le Fromage Puant')
