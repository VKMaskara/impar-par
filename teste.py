import time
import sys

# ANIMAÇÃO DE LOADING SIMPLES
def loading_simples():
    print("Loading simples funcionando!")
    for i in range(20):
        print(f'\rCarregando: [{"█" * i}{" " * (19-i)}] {i*5}%', end='', flush=True)
        time.sleep(0.1)
    print("\n✅ Concluído!")

# CRONÔMETRO SIMPLES
def cronometro_simples():
    print("Cronômetro - Ctrl+C para parar")
    try:
        inicio = time.time()
        while True:
            tempo_decorrido = time.time() - inicio
            horas = int(tempo_decorrido // 3600)
            minutos = int((tempo_decorrido % 3600) // 60)
            segundos = int(tempo_decorrido % 60)
            
            print(f'\rTempo: {horas:02d}:{minutos:02d}:{segundos:02d}', end='', flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n⏹️ Cronômetro parado!")

# ANIMAÇÃO DE MOVIMENTO SIMPLES
def movimento_simples():
    print("Animação de movimento - Ctrl+C para parar")
    try:
        pos = 0
        while True:
            linha = [" "] * 20
            linha[pos] = "●"
            print(f'\r[{"".join(linha)}]', end='', flush=True)
            
            pos = (pos + 1) % 20
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n🎯 Animação finalizada!")

# MENU PRINCIPAL
def main():
    while True:
        print("\n" + "="*40)
        print("ANIMAÇÕES NO TERMINAL")
        print("="*40)
        print("1. Loading Simples")
        print("2. Cronômetro")
        print("3. Movimento")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1-4): ")
        
        if opcao == "1":
            loading_simples()
        elif opcao == "2":
            cronometro_simples()
        elif opcao == "3":
            movimento_simples()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

# Execute o programa
if __name__ == "__main__":
    main()