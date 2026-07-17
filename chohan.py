import sys
import random

def return_random_dice():
    return random.randint(1,6)

def validate_bet(amount):
    while True:
        print(f"You have {amount} mon. How much do you bet?")
        user_bet = input('> ')
        if user_bet.upper() == 'QUIT' or user_bet.startswith('Q'):
            sys.exit()

        if not user_bet.isdecimal():
            continue
        user_bet = int(user_bet)
        if 0<user_bet<=amount:
            return user_bet

def decide_who_wins(user_response, sum_):
    if user_response.lower() == 'cho':
        return sum_%2==0
    elif user_response.lower() == 'han':
        return sum_%2!=0

def main():
    print("""In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
    """)
    total_given_amount = 5000
    while True:
        bet_amount = validate_bet(total_given_amount)
        print("""
The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor, still covering the
dice and asks for your bet. 
        """)

        while True:
            even_odd = input("CHO (even) or HAN (odd)?\n> ")
            if even_odd.lower() in ['cho', 'han']:
                break
            print("Invalid choice! Please type 'cho' or 'han'.")

        dice1 = return_random_dice()
        dice2 = return_random_dice()
        sum_amount = dice1 + dice2
        result = decide_who_wins(even_odd, sum_amount)

        print("The dealer lifts the cup to reveal:")
        print("{}-{}".format(dice1, dice2))

        if result:
            house_fee_amount = bet_amount // 10
            bet_amount -= house_fee_amount
            total_given_amount += bet_amount
            # display the info to the user
            print(f"You won! You take {bet_amount} mon.\n"
                  f"The house collects a {int(house_fee_amount)} mon fee.")
        else:
            print("You lost!")
            total_given_amount -= bet_amount

        if total_given_amount<=0:
            print("You are out of money")
            break

        user_continues = input("Do you want to continue? YES/NO\n> ")
        if user_continues.upper() != 'YES':
            break


if __name__=="__main__":
    main()

