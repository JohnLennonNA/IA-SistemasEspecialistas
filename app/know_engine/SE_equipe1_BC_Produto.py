from pyknow import *
from app.facts.Produto import Produto


class Produto(KnowledgeEngine):
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
          Produto(atrasoDU=P(lambda atrasoDU: atrasoDU < 20)),
          NOT(Produto(gatilho=W())))
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
          OR(Produto(fase_do_item='Supply'), Produto(fase_do_item='Financeiro')),
          NOT(Produto(gatilho=W())))
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

    # Regra 21
    @Rule(Evento(name='NfDevolvida'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando refatutamento')
        print('Atualiza o produto no processo para o status aguardando refatutamento ')

    # Regra 22
    @Rule(Evento(name='NfDevolvida'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando refatutamento')

    # Regra 23
    @Rule(Evento(name='ProdutoDevolvidoCD'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando aceite da devolução')
        print('Atualiza o produto no processo para o status aguardando aceite da devolução')

    # Regra 24
    @Rule(Evento(name='ProdutoDevolvidoCD'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando aceite da devolução')

    # Regra 25
    @Rule(Evento(name='BipeDeProdutoCd'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando confirmação da devolução')
        print('Atualiza o produto no processo para o status aguardando confirmação da devolução')

    # Regra 26
    @Rule(Evento(name='BipeDeProdutoCd'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando confirmação da devolução')

    # Regra 27
    @Rule(Evento(name='ClienteNaoConfirmouRecebimento'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta no status solicitar comprovante de entrega')
        print('Atualiza o produto no processo para o status solicitar comprovante de entrega')

    # Regra 28
    @Rule(Evento(name='ClienteNaoConfirmouRecebimento'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta no status solicitar comprovante de entrega')

    # Regra 29
    @Rule(Evento(name='SolicitadoComprovanteEntrega'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando envio do comprovante de entrega')
        print('Atualiza o produto no processo para o status aguardando envio do comprovante de entrega')

    # Regra 30
    @Rule(Evento(name='SolicitadoComprovanteEntrega'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando envio do comprovante de entrega')

    # Regra 31
    @Rule(Evento(name='NotaApreendidaPostoFiscal'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando geração de gnre')
        print('Atualiza o produto no processo para o status aguardando geração de gnre')

    # Regra 32
    @Rule(Evento(name='NotaApreendidaPostoFiscal'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando geração de gnre')

    # Regra 33
    @Rule(Evento(name='GnreEnviadoSefaz'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta gerando gnre')
        print('Atualiza o produto no processo para o status gerando gnre')

    # Regra 34
    @Rule(Evento(name='GnreEnviadoSefaz'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta gerando gnre')

    # Regra 35
    @Rule(Evento(name='GnreAutorizadoSefaz'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta no status gnre autorizada')
        print('Atualiza o produto no processo para o status gnre autorizada')

    # Regra 36
    @Rule(Evento(name='GnreAutorizadoSefaz'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta no status gnre autorizada')

    # Regra 37
    @Rule(Evento(name='GnreCriada'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando pagamento da gnre')
        print('Atualiza o produto no processo para o status aguardando pagamento da gnre')

    # Regra 38
    @Rule(Evento(name='GnreCriada'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando pagamento da gnre')

    # Regra 39
    @Rule(Evento(name='PagamentoGnreRealizado'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando comprovante de pagamento da gnre')
        print('Atualiza o produto no processo para o status aguardando comprovante de pagamento da gnre')

    # Regra 40
    @Rule(Evento(name='PagamentoGnreRealizado'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando comprovante de pagamento da gnre')

    # Regra 41
    @Rule(Evento(name='SolicitacaoDeGnreRealizada'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta enviado comprovante de pagamento de gnre para transportadora')
        print('Atualiza o produto no processo para o status enviado comprovante de pagamento de gnre para transportadora')

    # Regra 42
    @Rule(Evento(name='SolicitacaoDeGnreRealizada'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta enviado comprovante de pagamento de gnre para transportadora')

    # Regra 43
    @Rule(Evento(name='DivergenciaDeVolume'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando geração de carta de correção')
        print('Atualiza o produto no processo para o status aguardando geração de carta de correção')

    # Regra 44
    @Rule(Evento(name='DivergenciaDeVolume'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta aguardando geração de carta de correção')

    # Regra 45
    @Rule(Evento(name='CartaCorrecaoGerada'), AND(Evento(mapeado='1')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta enviado carta de correção para transportadora')
        print('Atualiza o produto no processo para o status enviado carta de correção para transportadora')

    # Regra 46
    @Rule(Evento(name='CartaCorrecaoGerada'), AND(Evento(mapeado='0')))
    def at200rg20(self):
        print('Avisa o cliente que o pedido esta enviado carta de correção para transportadora')


    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando trasportadora imprimir documentos auxiliares')
    #     print('Atualiza o produto no processo para o status aguardando trasportadora imprimir documentos auxiliares')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando trasportadora imprimir documentos auxiliares')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando emissão da NF')
    #     print('Atualiza o produto no processo para o status aguardando emissão da NF')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando emissão da NF')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando estorno')
    #     print('Atualiza o produto no processo para o status aguardando estorno')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando estorno')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando autorização de estorno')
    #     print('Atualiza o produto no processo para o status aguardando autorização de estorno')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando autorização de estorno')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando emissão da NF de indenizar')
    #     print('Atualiza o produto no processo para o status aguardando emissão da NF de indenizar')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando emissão da NF de indenizar')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de extravio')
    #     print('Atualiza o produto no processo para o status aguardando abertura da ocorrência de extravio')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de extravio')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de avaria')
    #     print('Atualiza o produto no processo para o status aguardando abertura da ocorrência de avaria')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de avaria')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de atraso')
    #     print('Atualiza o produto no processo para o status aguardando abertura da ocorrência de atraso')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de atraso')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de solicitação de informações complementares do cliente')
    #     print('Atualiza o produto no processo para o status aguardando abertura da ocorrência de solicitação de informações complementares do cliente')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando abertura da ocorrência de solicitação de informações complementares do cliente')
    #
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando aprovação do pedido')
    #     print('Atualiza o produto no processo para o status aguardando aprovação do pedido')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando aprovação do pedido')
    #
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando integração do pedido')
    #     print('Atualiza o produto no processo para o status aguardando integração do pedido')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando integração do pedido')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando geração da oc')
    #     print('Atualiza o produto no processo para o status aguardando geração da oc')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta aguardando geração da oc')
    #
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta gerando oc')
    #     print('Atualiza o produto no processo para o status gerando oc')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta gerando oc')
    #
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta com oc gerada com sucesso')
    #     print('Atualiza o produto no processo para o status oc gerada com sucesso')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta com oc gerada com sucesso')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta reservando produtos em estoque')
    #     print('Atualiza o produto no processo para o status reservando produtos em estoque')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta reservando produtos em estoque')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta em produto em produção')
    #     print('Atualiza o produto no processo para o status produto em produção')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta produto em produção')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='1')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta embalando produto')
    #     print('Atualiza o produto no processo para o status embalando produto')
    #
    # @Rule(Evento(name='OrdemDeCompraRealizada'), AND(Evento(mapeado='0')))
    # def at200rg20(self):
    #     print('Avisa o cliente que o pedido esta embalando produto')



