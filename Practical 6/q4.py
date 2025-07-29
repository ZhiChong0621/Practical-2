import random

answers = []
guesses = []
outputs = []

while True:
    answer = random.randint(1,2)

    guess = input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: ")

    if guess.isdigit():
        guess = int(guess)
    
        if guess == 0:
            print("Thank you for playing the game!")
            break
        else:
            answers.append(answer)
            guesses.append(guess)

            if answer == guess:
                print("Correct!\n")
                outputs.append(True)
            else:
                print("Wrong\n")
                outputs.append(False)
    else:
        print("Please enter 0,1 or 2 \n")
correct = [output for output in outputs if output]
incorrect = [output for output in outputs if not output]

print("Result")
print("-------")
print("You have made {} correct guess {}".format(len(correct),"es" if len(correct)>1 else ""),end = "")
print("and {} incorrect guess{}\n" .format(len(incorrect),"es" if len(incorrect)>1 else ""),end = "")

for i in range(len(answers)):
    print("Round #{:d}".format(i+1))
    print("Answer: {:s}".format("Head"if answers [i] == 1 else "Tail"))
    print("Guess: {:s}".format("Head"if guesses [i] == 1 else "Tail"))
    print("Result: {:s}".format("Correct\n"if outputs [i] == 1 else "Wrong\n"))