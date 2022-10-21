def quadrante(x, y):
    if(x == 0) or (y == 0):
        return ""
    elif((x > 0) and (y > 0)):
        return "Primeiro Quadrante"
    elif(x < 0) and (y > 0):
        return "Segundo Quadrante"
    elif(x < 0) and (y < 0):
        return "Terceiro Quadrante"
    else:
        return "Quarto Quadrante"





