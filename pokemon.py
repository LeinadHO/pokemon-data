# Importação dos módulos utilizados
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

# Teste
contador = 0
while contador < len(indices_pokedex):
    indice = indices_pokedex[contador].text
    # O try-expect garante que os pokémons e suas formas alternativas serão incluídas
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
    pokemon = f"{indice} {nome} {hp} {ataque} {defesa} {ataque_especial} {defesa_especial} {velocidade}"
    print(pokemon)  
    contador += 1
    
# Finalização da conexão entre o driver e o navegador
driver.close()

