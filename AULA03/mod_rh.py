"""Funcoes para cadastro e exibicao de colaboradores."""


def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    """Retorna os dados do colaborador em um dicionario padronizado."""
    return {
        "nome": nome,
        "cargo": cargo,
        "salario": salario,
    }


def exibir_colaboradores(lista_colaboradores: list) -> None:
    """Imprime os colaboradores cadastrados."""
    for colaborador in lista_colaboradores:
        print(
            f"Nome: {colaborador['nome']} | "
            f"Cargo: {colaborador['cargo']} | "
            f"Salario: R$ {colaborador['salario']:.2f}"
        )
