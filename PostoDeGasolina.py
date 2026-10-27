pontos1 = []
def media(veiculos, litros_total):
    if veiculos > 0:
        return litros_total / veiculos

def pontos_fidelidade(preco):
    pontos = preco * 0.10
    pontos1.append(pontos)
    return pontos
def finalização(litros,preco):
    print("\n----- ATENDIMENTO FINALIZADO -----")
    print(f"Litros abastecidos: {litros:.2f} L")
    print(f"Valor total a pagar: R$ {preco:.2f}")
def pay(pontos, preco):
    ponto_fidel = pontos * 0.10
    print("---Pagamento---")
    print("Escolha a Forma de Pagamento:")
    print("1- Pix")
    print("2- Débito")
    print("3- Crédito")
    print("4- Pontos Fidelidade")
    opcao = int(input("Escolha uma das opções: "))
    if opcao == 1:
        print("Gerando Chave Pix...")
        print("CHAVE PIX:60.964.458/0001-92")
        finalização()
    if opcao == 2:
        print("Aproxime ou Insira Seu Cartão de Débito:")
        finalização()
    if opcao == 3:
        print("Aproxime ou Insira Seu Cartão de Crédito:")
        finalização()
    if opcao == 4:
        pontos_fidelidade(preco)
        finalização()

def menu():
    valor_total = 0.0
    veiculos = 0
    litros_total = 0
    veiculos_acima_40l = 0

    
    comum = 6.70
    aditivada = 6.80
    premium = 8.50

    gnv = 4.7
    diesel= 6.8
    etanol= 3.9

    opcao = -1

    while opcao != 0:
        print ("1 - Gasolina | 2 - G.N.V | 3 - Etanol | 4 - Diesel | 5 - Relátorio | 0 - Encerrar Sistema")
        opcao = int(input("Escolha o Tipo De Combustível:"))
        if opcao == 1:
            
            print ("1 - Gasolina Comum")
            print ("2 - Gasolina Aditivada")
            print ("3 - Gasolina Premium")

            escolha = int(input("Escolha O Tipo de Gasolina: "))
            if escolha == 1:
                litros = float(input("Litros à Abastecer: "))
                if litros >= 40:
                    veiculos_acima_40l += 1

                print("Litros Abastecidos:", litros)
                print(f"Valor Total à Pagar: {preco:.2f}")

                veiculos += 1
                litros_total += litros
                valor_total += preco
                pay()
            elif escolha == 2:
                litros = float(input("Litros à Abastecer: "))
                if litros >= 40:
                    veiculos_acima_40l += 1
                    preco = aditivada * litros

                    print("Litros Abastecidos:", litros)
                    print(f"Valor Total à Pagar: {preco:.2f}")

                    veiculos += 1
                    litros_total += litros
                    valor_total += preco
                    pay()
            elif escolha == 3:
                litros = float(input("Litros à Abastecer: "))
                if litros >= 40:
                    veiculos_acima_40l += 1
                    preco = premium * litros
                    print("Litros Abastecidos:", litros) 
                    print(f"Valor Total à Pagar: {preco:.2f}")

                    veiculos += 1
                    litros_total += litros
                    valor_total += preco
                    pay()
            else:
                print("Tipo De Gasolina Invalido!")
                continue
                
        elif opcao == 2:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
                preco = gnv * litros

                veiculos += 1
                litros_total += litros
                valor_total += preco
                pay()
        elif opcao == 3:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
                preco = etanol * litros
       
                veiculos += 1
                litros_total += litros
                valor_total += preco
                pay()
        elif opcao == 4:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
                preco = diesel * litros
     

                veiculos += 1
                litros_total += litros
                valor_total += preco
                pay()
        elif opcao == 5:
            media_litros = media(veiculos, litros_total)
            print("|---------RELÁTORIO-----------------------|")
            print(f"| Veículos Atendidos:{veiculos:<16}     |")
            print(f"| Valor Total Arrecadado:R${valor_total:<15}|")
            print(f"| Litros Totais Abastecidos:{litros_total:<14}|")
            print(f"| Média de Litros por Veículos:{media_litros:<11}|")
            print(f"| Veículos com 40 Litros ou mais:{veiculos_acima_40l:<9}|")
            print("|-----------------------------------------|")
        elif opcao == 0:
            print("Sistema Encerrado")
        else:
            print("Opção Invalida!")

menu()