#This program is to guess the number

n=18
number_of_guesses=1
print("Number of guessess is 9 times only")
while(number_of_guesses<=9):
    guess_number=int(input("Guess the number: \n"))
    if guess_number<18:
        print("You entered less number plese try some higher number")
    elif guess_number>18:
        print("You entered higher number please try with less number")
    else:
        print("*****You won..!! *****\n")
        print(number_of_guesses,"number of guesses taken to get right number")
        break
    print(9-number_of_guesses,"number of guesses left \n")
    number_of_guesses = number_of_guesses+1
if (number_of_guesses>9):
    print("................Game Over.............")