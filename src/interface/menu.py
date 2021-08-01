def color_text(c: str, txt):
    """
        To edit the text color.

        :param c: color.
        :param txt: text
    """
    if c == 'red':
        return '\033[91m{}\033[m'.format(txt)
    elif c == 'white':
        return '\033[97m{}\033[m'.format(txt)
    elif c == 'green':
        return '\033[92m{}\033[m'.format(txt)
    elif c == 'yellow':
        return '\033[93m{}\033[m'.format(txt)
    elif c == 'blue':
        return '\033[94m{}\033[m'.format(txt)
    elif c == 'cyan':
        return '\033[96m{}\033[m'.format(txt)
    elif c == 'magenta':
        return '\033[95m{}\033[m'.format(txt)


def line(tam=43):
    """
        Returns the number of the argument size. Remembering that the size is in pixels.
    """
    return '-' * tam


def main_menu(opc:list[str]) -> int:
    """
        A main little boy ready.

        :param opc: options.

        There is no need for the exit option, the code does it automatically.
    """
    c = 1
    e = 'Exit the program.'
    for item in opc:
        print(f'[ {color_text("green", c)} ] - {color_text("white", item)}')
        c += 1
    print(f'[ {color_text("green", c)} ] - {color_text("white", e)}')
    print(line())
    print(color_text('yellow', 'Enter a number: '), end='')
    opc = int(input())
    if opc > c:
        print(color_text('red', 'You have crossed the limit of options!'))
    elif opc == 0:
        print(color_text('red', 'There is no option 0!'))
    return opc
