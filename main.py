import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from scipy import constants
from scipy import integrate


def psi_function(Lx, Ly, Lz, n1, n2, n3, x, y, z):
    return np.sqrt(8 / (Lx * Ly * Lz)) * np.sin(np.pi * n1 * x / Lx) * np.sin(np.pi * n2 * y / Ly) \
           * np.sin(np.pi * n3 * z / Lz)


def energy(Lx, Ly, Lz, n1, n2, n3):
    return sc.constants.h ** 2 / 8 / sc.constants.m_e * ((n1 / Lx) ** 2 + (n2 / Ly) ** 2 + (n3 / Lz) ** 2) * 10e12


if __name__ == '__main__':
    Lx = float(input("Введите положительное Lх, мкм: "))
    while not (Lx > 0):
        print("Величина введена неверно")
        Lx = float(input("Введите положительное Lх, мкм: "))
    Ly = float(input("Введите положительное Ly, мкм: "))
    while not (Ly > 0):
        print("Величина введена неверно")
        Ly = float(input("Введите положительное Ly, мкм: "))
    Lz = float(input("Введите положительное Lz, мкм: "))
    while not (Lz > 0):
        print("Величина введена неверно")
        Lz = float(input("Введите положительное Lz, мкм: "))
    n1 = int(input("Введите положительное целое n1: "))
    while not (n1 > 0):
        print("Величина введена неверно")
        n1 = int(input("Введите положительное целое n1: "))
    n2 = int(input("Введите положительное целое n2: "))
    while not (n2 > 0):
        print("Величина введена неверно")
        n2 = int(input("Введите положительное целое n2: "))
    n3 = int(input("Введите положительное целое n3: "))
    while not (n3 > 0):
        print("Величина введена неверно")
        n3 = int(input("Введите положительное целое n3: "))

    print("Энергия электрона:", energy(Lx, Ly, Lz, n1, n2, n3), "Дж")

    print("Введите границы области, в которой нужно найти вероятность нахождения электрона")
    x1 = float(input("Введите положительное x1 от 0 до Lх, мкм: "))
    while not (0 <= x1 < Lx):
        print("Величина введена неверно")
        x1 = float(input("Введите положительное x1 от 0 до Lх, мкм: "))
    x2 = float(input("Введите положительное x2 от x1 до Lх, мкм: "))
    while not (x1 < x2 <= Lx):
        print("Величина введена неверно")
        x2 = float(input("Введите положительное x2 от x1 до Lх, мкм: "))
    y1 = float(input("Введите положительное y1 от 0 до Ly, мкм: "))
    while not (0 <= y1 < Ly):
        print("Величина введена неверно")
        y1 = float(input("Введите положительное y1 от 0 до Ly, мкм: "))
    y2 = float(input("Введите положительное y2 от y1 до Ly, мкм: "))
    while not (y1 < y2 <= Ly):
        print("Величина введена неверно")
        y2 = float(input("Введите положительное y2 от y1 до Ly, мкм: "))
    z1 = float(input("Введите положительное z1 от 0 до Lz, мкм: "))
    while not (0 <= z1 < Lz):
        print("Величина введена неверно")
        z1 = float(input("Введите положительное z1 от 0 до Lz, мкм: "))
    z2 = float(input("Введите положительное z2 от z1 до Lz, мкм: "))
    while not (z1 < z2 <= Lz):
        print("Величина введена неверно")
        z2 = float(input("Введите положительное z2 от z1 до Lz, мкм: "))


    def density(x, y, z):
        return psi_function(Lx, Ly, Lz, n1, n2, n3, x, y, z) ** 2


    print("Вероятность нахождения электрона в указанной области:",
          integrate.tplquad(density, x1, x2, y1, y2, z1, z2)[0] * 100, "%")

    variable = input("Введите переменную (x, y, или z), значение которой будет зафиксировано для построения графиков: ")
    while not (variable == "x" or variable == "y" or variable == "z"):
        print("Величина введена неверно")
        variable = input(
            "Введите переменную (x, y, или z), значение которой будет зафиксировано для построения графиков: ")
    variable_value = float(input("Введите значение, которое будет зафиксировано для построения графиков: от 0 до L "
                                 "соответствующей переменной, мкм: "))

    if variable == "x":
        while not (0 < variable_value < Lx):
            print("Величина введена неверно")
            variable_value = float(
                input("Введите значение, которое будет зафиксировано для построения графиков: от 0 до Lx"))
        VAR1 = np.arange(-0.1 * Ly, 1.1 * Ly, Ly * 0.001)
        VAR2 = np.arange(-0.1 * Lz, 1.1 * Lz, Lz * 0.001)
        VAR1, VAR2 = np.meshgrid(VAR1, VAR2)
        PSI = psi_function(Lx, Ly, Lz, n1, n2, n3, variable_value, VAR1, VAR2)
        DENSITY = density(variable_value, VAR1, VAR2)
        var1_string = "y"
        var2_string = "z"
        fixed_var_string = "x"
    if variable == "y":
        while not (0 < variable_value < Ly):
            print("Величина введена неверно")
            variable_value = float(
                input("Введите значение, которое будет зафиксировано для построения графиков: от 0 до Ly"))
        VAR1 = np.arange(-0.1 * Lx, 1.1 * Lx, Lx * 0.001)
        VAR2 = np.arange(-0.1 * Lz, 1.1 * Lz, Lz * 0.001)
        VAR1, VAR2 = np.meshgrid(VAR1, VAR2)
        PSI = psi_function(Lx, Ly, Lz, n1, n2, n3, VAR1, variable_value, VAR2)
        DENSITY = density(VAR1, variable_value, VAR2)
        var1_string = "x"
        var2_string = "z"
        fixed_var_string = "y"
    if variable == "z":
        while not (0 < variable_value < Lz):
            print("Величина введена неверно")
            variable_value = float(
                input("Введите значение, которое будет зафиксировано для построения графиков: от 0 до Lz"))
        VAR1 = np.arange(-0.1 * Lx, 1.1 * Lx, Lx * 0.001)
        VAR2 = np.arange(-0.1 * Ly, 1.1 * Ly, Ly * 0.001)
        VAR1, VAR2 = np.meshgrid(VAR1, VAR2)
        PSI = psi_function(Lx, Ly, Lz, n1, n2, n3, VAR1, VAR2, variable_value)
        DENSITY = density(VAR1, VAR2, variable_value)
        var1_string = "x"
        var2_string = "y"
        fixed_var_string = "z"

    fig1 = plt.figure()
    ax = fig1.add_subplot(projection='3d')
    ax.plot_surface(VAR1, VAR2, PSI, alpha=0.9)
    plt.xlabel(var1_string)
    plt.ylabel(var2_string)
    plt.title("Волновая функция при зафиксированном значении " + fixed_var_string + " = " + str(variable_value))
    plt.show()

    fig2 = plt.figure()
    ax = fig2.add_subplot(projection='3d')
    ax.plot_surface(VAR1, VAR2, DENSITY, alpha=0.9)
    plt.xlabel(var1_string + ", мкм")
    plt.ylabel(var2_string + ", мкм")
    plt.title("Квадрат волновой функции (плотность вероятности) \n при зафиксированном значении "
              + fixed_var_string + " = " + str(variable_value))
    plt.show()
