import json
import os
import colorama
import ffmpeg
import pyfiglet
import requests


def limpar_tela():
    """
    Limpe o terminal


    :return:
    """
    if os.name == 'nt':  # Verifica se é Windows
        os.system("cls")
    else:
        os.system("clear")  # Assume que é Unix


def imprimir_texto_em_tamanho_maior(txt):

    width = 220  # Defina a largura desejada
    ascii_art = pyfiglet.figlet_format(f"\n{txt}", font='ansi_shadow', width=width)
    ascii_art2 = ("\t\t\t\t\t\t\tV1.0\n\n\n-ffmpeg instalado no path\n-conexão com a internet\n-estar inscrito no "
                  "curso que desejas baixar.\n\n")
    exibir_saida(f"{ascii_art}", "", ao_lado=True)
    exibir_saida(f"{ascii_art2}", "erro")





def exibir_saida(mensagem, tipo="tipo de cores", ao_lado=False):
    """
    Exibe uma mensagem colorida no console.

    Parâmetros:
    - mensagem (str): A mensagem a ser exibida.
    - tipo (str): O tipo da mensagem, que determina a cor.
                  Pode ser um dos seguintes: "erro", "info", "sucess", "confirm", "logo", "linha",
                  "azul", "cyan", "branco", "preto", "fundo_verde", "fundo_amarelo",
                  "fundo_azul", "fundo_ciano", "fundo_branco", "negrito", "invertido".
    - ao_lado (bool, opcional): Se True, a mensagem será exibida ao lado da última saída.
                               Caso contrário, a mensagem será exibida em uma nova linha.

    Exemplo de uso:
    >>> exibir_saida("Isso é uma mensagem de erro", "erro")
    >>> exibir_saida("Isso é uma mensagem informativa", "info", ao_lado=True)
    >>> exibir_saida("Isso é uma mensagem de sucesso", "sucess")
    """
    reset = colorama.Style.RESET_ALL
    cores = {
        "erro": colorama.Fore.RED,
        "info": colorama.Fore.MAGENTA,
        "sucess": colorama.Fore.GREEN,
        "confirm": colorama.Fore.YELLOW,
        "logo": colorama.Fore.LIGHTMAGENTA_EX,
        "linha": colorama.Fore.LIGHTRED_EX,
        "azul": colorama.Fore.BLUE,
        "cyan": colorama.Fore.CYAN,
        "branco": colorama.Fore.WHITE,
        "preto": colorama.Fore.BLACK,
        "fundo_verde": colorama.Back.GREEN,
        "fundo_amarelo": colorama.Back.YELLOW,
        "fundo_azul": colorama.Back.BLUE,
        "fundo_ciano": colorama.Back.CYAN,
        "fundo_branco": colorama.Back.WHITE,
        "negrito": colorama.Style.BRIGHT,
        "invertido": colorama.Style.BRIGHT + colorama.Back.BLACK + colorama.Fore.WHITE
    }

    cor = cores.get(tipo, "")
    mensagem_formatada = f"{cor}{colorama.Style.BRIGHT}{mensagem}{reset}"

    if ao_lado:
        print(mensagem_formatada, end="")
    else:
        print(mensagem_formatada)


def Infos(ID, HEADERS):
    get = f"https://www.udemy.com/api-2.0/courses/{ID}?"  # Faz a solicitação GET com os cabeçalhos
    response = requests.get(get, headers=HEADERS)

    # Exibe o código de status
    if response.status_code == 200:
        # Exibe o conteúdo do arquivo M3U8
        data = json.loads(response.text)
        id = data.get("id", "N?")
        title = data.get("title", "N?")
        idioma = data.get("locale", {})
        idioma = idioma.get("title", "N?")
        limpar_tela()
        exibir_saida("\n\n\n\nCurso id: ", "info", ao_lado=True)
        exibir_saida(id, "confirm")
        exibir_saida("Nome do curso : ", "info", ao_lado=True)
        exibir_saida(title, "confirm")
        exibir_saida("Idioma: ", "info", ao_lado=True)
        exibir_saida(idioma, "confirm")


    else:
        return "cool"


def headers_Padrao():
    """
    obtenha os cabeçalhos padrao exteo cookies


    :return:
    """

    HEADERS = {
        "accept": "*/*",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "Content-Type": "text/plain",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Cookie": 'COLOQUE SEU COOKIE AQUI',
        "Referer": "https://www.udemy.com/"
    }
    return HEADERS


def FFmpegas(url, titulo, output_dir):
    exibir_saida("Baixando o Vídeo..com ", "info", ao_lado=True)
    exibir_saida("ffmpeg", "erro", ao_lado=True)
    exibir_saida(" - - - > Aguarde...", "sucess")

    saida = str(output_dir) + "/" + str(titulo) + ".mkv"
    try:
        if os.path.exists(saida):
            os.remove(saida)

            # Inicia a conversão de forma assíncrona
        process = ffmpeg.input(url).output(saida).run_async(pipe_stdout=True, pipe_stderr=True)

        # Envia a saída do processo para o cliente em tempo real
        while True:
            output = process.stderr.readline().decode()
            if not output and process.poll() is not None:
                break
        exibir_saida("\t-- >\t", "sucess", ao_lado=True)
        exibir_saida(" Baixado! ", "confirm", ao_lado=True)
        exibir_saida("    <--\n\n", "sucess")
    except Exception as e:
        exibir_saida("ERRO: ", "", ao_lado=True)
        exibir_saida(f" {e}", "erro")


