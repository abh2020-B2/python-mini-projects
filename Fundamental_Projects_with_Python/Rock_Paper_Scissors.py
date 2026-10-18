# import and global variables
from random import choice as choice_pc
USER_CHOICES = ("rock", "paper", "scissor")

# create a function to get user input
def get_user_input():
    choice = input(f"Pick Your Choice (\"rock\", \"paper\", \"scissor\") :").lower()
    while choice not in USER_CHOICES:
        choice = input(f"Pick Your Choice (\"rock\", \"paper\", \"scissor\") :").lower()
    return choice

# create a function to get pc input
def get_pc_input():
    pc_input = choice_pc(USER_CHOICES)
    print(f"Computer Is Choice : {pc_input}")
    return pc_input

# compare and determine which one is winner
def determine_winner(user_input,pc_input):
    if user_input == pc_input:
        print("DRAW!")
    elif (user_input == "rock" and pc_input == "scissor") \
                or (user_input == "scissor" and pc_input == "paper") \
                or (user_input == "paper" and pc_input == "rock"):
        print("User WON!")
    else:
        print("Computer WON!")

# create a main function as runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input=user_input, pc_input=pc_input)
    print("End Of Game!")


# main an iterator for doing the game as much as need 
if __name__ == "__main__":
    answer = 'y'
    while answer == 'y':
        main()
        answer = input("Do You Want To Continue? (y/n): ")