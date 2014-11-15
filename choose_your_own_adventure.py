import sys 

class Game():
    
    def __init__(self, file, name):
        self.name = name
        self.end = False
        file = file.read()
        data = file.split("\n\n")
          
        self.title = data[0].split(",")[0]
        data = data[1:]
        self.story_text = []
        self.question = []
        self.input_string = []
        self.end_string = []
        self.continue_response = []
        self.end_response = []
        
        for number, paragraph in enumerate(data, 1):
            if number % 6 == 1:
                self.story_text.append(paragraph)
            elif number % 6 ==2:
                self.question.append(paragraph)
            elif number % 6 ==3:
                paragraph = paragraph + "\n" 
                self.input_string.append(paragraph)
            elif number % 6 ==4:
                self.end_string.append(paragraph) 
            elif number % 6 ==5:
                self.continue_response.append(paragraph)
            elif number % 6 ==0:
                self.end_response.append(paragraph.strip())   
                                
    def _choice(self, choices, input_string, end_string, index):
        choice = input(input_string) 
        
        while choice not in choices:
            choice = input(input_string)

        if choice == choices[0]:
            if index == len(self.story_text) - 1:
                self.end_game()
        elif choice == choices[1]:
            print(end_string, "\n")
            self.end_game()
    
    def create_story(self):
        print("Welcome to the story {}: {}\n".format(self.name, self.title))
        
        for i, paragraph in enumerate(self.story_text, 0):
            if not self.end:
                print(paragraph, "\n")
                print(self.question[i], "\n")
                self._choice((self.continue_response[i], self.end_response[i]), 
                              self.input_string[i], self.end_string[i], i)
      
    def end_game(self):
        self.end = True

def start_game():
    file = open(sys.argv[-1], "r")

    name = input("What is your name?\n") 
    new_game = Game(file, name)
    while new_game.end == False:
        new_game.create_story()
    
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
    