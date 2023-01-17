from deck import Deck
import time

def sum(hand):
    sum = 0
    ace = False
    for x in hand:
        val = x['val']
        ace = ace or (val == 1)
        if val>10:
            val = 10
        sum += val

    return sum, sum + 10*ace

def eval_hand(hand):
    shand = sum(hand)
    if shand[1] > 21:
        return shand[0]
    else:
        return shand[1]

deck = Deck(2)
deck.shuffle()
player = deck.hands[0]
dealer = deck.hands[1]
for i in range(2):
    deck.draw(player)
    deck.draw(dealer)

done = False

while True:
    print("-"*50)
    deck.print_hand([dealer[0], None])
    deck.print_hand(player)
    if sum(player)[0] > 21:
        print("you bust")
        done = True
        break
            
    x = input("\nHit or Stand: ")
    print("x is :",x)
    if x == "" or x.lower() == "h":
        deck.draw(player)    
    else:
        break

deck.print_hand(dealer, "D:", sum(dealer))
deck.print_hand(player, "P:", sum(player))

while not done and eval_hand(dealer) < 17:
    time.sleep(2)
    deck.draw(dealer)
    
    deck.print_hand(dealer, "D:", sum(dealer))
    deck.print_hand(player, "P:", sum(player))
    
    if sum(dealer)[0] > 21:
        print("Dealer bust")
        done = True

if not done:
    d_hand = eval_hand(dealer)
    p_hand = eval_hand(player)
    if p_hand > d_hand:
        print("You win")
    elif p_hand == d_hand:
        print("Draw")
    else:
        print("Dealer wins")