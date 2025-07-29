import random

# Generate a random number between 1 and 1000
ans = random.randint(1, 1000)
guesses = 0

while True:
    try:
        inp = int(input("Guess a number between 1 and 1000: "))
        guesses += 1

        if inp < ans:
            print("Too low!\n")
        elif inp > ans:
            print("Too high!\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {guesses} attempts.")
            break

    except ValueError:
        print("❌ Please enter a valid number!\n")
