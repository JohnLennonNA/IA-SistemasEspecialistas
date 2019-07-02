from app.facts.Produto import Produto
from app.know_engine.Logistica import Logistica
from app.know_engine.Pedido import Pedido

mt_ped = Pedido()
mt_ped.reset()

mt_ped.declare(Produto(tipo_de_venda='Loja'))
mt_ped.declare(Produto(fase_do_item='Supply'))
mt_ped.declare(Produto(atrasoDU=42))

mt_ped.run()

#mt_log = Logistica()
#mt_log.reset()

#mt_log.declare(Produto(perfil='Natureba'))
#mt_log.declare(Produto(fome='Faminto'))
#mt_log.declare(Produto(horario='Almoço'))

#mt_log.run()
