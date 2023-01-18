import random as r

class Deck:
    def __init__(self, hands):
        self.deck = self.createDeck()
        self.hands = self.defineHands(hands)

    def createDeck(self):
        deck = []
        suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        for i in suits:
            for u in range(13):
                deck.append({'val':u+1, 'suit':i})
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
    
    def draw_n(self, hand, n):
        for i in range(n):
            self.draw(hand)

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
            d += "\n"+self.convert(x['val'])+" of "+x['suit']
        return d

    def print_hand(self, hand, *args):
        pCard = [self.card_string(card, args) for card in hand]
        for l in range(13):
            for i in pCard:
                print(i[l],end="")
            print()
        if args:
            print(args)

    def card_string(self, card, args):
        con = dict(Hearts = '♥', Clubs = '♣', Spades = '♠', Diamonds = '♦')
        x = [[] for i in range(13)]
        x[0]= "┌───────────────┐"
        x[12]= "└───────────────┘"

        if card:
            if card['val'] == 1:
                x[1] = "│A              │"
                x[11] = "│              A│"
            elif card['val'] == 10:
                x[1] = "│10             │"
                x[11] = "│             10│"
            elif card['val'] == 11:
                x[1] = "│J              │"
                x[2] = f"│{con[card['suit']]}      ███▄    │"
                x[3] = "│      ▀████    │"
                x[9] = "│    ████▄      │"
                x[10] = f"│    ▀███      {con[card['suit']]}│"
                x[11] = "│              J│"
            elif card['val'] == 12:
                x[1] = "│Q              │"
                x[2] = f"│{con[card['suit']]}      ▄███    │"
                x[3] = "│       ████    │"
                x[9] = "│    ████       │"
                x[10] = f"│    ███▀      {con[card['suit']]}│"
                x[11] = "│              Q│"
            elif card['val'] == 13:
                x[1] = "│K              │"
                x[2] = f"│{con[card['suit']]}     ▐▄██▄▌   │"
                x[3] = "│       ████    │"
                x[9] = "│    ████       │"
                x[10] = f"│   ▐▀██▀▌     {con[card['suit']]}│"
                x[11] = "│              K│"
            else:
                x[1] = f"│{card['val']}              │"
                x[11] = f"│              {card['val']}│"
            if card['val'] > 10:
                x[4] = "│    ▄▄█████▄   │"
                x[5] = "│   █████████   │"
                x[6] = "│  ▐█████████▌  │"
                x[7] = "│   █████████   │"
                x[8] = "│   ▀█████▀▀    │"

            if card['val']<11:
                x[2] = f"│{con[card['suit']]}              │"
                x[10] = f"│              {con[card['suit']]}│"

                if card['val'] > 7:
                    x[3] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"
                    x[5] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"
                    x[7] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"
                    x[9] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"

                if card['val'] == 10 or card['val'] == 2 or card['val'] == 3:
                    x[4] = f"│       {con[card['suit']]}       │"
                    x[8] = f"│       {con[card['suit']]}       │"

                if card['val'] == 9 or card['val'] == 5 or card['val'] == 1 or card['val'] == 3:
                    x[6] = f"│       {con[card['suit']]}       │"
                            
                if card['val'] >= 4 and card['val'] <= 7:
                    x[4] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"
                    x[8] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"
                    
                if card['val'] == 6 or card['val'] == 7:
                    x[6] = f"│    {con[card['suit']]}     {con[card['suit']]}    │"

                if card['val'] == 7:
                    x[5] = f"│       {con[card['suit']]}       │"

        for c in range(13):
            if not x[c]:
                x[c] = "│               │"

        return x



