import random

# Generovani cisla
def get_random_number():
    return ''.join(random.sample('0123456789',4))

# Funkce pro ziskani poctu krav a byku
def get_bulls_cows(number, user_guess):
    bulls = sum((a==b) for a, b in zip(number, user_guess)) 
    cows = len(set(number) & set(user_guess)) - bulls  
    return bulls, cows

# Game
def game():
    number = get_random_number()
    guesses = 0  

    while True:
        guesses += 1
        user_guess = input("Zadej čtyřmístné číslo: ")
        
        # overeni pokusu 
        if not user_guess.isnumeric() or len(user_guess) != 4 or len(set(user_guess)) != 4:
            print("Chybný vstup, zkus to znovu")
            continue
        
        bulls, cows = get_bulls_cows(number, user_guess)
        
       
        if bulls == 4:
            print(f'Gratuluji, uhádl jsi číslo po {guesses} pokusech!')
            break
        else:
            print(f'{bulls} býci, {cows} krávy. Zkus to znovu.')

game()  