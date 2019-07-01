from pyknow import *
from ..facts.Gatilho import Gatilho


class Logistica(KnowledgeEngine):
    @Rule(Gatilho(perfil='Sofisticado'), Gatilho(fome='Pouca'), Gatilho(horario='Jantar'))
    def sugere_frances(self):
        print('Le Fromage Puant')

    @Rule(Gatilho(perfil='Ogro'), Gatilho(fome='Faminto'), Gatilho(horario='Almoço'))
    def sugere_churras(self):
        print('Churrascão Pança Cheia')

    @Rule(Gatilho(perfil='Natureba'), Gatilho(fome=W()), Gatilho(horario=W()))
    def sugere_vegeta(self):
        print('Lanchonete Santa Alface')

    @Rule(Gatilho(perfil='Curioso'))
    def sugere_qualquer_coisa(self):
        print('Qualquer Coisa Serve')