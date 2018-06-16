print("Please think of a number between 0 and 100!")
guess, guesshigh, guesslow = 50, 100, 0
while True:
    guess = int((guesshigh+guesslow)/2)
    print("Is your secret number: ", guess)
    s = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    if s == "h":
        guesshigh = guess
    elif s == "l":
        guesslow = guess
    elif s == "c":
        print("Game over. Your secret number is: ", str(guess),".")
        break
    else:
        print("Please enter a correct input.")
        

