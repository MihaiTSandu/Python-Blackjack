import random

class Dealer():
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aceBalance = 0
        
    def add_card(self, card):
        self.cards.append(card)
        
        if card.rank == 'Ace':
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += 11
                self.aceBalance += 1
        else:
            self.value += card.value
        
        if self.value >= 21 and self.aceBalance >= 1:
            self.aceBalance -= 1
            self.value -= 10

class Player():
    
    def __init__(self, chips):
        self.chips = chips
        self.value = 0
        self.cards = []
        self.aceBalance = 0
        
    def add_card(self, card):
        self.cards.append(card)
        
        if card.rank == 'Ace':
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += 11
                self.aceBalance += 1
        else:
            self.value += card.value
        
        if self.value >= 21 and self.aceBalance >= 1:
            self.aceBalance -= 1
            self.value -= 10

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
# The value of the Ace is defined in the Hand class
# There was a problem with the value of the Ace (solved?)!!!


        if self.rank == 'Two':
            self.value = 2
        elif self.rank == 'Three':
            self.value = 3
        elif self.rank == 'Four':
            self.value = 4
        elif self.rank == 'Five':
            self.value = 5
        elif self.rank == 'Six':
            self.value = 6
        elif self.rank == 'Seven':
            self.value = 7
        elif self.rank == 'Eight':
            self.value = 8
        elif self.rank == 'Nine':
            self.value = 9
        elif self.rank == 'Ten' or self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
            self.value = 10           
# The value of the Ace is defined in the Hand class                    
            
    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck():
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.cards = []
        for suit in self.suits:
            for rank in self.ranks:
                self.cards.append(Card(suit, rank))
                
    def __repr__(self):
        return str(self.cards)
    
    
    def shuffle(self):
        random.shuffle(self.cards)
        
    def add_card(self):
        self.cards.append(Card('Hearts', 'Ace'))

def take_bet(player):
    
    try:
        bet = int(input("Enter an amount for bet: "))
        if player.chips < bet:
            print ("Not enough credits. Enter a lower amount")
            take_bet(player)
        else:
            player.chips -= bet
            return bet
    except:
        print ("Please enter a number!")
        take_bet(player)

def hit(deck, hand):
    hand.add_card(deck.cards[0])
    deck.cards.pop(0)

def hit_or_stand(deck, player):
    choice = input("Do you want to hit again? (Y/N)")
    if choice.upper() == "Y":
        hit(deck, player)
        return True
    elif choice.upper() == "N":
        pass
    else:
        print("Please enter 'N' or 'Y'!")
        hit_or_stand(deck, player)

def show_player(player):
    print("   ")
    print("THE PLAYER'S CARDS:")
    for x in player.cards:
        print (x)
           
def show_dealer(dealer):
    print("   ")
    print("THE DEALER'S CARDS:")
    print ("**Card Hidden**")
    for x in range(1,len(dealer.cards)):
        print(dealer.cards[x])
        
def show_dealer_final(player):
    print("   ")
    print("THE DEALER'S CARDS:")
    for x in player.cards:
        print (x)

def game():
    print ("This is a game of BlackJack.")
    mydealer = Dealer()
    myplayer = Player(1000)
    
    def prepare():
        
        def ask():
            print(f"Your current credit is: {myplayer.chips}")
            choice = input("Do you want to play again? (Y/N)")
            if choice.upper() == "Y":
                prepare()
            elif choice.upper() == "N":
                pass
            else:
                print("Please enter 'N' or 'Y'!")
                ask()

        def start_game():
            if myplayer.value < 21:
                if hit_or_stand(mydeck,myplayer):
                    show_player(myplayer)
                    print(f"The total player value is: {myplayer.value}")    
                    start_game()
            if myplayer.value > 21:
                return 0

        def check_dealer():
            if myplayer.value > 21:
                pass
                
            elif mydealer.value < 17:
                hit(mydeck, mydealer)
                show_dealer(mydealer)
                check_dealer()
        
        def results():
            
            if myplayer.value > 21:
                print("Player Busted. Dealer wins!")
            elif mydealer.value > 21:
                print ("Dealer Busted. The Player wins!")
                myplayer.chips += 2 * bet  
                
            elif myplayer.value > mydealer.value:
                print ("Player won!")
                myplayer.chips += 2*bet
            
            elif myplayer.value == mydealer.value:
                print ("Draw!")
                myplayer.chips += bet
            
            elif myplayer.value < mydealer.value:
                print("Player Lost!")         
            ask()
            
        myplayer.cards = []
        myplayer.value = 0
        mydealer.cards = []
        mydealer.value = 0        
        mydeck = Deck()
        mydeck.shuffle()
        bet = take_bet(myplayer)

        hit(mydeck, myplayer)
        hit(mydeck, mydealer)

        show_player(myplayer)
        show_dealer(mydealer)
            
        start_game()
        check_dealer()
        print(f"The total dealer value is: {mydealer.value}")
        show_dealer_final(mydealer)
        results()
    prepare()

game()