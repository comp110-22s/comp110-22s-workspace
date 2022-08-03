"""Blackjack!"""

import random


player_cards = []
dealer_cards = []

while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has: X &", dealer_cards[1])


while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("You have:", player_cards)

while sum(dealer_cards) <= 16:
    dealer_cards.append(random.randint(1, 11))

if sum(dealer_cards) == 21:
    print("Dealer wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted.")

while sum(player_cards) < 21:
    draw_card = str(input("Do you want to hit or stay? "))
    if draw_card == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if sum(player_cards) > 21:
            print("You busted! Dealer wins.")
            break
        elif sum(player_cards) == 21:
            print("You win!")
            break
        elif sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
            break
        else:
            print("You win!")
            break

# def main() -> None:
#     assign_cards()


# def assign_cards() -> None:
#     dealer_cards = []
#     player_cards = []

#     while len(dealer_cards) != 2:
#         dealer_cards.append(random.randint(1, 11))
#         if len(dealer_cards) == 2:
#             print("Dealer has: X &", dealer_cards[1])

#     while len(player_cards) != 2:
#         player_cards.append(random.randint(1, 11))
#         if len(player_cards) == 2:
#             print("You have:", player_cards)

#     hit(player_cards)
#     dealer_hit(dealer_cards)
#     score(hit, dealer_hit)


# def hit(player_hand) -> int:
#     hit: str = input("Would you like another card? Y or N. ")
#     while sum(player_hand) <= 21:
#         if hit.lower == "y":
#             player_hand.append(random.randint(1, 11))
#             print("You have:", player_hand)
#         elif hit.lower == "n":
#             break
#     return sum(player_hand)


# def dealer_hit(dealer_hand) -> int:
#     while sum(dealer_hand) <= 16:
#         dealer_hand.append(random.randint(1, 11))
#     return sum(dealer_hand)


# def score(player_score, dealer_score) -> None:
#     if player_score > 21:
#         print("You went over 21. You lose.")
#         return None
#     if dealer_score > 21:
#         print("The dealer went over 21. You win!")
#         return None
#     if dealer_score == player_score:
#         print("Tie!")
#         return None
#     elif dealer_score > player_score:
#         print("You win")
#         return None
#     else:
#         print("You lose.")
#         return None


# if __name__ == "__main__":
#     main()