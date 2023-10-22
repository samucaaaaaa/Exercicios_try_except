def le_int(mensagem):
    while True:
        try:
            n = int(input(mensagem))
        except (ValueError, TypeError):
            print("ERRO: Digite um número inteiro válido!")
            continue
        except (KeyboardInterrupt):
            print("ERRO: Usuário preferiu não informar esse número!")
            break
        except Exception as erro:
            print("O ERRO encontrado foi: ", erro)
            break
        else: 
            return n
      
n = le_int("Digite um número: ")
print("O seu número é:",n)

