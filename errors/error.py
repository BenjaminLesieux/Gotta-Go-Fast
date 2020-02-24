class GGFError:
    WRONG_ARGUMENT = "[GGF] Une erreur d'argument a été detectée dans la classe : "

    def __init__(self, screen, type, directory):
        self.screen = screen
        self.type = type
        self.directory = directory

    def log(self):
        print(self.type + self.directory)
        self.screen.stop()
