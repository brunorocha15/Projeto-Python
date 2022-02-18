import os
from turtle import width
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

planilha = pd.read_excel("Covid-Brasil.xlsx")

regioes = planilha['REGIÕES']
obitos = planilha['ÓBITOS']

plt.pie(obitos, labels = regioes, autopct='%1.2f%%')

plt.savefig("Covid.png")

pdf = FPDF('p', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Times', '', 20)
texto_1 = "COVID-19 - de - Bruno Gonçalves Rocha\n \n O que é COVID-19? \n\nCOVID-19 é uma infecção respiratória causada pelo coronavírus SARS-CoV-2, potencialmente grave, de elevada transmissibilidade e de distribuição global.O SARS-CoV-2 é um betacoronavírus descoberto em amostras de lavado broncoalveolar obtidas de pacientes com pneumonia de causa desconhecida na cidade de Wuhan, província de Hubei, China, em dezembro de 2019. Pertence ao subgênero Sarbecovírus da família Coronaviridae e é o sétimo coronavírus conhecido a infectar seres humanos."
pdf.multi_cell(w=0,h=9,txt=texto_1,align='J')
pdf.image(name="covid.jpg",  x=30, y=151,w=153)


pdf.add_page()
pdf.set_font('Times', '', 20)
texto_2="\n \nSintomas\n\n Os sintomas agem de forma diferente entre os infectados,alguns infectados tem sintomas leves e outros sintomas mais fortes, pórem a maioria dos infectados não precisam ser hospitalizados.\n\n\n  //Febre\n\n //Coriza\n\n //Dor de garganta\n\n //Dor no corpo\n\n //Perda de paladar ou olfato\n\n //Dor de Cabeça\n\n //Diarreia\n\n //Cansaço "
pdf.multi_cell(w=0,h=9,txt=texto_2,align='J')


pdf.add_page()
pdf.set_font('Times', '', 20)
texto_3=" Vacina\n\nA vacinação está sendo tratada como prioridade número um do Ministério da Saúde e não para de avançar. Prova disso é que a pasta bateu um novo recorde: mais de 43 milhões de doses de vacinas Covid-19 foram distribuídas pelo Ministério da Saúde para os estados e o Distrito Federal somente em julho.\n\n *Doses:\n\n //Total de doses aplicadas: 380.878.261\n\n // Pessoas completamente vacinadas: 152.751.771\n\n //Pessoas com pelo menos uma dose: 174.949.012\n\n //Pessos que receberam a dose de reforso: 58.207.145 "
pdf.multi_cell(w=0,h=9,txt=texto_3,align='J')
pdf.image(name="vac.jpg",  x=30, y=176,w=153)


pdf.add_page()
pdf.set_font('Times', '', 20)
texto_4="Óbitos \n\nMesmo com o número de pessoas vacinadas aumentando precisamos nos prevenir, pois a pandemia não acabou e os números de pessoas contaminadas e óbitos não param de crescer, com 24.708.484 de casos confirmados e 641.902 de óbitos, analizando os números da para perceber que no Brasil a região Sudeste lidera o rank com mais casos seguidos de Nordeste e Sul,acredito que por causa das festas de fim de ano.\n\n\nVeja o gráfico:" 
pdf.multi_cell(w=0,h=9,txt=texto_4,align='J')
pdf.image(name="Covid.png",  x=30, y=136,w=173)

pdf.output("Covid.pdf")

print("O PDF foi crido com sucesso!")
os.system("pause")