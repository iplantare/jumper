from jumper import Jumper
from secret_word import Secret_Word

class Game:

    def __init__(self):
        self.secret_word = Secret_Word()
        self.parachute_guy = Jumper()


    def start_jumper(self):
        while True:
            self.secret_word.print_puzzle()           # self is a default parameter for my methods
            self.parachute_guy.print_parachute_guy()
            self.secret_word.ask_for_next_letter()
            result = self.secret_word.check_if_the_guess_is_right()
            if result != True:
                self.parachute_guy.remove_row_from_parachute()
            if self.check_game_over():
                break
        self.parachute_guy.print_parachute_guy()


    def check_game_over(self):
        #Check if you found the secret word 
        if self.secret_word.found_secret_word():
            return True
        #check if the parachute guy is dead
        if self.parachute_guy.is_dead():
            return True
        else:
            return False
        

        



    
