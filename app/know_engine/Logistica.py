from pyknow import *

from app.facts.Cliente import Cliente
from app.facts.Evento import Evento
from app.facts.Ocorrencia import Ocorrencia
from app.facts.Produto import Produto
from app.facts.Transportadora import Transportadora
from app.facts.Armazem import Armazem

def status(args):
    pass

def data(args):
    pass


def data_prevista(args):
    pass


def peso_produtos(args):
    pass


def valor_divida(args):
    pass


class Logistica(KnowledgeEngine):

    # Regra 1
    @Rule(Evento(name="Extravio"), Ocorrencia(status) != "novo" &  Ocorrencia(status) != "fechada")
    def at200rg20(self):
        print("não permitir abrir ocorrência de atraso")

    @Rule(Ocorrencia(data) < Cliente(data_prevista))
    def at200rg21(self):
        print("não abrir at ou abrir como indevida , sem notificar o cliente")

    @Rule(ColetaTranportadora = "fornecedor")
    def at200rg22(self):
        print("recalcular o prazo de entrega do produto")

    @Rule(Evento(name="ProdutoDisponivelColeta"),
    AND(Armazem(qtd_produtos="100") & Armazem(peso_produtos < "1000")))
    def at200rg23(self):
        print("Definir transportadora Y para coletar os produtos")

    @Rule(Evento(name="ProdutoDisponivelColeta"),
    Armazem(qtd_produtos="100"),
    Armazem(peso_produtos > "1000")& Armazem(peso_produtos < "4000"))
    def at200rg24(self):
        print("Definir transportadora X para coletar os produtos")

    @Rule( Evento(name="ProdutoDisponivelColeta"), Armazem(peso_produtos > "4000"))
    def at200rg25(self):
        print("Solicita coleta na indústria da transportadora de coleta FOB")

    @Rule(Evento(name="FaturamentoNota"),(Transportadora(valor_divida > "40000") & Transportadora(valor_divida < "80000")))
    def at200rg26(self):
        print("Bloquear faturamento de nota")

    @Rule( Evento(name="FaturamentoNota"),Transportadora(valor_divida > "80000"))
    def at200rg27(self):
        print("solicitar reunião com o gerente da transportadora")

    @Rule(Evento(name="SolicitacaoColetaFornecedor"))
    def at200rg28(self):
        print("Enviar Notfis para transportadora")

    @Rule(Evento(name="EmissaoCTE"))
    def at200rg29(self):
        print("Recalcular Prazo de entrega para os produtos")

    @Rule(Evento(name="DivergenciaProduto"), Produto(entrega="ForaDoPrazo"))
    def at200rg30(self):
        print("Cria uma indenização contra a transportadora devido atraso na entrega")

    @Rule(Evento(name="CriacaoOcorrencia"), Cliente(qtd_cocrrencias="4"))
    def at200rg31(self):
        print("Bloqueio de criação de ocorrencias")
        print("Abertura de Extravio")

    @Rule(Evento(name="AgendamentoColeta"), Cliente(qtd_cocrrencias="4"))
    def at200rg32(self):
        print("Bloqueio de criação de ocorrencias")
        print("Abertura de Extravio")

# =======
#
# # se a rota de entrega passar por são paulo, solicitar caminhão truk
# # se o volume de expedição semanal do fornecedor no rio grande do sul for de 5 toneladas, solicitar coleta diária com uma carreta
# # se o volume de expedição semanal do fornecedor em são paulo for de 5 toneladas, solicitar coleta diária 2 trucks por coleta
# # se o volume de expedição semanal do fornecedor em minas gerais for de 4 toneladas, solicitar coleta diária com uma carreta
# >>>>>>> Stashed changes
