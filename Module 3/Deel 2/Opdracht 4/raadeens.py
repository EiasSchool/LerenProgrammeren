import random

def main():
    score = 0
    total_rounds = 0
    max_rounds = 20

    while total_rounds < max_rounds:
        secret_number = random.randint(1, 1000)
        guesses = 0
        round_over = False

        while guesses < 10 and not round_over:
            guess = int(input("Doe een gok: "))
            guesses += 1

            if guess == secret_number:
                print("Geraden!")
                score += 1
                round_over = True
            elif abs(guess - secret_number) < 20:
                print("Je bent heel warm")
            elif abs(guess - secret_number) < 50:
                print("Je bent warm")
            else:
                print("Hoger" if guess < secret_number else "Lager")

        print(f"Score tot nu toe: {score}")
        total_rounds += 1

        if total_rounds < max_rounds:
            nog_een = input("Nog een getal raden? (ja/nee): ")
            if nog_een.lower() != 'ja':
                break

    print(f"Eindscore: {score}")

if __name__ == "__main__":
    main()
