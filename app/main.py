import pandas as pd
from datetime import date
from app.facts.Produto import Produto as ProductFact
from app.facts.Produto import Produto as EventoFact
from app.know_engine.Pedido import Produto
from app.know_engine.Pedido import Logistica

class Event(KnowledgeEngine):
    @Rule(EventoFact(name='Extravio'), OR(EventoFact(name='ProdutoDisponivelColeta')))
    def at204rg(self):
        mt_prdo = Logistica()
        mt_prdo.reset()
        mt_prdo.declare(EventoFact(name=row['NomeEvento']))
        mt_ped.run()

    @Rule(EventoFact(name='ConfirmacaoOC'), OR(EventoFact(name='PagamentoAprovado')))
    def at263rg(self):
        mt_ped = Produto()
        d1 = date.fromisoformat(row['Data Prevista Entrega'])
        d2 = date.today()
        atraso = (d2 - d1).days
        print(row['Desc Prod'], 'Atraso:', atraso)
        mt_ped.reset()
        mt_ped.declare(ProductFact(tipo_de_venda=row['Tipo de Venda']))
        mt_ped.declare(ProductFact(fase_do_item=row['Fase do Item']))
        if atraso > 0:
            mt_ped.declare(ProductFact(atrasoDU=atraso))
        mt_ped.run()


# Carrega a base
pedidos = pd.read_csv('ListaPedidos.csv', sep=';')

#Nomes das Colunas
print(pedidos.columns)

for index, row in pedidos.iterrows():
    # Calculo atraso do pedido

    mt_ped.reset()
    mt_ped.declare(ProductFact(name=row['Tipo de Venda']))
    if atraso > 0:
        mt_ped.declare(ProductFact(atrasoDU=atraso))
    #    mt_ped.declare(Produto(gatilho='-2d.u. Novo Prazo'))
    mt_ped.run()


#mt_log = Logistica()
#mt_log.reset()

#mt_log.declare(Produto(perfil='Natureba'))
#mt_log.declare(Produto(fome='Faminto'))
#mt_log.declare(Produto(horario='Almoço'))

#mt_log.run()

