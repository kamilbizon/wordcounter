from sys import argv, exit


def main():

    flags = []

    if len(argv) == 1:
        flags += ["-c", "-l", "-w"]
        read_file = ''
        read_file = input()


    if len(argv) == 2:
        if "--version" in argv:
            print("First version of word counter copy by Kamil Bizoń")
            exit()

        if "--help" in argv:
            print('''Usage: python wc.py [OPTION]... [FILE]
            print newline, word, and byte counts for each file

            The options below may be used to select which counts are printed, always  in  the  following  order:  newline,
           word, character, byte, maximum line length.

           -c, --bytes
                  print the byte counts

           -m, --chars
                  print the character counts

           -l, --lines
                  print the newline counts

            -L, --max-line-length
                  print the maximum display width

           -w, --words
                  print the word counts

           --help display this help and exit

           --version
                  output version information and exit

            Manual written by Paul Rubin and David MacKenzie.
            ''')
            exit()

        file_name = argv[-1]
        flags += ["-c", "-l", "-w"]
        file = open_file()
        read_file = file.read()
        file.close()

    elif len(argv) > 2:
        if argv[2]:
            for i in argv[1:]:
                flags += [i]
        file_name = argv[-1]
        file = open_file()
        read_file = file.read()
        file.close()

    count_by_flags(flags, read_file, file_name)


def count_by_flags(flags, read_file, file_name):

    if "-l" in flags or "--lines" in flags:
        number_of_lines = read_file.count('\n') + 1     # always one '\n' less than lines
        print(number_of_lines, " ", end='')
        flags.remove("-l")

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
        longest_line = max(open(argv[-1], 'r').readlines(), key=len)
        longest_line.strip('\n')
        longest_line_length = len(longest_line)
        print(longest_line_length)

    print(file_name)


def open_file():

    file = None
    try:
        file = open(argv[-1], 'r')
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
