import logic


# customized two errors
class ValueNotAlpha(Exception):
    """Raised when the input is not an alphabet letter"""
    pass


class ValueNotDesignated4Letter(Exception):
    """Raised when the input letter is an alphabet letter, but not the designated 4 letters"""
    pass


if __name__ == '__main__':
    matt = logic.start()

while True:
    try:
        user_input = input('Please enter the command: ')
        user_input = str(user_input).lower()
        if not user_input.isalpha():
            raise ValueNotAlpha
        if user_input.isalpha() and user_input != 'w' and user_input != 's' \
                and user_input != 'a' and user_input != 'd':
            raise ValueNotDesignated4Letter

        # 'w' = move up
        if user_input == 'w':
            matt, changes = logic.move_up(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 's' = move down
        elif user_input == 's':
            matt, changes = logic.move_down(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 'a' = move left
        elif user_input == 'a':
            matt, changes = logic.move_left(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 's' = move right
        elif user_input == 'd':
            matt, changes = logic.move_right(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

    except ValueNotAlpha:
        print("Invalid value")
        print('Please give the command only by 4 letters: w, s, a, d.')

    except ValueNotDesignated4Letter:
        print("Invalid value")
        print('Please give the command only by 4 letters: w, s, a, d.')


