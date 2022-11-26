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
        if not user_input.isalpha():
            raise ValueNotAlpha
        if user_input.isalpha() and user_input.lower() != 'w' and user_input.lower() != 's' \
                and user_input.lower() != 'a' and user_input.lower() != 'd':
            raise ValueNotDesignated4Letter

        # 'w' = move up
        if user_input == 'w' or user_input == 'W':
            matt, changes = logic.move_up(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 's' = move down
        elif user_input == 's' or user_input == 'S':
            matt, changes = logic.move_down(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 'a' = move left
        elif user_input == 'a' or user_input == 'A':
            matt, changes = logic.move_left(matt)
            status = logic.get_status(matt)
            print(status)

            if status == 'Game is not over.':
                logic.add_new_2(matt)
            else:
                break

            # 's' = move right
        elif user_input == 'd' or user_input == 'D':
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


