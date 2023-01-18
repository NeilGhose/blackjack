from deck import Deck

def matches(vals):
    score = 0
    straight = True
    for i in range(len(vals) - 1):
        straight = straight and (vals[i]+1 == vals[i+1])
        if not straight:
            score += (vals[i] == vals[i+1])
            if i<3:
                score += (vals[i] == vals[i+2])
            if i < 2:
                score += (vals[i] == vals[i+3])
    return score, straight


def eval_hand(hand):
    flush = True
    suit = hand[0]['suit']
    vals = [hand[0]['val'] + (hand[0]['val']==1) * 13]
    for card in hand[1:]:
        flush = flush and (card['suit'] == suit)
        vals.append(card['val'] + (card['val']==1) * 13)
    vals.sort()
    
    print(matches(vals))

        
deck = Deck(1)
player  = deck.hands[0]

deck.shuffle()

deck.draw_n(player, 5)

deck.print_hand(player)

eval_hand(player)