from ListaEncadeada import *
onibus = ListaEncadeada()
motorista = ListaEncadeada()
motoristaHorarios = ListaEncadeada()
rotas = ListaEncadeada()
cobrador = ListaEncadeada()
listaCheckIn = ListaEncadeada()

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
        infMotorista = input("Informe um nome a ser cadastrado\n").upper()
        cadDeficiencia = input("O motorista tem alguma deficiência \nque necessita veículo adaptado?\nSim ou não?\n").upper()
        while(not cadDeficiencia == "SIM" and not cadDeficiencia == ("NÃO")):
            cadDeficiencia = input("O motorista tem alguma deficiência \nque necessita veículo adaptado?\nSim ou não?").upper()
        motorista.insere_no_inicio(motorista, cadDeficiencia)
        motorista.insere_no_inicio(motorista, infMotorista)
        print(motorista)

def cadRota():
    linhaNumDias = int(input("Essa linha corre quantos dias\n"))
    if(linhaNumDias < 1 or linhaNumDias > 7):
        print("O valor tem que ser superior a 0 e menor que 8")
        return(cadRota())
    for i in range(linhaNumDias):
        print("1 - Domingo")
        print("2 - Segunda-feira")
        print("3 - Terça-feira")
        print("4 - Quarta-feira")
        print("5 - Quinta-feira")
        print("6 - Sexta-feira")
        print("7 - Sábado")
        diaJaCad = [None] * 8
        dia = -1
        horaInicial = -1
        horaFinal = -1
        minutosInicial = -1
        minutosFinal = -1

        while(True):
            dia = -1
            horaInicial = -1
            horaFinal = -1
            minutosInicial = -1
            minutosFinal = -1
            dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))
            while(dia < 1 or dia > 7):
                dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))

            while not diaJaCad[dia] == None:
                dia = int(input("Esse dia já foi cadastrado, informe outro dia:\n"))
                while dia < 1 or dia > 7:
                    dia = int(input("Informe um dia válido entre 1 a 7"))                
                
            diaJaCad[dia] = dia

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

            rotas.insere_no_inicio(rotas, horaEdia)

            linhaNumDias = linhaNumDias -1
            if(linhaNumDias == 0):
                break

        linhaNome = input("Informe um código para a linha\n")
        while(rotas.busca(rotas, linhaNome)):
            print("Esta linha já existe em nosso banco de dados")
            linhaNome = input("Informe um código para a linha\n")
        rotas.insere_no_inicio(rotas, linhaNome)
        if(linhaNumDias == 0):
            break
    
    print(rotas)

def cadMotoristaHorarios():
    motoristaBusca = input("Informe o nome do motorista a ser buscado\n").upper()
    while motorista.busca(motorista, motoristaBusca):    
        linhaNumDias = int(input("Quantos dias este motorista irá trabalhar?\n"))
        if(linhaNumDias < 1 or linhaNumDias > 7):
            print("O valor tem que ser superior a 0 e menor que 8")
            return(cadRota())
        for i in range(linhaNumDias):
            print("1 - Domingo")
            print("2 - Segunda-feira")
            print("3 - Terça-feira")
            print("4 - Quarta-feira")
            print("5 - Quinta-feira")
            print("6 - Sexta-feira")
            print("7 - Sábado")
            diaJaCad = [None] * 8
            dia = -1
            horaInicial = -1
            horaFinal = -1
            minutosInicial = -1
            minutosFinal = -1

            while(True):
                dia = -1
                horaInicial = -1
                horaFinal = -1
                minutosInicial = -1
                minutosFinal = -1
                dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))
                while(dia < 1 or dia > 7):
                    dia = int(input("Informe um dia da semana para cadastrar entre 1 e 7\n"))

                while not diaJaCad[dia] == None:
                    dia = int(input("Esse dia já foi cadastrado, informe outro dia:\n"))
                    while dia < 1 or dia > 7:
                        dia = int(input("Informe um dia válido entre 1 a 7"))                
                    
                diaJaCad[dia] = dia

                while(horaInicial < 0 or horaInicial > 23):
                    horaInicial = int(input("informe o horário inicial de entrada entre 00 a 23\n"))
                while(minutosInicial < 0 or minutosInicial > 59):
                    minutosInicial = int(input("Informe um valor para minutos válido\n"))
                while(horaFinal < 0 or horaFinal > 23):
                    horaFinal = int(input("informe o horário final de saida entre 00 a 23\n"))
                while(minutosFinal < 0 or minutosFinal > 59):
                    minutosFinal = int(input("Informe um valor para minutos válido\n"))
                Sdia = str(dia)
                ShoraInicial = str(horaInicial)
                SminutosInicial  = str(minutosInicial)
                ShoraFinal = str(horaFinal)
                SminutosFinal = str(minutosFinal)
                horaEdia = (Sdia + " " + ShoraInicial + ":" + SminutosInicial + " às " + ShoraFinal + ":" + SminutosFinal)

                motoristaHorarios.insere_no_inicio(motoristaHorarios, horaEdia)

                linhaNumDias = linhaNumDias -1
                if(linhaNumDias >= 0):
                    break

        motoristaHorarios.insere_no_inicio(motoristaHorarios, motoristaBusca)
        
        print(motoristaHorarios)
        if(linhaNumDias >= 0):
            break
    else:
        print("Motorista não encontrado")
        erroBusca = int(input("1 - Cadastrar novo motorista\n2 - Cadastrar horário do motorista\n"))
        if(erroBusca == 1):
            cadMotorista()
        elif(erroBusca == 2):
            cadMotoristaHorarios
        else:
            print("Valor inválido\n")


