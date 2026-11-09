
import random


def get_random_word():
    """Selecciona y devuelve una palabra aleatoria desde wordlist.txt"""
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        words = []

        for line in file:
            word = line.strip()

            # Conserva únicamente letras y espacios.
            word = "".join(
                char for char in word
                if char.isalpha() or char.isspace()
            )

            if word.strip():
                words.append(word)

    if not words:
        raise ValueError("La lista de palabras está vacía o no contiene palabras válidas.")

    return random.choice(words)
