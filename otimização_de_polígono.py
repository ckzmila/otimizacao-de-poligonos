# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def problem1(coordinate_list):
    """
    Remove pontos redundantes de um polígono!

    Args:
        coordinate_list (list[tuple[int, int]]):
            Lista de tuplas (x, y) representando os vértices do polígono em ordem.

    Returns:
        list[tuple[int, int]]: Lista otimizada de vértices (x, y) sem pontos redundantes.
    """
    optimized_polygon = []

    # Adiciona o primeiro ponto
    if coordinate_list:
        optimized_polygon.append(coordinate_list[0])

    # Percorre todos os pontos, exceto o primeiro e o último
    for i in range(1, len(coordinate_list) - 1):
        x1, y1 = optimized_polygon[-1]       # Último ponto mantido
        x2, y2 = coordinate_list[i]          # Ponto atual
        x3, y3 = coordinate_list[i + 1]      # Próximo ponto

        # Mantém o ponto se este não for colinear
        if (x3 - x1) * (y2 - y1) != (x2 - x1) * (y3 - y1):
            optimized_polygon.append((x2, y2))

    # Adiciona o último ponto
    optimized_polygon.append(coordinate_list[-1])

    return optimized_polygon


def get_points_from_user():
    """
    Solicita ao usuário que insira pontos manualmente no formato x,y.
    """
    points = []
    print("Digite as coordenadas no formato x,y. Digite 'fim' para encerrar:")
    while True:
        entrada = input("Ponto: ")
        if entrada.lower() == "fim":
            break
        try:
            x, y = map(int, entrada.split(","))
            points.append((x, y))
        except:
            print("Formato inválido! Use x,y (exemplo: 1,2)")
    return points


def plot_polygons(original, optimized):
    """
    Plota o polígono original e o otimizado lado a lado.
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Original
    ox, oy = zip(*original)
    axs[0].plot(ox, oy, marker="o")
    axs[0].set_title("Polígono Original")

    # Otimizado
    nx, ny = zip(*optimized)
    axs[1].plot(nx, ny, marker="o", color="green")
    axs[1].set_title("Polígono Otimizado")

    plt.show()


if __name__ == "__main__":
    print("Escolha uma opção:")
    print("1 - Usar polígono do teste")
    print("2 - Inserir meus próprios pontos")

    escolha = input("Opção: ")

    if escolha == "1":
        points = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4),
                  (3, 3), (3, 2), (2, 2), (2, 1), (1, 1)]
    else:
        points = get_points_from_user()

    optimized_points = problem1(points)

    print("\nPontos originais:", points)
    print("Pontos otimizados:", optimized_points)

    # Mostrar visualmente
    plot_polygons(points, optimized_points)
