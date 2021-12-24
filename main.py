import card
import deck
import player

# game setup
player_one = player.Player("One")
player_two = player.Player("Two")
new_deck = deck.Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round = 0

while game_on:
    round += 1

    if len(player_one.all_cards) == 0:
        print("Player one is out of cards, player two won!")
        print(f"Currently on round1 {round}")
        game_on = False
        break
    elif len(player_two.all_cards) == 0:
        print("Player two is out of cards, player one won!")
        print(f"Currently on round2 {round}")
        game_on = False
        break

    # player's cards on the table:

    player_one_cards = [player_one.remove_one()]
    player_two_cards = [player_two.remove_one()]

    # while at_war:

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            print(f"Currently on round3 {round}")
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            print(f"Currently on round4 {round}")
            at_war = False

        else:
            print("WAR!")
            if len(player_one.all_cards) < 3:
                print("player one is unable to declare war!\nPlayer two wins!")
                print(f"Currently on round5 {round}")
                game_on = False
                break
            elif len(player_two.all_cards) < 3:
                print("player two is unable to declare war!\nPlayer one wins!")
                print(f"Currently on round6 {round}")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
