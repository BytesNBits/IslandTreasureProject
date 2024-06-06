from message_printer import MessagePrinter
from user_input import UserInput


class Game:
    def __init__(self):
        self.dialogues = [
            "left or right?",
            "Swim or wait?",
            "Which door? red, blue, or yellow?",
            "Congrats! You found the treasure!",
            "Oh No! You lost",
            "You were eaten by a shark. GAME OVER.",
            "Wrong door, Bye Bye!"
        ]
        self.correct_choices = ["left", "wait", "yellow"]
        self.bad_choices = ["right", "swim", "red", "blue"]
        self.printer = MessagePrinter()
        self.user_input = UserInput()

    def start(self):
        self.printer.opening_message()
        self.main_story()

    def main_story(self):
        print(self.dialogues[0])
        user = self.user_input.get_choice("What is your choice? \n", ['left', 'right'])
        if user == self.correct_choices[0]:  # 'left'
            self.printer.slow_print(self.dialogues[1])
            user = self.user_input.get_choice("What is your choice? \n", ['swim', 'wait'])
            if user == self.correct_choices[1]:  # 'wait'
                self.printer.slow_print(self.dialogues[2])
                user = self.user_input.get_choice("What is your choice? \n", ['red', 'blue', 'yellow'])
                if user == self.correct_choices[2]:  # 'yellow'
                    self.printer.slow_print(self.dialogues[3])
                    self.printer.treasure_ending()
                elif user in self.bad_choices[2:]:  # 'red' or 'blue'
                    self.printer.slow_print(self.dialogues[6])
            elif user == self.bad_choices[1]:  # 'swim'
                self.printer.slow_print(self.dialogues[5])
        elif user == self.bad_choices[0]:  # 'right'
            self.printer.slow_print(self.dialogues[4])
        self.replay()

    def replay(self):
        while True:
            user = self.user_input.get_choice("Do you want to play again? (yes/y/no/n): \n ", ["yes", "y", "no", "n"])
            if user in ["yes", "y"]:
                self.start()  # Using 'self' to call the start method
            elif user in ["no", "n"]:
                self.printer.slow_print("Thanks for playing!")
                break
