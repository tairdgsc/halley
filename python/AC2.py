from ListaEncadeada import *
onibus = ListaEncadeada()
motorista = ListaEncadeada()
rotas = ListaEncadeada()

def cadOnibus():
    onibusModelo = input('Olá para cadastrar o onibus informe A para automatico e M para manual ').upper()
    while (not onibusModelo == "A" and not onibusModelo == "M"):
        onibusModelo = input('Olá para cadastrar o onibus informe A para automatico e M para manual ').upper()
    onibusModelo = onibusModelo + input('Informe um número de série ')
    print(onibusModelo)
    onibus.insere_no_inicio(onibus, onibusModelo)
    print(onibus)

def cadMotorista():
        print("Cadastro de motorista")
        infMotorista = input("Informe um nome a ser cadastrado\n")
        cadDeficiencia = input("O motorista tem alguma deficiência \nque necessita veículo adaptado?\nSim ou não?\n").upper()
        while(not cadDeficiencia == "SIM" and not cadDeficiencia == ("NÃO")):
            cadDeficiencia = input("O motorista tem alguma deficiência \nque necessita veículo adaptado?\nSim ou não?").upper()
        motorista.insere_no_inicio(motorista, infMotorista)
        motorista.insere_no_inicio(motorista, cadDeficiencia)
        print(motorista)

def cadRota():
    linhaNumDias = int(input("Essa linha corre quantos dias\n"))
    if(linhaNumDias < 0 and linhaNumDias > 7):
        print("O valor tem que ser superior a 0 e menor que 8")
        return(cadRota())
    for i in range(linhaNumDias-1):
        print("1 - Domingo")
        print("2 - Segunda-feira")
        print("3 - Terça-feira")
        print("4 - Quarta-feira")
        print("5 - Quinta-feira")
        print("6 - Sexta-feira")
        print("7 - Sábado")
        dia = -1
        diaJaCad = [None] * 8
        horaInicial = -1
        horaFinal = -1
        minutosInicial = -1
        minutosFinal = -1
        while(True):
            linhaNumDias = linhaNumDias -1
            dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))
            while(dia < 1 and dia > 7):
                dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))
            if diaJaCad[dia] == None:
                diaJaCad[dia] = dia
            else:
                while not diaJaCad[dia] == None:
                    dia = int(input("Esse dia já foi cadastrado, informe outro dia:\n"))
                diaJaCad[dia] = dia

            if(linhaNumDias == 0):
                break
        while(horaInicial < 0 or horaInicial > 23):
            horaInicial = int(input("informe o horário inicial da linha entre 00 a 23\n"))
        while(minutosInicial < 0 or minutosInicial > 59):
            minutosInicial = int(input("Informe um valor para minutos válido\n"))
        while(horaFinal < 0 or horaFinal > 23):
            horaFinal = int(input("informe o horário final da linha entre 00 a 23\n"))
        while(minutosFinal < 0 or minutosFinal > 59):
            minutosFinal = int(input("Informe um valor para minutos válido\n"))
        Sdia = str(dia)
        ShoraInicial = str(horaInicial)
        SminutosInicial  = str(minutosInicial)
        ShoraFinal = str(horaFinal)
        SminutosFinal = str(minutosFinal)
        horaEdia = (Sdia + " " + ShoraInicial + ":" + SminutosInicial + " às " + ShoraFinal + ":" + SminutosFinal)
        horaEdia = horaEdia + horaEdia
        rotas.insere_no_inicio(rotas, horaEdia)

    linhaNome = input("Informe um código para a linha\n")
    while(rotas.busca(rotas, linhaNome)):
        print("Esta linha já existe em nosso banco de dados")
        linhaNome = input("Informe um código para a linha\n")
    rotas.insere_no_inicio(rotas, linhaNome)
    
    print(rotas)

while True:
    print('Olá usuário o que deseja fazer?')
    print('1 - Cadastrar ônibus')
    print('2 - Cadastrar motorista')
    print('3 - Horário de rotas')
    print('5 - Horário para motoristas')
    print('6 - Designar ônibus')
    print('7 - Realizar check-in')
    print('8 - Cadastrar cobrador')
    print('8 - Colocar cobrador')
    selecaoNum = int(input('0 - Sair\n'))
    if(selecaoNum == 0):
        break
    elif(selecaoNum == 1):
        cadOnibus()
    elif(selecaoNum == 2):
        cadMotorista()
    elif(selecaoNum == 3):
        cadRota()