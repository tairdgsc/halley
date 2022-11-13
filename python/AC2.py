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
    if(linhaNumDias <= 0):
        print("O valor tem que ser superior a 0")
        return(cadRota())
    linhaDias = ""
    for i in range(linhaNumDias):
        print("1 - Domingo")
        print("2 - Segunda-feira")
        print("3 - Terça-feira")
        print("4 - Quarta-feira")
        print("5 - Quinta-feira")
        print("6 - Sexta-feira")
        print("7 - Sábado-feira")
        dia = int(input("Informe um dia ser cadastrado"))
        horaInicial = -1
        horaFinal = -1
        diaJaCad = []
        while(diaJaCad[dia] == diaJaCad[dia]):
            dia = int(input("Esse dia já foi cadastrado informe outro"))
            diaJaCad.insert(dia, dia)
        while(horaInicial >= 0 and horaInicial < 24 and horaFinal >= 0 and horaFinal < 24):
            horaInicial = input("informe o horário inicial da linha entre 00 a 23")
            horaFinal = input("informe o horário final da linha entre 00 a 23")
        horaEdia = str(horaInicial + " às " + horaFinal)
        linhaDias = linhaDias + " " + input("Informe o dia")
        linhaDias = linhaDias + " " + input("Informe o horário")

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