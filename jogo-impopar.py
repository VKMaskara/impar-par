# CRIAR UM JOGO DE PAR OU IMPAR COM UMA INTERFACE SIMPLES PARA O USUÁRIO
# DUPLA: KAIQUE SOUSA E VITOR KAUÊ
# DATA: 25/09/2025

import os
import random
import sys
import time

# Função para limpar a tela do terminal
def limpar_tela():
    """
    Limpa a tela do terminal.
    windows: cls
    linux/mac: clear
    """
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
    print('=-'*30)
    print('JOGO DE PAR OU ÍMPAR'.center(60))
    print('=-'*30)
    time.sleep(1)

# ========================= INÍCIO DO JOGO ========================= #
limpar_tela()  # Limpa a tela antes de iniciar
imprimir_cabecalho()  # Mostra o cabeçalho

# tela de boas vindas
nome = str(input('Olá, qual é o seu nome? ')).strip().title()  # Pede o nome do jogador
while True:
    resposta = input(f'Prazer em te conhecer, {nome}!\nMeu nome é Ímparius e vamos jogar? (S/N) ').strip().upper()  # Pergunta se quer jogar
    if resposta == 'S':
        print('Ótimo! Vamos começar!')
        break
    elif resposta == 'N':
        print('Tudo bem! Quando quiser jogar, é só me chamar.')
        sys.exit() # encerra caso o jogador não queira jogar
    else:
        print('⚠️ Resposta inválida. Por favor, digite S para sim ou N para não.')
        continue
    
time.sleep(2)  # Espera 2 segundos
limpar_tela()  # Limpa a tela
imprimir_cabecalho()  # Mostra o cabeçalho novamente

# regras do jogo
print('Regras do jogo:')
print('1. Você escolhe um número inteiro de 1 a 5 e se quer par ou ímpar.')
print('2. O Ímparius também escolhe um número.')
print('3. A soma decide o vencedor da rodada.')
print('4. Ao sair, exibiremos seu placar final.')

print('\nO jogo vai começar em:')
for i in range(10, 0, -1):
    print(f'{i}...', end='', flush=True)
    time.sleep(1)
print('\n')
print('=-'*30)
print(f'Jogo iniciado! Boa sorte, {nome}!'.center(60))
print('=-'*30)

time.sleep(2)  # Espera 2 segundos
limpar_tela()  # Limpa a tela
imprimir_cabecalho()  # Mostra o cabeçalho

# variáveis
placar_pontos = [{'nome': nome, 'pontos': 0}, {'nome': 'Ímparius', 'pontos': 0}]  # Inicializa o placar

# loop principal do jogo
while True:
    # escolha do jogador (número)
    while True:
        try:
            jogador_numero = int(input(f'{nome}, escolha um número inteiro de 1 a 5: '))  # Pede o número ao jogador
            if 1 <= jogador_numero <= 5:
                break
            else:
                print('⚠️ Por favor, escolha um número entre 1 e 5.')
        except ValueError:
            print('⚠️ Por favor, insira um número inteiro válido.')

    # escolha do jogador (par/ímpar)
    while True:
        jogador_escolha = input(f'{nome}, você quer par ou ímpar? (P/I) ').strip().upper()  # Pede par ou ímpar
        if jogador_escolha in ['P', 'I']:
            break
        else:
            print('⚠️ Escolha inválida. Digite P para par ou I para ímpar.')

    # escolha do Ímparius
    imparius_numero = random.randint(1, 5)  # Ímparius escolhe um número aleatório
    print(f'\n🤖 Ímparius escolheu o número {imparius_numero}.')

    # cálculo do resultado
    soma = jogador_numero + imparius_numero  # Soma os números
    resultado = 'P' if soma % 2 == 0 else 'I'  # Verifica se a soma é par ou ímpar
    print(f'A soma dos números é {soma}, que é {"par" if resultado == "P" else "ímpar"}.')

    # verificação do vencedor
    if jogador_escolha == resultado:
        print(f'🎉 Parabéns, {nome}! Você ganhou esta rodada.')
        placar_pontos[0]['pontos'] += 1  # Adiciona ponto ao jogador
    else:
        print('🤖 Ímparius ganhou esta rodada!')
        placar_pontos[1]['pontos'] += 1  # Adiciona ponto ao Ímparius

    # exibição do placar atual
    print('\n📊 Placar atual:')
    for jogador in placar_pontos:
        print(f"{jogador['nome']}: {jogador['pontos']} pontos")

    # opção de continuar ou sair
    while True:
        continuar = input('\nVocê quer jogar novamente? (S/N) ').strip().upper()
        if continuar == 'S':
            print('Ótimo! Vamos para a próxima rodada!')
            time.sleep(2)
            limpar_tela()
            imprimir_cabecalho()
            break  # Continua o loop principal para nova rodada
        elif continuar == 'N':
            print('Tudo bem! Quando quiser jogar, é só me chamar.')
            # Sai do loop principal do jogo
            limpar_tela()
            imprimir_cabecalho()
            imprimir_placar_final()
            print('\nObrigado por jogar! Até a próxima!')
            sys.exit()
        else:
            print('⚠️ Desculpa, não entendi sua resposta. Tente novamente.')
