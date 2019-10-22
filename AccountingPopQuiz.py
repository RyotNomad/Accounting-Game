import pygame
import time
import os

pygame.init()

display_width = 800
display_eight = 600

gameDisplay = pygame.display.set_mode((display_width,display_eight))
pygame.display.set_caption("Accounting Pop Quiz")
clock = pygame.time.Clock()

balloon1 = pygame.image.load(os.path.join('Blue.png'))
balloon2 = pygame.image.load(os.path.join('Blue.png'))
balloon3 = pygame.image.load(os.path.join('Blue.png'))

question_prompts = [
    "Which of the following is a solvency ratio? \n(A) Acid Test\n(B) Return on equity\n(C) Percentage net profit\n\n" ,
    "An example of a zero rated VAT item?\n(A) Brown bread\n(B) Lease of personal property\n(C) Salaries & wages\n\n" ,
    "Maximum number of owners in a partnership?\n(A) 20\n(B) 30\n(C) unlimited\n\n",
    "When rent is outstanding at year end, debit rent expense and credit?\n(A) Prepaid expense\n(B) Accrued expense\n(C) Accrued income\n\n",
    "When interest is capatilised on a loan account, debit interst expense and credit?\n(A) Bank\n(B) Debtors control\n(C) Loan\n\n",
    "Stationery left over at year end is transferred to?\n(A) Consumable stores on hand\n(B) Stationery expense\n(C) Trading stock\n\n",
    "Amount that will not be recovered from a debtor is called?\n(A) Debtors outstanding\n(B) Debtors control\n(C) Bad debts\n\n",
    "Which accounting concept states that assets are valued at the price they are purchased?\n(A) Historical cost concept\n(B) Prudence\n(C) Business entity concept\n\n",
    "The source document for credit purchase is?\n(A) Original invoice\n(B) Duoplicate invoice\n(C) Receipt\n\n",
    "When goods are returned to a creditor you are issued with a?\n(A) Credit note\n(B) Debit note\n(C) Inovice\n(\n"
]
color  = (0,0,0)
red = (200,0,0,)
white = (255,255,255)
green = (0,200,0)
blue = (0,0,255)
bright_red = (255,0,0)
bright_green = (0,255,0)
pygame.font.init()
font = pygame.font.Font("Arial.ttf", 20)
font1 = pygame.font.Font("freesansbold.ttf", 20)
txt = font1.render("A", True, color)
txt2 = font1.render("B",True, color)
txt3 = font1.render("C",True,color)
size = font.size("LOLOp")

answrs = ["A","A","C","B","C","A","C","A","A","B"]
b1x = 50
b1y = 400
b2x = 300
b2y = 400
b3x = 550
b3y = 400
currq = 0
background = pygame.image.load(os.path.join('backg.jpg'))
background = pygame.transform.scale(background, (800, 600))
running = True
while running:
    if(currq>9):
        break
    if(b1y <= 200):
        break;
    gameDisplay.blit(background,(0,0))
    gameDisplay.blit(balloon1, (b1x,b1y))
    gameDisplay.blit(balloon1, (b2x,b2y))
    gameDisplay.blit(balloon1, (b3x,b3y))
    gameDisplay.blit(txt,(b1x+70,b1y+100))
    gameDisplay.blit(txt2,(b2x+70,b2y+100))
    gameDisplay.blit(txt3,(b3x+70,b3y+100))
    time.sleep(0.1)
    b1y -= 1
    b2y -= 1
    b3y -= 1
    question = question_prompts[currq].split("\n")
    text = font.render(question[0], True, white)
    textRect = text.get_rect()
    gameDisplay.blit(text,(0,0))
    text = font.render(question[1],True,white)
    gameDisplay.blit(text,(0,30))
    text = font.render(question[2],True,white)
    gameDisplay.blit(text,(0,60))
    text = font.render(question[3],True,white)
    gameDisplay.blit(text,(0,90))
    text = font1.render("Score =" + str(((currq + 1) * 10)), True, (0, 0, 0))
    gameDisplay.blit(text, (600, 140))
    pygame.draw.rect(gameDisplay, (0,0,0), (0,170,800,20))
    Picture2 = pygame.image.load(os.path.join('spikes.png'))
    Picture2 = pygame.transform.scale(Picture2, (200, 20))
    rect = Picture2.get_rect()
    rect = rect.move((200, 190))
    gameDisplay.blit(Picture2, rect)
    Picture3 = pygame.image.load(os.path.join('spikes.png'))
    Picture3 = pygame.transform.scale(Picture3, (200, 20))
    rect = Picture3.get_rect()
    rect = rect.move((400, 190))
    gameDisplay.blit(Picture3, rect)
    Picture4 = pygame.image.load(os.path.join('spikes.png'))
    Picture4 = pygame.transform.scale(Picture4, (200, 20))
    rect = Picture4.get_rect()
    rect = rect.move((600, 190))
    gameDisplay.blit(Picture4, rect)
    Picture1 = pygame.image.load(os.path.join('spikes.png'))
    Picture1 = pygame.transform.scale(Picture1, (200, 20))
    rect = Picture1.get_rect()
    rect = rect.move((0, 190))
    gameDisplay.blit(Picture1, rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            if b1x-60 < x < b1x +150:
                if b1y-600 < y < b1y+550:
                    if answrs[currq] == "A":
                        currq=currq+1
                        b1x = 50
                        b1y = 400
                        b2x = 300
                        b2y = 400
                        b3x = 550
                        b3y = 400
                        time.sleep(1)
                    else:
                        time.sleep(0.5)
                        running = False;
                #if(b2x - 160 < x or x < b2x)
            if b2x-60 < x < b2x +150:
                if b2y-600 < y < b2y+550:
                    if(answrs[currq] == "B"):
                        currq=currq+1
                        b1x = 50
                        b1y = 400
                        b2x = 300
                        b2y = 400
                        b3x = 550
                        b3y = 400
                        time.sleep(1)

                    else:
                        time.sleep(0.5)
                        running = False
            if b3x-50 < x < b3x +150:
                if b3y-600 < y < b3y+550:
                    if(answrs[currq] == "C"):
                        currq=currq+1
                        b1x = 50
                        b1y = 400
                        b2x = 300
                        b2y = 400
                        b3x = 550
                        b3y = 400
                        time.sleep(1)

                    else:
                        time.sleep(0.5)
                        running = False;


if(currq >= 9):
    background1 = pygame.image.load(os.path.join('Winner.png'))
    background1 = pygame.transform.scale(background1, (800, 600))
    gameDisplay.blit(background1, (0, 0))
    text = font1.render("Your score is :" + str(((currq + 1) * 10)), True, (0, 0, 0))
    gameDisplay.blit(text, (260, 100))
else:
    background2 = pygame.image.load(os.path.join('lose.png'))
    background2 = pygame.transform.scale(background2, (800, 600))
    gameDisplay.blit(background2, (0, 0))
    text = font1.render("YOU HAVE LOST", True, red)
    gameDisplay.blit(text, (250, 500))
    text = font1.render("SCORE:" + str(((currq + 1) * 10)) , True, red)
    gameDisplay.blit(text, (300, 550))

pygame.display.flip()
time.sleep(5)
