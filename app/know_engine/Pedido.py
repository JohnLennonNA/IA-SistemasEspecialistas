from pyknow import *
from ..facts.Produto import Produto


class Pedido(KnowledgeEngine):
    # Regra 1
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
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
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)),
          Produto(gatilho='-2du Novo Prazo'))
    def at215(self):
        print('AT215')

    # Regra 4
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          AND(Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 20) & P(lambda atrasoDU: atrasoDU < 40))),
          OR(Produto(gatilho='-2du Prazo Original'), Produto(gatilho='Prev.Embarque')))
    def at225(self):
        print('AT225')

    # Regra 5
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)))
    def at205(self):
        print('AT205')

    # Regra 6
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Fob'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2du Novo Prazo'))
    def at210(self):
        print('AT210')

    # Regra 7
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Fob'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2du Prazo Original'))
    def at200(self):
        print('AT200')
