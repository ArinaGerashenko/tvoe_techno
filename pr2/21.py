from random import shuffle
class Hand:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":
                aces += 1
    
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

    def __str__(self):
        text = "%s 's contains:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value())
        return text

class Deck:
    def __init__(self):  
        import random
        ranks = "23456789TJQKA"
        suits = "КПЧБ"
        self.cards = [Card(r, s) for r in ranks for s in suits] 
        random.shuffle(self.cards)  

    def deal_card(self):
        return self.cards.pop()

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def card_value(self):

        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)



def new_game():
    d = Deck()
    player_hand = Hand("Player")
    dealer_hand = Hand("Dealer")
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("=" * 20)
    print(player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        ans = input('Брать ещё ? (y/n) ')
        if ans == "n":
            print("Вы выбрали стоп!")
            break
        else:
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Вы проиграли!")
                ans = input('Будете играть ещё ?(y/n) ')
                if ans == "n":
                    print("Всего доброго!!")
                    exit(0)
                else:
                    new_game()
                in_game = False
    print("=" * 20)
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("Раздающий проиграл")
                ans = input('Будете играть ещё ?(y/n) ')
                if ans == "n":
                    print("Всего доброго!!")
                    exit(0)
                else:
                    new_game()
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("Вы выиграли!")
            ans = input('Будете играть ещё ?(y/n) ')
            if ans == "n":
                print("Всего доброго!!")
                exit(0)
            else:
                new_game()
        else:
            print("Раздающий выиграл!")
            ans = input('Будете играть ещё ?(y/n) ')
            if ans == "n":
                print("Всего доброго!")
                exit(0)
            else:
                new_game()


new_game()
