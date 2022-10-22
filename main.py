import random

print("Protótipo da Semana 4 - Zombie Dice")
print("Bem-vindo(a) ao Zombie Dice!\n")

num_players = 0
while num_players < 2:
    try:
        num_players = int(input("Informe o número de jogadores: "))
        if num_players < 2:
            print("Aviso: Para iniciar, é necessário pelo menos 2 jogadores.")
    except ValueError:
        print("Aviso: O valor inserido precisa ser um número inteiro")

player_list = []
names = ''

i = 1
while i <= num_players:
    names = input(f"Digite o nome do jogador {i}: ").upper()
    if len(names) < 2:
        print(f"AVISO: O nome precisa ter pelo menos duas letras.")
    else:
        i += 1
        player_list.append(names)

player_list_fmt = ", ".join(player_list[:-1]) + " e " + player_list[-1]

green_dice = "CPCTPC"
yellow_dice = "TPCTPC"
red_dice = "TPTCPT"

list_dice = [green_dice, green_dice, green_dice, green_dice, green_dice, green_dice,
             yellow_dice, yellow_dice, yellow_dice, yellow_dice,
             red_dice, red_dice]

print("\nINICIANDO O JOGO...")
print(f"\nOs jogadores são: {player_list_fmt}")

player = 0
shot = 0
step = 0
brain = 0
random_dices = []

game = "True"
init = " "
random_faces = []
round_ = 1

while game == 'True':
    print(f'\n----------- RODADA PROTÓTIPO {round_} ----------\n')
    while init != "":
        init = input(f"Turno de {player_list[player]}. Tecle 'ENTER' para sortear 3 dados do tubo: ")
        random_dices = random.sample(list_dice, 3)
        if init == "":
            print("\nOs dados sorteados foram:")
            for dice in random_dices:
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
            print("Por favor, tecle 'ENTER' para iniciar")

    init = " "
    while init != "":
        init = input(f"\nAgora, tecle 'ENTER' para rolar dos dados: ")
        if init == "":
            print(f"\nAs faces dos dados foram: ")
            for face in random_faces:
                if face == 'P':
                    print('PASSOS: sua vítima escapou!')
                    step += 1
                elif face == 'T':
                    print('TIRO: sua vítima revidou!')
                    shot += 1
                elif face == 'C':
                    print('CÉREBRO: você devorou o cérebro de sua vítima!')
                    brain += 1
        if shot >= 3:
            print(f'\nVOCÊ PERDEU! Você levou {shot} tiros.')
            game = 'False'
        elif brain >= 12:
            print(f"\nVOCÊ GANHOU! Você comeu {brain} cérebros")
            game = 'False'

    print("\nSCORE ATUAL:")
    print(f"Cérebro(s): {brain}")
    print(f"Tiro(s): {shot}")

    if game == 'False':
        print('\n\nFINALIZANDO PARTIDA PROTÓTIPO... OBRIGADO POR EXECUTAR!')
        
    while init != 'S' and init != 'N' and init != 'X' and game == 'True':
        init = input("\nDeseja continuar rolando dados? (s = sim || n = não || x = sair)").upper()
        if init == 'N':
            print(f"Pontos deste turno: \n{brain} Cérebro(s), {step} passo(s) e {shot} tiro(s)")
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
