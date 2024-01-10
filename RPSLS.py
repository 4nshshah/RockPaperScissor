# rock paper scissor lizard spock
import math, time, random, pygame, sys, pygame.freetype

rock = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/rock.png')
paper = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/paper.png')
scissor = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/scissor.png')
lizard = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/lizard.png')
spock = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/spock.png')
computer = pygame.image.load('D:/Python Programs/rock paper scissor lizard s/icons8-computer-64.png')


players = ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']

rockPos = [390,175]
paperPos = [490,175]
scissorPos = [590,175]
lizardPos = [690,175]
spockPos =[790,175]


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

clock = pygame.time.Clock()   


pygame.init()

#screen
screen = pygame.display.set_mode([1280, 720])
running = True

#title and window
pygame.display.set_caption('Rock Paper Scissor Lizard Spock')
iconPosX = {'rock': 390, 'paper': 490, 'scissor':590, 'lizard': 690, 'spock': 790}
imageMap = {'rock': rock, 'paper': paper, 'scissor':scissor, 'lizard': lizard, 'spock': spock}
#images
GAME_FONT = pygame.freetype.Font("C:/Users/Admin/Downloads/BebasNeue-Regular.ttf", 60)
credit = pygame.freetype.Font("C:/Users/Admin/Downloads/BebasNeue-Regular.ttf", 35)
credit2 = pygame.freetype.Font("C:/Users/Admin/Downloads/BebasNeue-Regular.ttf", 15)
titleText = 'ROCK PAPER SCISSOR LIZARD SPOCK'
temp1 =0
#running loop
playerScore = computerScore = 0
i23 = 0
i34 = 0
while running:
    screen.fill((193, 191, 181))
    layIcon(screen, iconPosX, imageMap)
    showScore(playerScore, computerScore, screen, rockPos)
    key = 'shit'
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    win= tie = False
    GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
    
    credit.render_to(screen, (1050, 650), "made by ansh", (0,0,0))
    
    
    credit2.render_to(screen, (1050, 680), "icons:Flaticon.com", (0,0,0))
    
    screen.blit(computer, (580,550))
    pygame.display.update()
    move1, key = getClick()
    move2 = random.choice(players)
    compMove = getMoveKey(move2.lower(), imageMap)
    if pygame.mouse.get_pressed()[0] == 1:
        if move1 != '':
            moveIconX(iconPosX[move1.lower()], scissorPos[0], screen, titleText, key)

            if key == scissor:
                    screen.fill((193, 191, 181))
                    GAME_FONT.render_to(screen, (300, 75), titleText, (0, 0, 0))
                    screen.blit(scissor, scissorPos)
                    
                    screen.blit(computer, (580,550))
                    pygame.display.update()
            win, tie = evaluate(move1, move2)
            pygame.display.update()
            moveIconsY(scissorPos[1], scissorPos[1] + 100, scissorPos[0], screen, titleText,key, compMove, scissorPos)
            pygame.time.wait(50)
            if win:
                vibrateIcon(compMove, key, screen, (scissorPos[0], 450),(scissorPos[0], scissorPos[1] + 100))
                GAME_FONT.render_to(screen, (535, 375), "YOU WON", (0,0,0))
                pygame.display.update()
                pygame.time.wait(500)
                playerScore += 1
                
            if tie:
                GAME_FONT.render_to(screen, (535, 375), "ITS A TIE", (0,0,0))
                pygame.display.update()
                pygame.time.wait(500)
            
            if (not win) and (not tie):
                vibrateIcon(key, compMove, screen, (scissorPos[0], scissorPos[1] + 100), (scissorPos[0], 450))
                GAME_FONT.render_to(screen, (535, 375), "YOU LOST", (0,0,0))
                
                pygame.display.update()
                pygame.time.wait(500)
                computerScore += 1
            pygame.time.wait(150)
            moveIconsY(scissorPos[1] + 100, scissorPos[1], scissorPos[0], screen, titleText,key, compMove, scissorPos[0])
            moveIconX(scissorPos[0], iconPosX[move1.lower()], screen, titleText, key)
                
            

        clock.tick(60)
        pygame.display.update()
    


