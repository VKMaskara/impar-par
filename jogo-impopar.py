# CRIAR UM JOGO DE PAR OU IMPAR COM UMA INTERFACE SIMPLES PARA O USUÁRIO
# DUPLA: KAIQUE SOUSA E VITOR KAUÊ .. 
# DATA: 25/09/2025

import os # Função pra limpar a tela
import random # Escolhar do numero
import sys # função de finalizar o código e sair do loop
import time # Temporizador

# ========================= CORES USADAS ========================= #
VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

# ========================= FUNÇÕES ========================= #
# Função para limpar a tela do terminal
def limpar_tela():
    """
    Limpa a tela do terminal.
    windows: cls
    linux/mac: clear
    """
    print("\n" * 100)
    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela do terminal de acordo com o sistema operacional
    
# Função para imprimir o placar final do jogo
def imprimir_placar_final():
    print('\n' + '='*60)
    print('🏆 PLACAR FINAL 🏆'.center(60))
    print('='*60)
    print(f"{'JOGADOR':<30}{'PONTOS':>30}")
    print('-'*60)
    for jogador in placar_pontos:
        print(f"{jogador['nome']:<30}{jogador['pontos']:>30}")
    print('-'*60)
    total_pontos = sum(j['pontos'] for j in placar_pontos)
    print(f"{'TOTAL DE PONTOS':<30}{total_pontos:>30}")
    print('='*60)
    
    # Determina o vencedor
    if placar_pontos[0]['pontos'] > placar_pontos[1]['pontos']:
        print(f"\n🎉 Parabéns, {placar_pontos[0]['nome']}! Você venceu o jogo! 🎉")
    elif placar_pontos[0]['pontos'] < placar_pontos[1]['pontos']:
        print(f"\n{placar_pontos[1]['nome']} venceu o jogo! Tente novamente!")
    else:
        print("\n🤝 Empate! Que disputa acirrada!")

# Função para imprimir o cabeçalho do jogo
def imprimir_cabecalho():
    print(f'{CIANO}=-{RESET}'*30)
    print(f'{NEGRITO}{AZUL} JOGO DE PAR OU ÍMPAR{RESET}'.center(68))
    print(f'{CIANO}=-{RESET}'*30)
    time.sleep(1)

# ========================= INÍCIO DO JOGO ========================= #
limpar_tela()  # Limpa a tela antes de iniciar
imprimir_cabecalho()  # Mostra o cabeçalho

# tela de boas vindas
while True:
    nome = str(input(f'{AMARELO}Olá, qual é o seu nome? {RESET}')).strip().title()
    if nome and len(nome) >= 2:  # Pelo menos 2 caracteres
        break
    else:
        print(f'{VERMELHO}⚠️ Por favor, digite um nome válido (mínimo 2 letras).{RESET}')

while True:
    resposta = input(f'{AZUL}Prazer em te conhecer, {nome}!\nMeu nome é Ímparius e vamos jogar? (S/N) {RESET}').strip().upper()  # Pergunta se quer jogar
    if resposta == 'S':
        print(f'{VERDE}Ótimo! Vamos começar!{RESET}')
        break
    elif resposta == 'N':
        print(f'{AMARELO}Tudo bem! Quando quiser jogar, é só me chamar.{RESET}')
        sys.exit() # encerra caso o jogador não queira jogar
    else:
        print(f'{VERMELHO}⚠️ Resposta inválida. Por favor, digite S para sim ou N para não.{RESET}')
        continue
    
time.sleep(2)  # Espera 2 segundos
limpar_tela()  # Limpa a tela
imprimir_cabecalho()  # Mostra o cabeçalho novamente

# regras do jogo
print(f'{NEGRITO}{AZUL}Regras do jogo:{RESET}')
print(f'{VERDE}1. Você escolhe um número inteiro de 1 a 5 e se quer par ou ímpar.{RESET}')
print(f'{VERDE}2. O Ímparius também escolhe um número.{RESET}')
print(f'{VERDE}3. A soma decide o vencedor da rodada.{RESET}')
print(f'{VERDE}4. Ao sair, exibiremos seu placar final.{RESET}')

