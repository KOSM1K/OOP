# colors specified for current purpose
# in future make a class for controlling queue of printing to console.

colors = {
    'bas': '\033[0m',
    'gre': '\033[32m',
    'yel': '\033[33m\033[7m',
    'red': '\033[31m',
    'cya': '\033[36m\033[7m'
}


def printCLR(color, text):
    print(colors[color], text, colors['bas'], sep='', end='')


if __name__ == '__main__':
    printCLR('gre', '[I]')
    print(' something', end='')
