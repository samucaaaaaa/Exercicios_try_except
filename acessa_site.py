from urllib import request

def acessa_site(url:str):
    """
    Essa função recebe a url de um site no formato "http://www.site.com" e verifica se o mesmo está ou não acessível.

    Parameters:
        url: Url do site a ser analisado
    Returs:
        None

    Exemplo válido de uma url:
    >>> url = "http://www.google.com"
    >>> acessa_site(url)
    Consegui acessar o site Google com sucesso

    Exemplo inválido de uma url que não é uma string:
    >>> url = 12345
    >>> acessa_site(url)
    ERRO: A url 12345 informada não é uma string

    Exemplo inválido de uma url que não existe:
    >>> url = "oioioioi"
    >>> acessa_site(url)
    ERRO: Essa url não existe!
    """

    try:
        request.urlopen(url)
        elementos_string = url.split(".")
        nome_site = elementos_string[1].capitalize()
    except (TypeError, AttributeError, UnboundLocalError):
        print(f"ERRO: A url {url} informada não é uma string!") 
    except (ValueError):
        print("ERRO: Essa url não existe!")       
    except:
        print(f"ERRO: O site {nome_site} não está acessível no momento!")
    else: 
        print(f"Consegui acessar o site {nome_site} com sucesso!")
    finally:
        print("Muito obrigado! Volte sempre!")        
    return None

acessa_site("http://www.uol.com")
