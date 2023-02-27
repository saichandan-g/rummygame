import pygame
import random

# Colors used in project
AQUA = (0,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
OLIVE = (128,128,0)
TEAL = (0,128,128)
WHITE = (255,255,255)


class MovedCard(object):
    """This class represents the cards that will move on the screen"""
    moved = False #This variable is True when there is a card moving on 
    # the screen.
    moved_card = [] #This variable will contain the name of the card.
    card_d = ()
    cards = None #This is object 
    def click_up(self,deck_list):
        """This is used when the user release the mouse button."""
        print("welcome to Class: MovedCard, click_up",len(self.moved_card))
        if len(self.moved_card) > 0:
            for item in deck_list:      
                if not isinstance(item,Deck_2):
                    if item.check_pos() and item.check_card(self.moved_card):
                        item.add_card(self.moved_card)
                        self.moved = False
                        self.moved_card = []
                        if isinstance(self.cards,Deck_1):
                            self.cards.show_card()
                        self.cards = None
                        break
            else:
                self.cards.add_card(self.moved_card)
                self.moved = False
                self.moved_card = []
                self.cards = None

    def draw(self,screen,card_dict):
        """This draw the moved cards onto the screen"""
        if self.moved:
            pos = pygame.mouse.get_pos()
            x = pos[0] - self.card_d[0]
            y = pos[1] - self.card_d[1]
            for item in self.moved_card:
                screen.blit(card_dict[item],[x,y])
                y += 32
    
class Deck(object):
    """This is a parent class"""
    def __init__(self,x,y):
        self.cards = []
        # self.hidden = []
        self.rect = pygame.Rect(x,y,71,96)

    def check_pos(self):
        """This check if the cursor is on the card"""
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.rect.left and pos[0] <= self.rect.right:
            if pos[1] >= self.rect.top and pos[1] <= self.rect.bottom:
                return True
            else:
                return False
        else:
            return False

class Deck_1(Deck):
    """This is a child class"""
    def __init__(self,x,y,player="man"):
        #call parent's constructor:
        Deck.__init__(self,x,y)
        self.y = y
        self.hidden = []
        self.hpos = []
        self.player = player

    def extend_list(self,lst):
        self.hidden.extend(lst)
        self.cards.append(self.hidden.pop())
        if len(self.hidden) > 0:
            for i in range(len(self.hidden)):
                self.rect.top += 32
                self.hpos.append(self.rect.top)
        
    def draw_card(self,screen,card_dict):
        """This will draw all the cards on the screen"""
        pygame.draw.rect(screen,BLACK,[self.rect.left,self.rect.top,71,96],2)
        i = self.y
        if len(self.hidden) > 0:
            for item in self.hidden:
                if(self.player == "man"):
                    screen.blit(card_dict[item],[self.rect.left,i])
                else:
                    pygame.draw.rect(screen,TEAL,[self.rect.left,i,71,96])
                    pygame.draw.rect(screen,BLACK,[self.rect.left,i,71,96],2)
                i += 32
        if len(self.cards) > 0:
            for item in self.cards:
                screen.blit(card_dict[item],[self.rect.left,i])
                i += 32
                
    def add_card(self,card):
        if len(self.cards) > 0 or len(self.hidden) > 0:
            for i in range(len(card)):
                self.rect.top += 32
        else:
            for i in range(len(card)):
                if i > 0:
                    self.rect.top += 32
        self.cards.extend(card)

    def onClick(self,card):
        """This is used when the user press the mouse button"""
        if len(self.cards) > 0:
            top = self.rect.top
            lst = []
            for i in range(len(self.cards)):
                if self.check_pos():
                    pos = pygame.mouse.get_pos()
                    lst.insert(0,self.cards.pop())
                    card.card_d = (pos[0] - self.rect.left,pos[1] -
                                   self.rect.top)
                    card.moved = True
                    card.cards = self
                    card.moved_card.extend(lst)
                    if len(self.cards) > 0 or len(self.hidden) > 0:
                        self.rect.top -= 32
                    break
                else:
                    lst.insert(0,self.cards.pop())
                    self.rect.top -= 32
            else:
                self.rect.top = top
                self.cards.extend(lst)

    def show_card(self):
        if len(self.cards) == 0 and len(self.hidden) > 0:
            self.cards.append(self.hidden.pop())

    def check_card(self,moved_card):
        card = moved_card[0]
        result = True #False
        return result


class Deck_2(Deck):
    def __init__(self,x,y):
        #call parent's constructor:
        Deck.__init__(self,x,y)
        self.hidden_cards = []
        self.cards_list = []
        self.x = x
    
    def onClick(self,card):
        """This is used when the user press the mouse button"""
        if self.check_pos() and len(self.cards) > 0:
            pos = pygame.mouse.get_pos()
            c = self.cards.pop()
            card.moved_card.append(c)
            self.cards_list.remove(c)
            card.card_d = (pos[0] - self.rect.left,pos[1] - self.rect.top)
            card.moved = True
            card.cards = self
            self.rect.left -= 20
        else:
            pos = pygame.mouse.get_pos()
            flag = False
            if pos[0] >= 500 and pos[0] <= 571:
                if pos[1] >= 400 and pos[1] <= 490:
                    flag = True
            if flag:
                self.rect.left = self.x
                if len(self.hidden_cards) > 0:
                    self.cards = []
                    for i in range(3):
                        c = self.hidden_cards.pop()
                        self.cards_list.insert(0,c)
                        self.cards.append(c)
                        if len(self.hidden_cards) == 0 and i < 2:
                            break
                        
                else:
                    self.hidden_cards.extend(self.cards_list)
                    self.cards_list = []
                    self.cards = []

                if len(self.cards) > 1:
                    for i in range(len(self.cards)):
                        if i > 0:
                            self.rect.left += 20

    def draw_card(self,screen,card_dict):
        """This will draw all the cards on the screen"""
        x = self.x
        if len(self.hidden_cards) > 0:
            pygame.draw.rect(screen,WHITE,[500,400,71,96]) ####################TEAL
            pygame.draw.rect(screen,(255,0,0),[500,400,71,96],2)#################BLACK
            if len(self.cards_list) > 0 and len(self.cards) > 0:
                for item in self.cards:
                    screen.blit(card_dict[item],[x,self.rect.top])
                    x += 20
        else:
            if len(self.cards_list) > 0 and len(self.cards) > 0:
                for item in self.cards:
                    screen.blit(card_dict[item],[x,self.rect.top])
                    x += 20
            pygame.draw.ellipse(screen,WHITE,[480,410,60,60],5)#####################changed OLIVE

    def add_card(self,card):
        self.cards.extend(card)
        self.cards_list.extend(card)
        self.rect.left += 20

class Deck_3(Deck):
    def check_card(self,moved_card):
        result = True #False
        return result

    def onClick(self,card):
        """This is used when the user press the mouse button"""
        if self.check_pos() and len(self.cards) > 0:
            pos = pygame.mouse.get_pos()
            card.moved_card.append(self.cards.pop())
            card.card_d = (pos[0] - self.rect.left,pos[1] - self.rect.top)
            card.moved = True
            card.cards = self

    def add_card(self,card):
        self.cards.extend(card)

    def draw_card(self,screen,card_dict):
        """This will draw all the cards on the screen"""
        pygame.draw.rect(screen,(0,255,0),[self.rect.left,self.rect.top,71,96],2)##############BLACK
        if len(self.cards) > 0:
            screen.blit(card_dict[self.cards[-1]],[self.rect.left,self.rect.top])

def shuffle_cards():
    """This shuffle the cards"""
    randomPickedCards = []
    my_list = ["ace_clubs","2_clubs","3_clubs","4_clubs","5_clubs","6_clubs",
           "7_clubs","8_clubs","9_clubs","10_clubs","jack_clubs","queen_clubs",
           "king_clubs","ace_spades","2_spades","3_spades","4_spades",
           "5_spades","6_spades","7_spades","8_spades","9_spades","10_spades",
           "jack_spades","queen_spades","king_spades","ace_hearts","2_hearts",
           "3_hearts","4_hearts","5_hearts","6_hearts","7_hearts","8_hearts",
           "9_hearts","10_hearts","jack_hearts","queen_hearts","king_hearts",
           "ace_diamonds","2_diamonds","3_diamonds","4_diamonds","5_diamonds",
           "6_diamonds","7_diamonds","8_diamonds","9_diamonds","10_diamonds",
           "jack_diamonds","queen_diamonds","king_diamonds"]

    length = len(my_list)
    for i in range(length):
        if len(my_list) > 1:
            c = random.choice(my_list)
            randomPickedCards.append(c)
            my_list.remove(c)
        else:
            c = my_list.pop()
            randomPickedCards.append(c)

    return randomPickedCards