print(f'\n{AMARELO}O jogo vai começar em:{RESET}')
for i in range(10, 0, -1):
    if i > 5:
        cor = VERDE
    elif i > 2:
        cor = AMARELO
    else:
        cor = VERMELHO
    print(f'\r{cor}{i} segundos{RESET}', end='', flush=True) #flush=True para não travar
    time.sleep(1)

print('\n')
print(f'{CIANO}=-{RESET}'*30)
print(f'{NEGRITO}{AZUL}Jogo iniciado! Boa sorte, {nome}!{RESET}'.center(68))
print(f'{CIANO}=-{RESET}'*30)

time.sleep(2)  # Espera 2 segundos
limpar_tela()  # Limpa a tela
imprimir_cabecalho()  # Mostra o cabeçalho

# variável
placar_pontos = [{'nome': nome, 'pontos': 0}, {'nome': 'Ímparius', 'pontos': 0}]  # Inicializa o placar

# loop principal do jogo
while True:
    # escolha do jogador (número)
    while True:
        try:
            jogador_numero = int(input(f'{AZUL}{nome}, escolha um número inteiro de 1 a 5: {RESET}'))  # Pede o número ao jogador
            if 1 <= jogador_numero <= 5:
                break
            else:
                print(f'{VERMELHO}⚠️ Por favor, escolha um número entre 1 e 5.{RESET}')
        except ValueError:
            print(f'{VERMELHO}⚠️ Por favor, insira um número inteiro válido.{RESET}')

    # escolha do jogador (par/ímpar)
    while True:
        jogador_escolha = input(f'{AZUL}{nome}, você quer par ou ímpar? (P/I) {RESET}').strip().upper()  # Pede par ou ímpar
        if jogador_escolha in ['P', 'I']:
            break
        else:
            print(f'{VERMELHO}⚠️ Escolha inválida. Digite P para par ou I para ímpar.{RESET}')

    # escolha do Ímparius
    imparius_numero = random.randint(1, 5)  # Ímparius escolhe um número aleatório
    print(f'\n{MAGENTA}🤖 Ímparius escolheu o número {imparius_numero}.{RESET}')

    # cálculo do resultado
    soma = jogador_numero + imparius_numero  # Soma os números
    resultado = 'P' if soma % 2 == 0 else 'I'  # Verifica se a soma é par ou ímpar
    print(f'{CIANO}A soma dos números é {soma}, que é {"par" if resultado == "P" else "ímpar"}.{RESET}')

    # verificação do vencedor
    if jogador_escolha == resultado:
        print(f'{VERDE}🎉 Parabéns, {nome}! Você ganhou esta rodada.{RESET}')
        placar_pontos[0]['pontos'] += 1  # Adiciona ponto ao jogador
    else:
        print(f'{MAGENTA}🤖 Ímparius ganhou esta rodada!{RESET}')
        placar_pontos[1]['pontos'] += 1  # Adiciona ponto ao Ímparius

    # exibição do placar atual
    print(f'\n{AMARELO}📊 Placar atual:{RESET}')
    for jogador in placar_pontos:
        if jogador['pontos'] == max(j['pontos'] for j in placar_pontos):
            print(f"{VERDE}{jogador['nome']}: {jogador['pontos']} pontos 👑{RESET}")
        else:
            print(f"{BRANCO}{jogador['nome']}: {jogador['pontos']} pontos{RESET}")

    # opção de continuar ou sair
    while True:
        continuar = input(f'\n{AMARELO}Você quer jogar novamente? (S/N) {RESET}').strip().upper()
        if continuar == 'S':
            print(f'{VERDE}Ótimo! Vamos para a próxima rodada!{RESET}')
            time.sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            break  # Continua o loop principal para nova rodada
        elif continuar == 'N':
            # Sai do loop principal do jogo
            limpar_tela()  # Limpa a tela
            imprimir_cabecalho()  # Mostra o cabeçalho limpo no topo
            imprimir_placar_final()  # Mostra o placar final logo abaixo
            print(f'\n{CIANO}Obrigado por jogar! Até a próxima!{RESET}')
            sys.exit()
        else:
            print(f'{VERMELHO}⚠️ Desculpa, não entendi sua resposta. Tente novamente.{RESET}')