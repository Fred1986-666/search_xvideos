import requests
from bs4 import BeautifulSoup

def search_xvideos(query)
    # URL de pesquisa do Xvideos
    search_url = fhttpswww.xvideos.comk={query}
    
    # Faz a requisição HTTP
    response = requests.get(search_url)
    
    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200
        # Analisa o HTML da página
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontra todos os elementos que contêm informações de vídeos
        video_elements = soup.find_all('div', {'class' 'thumb'})
        
        # Exibe os títulos e links dos vídeos encontrados
        for video in video_elements
            link_tag = video.find('a')
            if link_tag
                title = link_tag.get('title', '')
                href = link_tag.get('href', '')
                if title and href
                    print(fTítulo {title})
                    print(fLink httpswww.xvideos.com{href})
                    print(-  50)
    else
        print(Erro ao fazer a requisição.)

if __name__ == __main__
    # Termo de pesquisa
    query = input(Digite o termo de pesquisa )
    # Realiza a pesquisa
    search_xvideos(query)