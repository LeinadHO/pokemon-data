# Importação das bibliotecas utilizadas
from selenium import webdriver
from selenium.webdriver.common.by import By

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

# Finalização da conexão entre o driver e o navegador
driver.close()

