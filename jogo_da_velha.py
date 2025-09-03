#=========================================================================================
# AD1 Fundamentos da Programação                                                         |
# Nome: Laredo Alvaro Nunes                                                              |
# Polo: Angra dos Reis                                                                   |
#=========================================================================================
def exibir_tabuleiro(tabuleiro):
    for i in range(3):
        linha = "|".join(tabuleiro[i])
        print(" " + linha)
        if i < 2:
            print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Linhas, colunas e diagonais
    for i in range(3):
        if all([tabuleiro[i][j] == jogador for j in range(3)]) or all([tabuleiro[j][i] == jogador for j in range(3)]):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    return all([celula in ['X', 'O'] for linha in tabuleiro for celula in linha])

def obter_posicao(tabuleiro):
    while True:
        try:
            pos = int(input("Escolha uma posição (1-9): ")) - 1
            if pos < 0 or pos > 8:
                print("Posição inválida.")
                continue
            linha, coluna = divmod(pos, 3)
            if tabuleiro[linha][coluna] in ['X', 'O']:
                print("Posição ocupada. Escolha outra.")
                continue
            return linha, coluna
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 9.")

def jogar():
    partidas = 0
    vitorias_x = 0
    vitorias_o = 0
    empates = 0

    while True:
        tabuleiro = [['_'] * 3 for _ in range(3)]
        jogador_atual = 'X'
        partidas += 1

        while True:
            print(f"\nJogador {jogador_atual}, sua vez:")
            exibir_tabuleiro(tabuleiro)
            linha, coluna = obter_posicao(tabuleiro)
            tabuleiro[linha][coluna] = jogador_atual

            if verificar_vitoria(tabuleiro, jogador_atual):
                exibir_tabuleiro(tabuleiro)
                print(f"\nJogador {jogador_atual} venceu!")
                if jogador_atual == 'X':
                    vitorias_x += 1
                else:
                    vitorias_o += 1
                break

            if verificar_empate(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print("\nEmpate!")
                empates += 1
                break

            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        print(f"\nPlacar até agora:")
        print(f"Partidas: {partidas} | Vitórias X: {vitorias_x} | Vitórias O: {vitorias_o} | Empates: {empates}")

        resposta = input("\nDesejam jogar novamente? (s/n): ").lower()
        if resposta != 's':
            print("Encerrando o jogo.")
            break

if __name__ == "__main__":
    jogar()