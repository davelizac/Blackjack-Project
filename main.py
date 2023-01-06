############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
##################################################
#coding space below this line
##################################################  

from art import logo
import random
from replit import clear

#MAIN FUNCTIONS:

def card_dealing():
    """Esta función se encargará de repartir las cartas a los jugadores"""
    #Presta atención a cómo se pueden asinar funciones a las variables (línea 33)!
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculating_score(cards):
    """Ésta función suma el puntaje obtenido de las cartas y evalúa si algún jugador obtuvo el Blackjack, así como si el 'As' en la baraja debe valer 1 u 11 en base a los puntajes obtenidos previamente"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) >= 20:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def comparing_score(user_score, computer_score):
    """Esta función evaluará cual de los jugadores gana el juego o si hay un empate"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game(): 
    
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False
     #FIST ROUND CARD FOR PLAYERS: This function is really different and interesting compare to the one that I originally made. Here in line 72 you make a for loop that doesn't loop through any list or dictionary but in an "artificial range", so to say, in order to add two cards to the player_cards and computers_cards lists.   
    for _ in range(2):
        user_cards.append(card_dealing()) #remember that here the cards are being randomly added to the player_cards list through a function that you previously defined
        computer_cards.append(card_dealing())

    while not is_game_over:
        user_score = calculating_score(user_cards)
        computer_score = calculating_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(card_dealing())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
         computer_cards.append(card_dealing())
         computer_score = calculating_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(comparing_score(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()


                
        


