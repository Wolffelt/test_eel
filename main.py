import eel
import random

combo = ['a', 'b', 'c', 'd', 'i', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$',
         '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\',
         ']', '^', '_', '`', '{', '|', '}', '~']


@eel.expose
def generator(num):
    password = list()
    if num.isdigit():
        num = int(num)
        if num != 0 and 6 <= num <= 20:
            for passwords in range(num):
                password.append(random.choice(combo))
            result = "".join(password)
            return result

        else:
            return "none"
    else:
        return "none"


eel.init('web')
eel.start('index.html', size=(580, 420))