def menu(choices):
    while True:
        s = input(f'Choose from {"/".join(choices)}: ').strip()

        if s in choices:
            return s

        print(f'{s} is invalid; try again')