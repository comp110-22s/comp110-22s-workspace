"""Blackjack!"""

import random


def main() -> None:
    assignCardsToPlayers()


def assignCardsToPlayers() -> None:
    playerCards = []
    dealerCards = []

    while len(dealerCards) != 2:
        dealerCards.append(random.randint(1, 11))
    print("Dealer has: X &", dealerCards[1])

    while len(playerCards) != 2:
        playerCards.append(dealNewCard())
    print("You have:", playerCards)

    playerHitOrStay(dealerCards, playerCards)


def dealNewCard() -> int:
    card: int = random.randint(1, 11)
    if card == 1 or card == 11:
        aceCardValue = str(input("You got an ace. Would you like it to be a 1 or 11? "))
        if aceCardValue == "1":
            return 1
        else:
            return 11
    else:
        return card


def playerHitOrStay(dealerCards, playerCards) -> None:
    while sum(playerCards) < 21:
        hitInput = str(input("Do you want to hit or stay? "))
        if hitInput == "hit":
            playerCards.append(dealNewCard())
            print("You now have a total of " + str(sum(playerCards)) + " from these cards", playerCards)
        else:
            break
    testSumOfCards(dealerCards, playerCards)


def dealerHitOrStay(dealerCards, playerCards) -> None:
    print("Dealer has:", dealerCards)
    while sum(dealerCards) <= 16:
        dealerCards.append(random.randint(1, 11))
        print("Dealer hits. New hand:", dealerCards)
        if sum(dealerCards) > 21:
            print("Dealer busts! You win!")
            return
        input("Press enter to continue ")
    determineWhoWon(dealerCards, playerCards)


def testSumOfCards(dealerCards, playerCards) -> None:
    if sum(playerCards) > 21:
        print("Bust! You lose.")
        return
    dealerHitOrStay(dealerCards, playerCards)


def determineWhoWon(dealerCards, playerCards) -> None:
    if sum(dealerCards) == sum(playerCards):
        print("Tie!")
    if (sum(dealerCards) > sum(playerCards)):
        print("Dealer wins.")
    if (sum(dealerCards) < sum(playerCards)):
        print("You win!")


if __name__ == "__main__":
    main()