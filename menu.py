def menu(choices):
    while True:
        s = input(f'Choose from {"/".join(choices)}: ').strip()

        if s in choices:
            return s

        print(f'{s} is invalid; try again')

if __name__ == '__main__':
    choices = 'abc'

    user_choice = menu(choices)
    print(f'You chose {user_choice}.')
