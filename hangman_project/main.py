
#!/usr/bin/python3

from game import HangmanGame
from utils import get_random_word


def main():
    """Inicia el juego y solicita una letra válida al usuario."""
    word = get_random_word()
    game = HangmanGame(word)

    print("¡Bienvenido al juego del ahorcado!")
    print(game.display_progress())

    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida. Ingresa una sola letra.")
            continue

        if letter in game.guessed_letters:
            print("Ya ingresaste esa letra. Intenta con otra.")
            continue

        game.guessed_letters.append(letter)
        print("Letra ingresada correctamente.")
        break


if __name__ == "__main__":
    main()
