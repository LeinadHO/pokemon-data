# Importação dos módulos utilizados
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from openpyxl import Workbook

# Criação do driver que acessará o navegador
driver = webdriver.Firefox()
driver.get("https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_in_Generation_IX")

# Obtenção dos dados de status base dos pokémons
indices_pokedex = driver.find_elements(By.CLASS_NAME, "r")
nomes = driver.find_elements(By.CLASS_NAME, "l")
hps = driver.find_elements(By.XPATH, "//td[@style='background:#9EE865']")
ataques = driver.find_elements(By.XPATH, "//td[@style='background:#F5DE69']")
defesas = driver.find_elements(By.XPATH, "//td[@style='background:#F09A65']")
ataques_especiais = driver.find_elements(By.XPATH, "//td[@style='background:#66D8F6']")
defesas_especiais = driver.find_elements(By.XPATH, "//td[@style='background:#899EEA']")
velocidades = driver.find_elements(By.XPATH, "//td[@style='background:#E46CCA']")

# Criação do arquivo onde serão escritos os dados extraídos
wb = Workbook()
folha = wb.active
folha['A1'] = "Número na Pokédex"
folha['B1'] = "Nome"
folha['C1'] = "HP"
folha['D1'] = "Ataque"
folha['E1'] = "Defesa"
folha['F1'] = "Ataque Especial"
folha['G1'] = "Defesa Especial"
folha['H1'] = "Velocidade"

# Filtragem, formatação e escrita dos dados no arquivo 
contador = 0
while contador < len(indices_pokedex):
    indice = indices_pokedex[contador].text
    # O try-expect garante que os pokémons e todas as suas formas alternativas (se existirem) serão incluídas
    try:
        nome_alternativo = nomes[contador].find_element(By.TAG_NAME, "small")
        primeiro_nome = nomes[contador].find_element(By.TAG_NAME, "a").text
        nome_versao = nome_alternativo.text
        nome = f"{primeiro_nome} - {nome_versao}"
    except NoSuchElementException:
        nome = nomes[contador].text
    hp = hps[contador].text
    ataque = ataques[contador].text
    defesa = defesas[contador].text
    ataque_especial = ataques_especiais[contador].text
    defesa_especial = defesas_especiais[contador].text
    velocidade = velocidades[contador].text
    folha[f'A{contador+2}'] = indice
    folha[f'B{contador+2}'] = nome
    folha[f'C{contador+2}'] = hp
    folha[f'D{contador+2}'] = ataque
    folha[f'E{contador+2}'] = defesa
    folha[f'F{contador+2}'] = ataque_especial
    folha[f'G{contador+2}'] = defesa_especial
    folha[f'H{contador+2}'] = velocidade
    contador += 1
wb.save("pokemons_status.xlsx")

# Finalização da conexão entre o driver e o navegador
driver.close()

