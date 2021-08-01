from random import randint, choice
from src.interface.menu import color_text
from time import sleep


def factorial(num: int):
    """
        Calculates the factorial of a number.

        :param num: Number
    """
    tot = 1
    for n in range(1, num + 1):
        tot *= n
    return tot

def combination(p: int):
    """
        Do a cobinatorial analysis using the Combination.

        :param p: number of elements that are repeated
    """
    all_characteres = 71
    return int(factorial(all_characteres)/ factorial(p) * factorial(all_characteres - p))


def generate(word=None, symbols=False, only_numbers=False, numbers=False, uppers=False, position=False, limit=8):
    """
    Generates a random password of 8 or more characters between letters and numbers.

    :param word: word you want to add to the generator.
    if a word is added, only random numbers will be generated that will fill the space to the limit.
    :param max: maximum number that will be generated.
    :param simb: chooses whether to add symbols.
    :param only_numbers: choose whether there will be only numbers.
    :param cap: choose if there will be capital letters.
    :param pos: Changes the position of the name parameter.
"""

    letters = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    )
    while True:
        result: str = ''
        # geração de números
        if only_numbers:
            for c in range(0, limit):
                result += str(randint(0, 9))
        else:
            # geração da palavra-chave
            if word is not None:
                lenght = len(word)
                if numbers:
                    for _ in range(0, limit - lenght + 1):
                        result += str(randint(0, 9))
                elif not numbers:
                    for _ in range(0, limit - lenght + 1):
                        result += choice(letters)
                if position:
                    result = word + result
                elif not position:
                    result += word

            # parte da geração aleatória
            if word is None:
                letters2 = list(letters[:])
                if uppers:
                    for letter in letters:
                        letters2.append(letter.upper())
                if symbols:
                    letters2.append('#')
                    letters2.append('@')
                    letters2.append('+')
                    letters2.append('%')
                    letters2.append('$')
                    letters2.append('!')
                    letters2.append('?')
                    letters2.append('&')
                    letters2.append('*')
                if numbers:
                    for c in range(9):
                        letters2.append(c)
                for c in range(limit):
                    result += str(choice(letters2))
        yield result


def main(archive: str, **kwargs):
    """
        Main function.
    """
    limit = kwargs.get("limit")
    word = kwargs.get("word")
    if limit is None:
        limit = 8
    if word is not None:
        limit -= len(word)
    repeat = limit

    possibilities = {}
    n_possibilites = combination(repeat)
    print(f"Were calculated {color_text('yellow', n_possibilites)} possibilities.")
    print(color_text('white', 'generating ...'))
    print(color_text("yellow", "Press Ctrl + C to stop the script at any time."))
    sleep(3)
    with open(archive, "w+") as file:
        while n_possibilites > 0:
            try:
                for out in generate(kwargs.items()) if kwargs else generate():
                    possibilities[out] = 1
                    if possibilities[out] > 1:
                        print("\033[K", color_text("red", out), end="\r")
                    else:
                        possibilities[out] += 1
                        n_possibilites -= 1
                        file.write(out)
                        print("\033[K", color_text("white", out), end="\r")
                            
            except KeyboardInterrupt:
                print("Script stopped by user.")