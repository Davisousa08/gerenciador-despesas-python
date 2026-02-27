from services import adicionar_despesa, listar_despesas, total_por_categoria

def menu():
    while True:
        print("\n=== Gerenciador de Despesas Pessoais ===")
        print("1. Adicionar despesa")
        print("2. Listar todas despesas")
        print("3. Ver total por categoria")
        print("4. Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            descricao = input("Descrição (ex: Dogão do calçadão): ")
            categoria = input("Categoria (ex: Alimentação, Transporte): ")
            while True:
                try:
                    valor = float(input("Valor (ex: 15.50): "))
                    break
                except ValueError:
                    print("Valor inválido, digite um número.")
            adicionar_despesa(descricao, categoria, valor)

        elif opcao == '2':
            listar_despesas()

        elif opcao == '3':
            total_por_categoria()

        elif opcao == '4':
            print("Tchau! Controle seus gastos e boa sorte!")
            break

        else:
            print("Opção inválida, tenta de novo.")

if __name__ == "__main__":
    menu()