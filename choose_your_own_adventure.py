class Game():
    
    def __init__(self, name):
        self.name = name
        self.end = False
    
    def _choice(self, choices, input_string, next, end_string):
        choice = input(input_string) 

        while choice not in choices:
            choice = input(input_string) 
            
        if choice == choices[0]:
            next()
        elif choice == choices[1]:
            print(end_string)
            self.end_game()
     
    def start(self):
        print("""
        Welcome, {}.  
        You run into the building, and see a body in the middle of the room.
        Out of the corner of your eye, you spot a figure scrambling out the window
                
        Do you:
        - Stay and check the body, or
        - Chase the figure!""".format(self.name))
        print()
        
        input_string = "Enter 1 to stay; enter 2 to chase\n"
        end_string = "DEATH!!"
        self._choice(("1", "2"), input_string, self.check_house, end_string)

    def check_house(self):
        print("""
        The body is a man, who is not responsive. You think to yourself that you 
        should probably check the rest of the house.
        The house has two floors.
        
        Do you:
        - Stay downstairs and check the other rooms, or
        - Go upstairs and take a look there?""")
        print()
        
        input_string = "Enter 1 to go downstairs; enter 2 to check upstairs\n"
        end_string = "Eaten by goblins!!"
        self._choice(("2", "1"), input_string, self.go_upstairs, end_string)
        
    def go_upstairs(self):
        print("""
        You hear commotion coming from a room at the end of the corridor. 
        
        Do you:
        - Investigate, or
        - Call for help?""")
        print()
        
        input_string = "Enter 1 to go investigate; enter 2 to call for help\n"
        end_string = "DEATH!!"
        self._choice(("1", "2"), input_string, self.investigate, end_string)
    
    def investigate(self):
      
        print("""
        You find a woman lying on the floor in a pool of blood.

        Do you:
        - Phone an ambulance or
        - Question her?""")
        print()

        input_string = "Enter 1 to phone an ambulance; enter 2 to question her\n"
        end_string = "DEATH!!"
        self._choice(("2", "1"), input_string, self.question, end_string)
    
    def question(self):
        
        print("""
        You question the woman who tells you that she has been stabbed 
        by the vicious killer Kate. Well done Detective {}!""".format(self.name))
        self.end_game()
    def end_game(self):
        self.end = True

def start_game():
    name = input("What is your name?\n") 
    new_game = Game(name)
    while new_game.end == False:
        new_game.start()
    
    print("\n============")
    print("Game over")
    print("=============\n")
    restart = input("Would you like to play again? Y/N\n")

    if restart.upper() == "Y":
        start_game()

print("=========================")
print("Choose Your Own Adventure")
print("=========================")
start_game()
    