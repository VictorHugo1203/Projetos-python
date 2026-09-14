def media(veiculos, litros_total):
    if veiculos > 0:
        return litros_total / veiculos

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

    opcao = 10

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
                preco = comum * litros

                print("Litros Abastecidos:", litros)
                print(f"Valor Total à Pagar: {preco:.2f}")

                veiculos += 1
                litros_total += litros
                valor_total += preco

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
            else:
                print("Tipo De Gasolina Invalido!")
                continue
                
            print("\n----- ATENDIMENTO FINALIZADO -----")
            print(f"Litros abastecidos: {litros:.2f} L")
            print(f"Valor total a pagar: R$ {preco:.2f}")
                
            veiculos += 1
            litros_total += litros
            valor_total += preco
                
            if litros >= 40:
                veiculos_acima_40l += 1

        elif opcao == 2:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
            preco = gnv * litros

            print("\n----- ATENDIMENTO FINALIZADO -----")
            print(f"Litros abastecidos: {litros:.2f} L")
            print(f"Valor total a pagar: R$ {preco:.2f}")

            veiculos += 1
            litros_total += litros
            valor_total += preco
            
        elif opcao == 3:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
            preco = etanol * litros

            print("\n----- ATENDIMENTO FINALIZADO -----")
            print(f"Litros abastecidos: {litros:.2f} L")
            print(f"Valor total a pagar: R$ {preco:.2f}")

            veiculos += 1
            litros_total += litros
            valor_total += preco

        elif opcao == 4:
            litros = float(input("Litros à Abastecer: "))
            if litros >= 40:
                veiculos_acima_40l += 1
            preco = diesel * litros
            
            print("\n----- ATENDIMENTO FINALIZADO -----")
            print(f"Litros abastecidos: {litros:.2f} L")
            print(f"Valor total a pagar: R$ {preco:.2f}")

            veiculos += 1
            litros_total += litros
            valor_total += preco

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