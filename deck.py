import random as r
import time

class Deck:
    def __init__(self, hands):
        self.deck = self.createDeck()
        self.hands = self.defineHands(hands)

    def createDeck(self):
        deck = []
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        for i in suits:
            for u in range(13):
                deck.append([u+1,i])
        return deck

    def defineHands(self, num_hands):
        hands = []
        for hand in range(num_hands):
            hands.append([])
        return hands

    def shuffle(self):
        r.shuffle(self.deck)

    def draw(self, hand):
        hand.append(self.deck.pop())

    def convert(self, n):
        if n is 1:
            n = "Ace"
        elif n is 11:
            n = "Jack"
        elif n is 12:
            n = "Queen"
        elif n is 13:
            n = "King"
        else:
            n = str(n)

        return n

    def print_deck(self, hand):
        d = ""
        for x in hand:
            d += "\n"+convert(x[0])+" of "+x[1]
        return d

    def print_hand(self, hand):
        pCard = [self.card_string(card) for card in hand]
        for l in range(13):
            for i in pCard:
                print(i[l],end="")
            print()

    def card_string(self, card):
        con = dict(Hearts = '♥', Clubs = '♣', Spades = '♠', Diamonds = '♦')
        x = [[] for i in range(13)]
        x[0]= "┌───────────────┐"
        x[12]= "└───────────────┘"

        if card:
            if card[0] == 1:
                x[1] = "│A              │"
                x[11] = "│              A│"
            elif card[0] == 10:
                x[1] = "│10             │"
                x[11] = "│             10│"
            elif card[0] == 11:
                x[1] = "│J              │"
                x[2] = f"│{con[card[1]]}      ███▄    │"
                x[3] = "│      ▀████    │"
                x[9] = "│    ████▄      │"
                x[10] = f"│    ▀███      {con[card[1]]}│"
                x[11] = "│              J│"
            elif card[0] == 12:
                x[1] = "│Q              │"
                x[2] = f"│{con[card[1]]}      ▄███    │"
                x[3] = "│       ████    │"
                x[9] = "│    ████       │"
                x[10] = f"│    ███▀      {con[card[1]]}│"
                x[11] = "│              Q│"
            elif card[0] == 13:
                x[1] = "│K              │"
                x[2] = f"│{con[card[1]]}     ▐▄██▄▌   │"
                x[3] = "│       ████    │"
                x[9] = "│    ████       │"
                x[10] = f"│   ▐▀██▀▌     {con[card[1]]}│"
                x[11] = "│              K│"
            else:
                x[1] = f"│{card[0]}              │"
                x[11] = f"│              {card[0]}│"
            if card[0] > 10:
                x[4] = "│    ▄▄█████▄   │"
                x[5] = "│   █████████   │"
                x[6] = "│  ▐█████████▌  │"
                x[7] = "│   █████████   │"
                x[8] = "│   ▀█████▀▀    │"

            if card[0]<11:
                x[2] = f"│{con[card[1]]}              │"
                x[10] = f"│              {con[card[1]]}│"

                if card[0] > 7:
                    x[3] = f"│    {con[card[1]]}     {con[card[1]]}    │"
                    x[5] = f"│    {con[card[1]]}     {con[card[1]]}    │"
                    x[7] = f"│    {con[card[1]]}     {con[card[1]]}    │"
                    x[9] = f"│    {con[card[1]]}     {con[card[1]]}    │"

                if card[0] == 10 or card[0] == 2 or card[0] == 3:
                    x[4] = f"│       {con[card[1]]}       │"
                    x[8] = f"│       {con[card[1]]}       │"

                if card[0] == 9 or card[0] == 5 or card[0] == 1 or card[0] == 3:
                    x[6] = f"│       {con[card[1]]}       │"
                            
                if card[0] >= 4 and card[0] <= 7:
                    x[4] = f"│    {con[card[1]]}     {con[card[1]]}    │"
                    x[8] = f"│    {con[card[1]]}     {con[card[1]]}    │"
                    
                if card[0] == 6 or card[0] == 7:
                    x[6] = f"│    {con[card[1]]}     {con[card[1]]}    │"

                if card[0] == 7:
                    x[5] = f"│       {con[card[1]]}       │"

        for c in range(13):
            if not x[c]:
                x[c] = "│               │"

        return x



def min_sum(hand):
    sum = 0
    for x in hand:
        if x[0]>10:
            sum += 10
        else:
            sum += x[0]
    return sum

def max_sum(hand):
    sum = 0
    for x in hand:
        if x[0]>10:
            sum += 10
        elif x[0]==1:
            sum += 11
        else:
            sum += x[0]
    return sum

deck = Deck(2)
deck.shuffle()
player = deck.hands[0]
dealer = deck.hands[1]
for i in range(2):
    deck.draw(player)
    deck.draw(dealer)

done = False

while True:
    deck.print_hand([dealer[0], None])
    deck.print_hand(player)
    if min_sum(player) > 21:
        print("bust")
        done = True
        break
            
    x = input("\nHit or Stand: ")
    if x.lower() is "" or x.lower() is "hit":
        deck.draw(player)    
    else:
        break

deck.print_hand(dealer)
deck.print_hand(player)
while not done:
    time.sleep(2)
    if min_sum(dealer) < 17:
        deck.draw(dealer)
    else:
        break
    
    deck.print_hand(dealer)
    deck.print_hand(player)
    
    if min_sum(player) > 21:
        print("Dealer bust")
        break
