#!/usr/bin/env python
import pygame
import random
import time
from classes import *

# Colors used in project
AQUA = (0,255,255)
BLACK = (0,0,0)
GREEN = (0,128,0)
OLIVE = (128,128,0)
TEAL = (0,128,128)
WHITE = (255,255,255)
#-----------------------
def scoreCalculator(p):
    total_score = 0
    for i in p:
        if "10_" in i:
            total_score = total_score + 10
        if "9_" in i:
            total_score = total_score + 9
        if "8_" in i:
            total_score = total_score + 8
        if "7_" in i:
            total_score = total_score + 7
        if "6_" in i:
            total_score = total_score + 6
        if "5_" in i:
            total_score = total_score + 5
        if "4_" in i:
            total_score = total_score + 4
        if "3_" in i:
            total_score = total_score + 3
        if "2_" in i:
            total_score = total_score + 2
        if "1_" in i:
            total_score = total_score + 1
        if "jack_" in i:
            total_score = total_score + 10
        if "king_" in i:
            total_score = total_score + 10
        if "queen_" in i:
            total_score = total_score + 10
    if(total_score > 80):
        total_score = 80
    return total_score
            


def main():
    print("Game is running")
    pygame.init()

    # Set the width and height of the screen [width, height]
    
    screen = pygame.display.set_mode([1260,800])

    pygame.display.set_caption("Playing cards")

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    #-------------------------------------------
    card_dict = {} #This dictionary holds the images of the cards
    img = pygame.image.load("Images/ace_clubs.png").convert()
    card_dict["ace_clubs"] = img
    img = pygame.image.load("Images/2_clubs.png").convert()
    card_dict["2_clubs"] = img
    img = pygame.image.load("Images/3_clubs.png").convert()
    card_dict["3_clubs"] = img
    img = pygame.image.load("Images/4_clubs.png").convert()
    card_dict["4_clubs"] = img
    img = pygame.image.load("Images/5_clubs.png").convert()
    card_dict["5_clubs"] = img
    img = pygame.image.load("Images/6_clubs.png").convert()
    card_dict["6_clubs"] = img
    img = pygame.image.load("Images/7_clubs.png").convert()
    card_dict["7_clubs"] = img
    img = pygame.image.load("Images/8_clubs.png").convert()
    card_dict["8_clubs"] = img
    img = pygame.image.load("Images/9_clubs.png").convert()
    card_dict["9_clubs"] = img
    img = pygame.image.load("Images/10_clubs.png").convert()
    card_dict["10_clubs"] = img
    img = pygame.image.load("Images/jack_clubs.png").convert()
    card_dict["jack_clubs"] = img
    img = pygame.image.load("Images/queen_clubs.png").convert()
    card_dict["queen_clubs"] = img
    img = pygame.image.load("Images/king_clubs.png").convert()
    card_dict["king_clubs"] = img
    img = pygame.image.load("Images/ace_spades.png").convert()
    card_dict["ace_spades"] = img
    img = pygame.image.load("Images/2_spades.png").convert()
    card_dict["2_spades"] = img
    img = pygame.image.load("Images/3_spades.png").convert()
    card_dict["3_spades"] = img
    img = pygame.image.load("Images/4_spades.png").convert()
    card_dict["4_spades"] = img
    img = pygame.image.load("Images/5_spades.png").convert()
    card_dict["5_spades"] = img
    img = pygame.image.load("Images/6_spades.png").convert()
    card_dict["6_spades"] = img
    img = pygame.image.load("Images/7_spades.png").convert()
    card_dict["7_spades"] = img
    img = pygame.image.load("Images/8_spades.png").convert()
    card_dict["8_spades"] = img
    img = pygame.image.load("Images/9_spades.png").convert()
    card_dict["9_spades"] = img
    img = pygame.image.load("Images/10_spades.png").convert()
    card_dict["10_spades"] = img
    img = pygame.image.load("Images/jack_spades.png").convert()
    card_dict["jack_spades"] = img
    img = pygame.image.load("Images/queen_spades.png").convert()
    card_dict["queen_spades"] = img
    img = pygame.image.load("Images/king_spades.png").convert()
    card_dict["king_spades"] = img
    img = pygame.image.load("Images/ace_hearts.png").convert()
    card_dict["ace_hearts"] = img
    img = pygame.image.load("Images/2_hearts.png").convert()
    card_dict["2_hearts"] = img
    img = pygame.image.load("Images/3_hearts.png").convert()
    card_dict["3_hearts"] = img
    img = pygame.image.load("Images/4_hearts.png").convert()
    card_dict["4_hearts"] = img
    img = pygame.image.load("Images/5_hearts.png").convert()
    card_dict["5_hearts"] = img
    img = pygame.image.load("Images/6_hearts.png").convert()
    card_dict["6_hearts"] = img
    img = pygame.image.load("Images/7_hearts.png").convert()
    card_dict["7_hearts"] = img
    img = pygame.image.load("Images/8_hearts.png").convert()
    card_dict["8_hearts"] = img
    img = pygame.image.load("Images/9_hearts.png").convert()
    card_dict["9_hearts"] = img
    img = pygame.image.load("Images/10_hearts.png").convert()
    card_dict["10_hearts"] = img
    img = pygame.image.load("Images/jack_hearts.png").convert()
    card_dict["jack_hearts"] = img
    img = pygame.image.load("Images/queen_hearts.png").convert()
    card_dict["queen_hearts"] = img
    img = pygame.image.load("Images/king_hearts.png").convert()
    card_dict["king_hearts"] = img
    img = pygame.image.load("Images/ace_diamonds.png").convert()
    card_dict["ace_diamonds"] = img
    img = pygame.image.load("Images/2_diamonds.png").convert()
    card_dict["2_diamonds"] = img
    img = pygame.image.load("Images/3_diamonds.png").convert()
    card_dict["3_diamonds"] = img
    img = pygame.image.load("Images/4_diamonds.png").convert()
    card_dict["4_diamonds"] = img
    img = pygame.image.load("Images/5_diamonds.png").convert()
    card_dict["5_diamonds"] = img
    img = pygame.image.load("Images/6_diamonds.png").convert()
    card_dict["6_diamonds"] = img
    img = pygame.image.load("Images/7_diamonds.png").convert()
    card_dict["7_diamonds"] = img
    img = pygame.image.load("Images/8_diamonds.png").convert()
    card_dict["8_diamonds"] = img
    img = pygame.image.load("Images/9_diamonds.png").convert()
    card_dict["9_diamonds"] = img
    img = pygame.image.load("Images/10_diamonds.png").convert()
    card_dict["10_diamonds"] = img
    img = pygame.image.load("Images/jack_diamonds.png").convert()
    card_dict["jack_diamonds"] = img
    img = pygame.image.load("Images/queen_diamonds.png").convert()
    card_dict["queen_diamonds"] = img
    img = pygame.image.load("Images/king_diamonds.png").convert()
    card_dict["king_diamonds"] = img
    #This variable below will hold all the names of the cards.
    card_list = shuffle_cards()
    #The list below will hold all the deck-objects.
    deck_list = [Deck_2(550,400),Deck_1(30,120),Deck_1(1079,120,"comp"),
                 Deck_3(500,250),Deck_3(500,250),Deck_3(10,10),Deck_3(81,10),Deck_3(152,10),
                 Deck_3(223,10),Deck_3(294,10),Deck_3(365,10),Deck_3(436,10),Deck_3(507,10)
                 ,Deck_3(578,10),Deck_3(649,10),Deck_3(720,10),Deck_3(791,10),Deck_3(862,10),
                 Deck_3(294,610),Deck_3(365,610),Deck_3(436,610),Deck_3(507,610),Deck_3(578,610),Deck_3(649,610)
                 ,Deck_3(720,610),Deck_3(791,610),Deck_3(862,610)
                 ,Deck_3(933,610),Deck_3(1004,610),Deck_3(1075,610),Deck_3(1146,610)]
    movedcard = MovedCard()
    deck_list[1].extend_list(card_list[:13])
    del card_list[:13]
    deck_list[2].extend_list(card_list[:13])
    del card_list[:13]
    
    deck_list[0].hidden_cards.extend(card_list)
    game_over = False
    font = pygame.font.Font(None,25)
    winner = ""
    runner = ""
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos[0],pos[1])
                for item in deck_list:
                    item.onClick(movedcard)
                if(pos[0]>=138 and pos[1]>=324 and pos[0]<= 238 and pos[1]<= 374):
                    winner = 'p1'
                    runner = 'p2'
                    game_over = True
                if(pos[0]>=905 and pos[1]>=304 and pos[0]<=1005 and pos[1]<= 354):
                    winner = 'p2'
                    runner = 'p1'
                    game_over = True


            if event.type == pygame.MOUSEBUTTONUP:
                movedcard.click_up(deck_list)

        # Frame making starts here 1) fill background with green.
        screen.fill((GREEN))

        # --- Drawing code should go here
        for item in deck_list:
            item.draw_card(screen,card_dict)
        movedcard.draw(screen,card_dict)
        if game_over:
            try:
                p1_cards = []
                p2_cards = []
                for i in range(5,18):
                    p1_cards.append(deck_list[i].cards[0])
                    p2_cards.append(deck_list[i+13].cards[0])
                # print("p1 = ",p1_cards)
                # print("p2 = ",p2_cards)

                if winner == 'p1':
                    p2score = scoreCalculator(p2_cards)
                    notify = "Winner : P1 Score : "+str(p2score+20)
                    notify2= "Runner : P2 Score : "+str(p2score) 
                    text = font.render(notify,True,BLACK)
                    text2 = font.render(notify2,True,BLACK)
                
                if winner == 'p2' :
                    p1score = scoreCalculator(p1_cards)
                    notify = "Winner : P2 Score : "+str(p1score+20)
                    notify2= "Runner : P1 Score : "+str(p1score) 
                    text = font.render(notify,True,BLACK)
                    text2 = font.render(notify2,True,BLACK)
            except :
                noti = "not complete"
                noti2 = "Restart game"
                text = font.render(noti,True,BLACK)
                text2 = font.render(noti2,True,BLACK)
                

            pygame.draw.rect(screen,AQUA,[245,246,250,100])
            screen.blit(text,[250,250])
            screen.blit(text2,[250,300])

        pygame.draw.rect(screen, (0,0,0),(138,324, 100, 50))
        screen.blit(font.render('DONE-P1', True, (255,255,255)), (140,326)) 
        pygame.draw.rect(screen, (0,0,0),(905,304, 100, 50))
        screen.blit(font.render('DONE-P2', True, (255,255,255)), (910,306)) 
         # Go ahead and update the screen with what we've drawn.
        openDeck = font.render("Open Deck",True,WHITE)
        screen.blit(openDeck,[586,299])
        openDeck = font.render("Player1 Slot",True,WHITE)
        screen.blit(openDeck,[439,123])
        openDeck = font.render("Player2 Slot",True,WHITE)
        screen.blit(openDeck,[670,589])
        pygame.display.flip()
        


        # --- Limit to 20 frames per second
       
        clock.tick(20)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()

if __name__ == '__main__':
    main()
    print("Successfully exited")
