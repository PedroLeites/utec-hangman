
class HangmanGame:
    """Representa el estado y el progreso de una partida de ahorcado."""

    def __init__(self, word):
        """Inicializa una nueva partida."""
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra las letras adivinadas y oculta las restantes."""
        progress = ""

        for letter in self.word:
            if letter.isalpha():
                if letter in self.guessed_letters:
                    progress += letter + " "
                else:
                    progress += "_ "
            else:
                progress += letter + " "

        return progress.strip()


    def process_guess(self, letter):
        """Procesa una letra ingresada por el jugador."""
        if letter in self.word:
            if letter not in self.guessed_letters:
                self.guessed_letters.append(letter)
            return True

        self.errors += 1
        return False


    def is_won(self):
        """Comprueba si el jugador ha adivinado todas las letras."""
        for letter in self.word:
            if letter.isalpha() and letter not in self.guessed_letters:
                return False
        
        return True

    def is_lost(self):
        """Comprueba si el jugador ha alcanzado el máximo de errores."""
        if self.errors >= self.max_errors:
            return True
        
        return False