def cadCobrador():
    print("Cadastro de cobrador")
    infCobrador = input("Informe um nome a ser cadastrado\n")
    cobrador.insere_no_inicio(cobrador, infCobrador)
    print(cobrador)

class CheckIn():
    def __init__(self, onibus, motorista, motor, pneu, tanque, lanterna, elevador, status):
        self.onibus = onibus
        self.motorista = motorista
        self.motor = motor
        self.pneu = pneu
        self.tanque = tanque
        self.lanterna = lanterna
        self.elevador = elevador
        self.status = status

def checkIn():
    print("Check-in do ônibus.")
    infOnibus = input("Informe o ônibus a ser verificado:\n")
    infMotorista = input("Informe o nome do motorista responsável:\n")
    infMotor = ""
    infPneu = ""
    infTanque = ""
    infLanterna = ""
    infElevador = ""

    while(not infMotor == "SIM" and not infMotor == ("NÃO")):
        infMotor = input("O motor está em boas condições? Sim ou Não\n").upper()

    while(not infPneu == "SIM" and not infPneu == ("NÃO")):
        infPneu = input("Os pneus estão em boas condições? Sim ou Não\n").upper()

    while(not infTanque == "SIM" and not infTanque == ("NÃO")):
        infTanque = input("O tanque está cheio? Sim ou Não\n").upper()

    while(not infLanterna == "SIM" and not infLanterna == ("NÃO")):
        infLanterna = input("As lanternas e setas estão em boas condições? Sim ou Não\n").upper()

    while(not infElevador == "SIM" and not infElevador == ("NÃO")):
        infElevador = input("O elevador está em boas condições? Sim ou Não\n").upper()

    if(infMotor == "NÃO" or infPneu == "NÃO" or infTanque == "NÃO" or infLanterna == "NÃO" or infElevador == "NÃO"):
        print("Verificação não aprovada. Chame um supervisor!")
        checkin = CheckIn(infOnibus, infMotorista, infMotor, infPneu, infTanque, infLanterna, infElevador, "REPROVADO")
    else:
        print("Verificação aprovada. Boa viagem!")
        checkin = CheckIn(infOnibus, infMotorista, infMotor, infPneu, infTanque, infLanterna, infElevador, "APROVADO")
    listaCheckIn.insere_depois(checkin)
    print(list(checkin.__dict__.values()))

def desOnibus():
    print("Designar Ônibus")
    print("Esses são os ônibus cadastrados:")
    print(onibus)
    onibusDesignado = input("Qual dos ônibus cadastrados deseja designar?\n").upper()
    if(onibus.busca(onibus, onibusDesignado)):
        print("Ônibus designado com sucesso!")
    else:
        while(not onibus.busca(onibus, onibusDesignado)):
            onibusDesignado = input("Ônibus inexistente, digite outro por favor:\n").upper()
        else:
            print("Ônibus designado com sucesso!")
        
def desCobrador():
    print("Designar Cobrador")
    print("Esses são os cobradores cadastrados:")
    print(cobrador)
    cobradorDesignado = input("Qual dos cobradores cadastrados deseja designar?\n").upper()
    if(cobrador.busca(cobrador, cobradorDesignado)):
        print("Cobrador designado com sucesso!")
    else:
        while(not cobrador.busca(cobrador, cobradorDesignado)):
            cobradorDesignado = input("Cobrador inexistente, digite outro por favor:\n").upper()
        else:
            print("Cobrador designado com sucesso!")
    
while True:
    print('Olá usuário o que deseja fazer?')
    print('1 - Cadastrar ônibus')
    print('2 - Cadastrar motorista')
    print('3 - Horário de rotas')
    print('4 - Horário para motoristas')
    print('5 - Designar ônibus')
    print('6 - Realizar check-in') #motorista realiza check in antes de iniciar rota
    print('7 - Cadastrar cobrador')
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
    elif(selecaoNum == 4):
        cadMotoristaHorarios()
    elif(selecaoNum == 5):
        desOnibus()
    elif(selecaoNum == 6):
        checkIn()
    elif(selecaoNum == 7):
        cadCobrador()
    elif(selecaoNum == 8):
        desCobrador()