def ObterLNKs(ID_curso, ID_Lecture, head):
    get = f"https://www.udemy.com/api-2.0/users/me/subscribed-courses/{ID_curso}/lectures/{ID_Lecture}/?fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,course_is_drmed,media_sources,captions,thumbnail_sprite,slides,slide_urls,download_urls,external_url&q=0.3108014137011559"
    # Faz a solicitação GET com os cabeçalhos
    response = requests.get(get, headers=head)

    # Exibe o código de status
    if response.status_code == 200:
        # Exibe o conteúdo do arquivo M3U8
        content = json.loads(response.text)
        # Verificar se a URL do vídeo existe
        if 'media_sources' in content['asset'] and len(content['asset']['media_sources']) > 0:
            video_url = content['asset']['media_sources'][0]['src']
        else:
            video_url = ""

        return video_url
    else:
        return "cool"


def ObterItems(link, head):
    pesquisa = link
    get = f"https://www.udemy.com/api-2.0/courses/{pesquisa}/subscriber-curriculum-items/?caching_intent=True&fields%5Basset%5D=title%2Cfilename%2Casset_type%2Cstatus%2Ctime_estimation%2Cis_external&fields%5Bchapter%5D=title%2Cobject_index%2Cis_published%2Csort_order&fields%5Blecture%5D=title%2Cobject_index%2Cis_published%2Csort_order%2Ccreated%2Casset%2Csupplementary_assets%2Cis_free&fields%5Bpractice%5D=title%2Cobject_index%2Cis_published%2Csort_order&fields%5Bquiz%5D=title%2Cobject_index%2Cis_published%2Csort_order%2Ctype&pages&page_size=400&fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,course_is_drmed,media_sources,captions,thumbnail_sprite,slides,slide_urls,download_urls,external_url&q=0.3108014137011559"

    response = requests.get(get, headers=head)
    # Exibe o código de status
    if response.status_code == 200:
        # Exibe o conteúdo do arquivo M3U8
        content = json.loads(response.text)
        return content
    else:
        # Exibe o conteúdo do arquivo M3U8
        content = json.loads(response.text)

        return content


def Menu():
    # Diretório para salvar os segmentos
    output_dir = "Dowloads/"
    os.makedirs(output_dir, exist_ok=True)
    try:
        while True:
            exibir_saida("DIgite o link do seu Curso: ", "confirm", ao_lado=True)

            link = input("")

            if link.startswith("https://"):
                I = link.split("course_id=")
                ID = I[1]

                exibir_saida("DIgite o Cookie: ", "confirm", ao_lado=True)
                COOKIES = input("")
                break
            else:
                exibir_saida("Valores inválido !", "erro")
                continue

        HEADERS = {
            "accept": "*/*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "Content-Type": "text/plain",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "Cookie": COOKIES,
            "Referer": "https://www.udemy.com/"
        }

        Infos(ID, HEADERS)

        v = ObterItems(ID, HEADERS)

        if v != None:
            videos = v.get('results', [])  # Obtém a lista de vídeos ou uma lista vazia se 'results' não existir
            quanti = v.get("count", "N/A")
            links_1 = v.get("next")
            links_2 = v.get("previous")

            exibir_saida("\n\n-------> BAIXANDO VIDEOS DO CURSO", "sucess", ao_lado=True)
            exibir_saida(" <-------\n", "sucess")
            for video_dict in videos:
                asset_video = video_dict.get("asset",
                                             {})  # Obtém o dicionário 'asset' ou um dicionário vazio se não existir
                titulo_do_video = asset_video.get("filename", "")  # Obtém o nome do vídeo ou usa "N/A" se não existir
                id_do_video = video_dict.get("id", "N/A")  # Obtém o ID do vídeo ou usa "N/A" se não existir
                asset_type = asset_video.get("asset_type", "N/a")
                index = video_dict.get("object_index", "N?")
                a = ObterLNKs(ID, id_do_video, HEADERS)

                if a != "cool" and a != "" and a != None:
                    nome = f"{index}.{titulo_do_video}"

                    exibir_saida(f"\n\nTipo: ", "info", ao_lado=True)
                    exibir_saida(f"{asset_type}", "confirm")

                    exibir_saida(f"Titulo: ", "info", ao_lado=True)
                    exibir_saida(f"{index}.{titulo_do_video}", "erro")

                    exibir_saida(f"Link: ", "info", ao_lado=True)
                    exibir_saida(f" {a}\n\n", "confirm")

                    FFmpegas(a, nome)
    except KeyboardInterrupt:
        limpar_tela()
        exibir_saida("INterrompido !\n\n", "erro")
    except Exception as e:

        exibir_saida("ERRO -- > ", "erro", ao_lado=True)
        exibir_saida(e, "confirm")

# Menu()
