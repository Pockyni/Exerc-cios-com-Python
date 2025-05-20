def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
#escollha do serviço caso nao for a opção vai ser inválido. 
        servico = input(">>").upper()

        if servico in ["DIG", "ICO", "IPB", "FOT"]:
            return servico
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")


def num_pagina():
    while True:
        try:
            #escolha dods numeros de paginas com limite...
            paginas = int(input("\nEntre com o número de páginas: "))
            if paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez.")
                print("Por favor, entre com o número de páginas novamente.")
            elif paginas <= 0:
                print("Número inválido. Digite um valor positivo.")
            else:
                return paginas
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

#adicionar mais serviços e retorno do valor. 
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")

        opcao = input(">>")
        if opcao == "1":
            return 15.00
        elif opcao == "2":
            return 40.00
        elif opcao == "0":
            return 0.00
        else:
            print("Opção inválida, escolha novamente.")


def main():
    print("Bem vindo a Copiadora da Nicole Albuquerque")

    servico = escolha_servico()
    paginas = num_pagina()

    # Preço por serviço
    precos = {
        "DIG": 1.10,
        "ICO": 1.00,
        "IPB": 0.40,
        "FOT": 0.20
    }
#condicional
    preco_unitario = precos[servico]

    # Aplica desconto se necessário
    if paginas >= 200:
        preco_unitario *= 0.85  # 15% de desconto

    extra = servico_extra()

    total = (preco_unitario * paginas) + extra

    print(f"\nTotal: R$ {total:.2f} (serviço: {preco_unitario:.2f} * páginas: {paginas} + extra: {extra:.2f})")


# Executa o programa
main()
