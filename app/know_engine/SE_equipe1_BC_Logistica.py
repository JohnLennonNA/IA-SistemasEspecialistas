from pyknow import *
from app.facts.Produto import Produto


class Logistica(KnowledgeEngine):
    @Rule(Produto(perfil='Sofisticado'), Produto(fome='Pouca'), Produto(horario='Jantar'))
    def sugere_frances(self):
        print('Le Fromage Puant')


# se a rota de entrega passar por são paulo, solicitar caminhão truk
# se o volume de expedição semanal do fornecedor no rio grande do sul for de 5 toneladas, solicitar coleta diária com uma carreta
# se o volume de expedição semanal do fornecedor em são paulo for de 5 toneladas, solicitar coleta diária 2 trucks por coleta
# se o volume de expedição semanal do fornecedor em minas gerais for de 4 toneladas, solicitar coleta diária com uma carreta