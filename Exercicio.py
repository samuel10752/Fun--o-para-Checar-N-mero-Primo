def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Teste de 1 a 100
for numero in range(1, 101):
    if eh_primo(numero):
        print(f"{numero} é primo")