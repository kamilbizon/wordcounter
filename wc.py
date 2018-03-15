from sys import argv, exit



def main():
    if len(argv) == 1:
        pass
    elif len(argv) > 2:
        if argv

    file = open_file()

    read_file = file.read()

    number_of_lines = len(open(argv[-1], 'r').readlines())
    number_of_words = len(read_file.split())
    number_of_characters = len(read_file)
    size_of_file = read_file.__sizeof__()

    file.close()

    print(number_of_lines, " ", number_of_words, " ", number_of_characters, " ", size_of_file, " ", argv[-1])


def open_file():
    file = None
    try:
        file = open(argv[-1], 'rU')
    except FileNotFoundError:
        print("wc: ", argv[-1], ": No such file or directory")
        exit()
    except PermissionError:
        print("wc:", argv[-1], ": Permission denied")
        exit()
    except IsADirectoryError:
        print("wc:", argv[-1], ": Is Directory")
        print("0\t0\t0 ", argv[-1])
        exit()

    return file


if __name__ == '__main__':
    main()