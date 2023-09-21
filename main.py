import random

# Initialize the deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Define card values
card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(card_values[card['rank']] for card in hand)
    # Check for aces and adjust their value if needed
    for card in hand:
        if card['rank'] == 'Ace' and value > 21:
            value -= 10
    return value


# Function to deal a card from the deck
def deal_card():
    return deck.pop(random.randint(0, len(deck) - 1))


# Initialize player and dealer hands
player_hand = [deal_card(), deal_card()]
dealer_hand = [deal_card(), deal_card()]

# Game loop
while True:
    print("\nPlayer's Hand:")
    for card in player_hand:
        print(f"{card['rank']} of {card['suit']}")
    player_value = calculate_hand_value(player_hand)
    print(f"Total Value: {player_value}")

    # Check for player bust
    if player_value > 21:
        print("Player busts! Dealer wins.")
        break

    action = input("Do you want to 'hit' or 'stand'? ").lower()

    if action == 'hit':
        player_hand.append(deal_card())
    elif action == 'stand':
        break

# Dealer's turn
while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(deal_card())

print("\nDealer's Hand:")
for card in dealer_hand:
    print(f"{card['rank']} of {card['suit']}")
dealer_value = calculate_hand_value(dealer_hand)
print(f"Total Value: {dealer_value}")

# Determine the winner
if dealer_value > 21:
    print("Dealer busts! Player wins.")
elif player_value > dealer_value:
    print("Player wins!")
elif dealer_value > player_value:
    print("Dealer wins!")
else:
    print("It's a tie!")

