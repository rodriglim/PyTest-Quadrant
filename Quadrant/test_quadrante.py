import funcaoQuadrante

def testar():

    x = -4
    y = 15

    quadranteResultado1 = funcaoQuadrante.quadrante(x, y)

    assert quadranteResultado1 == "Segundo Quadrante"

    x = -4
    y =  -8

    quadranteResultado2 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado2 == "Terceiro Quadrante"

    x = 4
    y =  -8

    quadranteResultado3 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado3 == "Quarto Quadrante"

    
    x = 4
    y = 8

    quadranteResultado4 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado4 == "Primeiro Quadrante"

    
    x = 0
    y =  -8

    quadranteResultado5 = funcaoQuadrante.quadrante(x, y)
    assert quadranteResultado5 == "Quarto Quadrante"