import pandas as pd
from datetime import date
from app.facts.Produto import Produto as ProductFact
from app.facts.Produto import Produto as EventoFact
from app.know_engine.Pedido import Produto
from app.know_engine.Pedido import Logistica

class Event(KnowledgeEngine):
    @Rule(AS.event << OR(EventoFact(name='Extravio'), EventoFact(name='ProdutoDisponivelColeta')))
    def at204rg(self, event):
        mt_prdo = Logistica()
        mt_prdo.reset()
        mt_prdo.declare(EventoFact(name=event["name"]))
        mt_ped.run()

    @Rule(AS.event << OR( EventoFact(name='ConfirmacaoOC'), EventoFact(name='PagamentoAprovado')))
    def at263rg(self, event):
        mt_ped = Produto()
        mt_ped.reset()
        mt_ped.declare(EventoFact(name=event["name"]))
        mt_ped.run()


# Carrega a base
pedidos = pd.read_csv('ListaPedidos.csv', sep=';')

#Nomes das Colunas
print(pedidos.columns)

for index, row in pedidos.iterrows():
    # Calculo atraso do pedido

    mt_event = Event()
    mt_event.reset()
    mt_event.declare(EventoFact(name=row['NomeEvento']))
    mt_event.run()


#mt_log.reset()

#mt_log.declare(Produto(perfil='Natureba'))
#mt_log.declare(Produto(fome='Faminto'))
#mt_log.declare(Produto(horario='Almoço'))

#mt_log.run()

