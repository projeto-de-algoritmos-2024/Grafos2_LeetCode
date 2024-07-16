from typing import List


def longestCycle(self, edges: List[int]) -> int:
    comprimento = -1  # tamanho do maior cliclo encontrado.
    time = 1  # será usada para marcar o tempo de visita dos nós.
    timeVisited = [0] * len(edges)  # lista para armazenar o tempo de visita de cada nó.

    for i in range(len(edges)):  # Percorre todos os nós na lista 'edges'.
        if timeVisited[i]:  # Se o nó já foi visitado, pula para o próximo nó.
            continue
        startTime = time  # Armazena o tempo atual na variável 'startTime'.
        u = i  # Inicializa a variável 'u' com o valor do índice atual 'i'.
        while u != -1 and not timeVisited[u]:  # Continua enquanto 'u' não for -1 e 'u' ainda não foi visitado.
            timeVisited[u] = time  # Marca o nó 'u' com o tempo atual.
            time += 1  # Incrementa o tempo.
            u = edges[u]  # Move para o próximo nó na lista 'edges'.
        if u != -1 and timeVisited[u] >= startTime:  # Se 'u' não for -1 e 'timeVisited[u]' for maior ou igual a 'startTime', um ciclo foi encontrado.
            comprimento = max(comprimento, time - timeVisited[u])  # Atualiza 'comprimento' com o comprimento do ciclo, se for maior que o valor atual de 'comprimento'.

    return comprimento  # Retorna o comprimento do ciclo mais longo encontrado, ou -1 se nenhum ciclo foi encontrado.