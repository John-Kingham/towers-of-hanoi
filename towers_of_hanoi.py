from stack import *


class Game:

    # set up a new game with a specified number of disks
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.num_moves = 0
        self.left_stack = Stack("Left")
        self.middle_stack = Stack("Middle")
        self.right_stack = Stack("Right")
        self.stacks = [self.left_stack, self.middle_stack, self.right_stack]
        for i in range(num_disks, 0, -1):
            self.left_stack.push(i)

    # return the minimum possible number of moves
    def get_min_moves(self):
        return 2**self.num_disks - 1

    # return whether the game is over or not
    def is_over(self):
        return self.right_stack.get_size() == self.num_disks

    # returns the state of the game's stacks as a string
    def to_String(self):
        as_string = ""
        for stack in self.stacks:
            as_string += "\n" + stack.to_string()
        return as_string

    # make a move as specified by the user (and let the user know if the move isn't valid)
    def move(self, from_stack, to_stack):

        # check that the move is valid
        first_stack = self.stacks[from_stack]
        second_stack = self.stacks[to_stack]
        if first_stack.is_empty():
            message = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            message += f"\nInvalid move. You are trying to move from an empty stack is empty. Try again.\n"
            message += "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            return message
        elif (not second_stack.is_empty()) and (
            int(first_stack.peek()) > int(second_stack.peek())
        ):
            message = "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            message += f"\nInvalid move. You are moving a larger disk onto a smaller disk. Try again.\n"
            message += "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
            return message

        # a valid move has been chosen so remove the disk from the first stack and move it to the second stack
        second_stack.push(first_stack.pop())
        self.num_moves += 1
        return None

    def get_num_moves(self):
        return self.num_moves


def main():
    """
    A Towers of Hanoi game for the terminal.
    """
    # initialise variables
    initials = {"L": ["Left", 0], "M": ["Middle", 1], "R": ["Right", 2]}

    # welcome the user
    print(
        """\n
###################################
WELCOME TO THE TOWERS OF HANOI GAME   
###################################
        """
    )

    # ask the user how many disks they want to play with
    num_disks = 0
    while num_disks < 3:
        num_disks = int(
            input("\nHow many disks do you want to play with (at least 3)?\n")
        )
    game = Game(num_disks)

    # tell the user the minimum possible number of moves
    print(
        f"\nFor {num_disks} disks, the optimal number of moves is {game.get_min_moves()}\n"
    )

    # while the game isn't over
    while not game.is_over():

        # ask for the next move (and keep asking until their input and move are valid)
        while True:

            # show the current state of the stacks
            print("\n...Current Stacks...\n")
            print(game.to_String())

            # ask which stack to move from and to
            for initial in initials.keys():
                print(f"Choose {initial} for {initials[initial][0]}")
            from_option = input("\nWhich stack do you want to move from?\n")
            to_option = input("\nWhich stack do you want to move to?\n")

            # check that the option is valid
            if from_option not in initials.keys() or to_option not in initials.keys():
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("\nInvalid choice. Please choose again.\n")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                continue

            # try to make the move
            message = game.move(initials[from_option][1], initials[to_option][1])
            if message:
                # if the move wasn't valid, tell the user what they did wrong and ask them to try again
                print(message)
                continue
            else:
                # if the move was valid, carry on with the game
                break

    # the game is over, so tell the user how many moves they took compared to the optimal number
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(
        f"\nWell done! You completed the game in {game.get_num_moves()} moves compared to the minimum possible number of {game.get_min_moves()}.\n"
    )
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


if __name__ == "__main__":
    main()
