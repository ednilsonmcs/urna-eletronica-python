import array
from candidato import Candidato

# Cadastra candidatos
candidatos = [
        Candidato(1, "Ednilson Messias", "Presidente", 99, "Pantera"),
        Candidato(2, "Renata Gomes", "Presidente", 88, "Gavião"),
        Candidato(3, "Georgen", "Senador", 881, "Gavião"),
        Candidato(4, "Marco Antônio", "Senador", 882, "Gavião"),
        Candidato(5, "Nadilson Lima", "Senador", 991, "Pantera")
    ]

votosPresidente = []
votosSenador = []

print("################################")
print("####### ELEIÇÕES ABERTAS #######")
print("################################\n")

print("0 - Iniciar uma sessão de votação")
print("1 - Encerrar as eleições\n")

#Inicia loop para Eleições
opcao = input("Digite a opção desejada:\n")
while opcao != "1":
    match opcao:
        case "0":
            for candidato in candidatos:
                print("Nome: " + candidato.nome + " (" + candidato.cargo + ") " + " Partido: " + candidato.partido + " Número: " + str(candidato.numero))
            
            print("\n")
            votosPresidente.append(input("Digite o número para PRESIDENTE:\n"))
            # TODO verificar se o número é um dos presidentes cadastrados, se não for pedir pra informar um número ou dar a opção de abortar (colocar em um while)

            votosSenador.append(input("Digite o número para SENADOR:\n"))
            # TODO verificar se o número é um dos senadores cadastrados, se não for pedir pra informar um número ou dar a opção de abortar (colocar em um while)

            print("\n")
            print("################################")
            print("####### ELEIÇÕES ABERTAS #######")
            print("################################\n")

            print("0 - Iniciar uma sessão de votação")
            print("1 - Encerrar as eleições\n")
            opcao = input("Digite a opção desejada:\n")
        case "1":
            continue
        case _: 
            print("Opção invalida:\n")
            print("0 - Iniciar uma sessão de votação")
            print("1 - Encerrar as eleições\n")
            opcao = input("Digite a opção desejada:\n")


# TODO apresentar votos sumarizados como nome dos canditados e quantos votos receberam

for voto in votosPresidente:
    print("Votos para PRESIDENTE:\n")
    print(voto)
print("\n")

for voto in votosSenador:
    print("Votos para SENADOR:\n")
    print(voto)
print("\n")

