class UserInput:
    def get_choice(self, prompt, valid_choices):
        while True:
            user_input = input(prompt).lower()
            if user_input in valid_choices:
                return user_input
            else:
                print("Invalid choices, please try again.")
