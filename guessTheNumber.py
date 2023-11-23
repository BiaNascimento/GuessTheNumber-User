import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    tentativas = 0
    limite = 5
    while guess != random_number:
        guess = int(input(f'Adivinhe um número entre 1 e {x} '))
        tentativas = tentativas+1
        if tentativas == limite:
            print(f"Suas tentativas esgotaram, o número secreto é {random_number}!")
            break
        if guess < random_number:
            print(f"O número secreto é maior que {guess}, você tem {limite-tentativas} tentativas")
        elif guess > random_number:
            print(f"O número secreto é menor que {guess}, você tem {limite-tentativas} tentativas")
    else:
        print(f"Você encontrou, o número secreto é {random_number}!")


guess(100)