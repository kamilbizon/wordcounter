from sys import argv, exit



def main():

    flags = []
    if len(argv) == 2:
        flags += ["-c", "-l", "-w"]
    elif len(argv) > 2:
        if argv[2]:
            for i in argv[1:-1]:
                flags += [i]

    file = open_file()

    read_file = file.read()

    count_by_flags(flags, read_file)


    file.close()



def count_by_flags(flags, read_file):

    if "--version" in flags:
        print("First version of word counter copy by Kamil Bizoń :)")
        exit()

    if "-l" in flags or "--lines" in flags:
        number_of_lines = len(open(argv[-1], 'r').readlines())
        print(number_of_lines, " ", end='')

    if "-w" in flags or "-words" in flags:
        number_of_words = len(read_file.split())
        print(number_of_words, " ", end='')

    if "-m" in flags or "--chars" in flags:
        number_of_characters = len(read_file)
        print(number_of_characters, " ", end='')

    if "-c" in flags or "--bytes" in flags:
        size_of_file = int(read_file.__sizeof__() / 4)
        print(size_of_file, " ", end='')

    if "-L" in flags or "--max-line-length" in flags:
        longest_line_length = 15
        print(longest_line_length)

    print(argv[-1])




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