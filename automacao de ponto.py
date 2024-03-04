from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def acionar_ponto(usuario, senha, hora_entrada, hora_saida, id_botao_registrar_ponto):
    # Inicializar o navegador (nesse caso, o Chrome)
    driver = webdriver.Chrome()

    try:
        # Abrir a página de login do sistema
        driver.get("https://bateponto.pontotel.com.br/")

        # Preencher o formulário de login
        input_usuario = driver.find_element_by_name("username")
        input_senha = driver.find_element_by_name("password")

        input_usuario.send_keys(usuario)
        input_senha.send_keys(senha)

        # Enviar o formulário
        input_senha.send_keys(Keys.RETURN)

        # Aguardar alguns segundos para garantir que a página seja carregada
        time.sleep(5)

        # Preencher o campo de hora de entrada
        input_hora_entrada = driver.find_element_by_name("nome_do_campo_hora_entrada")
        input_hora_entrada.send_keys(hora_entrada)

        # Preencher o campo de hora de saída
        input_hora_saida = driver.find_element_by_name("nome_do_campo_hora_saida")
        input_hora_saida.send_keys(hora_saida)

        # Realizar a ação de acionar o ponto
        button_registrar_ponto = driver.find_element_by_id(id_botao_registrar_ponto)
        button_registrar_ponto.click()

        print("Ponto acionado com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Fechar o navegador
        driver.quit()

# Substitua os valores pelos fornecidos
usuario = "xxxxxxx@xxx.xxxxx.xxx"
senha = "xxxxxxxxx"
hora_entrada = "07:55"
hora_saida = "12:05"
id_botao_registrar_ponto = "vitor.freitas@unigranrio.com.br"

# Chamar a função acionar_ponto com os dados fornecidos
acionar_ponto(usuario, senha, hora_entrada, hora_saida, id_botao_registrar_ponto)
