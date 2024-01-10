import math, time, random, pygame, sys, pygame.freetype
from RPSLS import rock, paper, scissor, lizard, spock
def evaluate(move1, move2):
    """evaluates the moves played and returns who won""" 
    rockStrength = ['Scissor', 'Lizard']#These are the strengths and weaknesses of each move
    paperStrength = ['Rock', 'Spock']
    scissorStrength = ['Paper', 'Lizard']
    lizardStrength = ['Spock', 'Paper']
    spockStrength = ['Rock', 'Scissor']
    key = False
    key2 = ''
    if not move1 == move2:
        if move1 == 'Rock':
            if move2 in rockStrength:
                key = True

        elif move1 == 'Scissor':
            if move2 in scissorStrength:
                key = True

        elif move1 == 'Paper':
            if move2 in paperStrength:
                key = True

        elif move1 == 'Lizard':
            if move2 in lizardStrength:
                key = True

        elif move1 == 'Spock':
            if move2 in spockStrength:
                key = True
    else:
        key2 = 'tie'
        time.sleep(0.7)
    return key, key2


def getMoves(checker):
    """inputs the moves of players and returns both of them"""
    temporary = True
    global multiplayer
    while 1:
        if checker and temporary:
            print("Press 1 to play against the computer...\nPress 2 to play against an opponent locally...")
            key = input()
            if key == '1':
                move0 = random.choice(players)
                break
            elif key == '2':
                multiplayer = True
                temporary = False
                continue
                
        elif not checker and not temporary:
            if multiplayer:
                print("Player 1 play your move.")
                move0 = input().lower().capitalize()
                break
            else:
                move0 = random.choice(players)
                break
        break

    print("Player 2 play your move.")
    move2 = input().lower().capitalize()
    

    return move0, move2


def getClick():
    global rock, paper, scissor, lizard, spock
    identify = ''
    click = pygame.mouse.get_pressed()
    move = ''
    time.sleep(0.07)
    r = 390
    y = 175
    if click[0] == 1:
        mousePos = pygame.mouse.get_pos()
        if r + 64 > mousePos[0]>r and y + 64 > mousePos[1] > y:
            move = 'rock'
            identify = rock
        elif r + 100 + 64 > mousePos[0]>r + 100 and y + 64>mousePos[1]>y:
            move = 'paper'
            identify =  paper
        elif r + 200 + 64> mousePos[0]>r+200 and y+64> mousePos[1]>y:
            move = 'scissor'
            identify =  scissor
        elif r+300 + 64> mousePos[0]>r+300 and y+64>mousePos[1]>y:
            move = 'lizard'
            identify =  lizard
        elif r + 400  + 64> mousePos[0]>r+400 and y+64>mousePos[1]>y:
            move = 'spock'
            identify =  spock
        
    return move.capitalize(), identify


def layIcon(window, iconMap, positionMap):
    global rock, paper, scissor, lizard, spock
    for i in iconMap:
        window.blit(positionMap[i], (iconMap[i], 175))

    
def moveIconX(x, finalx, screen , titleText, key ):
    if x < finalx: 
        for i in range(x, finalx):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            j = i
            screen.blit(key, (j, 175))
            
            screen.blit(computer, (580,550))
            pygame.display.update()
    elif x > finalx:
        for i in range(x, finalx-1, -1):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            j = i
            screen.blit(key, (j, 175))
            
            screen.blit(computer, (580,550))
            pygame.display.update()


def moveIconsY(y, finaly, x, screen, titleText, key1, key2, centerPosition):
    if y < finaly: 
        for i in range(y, finaly):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            j = i
            screen.blit(key1, (x, j))
            screen.blit(key2, (centerPosition[0], -j + 465 + finaly))
            
            screen.blit(computer, (580,550))
            pygame.display.update()
    elif y > finaly:
        for i in range(y, finaly-1, -1):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            j = i
            screen.blit(key1, (x, j))
            screen.blit(key2, (x, -j - 465 + finaly))
            
            screen.blit(computer, (580,550))
            pygame.display.update()


def showScore(player, computer, window, referencePos):
    medFault = pygame.freetype.Font("C:/Users/Admin/Downloads/BebasNeue-Regular.ttf", 42)
    medFault.render_to(window, (referencePos[0] + 75, referencePos[1] + 150), 'you', (0,0,0))
    medFault.render_to(window, (referencePos[0] + 90, referencePos[1] + 200), str(player), (0,0,0))
    medFault.render_to(window, (referencePos[0] + 300, referencePos[1] + 150), 'computer', (0,0,0))
    medFault.render_to(window, (referencePos[0] + 355, referencePos[1] + 200), str(computer), (0,0,0))


def vibrateIcon(key, key2, window, referencePos, secondPos):
    
    for j in range(10,25, 5):
        for i in range(j):
            x = referencePos[0]
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            screen.blit(computer, (580,550))
            window.blit(key2, secondPos)
            window.blit(key, (referencePos[0] + i, referencePos[1]))
            pygame.display.update()
        x += j 
        for i in range(j+j):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            screen.blit(computer, (580,550))
            window.blit(key2, secondPos)
            window.blit(key, (x-i, referencePos[1]))
            pygame.display.update()
        x -= (j+j)
        for i in range(j+j):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            screen.blit(computer, (580,550))
            window.blit(key2, secondPos)
            window.blit(key, (x+i, referencePos[1]))
            pygame.display.update()
        x += (j+j)
        for i in range(j):
            screen.fill((193, 191, 181))
            GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
            screen.blit(computer, (580,550))
            window.blit(key2, secondPos)
            window.blit(key, (x-i, referencePos[1]))
            pygame.display.update()


def getMoveKey(move, iconMap):
    return iconMap[move]
