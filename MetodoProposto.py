import numpy as np

def methodProposed(f, df, x0, x1, rtol=0.000001, n = 100):

    if f(x0)*f(x1) > 0:
        print("Não existe raiz")
        return

    iteracao = 0
    xn = x0
    erroAtual = 0


    while True:
        xnAnterior = xn

        if df(x0) == 0:
            temp = x0
            x0 = x1
            x1 = temp

        xn = (1 / 2 * (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))) + 1 / 2 * (x0 - (f(x0) / df(x0)))
        iteracao = iteracao + 1
        if xn != 0:
            erroAtual = np.abs((xn - xnAnterior)/xn)*100

        if f(xn)*f(x0) < 0:
            if np.abs(f(x0)) < np.abs(f(xn)):
                continue
            else:
                x1 = x0
                x0 = xn

        elif f(xn)*f(x0) > 0:
            if np.abs(f(xn)) < np.abs(f(x1)):
                x0 = xn
            else:
                x0 = x1
                x1 = xn
        else:
            erroAtual = 0

        if erroAtual <= rtol or iteracao >= n:
            break

    return xn
