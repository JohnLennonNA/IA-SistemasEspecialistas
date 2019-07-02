from pyknow import *
from app.facts.Produto import Produto


class Pedido(KnowledgeEngine):
    ########
    # LOJA #
    ########
    # Regra 1
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 40)))
    def at240rg1(self):
        print('AT240 - Regra 1')

    # Regra 2
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          AND(Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 20) & P(lambda atrasoDU: atrasoDU < 40))),
          Produto(gatilho='-2du Prazo Original'))
    def at230rg2(self):
        print('AT230 - Regra 2')

    # Regra 3
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)),
          Produto(gatilho='-2du Novo Prazo'))
    def at215rg3(self):
        print('AT215 - Regra 3')

    # Regra 4
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          AND(Produto(atrasoDU=P(lambda atrasoDU: atrasoDU > 20) & P(lambda atrasoDU: atrasoDU < 40))),
          OR(Produto(gatilho='-2du Prazo Original'), Produto(gatilho='Prev.Embarque')))
    def at225rg4(self):
        print('AT225 - Regra 4')

    # Regra 5
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)))
    def at205rg5(self):
        print('AT205 - Regra 5')

    # Regra 6
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Fob'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2du Novo Prazo'))
    def at210rg6(self):
        print('AT210 - Regra 6')

    # Regra 7
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Fob'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2du Prazo Original'))
    def at200rg7(self):
        print('AT200 - Regra 7')

    # Regra 8
    @Rule(Produto(tipo_de_venda='Loja'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Fob')),
          Produto(gatilho='Prev.Embarque'))
    def at205rg8(self):
        print('AT205 - Regra 8')

    ###########
    # TROCA   #
    ###########
    # Regra 9
    @Rule(Produto(tipo_de_venda='Troca'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(gatilho='-2d.u. Novo Prazo'))
    def at240rg9(self):
        print('AT240 - Regra 9')

    # Regra 10
    @Rule(Produto(tipo_de_venda='Troca'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')))
    def at235rg10(self):
        print('AT235 - Regra 10')

    # Regra 11 e 13 juntou, mesma regra
    @Rule(Produto(tipo_de_venda='Troca'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Fob'), Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2d.u. Novo Prazo'))
    def at220rg11(self):
        print('AT220 - Regra 11')

    # Regra 12
    @Rule(Produto(tipo_de_venda='Troca'),
          OR(Produto(fase_do_item='Operação Fiscal'), Produto(fase_do_item='Fob')),
          OR(Produto(gatilho='-2d.u. Prazo Original'), Produto(gatilho='Prev.Embarque')))
    def at210rg12(self):
        print('AT210 - Regra 12')

    # Regra 13
    # Juntou com a 11

    # Regra 14
    @Rule(Produto(tipo_de_venda='Troca'),
          OR(Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Hub')),
          Produto(gatilho='-2d.u. Prazo Original'))
    def at200rg14(self):
        print('AT200 - Regra 14')

    ###############
    # ASSISTENCIA #
    ###############
    # Regra 15
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(gatilho='-2d.u. Novo Prazo'))
    def at240rg15(self):
        print('AT240 - Regra 15')

    # Regra 16
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(gatilho='-2d.u. Prazo Original'))
    def at235rg16(self):
        print('AT235 - Regra 16')

    # Regra 17
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          Produto(gatilho='Prev.Embarque'))
    def at230rg17(self):
        print('AT230 - Regra 17')

    # Regra 18
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Fob'), Produto(fase_do_item='Operação Fiscal')),
          Produto(gatilho='-2d.u. Novo Prazo'))
    def at220rg18(self):
        print('AT220 - Regra 18')

    # Regra 19
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Fob'), Produto(fase_do_item='Operação Fiscal')))
    def at210rg19(self):
        print('AT210 - Regra 19')

    # Regra 20
    @Rule(Produto(tipo_de_venda='Assistencia'),
          OR(Produto(fase_do_item='Porta a Porta'), Produto(fase_do_item='Hub')))
    def at200rg20(self):
        print('AT200 - Regra 20')
