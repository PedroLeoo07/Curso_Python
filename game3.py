import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    print(f"Você tem {max_tentativas} tentativas.")
    
    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if tentativas == max_tentativas:
            print(f"Fim de jogo! O número secreto era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()
