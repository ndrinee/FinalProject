#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:50:59 2023

@author: ndrineavdiu
"""

import random



def menu():
    print("\nChoose a variety of Blackjack:")
    print("\n1. Standard Blackjack")
    print("2. Blackjack with a Twist")
    print("3. Spanish 21")
    print("4. Check the rules")
    print("5. Quit")
    
# Function to choose the variety of Blackjack 
def main():
    while True:
        menu()
        choice = input("Enter the number of your choice: \n")
        if choice == '1':
            print("You selected Standard Blackjack.")
            play_blackjack()
        elif choice == '2':
            print("You selected Blackjack with a Twist.")
            play_blackjack_with_twist()
        elif choice == '3':
            print("You selected Spanish 21.")
            play_spanish_21()
        elif choice=="4":
            file=open("rules.txt","r")
            rules=file.read()
            print(rules)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid option (1-4).")

# Creating the card game
def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Function to calculate hand value
def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 11
            num_aces += 1
        else:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
            value += values.get(rank, 0)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function to display the hand
def display_hand(hand):
    for card in hand:
        print(card['rank'] + ' of ' + card['suit'])


# Function for the Blackjack game
def play_blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]


    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print("Value of your hand:", player_value)

        if player_value == 21:
            print("Blackjack! You win.")
        
            break
        elif player_value > 21:
            print("You busted. Dealer wins.")
            
            break

        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_hand_value(dealer_hand)
            print("Value of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("Dealer busted. You win!")
               
            elif dealer_value >= player_value:
                print("Dealer wins.")
                
            else:
                print("You win!")
                
            break



# Calculate hand value with a twist
def calculate_hand_value_blackjackTwist(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 1  # In this twist, 'A' is worth 1 point
            num_aces += 1
        else:
            values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
            value += values.get(rank, 0)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function for the Blackjack with a twist
def play_blackjack_with_twist():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print("\nValue of your hand:", player_value)

        if player_value == 21:
            print("\nBlackjack! You win.")
            break
        elif player_value > 21:
            print("\nYou busted. Dealer wins.")
            break

        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_hand_value_blackjackTwist(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_hand_value_blackjackTwist(dealer_hand)
            print("\nValue of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("\nDealer busted. You win!")
            elif dealer_value >= player_value:
                print("\nDealer wins.")
            else:
                print("\nYou win!")
            break

# Create a Spanish deck
def create_spanish_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

# Calculate hand value in Spanish 21
def calculate_spanish_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank == 'A':
            value += 1  # In Spanish 21, 'A' is worth 1 point
            num_aces += 1
        elif rank in ['J', 'Q', 'K']:
            value += 10  # Face cards are worth 10 points
        else:
            value += int(rank)

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value

# Function for Spanish 21
def play_spanish_21():
    deck = create_spanish_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    while True:
        print("\nYour hand:")
        display_hand(player_hand)
        player_value = calculate_spanish_hand_value(player_hand)
        print("Value of your hand:", player_value)

        if player_value == 21:
            print("\nSpanish 21! You win.")
            break
        elif player_value > 21:
            print("\nYou busted. Dealer wins.")
            break

        action = input("\nDo you want to 'hit' or 'stand'? ").lower()
        if action == 'hit':
            player_hand.append(deck.pop())
        else:
            while calculate_spanish_hand_value(dealer_hand) < 17:
                dealer_hand.append(deck.pop())

            print("\nDealer's hand:")
            display_hand(dealer_hand)
            dealer_value = calculate_spanish_hand_value(dealer_hand)
            print("\nValue of the dealer's hand:", dealer_value)

            if dealer_value > 21:
                print("\nDealer busted. You win!")
            elif dealer_value >= player_value:
                print("\nDealer wins.")
            else:
                print("\nYou win!")
            break

main()

