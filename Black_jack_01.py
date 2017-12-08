import random

#variables

ace_of_hearts = 11
ace_of_spades = 11
ace_of_clubs = 11
ace_of_diamonds = 11


king_of_hearts = 10
king_of_spades = 10
king_of_diamonds = 10
king_of_clubs = 10


queen_of_hearts = 10
queen_of_diamonds = 10
queen_of_spades = 10
queen_of_clubs = 10


jack_of_hearts = 10
jack_of_spades = 10
jack_of_clubs = 10
jack_of_diamonds = 10


ten_of_hearts = 10
ten_of_clubs = 10
ten_of_diamonds = 10
ten_of_spades = 10


nine_of_hearts = 9
nine_of_spades = 9
nine_of_clubs = 9
nine_of_diamonds = 9


eight_of_hearts = 8
eight_of_clubs = 8
eight_of_diamonds = 8
eight_of_spades = 8


seven_of_hearts = 7
seven_of_clubs = 7
seven_of_spades = 7
seven_of_diamonds = 7


six_of_hearts = 6
six_of_diamonds = 6
six_of_clubs = 6
six_of_spades = 6


five_of_hearts = 5
five_of_diamonds = 5
five_of_clubs = 5
five_of_spades = 5


four_of_hearts = 4
four_of_diamonds = 4
four_of_spades = 4
four_of_clubs = 4


three_of_hearts = 3
three_of_spades = 3
three_of_clubs = 3
three_of_diamonds = 3


two_of_hearts = 2
two_of_clubs = 2
two_of_diamonds = 2
two_of_spades = 2



list_of_cards = [two_of_spades, two_of_diamonds, two_of_clubs, two_of_hearts,three_of_diamonds,
                 three_of_clubs, three_of_spades, three_of_hearts, four_of_clubs, four_of_spades,
                 four_of_diamonds, four_of_hearts, five_of_spades, five_of_clubs,  five_of_diamonds,
                 five_of_hearts, six_of_spades, six_of_clubs, six_of_diamonds, six_of_hearts,
                 seven_of_diamonds, seven_of_spades, seven_of_clubs, seven_of_hearts,
                 eight_of_spades, eight_of_diamonds, eight_of_clubs, eight_of_hearts,
                 nine_of_diamonds, nine_of_clubs, nine_of_spades, nine_of_hearts,
                 ten_of_spades, ten_of_diamonds, jack_of_spades, ten_of_hearts,
                 jack_of_diamonds, jack_of_clubs, jack_of_spades,  jack_of_hearts,
                 queen_of_clubs, queen_of_spades, queen_of_diamonds, queen_of_hearts,
                 king_of_clubs, king_of_diamonds, king_of_spades, king_of_hearts,
                 ace_of_diamonds, ace_of_clubs, ace_of_spades, ace_of_hearts]




random_card_1 = random.choice(list_of_cards)
random_card_2 = random.choice(list_of_cards)
#print list out

def print_list(cards):
    for i in cards:
        print(i, end = " ")


def deal_cards_for_player_1(random_card_1, random_card_2):
    random_card_1 = random.choice(list_of_cards)
    random_card_2 = random.choice(list_of_cards)
    list_of_cards.remove(random_card_1)
    list_of_cards.remove(random_card_2)
    total = random_card_1 + random_card_2
    print("Your cards will be", random_card_1, "and", random_card_2, "which equals", total,"\n")
    if total == 21:
        print("You have a natural black jack. If the dealer doesn't get a black jack than you won againts the dealer.")
    elif total < 21:
        print("your cards equal", total, "which is", 21-total, "points away from a black jack.\n")
        hit_or_stand = int(input("if you would want another card choose 1 to stay with what you have choose 2: "))

        if hit_or_stand == 1:
            random_card_3 = random.choice(list_of_cards)
            total += random_card_3
            print("The card you got is", random_card_3, "which in total now you have", total)
            if total == 21:
                print("you got a black jack lets see what he dealer gets")
            elif total < 21:
                 print("your cards equal", total, "which is", 21-total, "points away from a black jack.\n")
                 hit_or_stand = int(input("if you would want another card choose 1 to stay with what you have choose 2: "))
                 if hit_or_stand == 1:
                     random_card_4 = random.choice(list_of_cards)
                     total += random_card_4
                 elif hit_or_stand == 2:
                     print("Your total is", total, "good luck against the dealer")
            elif total > 21:
                print("You went over 21 you lost")
        elif hit_or_stand == 2:
            print("okay your toal is", total,"lets see if you will beat the dealer")

def deal_cards_for_player_2(random_card_1, random_card_2):
    random_card_1 = random.choice(list_of_cards)
    random_card_2 = random.choice(list_of_cards)
    list_of_cards.remove(random_card_1)
    list_of_cards.remove(random_card_2)
    total = random_card_1 + random_card_2
    print("Your cards will be", random_card_1, "and", random_card_2, "which equals", total,"\n\n")
        

def deal_cards_for_dealer(random_card_1, random_card_2):
 
    random_card_1 = random.choice(list_of_cards)
    random_card_2 = random.choice(list_of_cards)
    list_of_cards.remove(random_card_1)
    list_of_cards.remove(random_card_2)
    print("The dealers cards will be", random_card_1, "and the second card is unrevealed unbtill the last player is done\n\n")       



def number_of_players(num):
    if num == 1:
        
        deal_cards_for_player_1(random_card_1, random_card_2)
        deal_cards_for_dealer(random_card_1, random_card_2)
        
        
    elif num == 2:
        deal_cards_for_player_1(random_card_1, random_card_2)
        deal_cards_for_player_2(random_card_1, random_card_2)
        deal_cards_for_dealer(random_card_1, random_card_2)


    
        


numberOfPlayers = int(input("How many players do want to play?: "))

number_of_players(numberOfPlayers)

print_list(list_of_cards)





















#print_list(list_of_cards) 
#deleting the random card choosen
#random_card = random.choice(list_of_cards)


#print(random_card)

#print()

#list_of_cards.remove(random_card)





#########################################################################
#del list_of_cards[random_card]                                         #
#                                                                        #
#if random_card == two_of_spades:                                       #
#    del list_of_cards[random_card]                                     #
#                                                                        #
#elif random_card == two_of_clubs:                                      #
#    del list_of_cards[random_card]                                     #
#########################################################################


#print_list(list_of_cards)
    


