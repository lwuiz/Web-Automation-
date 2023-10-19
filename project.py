from selenium import webdriver
import openpyxl

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get('https://www.novaliderinformatica.com.br/computadores-gamers')

nomes_produtos= driver.find_elements_by_xpath("//a[@class='nome-produto']")

precos= driver.find_elements_by_xpath("//strong[@class='preco-promocional']")

precos_desconto= driver.find_elements_by_xpath("//span[@class='desconto-a-vista preco-avista-wrap']")

workbook= openpyxl.Workbook()

workbook.create_sheet('infos')

sheet_produtos= workbook['infos']

sheet_produtos['A1'].value = 'Nome do produto'
sheet_produtos['B1'].value = 'Preço do produto'
sheet_produtos['C1'].value = 'Preço a vista'

for titulo, preco in zip(nomes_produtos,precos):
    sheet_produtos.append([titulo.text,preco.text])

for i, desconto in enumerate(precos_desconto,start= 1):
    cell = sheet_produtos[f'C{i}']  
    cell.value = desconto.text  

workbook.save('automate.xlsx')