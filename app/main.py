from pyknow import *
from facts.Gatilho import Gatilho

class EscolherRestaurante(KnowledgeEngine):
    @Rule(Usuario(perfil='Sofisticado'), Usuario(fome='Pouca'), Usuario(horario='Jantar'))
    def sugere_frances(self):
        print('Le Fromage Puant')

    @Rule(Usuario(perfil='Ogro'), Usuario(fome='Faminto'), Usuario(horario='Almoço'))
    def sugere_churras(self):
        print('Churrascão Pança Cheia')

    @Rule(Usuario(perfil='Natureba'), Usuario(fome=W()), Usuario(horario=W()))
    def sugere_vegeta(self):
        print('Lanchonete Santa Alface')

    @Rule(Usuario(perfil='Curioso'))
    def sugere_qualquer_coisa(self):
        print('Qualquer Coisa Serve')


motor = EscolherRestaurante()
motor.reset()

motor.declare(Usuario(perfil='Natureba'))
motor.declare(Usuario(fome='Faminto'))
motor.declare(Usuario(horario='Almoço'))

motor.run()