# -*- coding: utf-8 -*-
from fpdf import FPDF
import datetime

def imprimirData():
    Meses=('janeiro','fevereiro','mar','abril','maio','junho',
       'julho','agosto','setembro','outubro','novembro','dezembro')
    agora = datetime.date.today()
    dia = agora.day
    mes=(agora.month-1)
    mesExtenso = Meses[mes]
    ano = agora.year
    resultado = str(dia) + " de " + mesExtenso + " de " + str(ano) + "."
    return resultado

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('cabecalho.png', 90, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 10)
        # Move to the right
        # Title
        self.ln(35)
        self.cell(70)
        self.cell(50, 5, u'MINISTÉRIO DA EDUCAÇÃO', 0, 1, 'C')
        self.cell(70)
        self.cell(50, 5, u'UNIVERSIDADE FEDERAL DO CARIRI', 0, 1, 'C')
        self.cell(70)
        # Line break
        self.cell(50, 5, u'PRÓ-REITORIA DE PESQUISA, PÓS-GRADUAÇÃO E INOVAÇÃO', 0, 1, 'C')
        self.cell(70)
        self.cell(50, 5, u'COORDENADORIA DE PESQUISA', 0, 1, 'C')

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-55)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        #self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')
        self.image('rodape.png', 5, 250, 200)
        self.cell(0, 5, 'DOCUMENTO ASSINADO DIGITALMENTE: ' , 0, 1, 'C')
        self.cell(0, 5, 'Autenticidade pode ser verificada em: http://prpi.ufca.edu.br ' , 0, 1, 'C')

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
## TODO: Ajustar margens
pdf.set_margins(20,20,20)
nome = "RAFAEL PERAZZO BARBOSA MOTA"
cpf = "026752874-40"
orientador = "Daniel Macedo Batista"
projeto = "Mecanismos para economia de energia em RFID"
ch = "12 horas"
vigencia_inicio = "agosto de 2017"
vigencia_fim = "julho de 2018"
modalidade = "PIBIC"

pdf.ln(10)
pdf.set_font('Times', 'B', 16)
pdf.cell(0, 10, u'DECLARAÇÃO ', 0, 1,'C')
pdf.ln(10)
pdf.set_font('Times', '', 12)
texto = u'Declaramos para os devidos fins que ' + nome + ', CPF: ' + cpf
texto = texto + u" , foi bolsista do Programa Institucional de Bolsas de Iniciação Científica (" + modalidade + "), "
texto = texto + u"sob orientação do professor(a) " + orientador + u" com o projeto intitulado " + projeto
texto = texto + u" desempenhando suas atividades com carga horária de " + ch + u" semanais.\n"
texto = texto + u"A participação do(a) discente em questão no referido Projeto de Pesquisa foi de " + vigencia_inicio + " a " + vigencia_fim + "."
pdf.multi_cell(190, 10, texto, 0, 1,'J')

pdf.ln(20)

pdf.cell(0,5,u"Juazeiro do Norte, " + imprimirData(),0,1,'R')
pdf.image('assinatura.jpg', 70, 185, 66)
pdf.line(60,200,150,200)
pdf.ln(20)
pdf.cell(0,5,u"RAFAEL PERAZZO BARBOSA MOTA",0,1,'C')
pdf.cell(0,5,u"COORDENADOR DE PESQUISA",0,1,'C')
pdf.cell(0,5,u"SIAPE: 1570709",0,1,'C')
pdf.output('declaracao.pdf', 'F')
