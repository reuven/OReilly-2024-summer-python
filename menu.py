def menu(choices):
    while True:
        s = input('Choose: ').strip()

        if s in choices:
            return s

        print(f'{s} is invalid; try again')