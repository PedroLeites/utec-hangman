
#!/usr/bin/python3

from game import HangmanGame
from utils import get_random_word


def main():
    """Inicia el juego y solicita una letra válida al usuario."""
    word = get_random_word()
    game = HangmanGame(word)

    print("¡Bienvenido al juego del ahorcado!")
    game.display_hangman()
    print("\nPalabra:", game.display_progress())

    while not game.is_won() and not game.is_lost():
        letter = input("\nIngresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida. Ingresa una sola letra.")
            continue

        if letter in game.guessed_letters:
            print("Ya ingresaste esa letra. Intenta con otra.")
            continue

        if game.process_guess(letter):
            print("¡Correcto! La letra está en la palabra.")
            game.display_hangman()
        else:
            print("Incorrecto. La letra no está en la palabra.")
            game.display_hangman()

        print("\nPalabra:", game.display_progress())
        print("Letras adivinadas:", game.guessed_letters)
        print("Intentos restantes:", game.max_errors - game.errors)
    
    if game.is_won():
        print("\n¡Ganaste!")
    else:
        print("\nTe quedaste sin intentos. Fin del juego.")
        print("La palabra era:", game.word)
    

if __name__ == "__main__":
    main()
