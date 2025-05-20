# Boas-vindas 
print("Bem-vindo à Loja de Gelados da Nicole Albuquerque")
print("-------------------------Cardápio-------------------------")
print("---| Tamanho |  Cupuaçu (CP)  |  Açaí (AC)  |---")
print("---|    P    |   R$ 9.00      |  R$ 11.00   |---")
print("---|    M    |   R$ 14.00     |  R$ 16.00   |---")
print("---|    G    |   R$ 18.00     |  R$ 20.00   |---")
print("----------------------------------------------------------\n")

# Atribuindo a condicional total
total = 0

while True:
    # Solicita o sabor. Usei upper para aumentar as letras.
    sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
    if sabor != "CP" and sabor != "AC":
        print("Sabor inválido. Tente novamente\n")  
        continue

    # Solicita o tamanho
    tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente\n")  # [SAÍDA DE CONSOLE 3 de 4]
        continue

    # Estrutura aninhada dos tamanhos, preços com elif e if.
    preco = 0
    if sabor == "CP":
        if tamanho == "P":
            preco = 9.00
        elif tamanho == "M":
            preco = 14.00
        elif tamanho == "G":
            preco = 18.00
    elif sabor == "AC":
        if tamanho == "P":
            preco = 11.00
        elif tamanho == "M":
            preco = 16.00
        elif tamanho == "G":
            preco = 20.00

    # Mostra o item escolhido com preço
    nome_sabor = "Cupuaçu" if sabor == "CP" else "Açaí"
    print(f"Você pediu um {nome_sabor} no tamanho {tamanho}: R$ {preco:.2f}\n")

    # Soma ao acumulador [EXIGÊNCIA DE CÓDIGO 5 de 8]
    total += preco

    # Deseja mais algo? 
    mais = input("Deseja mais alguma coisa? (S/N): ").upper()
    if mais == "N":
        break 
    elif mais != "S":
        print("Resposta inválida. Considerando como 'N'. Encerrando o pedido.")
        break

# Mostra o total final
print(f"\nValor total do pedido: R$ {total:.2f}")
