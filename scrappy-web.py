import requests
from bs4 import BeautifulSoup

def buscar_informacoes(url, palavra_chave):
    # Fazendo a solicitação HTTP para obter o conteúdo da página da web
    response = requests.get(url)
    
    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Analisando o conteúdo HTML da página
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Procurando por ocorrências da palavra-chave no conteúdo da página
        conteudo = soup.get_text().lower()  # Convertendo o conteúdo para minúsculas
        ocorrencias = conteudo.count(palavra_chave.lower())
        
        # Retornando o número de ocorrências encontradas
        return ocorrencias
    else:
        # Se a solicitação não foi bem-sucedida, imprimir mensagem de erro
        print("Erro ao acessar a página:", response.status_code)
        return None

# URL da página da web a ser rastreada
url = 'https://www.exemplo.com'

# Palavra-chave a ser procurada
palavra_chave = 'exemplo'

# Chamando a função para buscar informações
ocorrencias_palavra_chave = buscar_informacoes(url, palavra_chave)

# Verificando se houve ocorrências da palavra-chave
if ocorrencias_palavra_chave is not None:
    print(f"A palavra-chave '{palavra_chave}' foi encontrada {ocorrencias_palavra_chave} vezes na página {url}.")
else:
    print("Não foi possível obter informações.")
