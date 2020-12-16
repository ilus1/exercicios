'''
nome = "Fernando Miranda Calil"
matricula = "19/0106565"
email = "ilusdasilva@email.com"
usuario_github = "ilus1"
'''


# Conjunto de estados válidos
Q = {"A", "B", "C", "D"}

# Alfabeto de entrada
alfabeto = {"a", "b", "c"}

# Estado inicial
q0 = "A"

# Conjunto de estados finais
finais = {"D"}

# Tabela de transição
transicoes = {
    ("A", "b"): "B",
    ("B", "a"): "B",
    ("B", "c"): "C",
    ("B", "b"): "D",
    ("D", "b"): "A",
    ("C", "a"): "B",
}


def automaton(transicoes, q0, finais, input_string):
    state = q0

    for c in input_string:
        old = state
        try:
            state = transicoes[state, c]
        except KeyError:
            state = None

    return state in finais


st = input("Entrada: ")
print("Aceito")if automaton(transicoes, q0, finais, st) else print("Rejeitado")
