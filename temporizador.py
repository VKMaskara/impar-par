import time

print("⏰ Temporizador: ", end="")
for i in range(5, 0, -1):
    if i <= 3:
        print(f'\r🔴 TEMPO CRÍTICO: {i} segundos!', end='', flush=True)
    else:
        print(f'\r⏰ Temporizador: {i} segundos', end='', flush=True)
    time.sleep(1)
print('\r🎉 TEMPO ESGOTADO! ⏰')