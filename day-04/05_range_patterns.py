secretno = 12
attempts = 0
correctguess = False


while attempts < 5 and correctguess == False:
    guess = input("Guess the secret number: ")
    if guess.isdigit():
        guessval = int(guess)    
        if guessval < 1 and guessval > 20:
            print("Please enter an numeric value ranging from 1 to 20")
        else:
            attempts += 1
            if guessval == secretno:
                print("Your guess is correct, WOW!")
                correctguess = True
            elif guessval < secretno:
                print("Too low")
            else:
                print("Too high")
    else:
        print("Please enter a numeric value") 
if correctguess == False:
    print(" You could not guess the number, The secret number is: ",secretno)

        
            
    
