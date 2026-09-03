"""Menu principal do cadastro de colaboradores."""

from mod_rh import cadastrar_colaborador, exibir_colaboradores


def main() -> None:
    """Executa o menu interativo do sistema de RH."""
    colaboradores = []

    while True:
        print("\n1 - Cadastrar")
        print("2 - Listar")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            cargo = input("Cargo: ").strip()
            salario = float(input("Salario: ").replace(",", "."))
            colaboradores.append(
                cadastrar_colaborador(nome, cargo, salario)
            )
            print("Colaborador cadastrado com sucesso.")
        elif opcao == "2":
            exibir_colaboradores(colaboradores)
        elif opcao == "0":
            print("Encerrando o sistema.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
