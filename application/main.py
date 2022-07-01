from servicos.reservaService import calcularValor
from servicos.metodosBancoService import inserir, getByCpf, setarCheckInOuCheckOut, atualizarDados, getAllByCpf, \
    getAllByCpfEStatus
from time import sleep

opcoesMenu = {1: 'Cadastrar uma reserva',
              2: 'Entrada do cliente (Check in)',
              3: 'Saída do cliente (Check out)',
              4: 'Alterar reserva',
              5: 'Relatórios',
              6: 'Sair'}

contadorReservas = 0
sairDaAplicacao = False

def realizarCheckInOuCheckOut(condicao, set, tipo):
    print('-' * 5, f'{tipo}', '-' * 5)
    reservaEscolhida = 'ç2as,dzaksd'
    dicionarioReservas = {}
    reservas = []
    while reservas == []:
        cpf = input('Cpf para realizar check-in: ')
        reservas = getByCpf(cpf, condicao)
        if reservas == []:
            print('Nenhum registro encontrado')
    if len(reservas) > 1:
        print('-' * 3, f'{len(reservas)} Reservas encontradas', '-' * 3)
        for i in range(0, len(reservas)):
            print(f'Reserva {i} = Tipo quarto: {reservas[i][4]}, número de pessoas: {reservas[i][3]}')
            dicionarioReservas.update({i: reservas[i][0]})

        while not reservaEscolhida in dicionarioReservas.keys():
            try:
                reservaEscolhida = int(input('Digite o número da reserva escolhida: '))
                if not reservaEscolhida in dicionarioReservas.keys():
                    print('Valor inexistente')
                else:
                    reservaEscolhida = dicionarioReservas[reservaEscolhida]
                    break
            except:
                print('Valor digitado incorretamente')

    else:
        reservaEscolhida = reservas[0][0]

    setarCheckInOuCheckOut(reservaEscolhida, set)
    print('-' * 30, f'{tipo} realizado com sucesso!', '-' * 30)
    sleep(3)


def realizarBusca(cpf, status):
    reservas = getAllByCpfEStatus(cpf, status)

    if not reservas == []:
        for i in range(0, len(reservas)):
            print(f'\n{i + 1} - Reserva {status}: ')
            print(f'Nome pessoa titular: {reservas[i][0]}')
            print(f'CPF pessoa titular: {reservas[i][1]}')
            print(f'Número de pessoas: {reservas[i][2]}')
            print(f'Número do quarto: {reservas[i][3]}')
            print(f'Número de dias: {reservas[i][4]}')
            print(f'Valor: {reservas[i][5]}')
            print(f'Status: {reservas[i][6]}')
        return True


