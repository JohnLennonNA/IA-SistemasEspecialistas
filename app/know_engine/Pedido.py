from pyknow import *
from ..facts.Produto import Produto


class Pedido(KnowledgeEngine):
    # Regra 1
    @Rule(Produto(tipo_de_venda='Loja'), OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 40)))
    def at240(self):
        print('AT240')

    # Regra 2
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          AND(Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 20) & P(lambda atrasoDU: atrasoDU < 40))),
          Produto(gatilho='-2du Prazo Original'))
    def at230(self):
        print('AT230')

    # Regra 3
    @Rule(Produto(tipo_de_venda='Loja'), OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)),
          Produto(gatilho='-2du Novo Prazo'))
    def at215(self):
        print('AT215')

#3--SE(E(
#Tipo de Venda=Loja;OU(
#Fase do Item=Supply;
#Fase do Item=Financeiro);
#Atraso em D.U<20;
#Gatilho=-2d.u. Novo Prazo);
# "AT215";
