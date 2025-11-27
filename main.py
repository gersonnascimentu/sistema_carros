# main.py

from models.carro import Carro

lista = Carro("", "", "").carregar_todos

def marcas_principais():
    marca = "Marca: Fiat"
    modelo = "Modelo: Uno"
    ano = "Ano: 2026"
    carro = Carro(marca, modelo, ano)
    carro.salvar_carro()

    marca = ("Marca: Chevrolet")
    modelo = ("Modelo: Onix")
    ano = ("Ano: 2026")
    carro = Carro(marca, modelo, ano)
    carro.salvar_carro()

    marca = ("Marca: Volkswagen")
    modelo = ("Modelo: Fusca")
    ano = ("Ano: 2026")
    
    carro = Carro(marca, modelo, ano)
    carro.salvar_carro()



def menu():
    print("\n=== SISTEMA DE CADASTRO DE CARROS ===")
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def menu2():
    print("\n=== ESCOLHA A MARCA ===")
    print("1 - Fiat")
    print("2 - Chevrolet")
    print("3 - Volkswagen")
    print("4 - Outras Opções de cadastro")
    print("0 - Voltar")
    

while True:
    opcao = menu()

    if opcao == "1":
        print("\n--- CADASTRAR CARRO ---")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")

        carro = Carro(marca, modelo, ano)
        carro.salvar_carro()

        print("Carro salvo com sucesso!")

    elif opcao == "2":
        print("\n--- LISTA DE CARROS ---")

        lista = Carro("", "", "").carregar_todos()

        if not lista:
            print("Nenhum carro cadastrado ainda.")
        else:
            for c in lista:
                print(f"{c['marca']} - {c['modelo']} - {c['ano']}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("\nOpção inválida!")