while not sairDaAplicacao:
    print('\n', '=' * 20)
    for opcaoNum in opcoesMenu:
        print(opcaoNum, '-', opcoesMenu.get(opcaoNum))

    print('=' * 20)
    opcaoEscolhida = 10
    while opcaoEscolhida != 1 and opcaoEscolhida != 2 and opcaoEscolhida != 3 and opcaoEscolhida != 4 and opcaoEscolhida != 5 and opcaoEscolhida != 6:
        try:
            opcaoEscolhida = int(input('Escolha uma das opções: '))
            if opcaoEscolhida != 1 and opcaoEscolhida != 2 and opcaoEscolhida != 3 and opcaoEscolhida != 4 and opcaoEscolhida != 5 and opcaoEscolhida != 6:
                print('Opção inválida')
        except:
            print('\nSomente números são aceitos')

    print('\n')
    if opcaoEscolhida == 1:
        print('-' * 5, 'Cadastro de Reservas', '-' * 5)
        processoFinalizado = False
        while not processoFinalizado:
            try:
                nome = input('Nome da pessoa titular: ').strip()
                cpf = input('CPF: ').strip()
                numPessoas = int(input('Número de pessoas: '))
                tipoQuarto = 'Y'
                while tipoQuarto != 'S' and tipoQuarto != 'D' and tipoQuarto != 'P':
                    tipoQuarto = input('Tipo do Quarto ( S – Standar, D – Deluxe, P – Premium): ').upper().strip()
                    if tipoQuarto != 'S' and tipoQuarto != 'D' and tipoQuarto != 'P':
                        print('Tipo de quarto inválido')
                numDias = int(input('Número de dias: '))
                valor = calcularValor(numPessoas, numDias, tipoQuarto)
                status = 'Y'
                while status != 'C' and status != 'A' and status != 'F' and status != 'R':
                    status = input('Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado): ').upper().strip()
                    if status == '':
                        status = 'R'
                        break
                    elif status != 'C' and status != 'A' and status != 'F' and status != 'R':
                        print('Status inválido')

                processoFinalizado = True
                inserir((nome, cpf, numPessoas, tipoQuarto, numDias, valor, status))
                print('-' * 30, 'Cadastro realizado com sucesso!', '-' * 30)
                sleep(3)

            except:
                print('Digitação incorreta')

    elif opcaoEscolhida == 2:
        realizarCheckInOuCheckOut('R', 'A', 'Check-in')

    elif opcaoEscolhida == 3:
        realizarCheckInOuCheckOut('A', 'F', 'Check-out')

    elif opcaoEscolhida == 4:
        print('-' * 5, 'Alterar dados', '-' * 5)
        reservaEscolhida = 'ç2as,dzaksd'
        dicionarioReservas = {}
        reservas = []
        while reservas == []:
            cpf = input('Cpf para realizar alteração: ')
            reservas = getAllByCpf(cpf)
            if reservas == []:
                print('Nenhum registro encontrado')
        if len(reservas) > 1:
            print('-' * 3, f'{len(reservas)} Reservas encontradas', '-' * 3)
            for i in range(0, len(reservas)):
                print(f'Reserva {i} = Tipo quarto: {reservas[i][4]}, número de pessoas: {reservas[i][3]}')
                dicionarioReservas.update({i: reservas[i][0]})

            while not reservaEscolhida in dicionarioReservas.keys():
                try:
                    reservaEscolhida = int(input('Digite o número da reserva escolhida: '))
                    if not reservaEscolhida in dicionarioReservas.keys():
                        print('Valor inexistente')
                    else:
                        reservaEscolhida = dicionarioReservas[reservaEscolhida]
                        break
                except:
                    print('Valor digitado incorretamente')

        else:
            reservaEscolhida = reservas[0][0]

        processoFinalizado = False
        while not processoFinalizado:
            try:
                numPessoas = int(input('Número de pessoas: '))
                tipoQuarto = 'Y'
                while tipoQuarto != 'S' and tipoQuarto != 'D' and tipoQuarto != 'P':
                    tipoQuarto = input('Tipo do Quarto ( S – Standar, D – Deluxe, P – Premium): ').upper().strip()
                    if tipoQuarto != 'S' and tipoQuarto != 'D' and tipoQuarto != 'P':
                        print('Tipo de quarto inválido')
                numDias = int(input('Número de dias: '))
                valor = calcularValor(numPessoas, numDias, tipoQuarto)
                status = 'Y'
                while status != 'C' and status != 'A' and status != 'F' and status != 'R':
                    status = input('Status (R - Reservado, C – Cancelado, A – Ativo, F - Finalizado): ').upper().strip()
                    if status == '':
                        status = 'R'
                        break
                    elif status != 'C' and status != 'A' and status != 'F' and status != 'R':
                        print('Status inválido')

                processoFinalizado = True
                atualizarDados(numPessoas, tipoQuarto, numDias, valor, status, reservaEscolhida)
                print('-' * 30, f'Atualização realizada com sucesso!', '-' * 30)
                sleep(3)

            except:
                print(processoFinalizado)
                print('Digitação incorreta')

    elif opcaoEscolhida == 5:
        print('-' * 5, 'Relatório de reservas: ', '-' * 5)
        cpf = input('Cpf para realizar busca: ')
        a = realizarBusca(cpf, 'R')
        b = realizarBusca(cpf, 'C')
        c = realizarBusca(cpf, 'A')
        d = realizarBusca(cpf, 'F')

        if not(a or b or c or d):
            print(f'\nSem reservas para o cpf {cpf}')

        print('-' * 30, f'Relatórios emitidos com sucesso!', '-' * 30)
        sleep(3)


    elif opcaoEscolhida == 6:
        print('-' * 3, 'Processo finalizado com sucesso', '-' * 3)
        sairDaAplicacao = True
        break
