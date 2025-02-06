from stack import *


def main():
    """
    A Towers of Hanoi game for the terminal.
    """
    # initialise variables
    left_stack = Stack("Left")
    middle_stack = Stack("Middle")
    right_stack = Stack("Right")
    stacks = [left_stack, middle_stack, right_stack]
    initials = [stack.get_name()[0] for stack in stacks]
    num_moves = 0

    # welcome the user
    print(
        '''\n
###################################
WELCOME TO THE TOWERS OF HANOI GAME   
###################################
        ''')

    # populate the left stack with the number of disks specified by the user
    num_disks = 0
    while num_disks < 3:
        num_disks = int(
            input("\nHow many disks do you want to play with (at least 3)?\n")
        )
    for i in range(num_disks, 0, -1):
        left_stack.push(i)

    # tell the user the optimal number of moves with this many disks
    optimal_moves = 2 ** num_disks - 1
    print(f'\nFor {num_disks} disks, the optimal number of moves is {optimal_moves}\n')

    # while the game isn't over
    while right_stack.get_size() < num_disks:
        
        # ask the user for their next move (and keep asking until their input and move are valid)
        while True:

            # show the current state of the stacks
            print('\n...Current Stacks...\n')
            for stack in stacks:
                stack.print_items()

            # ask which stack to move a disk from and to
            for i in range(len(stacks)):
                print(f'Choose {initials[i]} for {stacks[i].get_name()}')
            from_option = input('\nWhich stack do you want to move from?\n')
            to_option = input('\nWhich stack do you want to move to?\n')

            # check that the input is valid
            if from_option not in initials or to_option not in initials:
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print('\nInvalid choice. Please choose again.\n')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                continue
            from_stack = [stack for stack in stacks if stack.get_name()[0] == from_option][0] 
            to_stack = [stack for stack in stacks if stack.get_name()[0] == to_option][0] 

            # check that the move is valid
            if from_stack.is_empty():
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(f'\nInvalid move. {from_stack.get_name()} stack is empty. Try again.\n')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                continue
            elif (not to_stack.is_empty()) and (int(from_stack.peek()) > int(to_stack.peek())):
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                print(f'\nInvalid move. You are moving a larger disk onto a smaller disk. Try again.\n')
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                continue
            else:
                break
        
        # when a valid move has been chosen, remove the disk from the old stack and move it to the new stack
        to_stack.push(from_stack.pop())
        num_moves += 1

    # tell the user how many moves they took compared to the optimal number
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print(f'\nWell done! You completed the game in {num_moves} moves compared to the minimum possible number of {optimal_moves}.\n')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

if __name__ == "__main__":
    main()
