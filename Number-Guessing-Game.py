
import random

# Number Guessing Game
print("🎮 Welcome to Number Guessing Game!")

number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        
        # check range
        if guess < 1 or guess > 100:
            print("⚠️ Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess == number:
            print("🎉 Correct! You won!")
            print("Attempts:", attempts)
            break
        elif guess > number:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")