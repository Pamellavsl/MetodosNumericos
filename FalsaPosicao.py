def falsaPosicao(f, xu, xl, erro, itMax):
    num_iteracoes  = 0
    x = xu
    erro_inicial = 1
    while(erro_inicial  >= erro and num_iteracoes <itMax):
        x_ = x
        x = xu - f(xu) * (xl - xu) / (f(xl) - f(xu))
        erro_inicial  = np.abs(x - x_ /x)
        if(f(xu)*f(x) < 0):
            xl = x
        else:
            xu = x
        num_iteracoes = num_iteracoes  + 1
    return x
