# my_project/__init__.py

# Import key classes to make them available at the package level
from game import Game
from message_printer import MessagePrinter
from user_input import UserInput

__all__ = ["Game", "MessagePrinter", "UserInput"]

if __name__ == "__main__":
    game = Game()
    game.start()
