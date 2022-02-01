
import random

INTENTOS = 10
try:

    def lower_limitation ():
        lower_limit = int (input ("Please, enter the lower limit of your guessing range: "))
        if lower_limit < 0:
            print ("Values must be positive, please re-introduce a number")
            lower_limit = input ()
        else:
            return (lower_limit)        

    def upper_limitation ():
        upper_limit = int (input ("Please, enter the upper limit of your guessing range: "))
        if upper_limit < 0:
            print ("Values must be positive, please re-introduce a number")
            upper_limit = input ()
        else:
            return (upper_limit) 

    case_lower = lower_limitation ()
    case_upper = upper_limitation ()

    print (f"Your random number will be between {case_lower} and {case_upper}.")

    def random_number_game ():
        guess_number = int (input ("Let's play a game :). Introduce a number: "))
        x = int (random.randint (case_lower, case_upper))
        trial_count = 0
    
        
        while guess_number != x: 
            if guess_number < case_lower or guess_number > case_upper:
                print (f"Remember your limits are {case_lower} and {case_upper}. Please, re-enter a number.")
                guess_number = int (input ())        
            elif guess_number < x:
                print ("You went too low, try again.")
                guess_number = int (input ())
            elif guess_number > x:
                print ("You went too high, try again.")
                guess_number = int (input ())
            trial_count = trial_count + 1
            if trial_count == INTENTOS:
                print ("You have tried reached the max amount of trials jaja.")
                break
        if trial_count != INTENTOS:
            print ("Fucking amazing mate, you guessed it.")
        return ()


    random_number_game ()
except Exception:
    print ("Solo se pueden introducir números")

