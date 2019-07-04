import pandas as pd
from datetime import date
from app.facts.Produto import Produto
from app.know_engine.Pedido import Pedido

# Carrega a base
pedidos = pd.read_csv('ListaPedidos.csv', sep=';')

#Nomes das Colunas
print(pedidos.columns)

mt_ped = Pedido()

for index, row in pedidos.iterrows():
    # Calculo atraso do pedido
    d1 = date.fromisoformat(row['Data Prevista Entrega'])
    d2 = date.today()
    atraso = (d2 - d1).days

    print(row['Desc Prod'], 'Atraso:', atraso)

    mt_ped.reset()
    mt_ped.declare(Produto(tipo_de_venda=row['Tipo de Venda']))
    mt_ped.declare(Produto(fase_do_item=row['Fase do Item']))
    if atraso > 0:
        mt_ped.declare(Produto(atrasoDU=atraso))
#    mt_ped.declare(Produto(gatilho='-2d.u. Novo Prazo'))
    mt_ped.run()


#mt_log = Logistica()
#mt_log.reset()

#mt_log.declare(Produto(perfil='Natureba'))
#mt_log.declare(Produto(fome='Faminto'))
#mt_log.declare(Produto(horario='Almoço'))

#mt_log.run()

