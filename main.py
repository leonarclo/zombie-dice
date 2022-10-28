import random

name = 'Leonardo dos Santos Lima'
course = 'Análise e Desenvolvimento de Sistemas'
print(f'\n********************************************\n'
      f'Aluno: {name}\n'
      f'Curso: {course}\n'
      f'********************************************\n')

print("PROTÓTIPO (Semana 4)")
print(" ****** BEM-VINDO(A) AO ZOMBIE DICE! ****** \n")

num_players = 0
while num_players < 2 or num_players > 20:  # Selecionar o número de jogadores.
    try:
        num_players = int(input("Informe o número de jogadores: "))
        if num_players < 2:
            print("AVISO: Para iniciar, é necessário pelo menos 2 jogadores.")
        elif num_players > 20:
            print("AVISO: O número máximo por rodada é de 20 jogadores.")
    except ValueError:
        print("AVISO: O valor inserido precisa ser um número inteiro.")

player_list = []
names = ''

i = 1
while i <= num_players:  # Digitar o nome dos jogadores.
    names = input(f"Digite o nome do jogador {i}: ").upper()
    if len(names) < 2:
        print(f"AVISO: O nome precisa ter pelo menos duas letras.")
    else:
        i += 1
        player_list.append(names)   # Salvar os jogadores em uma lista.

player_list_fmt = ", ".join(player_list[:-1]) + " e " + player_list[-1]   # Formatar o nome dos jogadores.

# Definindo as faces de cada cor de dado.
green_dice = "CPCTPC"
yellow_dice = "TPCTPC"
red_dice = "TPTCPT"

# Incluindo o total de dados em uma lista.
list_dice = [green_dice, green_dice, green_dice, green_dice, green_dice, green_dice,
             yellow_dice, yellow_dice, yellow_dice, yellow_dice,
             red_dice, red_dice]

print("\nINICIANDO O JOGO...")
print(f"\nOs jogadores são: {player_list_fmt}")

# Variáveis de jogo.
round_ = 1
player = 0
shot = 0
step = 0
brain = 0
random_dices = []
random_faces = []

# Variáveis de controle.
game = "True"
init = " "


while game == 'True':
    print(f'\n----------- RODADA PROTÓTIPO {round_} ----------\n')
    while init != "":
        init = input(f"Turno de {player_list[player]}. Tecle 'ENTER' para sortear 3 dados do tubo: ")
        random_dices = random.sample(list_dice, 3)  # Sorteio randômico de três dados da lista.
        if init == "":
            print("\nOs dados sorteados foram:")
            for dice in random_dices:  # Listando os dados sorteados.
                if dice == "CPCTPC":
                    print("VERDE")
                    random_faces.append(random.choice(dice))
                elif dice == "TPCTPC":
                    print("AMARELO")
                    random_faces.append(random.choice(dice))
                elif dice == "TPTCPT":
                    print("VERMELHO")
                    random_faces.append(random.choice(dice))
        else:
            print("AVISO: Por favor, tecle 'ENTER' para iniciar")

    init = " "
    while init != "":
        init = input(f"\nAgora, tecle 'ENTER' para rolar os dados: ")
        if init == "":
            print(f"\nAs faces dos dados foram, respectivamente: ")
            for face in random_faces:  # Listando a face dos dados sorteados.
                if face == 'P':
                    print('PASSOS: sua vítima escapou!')
                    step += 1
                elif face == 'T':
                    print('TIRO: sua vítima revidou!')
                    shot += 1
                elif face == 'C':
                    print('CÉREBRO: você devorou o cérebro de sua vítima!')
                    brain += 1
        if shot >= 3:  # Condição de derrota.
            print(f'\nVOCÊ PERDEU! Você levou {shot} tiros.')
            game = 'False'
        elif brain >= 12:  # Condição de vitória.
            print(f"\nVOCÊ GANHOU! Você comeu {brain} cérebros")
            game = 'False'

    # Placar da rodada atual.
    print("\nSCORE ATUAL:")
    print(f"Cérebro(s): {brain}")
    print(f"Tiro(s): {shot}")

    if game == 'False':
        print('\n\nFINALIZANDO PARTIDA PROTÓTIPO... OBRIGADO POR EXECUTAR!')

    while init != 'S' and init != 'N' and init != 'X' and game == 'True':
        init = input("\nDeseja continuar rolando dados? (s = sim || n = não || x = sair)").upper()
        if init == 'N':
            print(f"Pontos deste turno: \n{brain} Cérebro(s), {step} passo(s) e {shot} tiro(s)\n")
            if player == num_players - 1:
                game = 'False'
                print('\n\nFINALIZANDO PARTIDA PROTÓTIPO... OBRIGADO POR EXECUTAR!')
            else:
                player += 1
                shot = 0
                step = 0
                brain = 0
                random_dices = []
                random_faces = []
                print("INICIANDO A RODADA DO PRÓXIMO JOGADOR")
        elif init == 'S':
            random_dices = []
            random_faces = []
            print("\nINICIANDO MAIS UM TURNO...\n")
        elif init == 'X':
            print("SAINDO DA PARTIDA PROTÓTIPO... OBRIGADO POR EXECUTAR!")
            game = "False"
