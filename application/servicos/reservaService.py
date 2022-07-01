def calcularValor(numPessoas, numDias, tipoQuarto):
    valorPorPessoa = 0
    if tipoQuarto == 'S':
        valorPorPessoa = 100
    elif tipoQuarto == 'D':
        valorPorPessoa = 200
    elif tipoQuarto == 'P':
        valorPorPessoa = 300

    return round(numPessoas * valorPorPessoa * numDias, 2)

