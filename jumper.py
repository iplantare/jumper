from sqlite3 import Row


class Jumper:

    def __init__(self):
        row1   =  "  ___ "            
        row2   =  " /___\ "             
        row3   =  " \   / "           
        row4   =  "  \ / "           
        row5   =  "   0  "
        row6   =  "  /|\ "           
        row7   =  "  / \ "
        row8   =  "^^^^^^^^^^"
                              
        self.parachute_rows = [row1, row2, row3, row4, row5, row6, row7, row8]
        
    def print_parachute_guy(self):
        for row in self.parachute_rows:
            print(row)

    def remove_row_from_parachute(self):
        self.parachute_rows.pop(0)   
        if self.is_dead():
            self.parachute_rows[0] = "   X"

    def is_dead(self):
        if len(self.parachute_rows) <= 4:
            return True
        else:
            return False
        


# my_parachute = Jumper()
# my_parachute.print_parachute_guy()
# my_parachute.remove_row_from_parachute()
# my_parachute.print_parachute_guy()



