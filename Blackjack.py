import random

deck = set()
numbers = ["ace", 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, "jack", "queen", "king"]
kinds = ["heart", "diamond", "spade", "club"]

for kind in kinds:
    for number in numbers:
        card = (kind, number)
        deck.add(card)

list_deck = list(deck)
random.shuffle(list_deck)

def hand_values(hand):
    sum = 0
    ace_count = 0
    for card in hand:
        n = card[1]
        if n == "jack" or n == "queen" or n == "king":
            sum += 10
        elif n == "ace":
            ace_count += 1
            sum += 11       #Ace = 11 initially
        else:
            sum += n

    #Ace = 1 if sum exceeds 21
    while sum > 21 and ace_count:
        sum -= 10
        ace_count -= 1

    return sum


def player(hand):
    hand.append(list_deck.pop())
    hand.append(list_deck.pop())
    print(f"Initial hand : {hand[0]}, {hand[1]}")

    while True:
        hand_value = hand_values(hand)
        print(f"Current hand value: {hand_value}")

        if hand_value == 21:
            print("Player wins!")
            return hand_value, "player"

        elif hand_value > 21:
            print("Player lost!")
            return hand_value, "computer"

        # Player chooses to hit or stand
        choice = input("H - Hit or S - Stand: ").strip().upper()
        if choice == "H":
            hand.append(list_deck.pop())
        elif choice == "S":
            return hand_value, None


def computer(players_value):
    computer_hand = []
    computer_hand.append(list_deck.pop())
    computer_hand.append(list_deck.pop())
    print(f"Computer's initial hand: {computer_hand[0]} and {computer_hand[1]}")

    while True:
        comp_value = hand_values(computer_hand)
        print(f"Computer's current hand value: {comp_value}")

        if comp_value == 21:
            print("Computer wins!")
            break

        elif comp_value > 21:
            print("Computer busts! Player wins!")
            break

        elif comp_value >= players_value:
            print("Computer wins!")
            break

        computer_hand.append(list_deck.pop())  # Computer draws another card

    # Print Computer's final hand before returning the result
    print("\nComputer's final hand:", end=" ")
    for card in computer_hand:
        print(f"{card}", end=" ")
    print(f"\nComputer's final hand value: {comp_value}")

    # Return winner based on result
    if comp_value > 21:
        return "player"
    else:
        return "computer"

def main():
    print("\n" + "=" * 20 + " Welcome to Blackjack " + "=" * 20)
    rounds = 0
    score = [0, 0]  # score[0] is the player, score[1] is the computer

    while True:
        rounds += 1
        print("=" * 15)
        print(f"Round {rounds}")
        print("=" * 15)

        hand = []
        player_value, winner = player(hand)
        game_over = False

        if winner == "player":
            score[0] += 1
            game_over = True
        elif winner == "computer":
            score[1] += 1
            game_over = True
        else:
            # Continue to computer's turn if player hasn't won or lost yet
            winner = computer(player_value)
            if winner == "player":
                score[0] += 1
            else:
                score[1] += 1

        # Print player's final hand and value
        print("\nPlayer's final hand:", end=" ")
        for card in hand:
            print(f"{card}", end=" ")
        print(f"\nPlayer's final hand value: {player_value}")
        print("=" * 40)

        # Print the score
        print(f"Score: Player {score[0]} - Computer {score[1]}")

        ch = input("Do you want to play again (Y - YES, N - NO)? ").strip().upper()
        if ch == "N":
            break

main()
