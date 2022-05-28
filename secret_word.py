import random


class Secret_Word:

    def __init__(self):
        
        self.secret = random.choice(["water", "raton", "codes"]) 

        self.puzzle_state = ["_", "_", "_", "_", "_"]
        self.next_guess = ""



    def print_puzzle(self):
      print(self.puzzle_state) 
    

    def ask_for_next_letter(self):
        self.next_guess = input("What is the next letter?")
        
    
    def check_if_the_guess_is_right(self):
        result = False
        for i, letter in enumerate(self.secret): 
            if letter == self.next_guess:
                result = True
                self.puzzle_state[i] = self.next_guess
        
        if result:
            print(f"Letter {self.next_guess} is in the secret word")
        else:
            print(f"Sorry, letter {self.next_guess} is not in the secret word ")

        return result

    def found_secret_word(self):
        if "_" in self.puzzle_state:
            return False
        else:
            return True



# my_secret = Secret_Word()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()
# my_secret.ask_for_next_letter()
# my_secret.check_if_the_guess_is_right()
# my_secret.print_puzzle()



