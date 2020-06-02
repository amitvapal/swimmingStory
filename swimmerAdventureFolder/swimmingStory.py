"""
Amitva Pal
6/7 
#Assignment: Pygame Emoji Adventure Story Program 
#Description: Swimming adventure story
#Credits: Luke Szfranski, Mrs. Klosky for starter template code.
#Note: all images must be saved to same directory as this python file.
"""


import pygame, sys, math,random

#Initializing game engine
pygame.init()

#Set up drawing surface
w = 640
h = 550
size = (w,h)
surface = pygame.display.set_mode(size)

#Set window title bar
pygame.display.set_caption("Swimming Story")

#Color Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
DARKGREEN = (25, 109, 0)

#Set Rectangle bounds of where Left and right decision images will be located- use pygame.RECT
LEFT= pygame.Rect(w/20, h*1/3, 120, 120)
RIGHT= pygame.Rect(w-w/10-90,h*1/3, 120, 120)  
MIDDLE= pygame.Rect(w/2.5, h/10, 120, 120)

'''
draws boxes & border around the drawing surface for the game
function written by Luke Szfranski
'''
def drawBorder():
    pygame.draw.rect(surface,DARKGREEN,(0,2*h/3,w,h/3),0)
    pygame.draw.rect(surface,BLACK,(0,0,w,20),0)
    pygame.draw.rect(surface,BLACK,(0,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,h-20,w,20),0)
    pygame.draw.rect(surface,BLACK,(w-20,0,20,h),0)
    pygame.draw.rect(surface,BLACK,(0,2*h/3,w,20),0)

'''
displays text left aligned at the line location specified. words display in specified size
  words- the text to display
  line- either UPPERLINE, MIDDLELINE, LOWERLINE
  size- integer value of text size
'''
def displayText(words,line,size):
    font = pygame.font.SysFont('Arial',size,1,0)
    text = font.render(words,1,WHITE)
    bounds = text.get_rect()
    bounds.topleft = line
    surface.blit(text,bounds)
    
'''
displays an image file picture at the location specified
   location- tuple of x,y values of where to place the picture
   picture- image filename 
'''
def displayPicture(picture,location):
    surface.blit(pygame.image.load(picture).convert_alpha(),location)
    
'''
returns 3-picture tuple of the main image and two choices for the next level (level below current level)
   levelcode- next level of game to be played
'''
def getPictures(levelCode):
    leftPic=''
    rightPic=''
    middlePic=''
    
    
    # Add your code here with if statements to set the left choice, middle (pic that describes current level), and right choice
    
    if levelCode == '1':
        leftPic='carbsBar.png'
        rightPic='proteinBar.png'
        middlePic='manShrugging.png' 
    elif levelCode == '2A':
        leftPic='legPeice.png'
        rightPic='spaghetti.png'
        middlePic='manShrugging.png'
    elif levelCode == '2B':
        leftPic='swimmer.png'
        rightPic='barfEmoji.png'
        middlePic='manShrugging.png'
    elif levelCode == '2C':
        leftPic='swimmer.png'
        rightPic='monsterDrink.png'
        middlePic='manShrugging.png'
    elif levelCode == '2D':
        leftPic='tangerine.png'
        rightPic='swimmer.png'
        middlePic='manShrugging.png'
    elif levelCode == '3A':
        leftPic='smiling.png'
        rightPic='smiling.png'        
        middlePic='smiling.png'
    elif levelCode == '3B':
        leftPic='opps.png'
        rightPic='opps.png'        
        middlePic='opps.png'  
    elif levelCode == '3C':
        leftPic='smiling.png'
        rightPic='smiling.png'                
        middlePic='smiling.png'
    elif levelCode == '3D':
        leftPic='opps.png'
        rightPic='opps.png'        
        middlePic='opps.png' 
    elif levelCode == '3E':
        leftPic='opps.png'
        rightPic='opps.png'        
        middlePic='opps.png'    
    elif levelCode == '3F':
        leftPic='smiling.png'
        rightPic='smiling.png'        
        middlePic='smiling.png' 
    elif levelCode == '3G':
        leftPic='poop.png'
        rightPic='poop.png'        
        middlePic='poop.png'
    elif levelCode == '3H':
        leftPic='smiling.png'
        rightPic='smiling.png'        
        middlePic='smiling.png'  
    
        
    return (leftPic,middlePic, rightPic)
 
'''
    returns the game text at the current level
       levelCode- current level
'''

def getLevelText(levelCode):
    if levelCode=='1':
        return "You are at your first swimming competition this weekend. What do you do first? Do you plan to eat a protein bar or eat carb bar? "
    elif levelCode=='2A':
        return "You decided to eat a 15 piece bucket of chicken. It is time to swim your event but you are too full to move. What will you do? Go to the sink or do it in the pool while you are swimming "
    elif levelCode=='2B':
        return "Too much chicken makes you want to throw up. What will you do? Will you swim or throwup?"
    elif levelCode=='2C':
        return "You decide to eat some bluberries and is flowing with energy. It is time to swim your event. But you are very nervous. What do you do? Take a pill to slow it down or just go anyways"      
    elif levelCode=='2D':
        return "You decided to eat a sandwich. It is time to swim your event but you feel uncomfertable and need to go to the bathroom. What will you do? Will you hold it in or just send it in the water"    
    elif levelCode=='3A':
        return "Good job you came first in your swimming competion."  
    elif levelCode=='3B':
        return "You were to fast that you broke the laws of physics and tore the whole pool up. So you didn't win" 
    elif levelCode=='3C':
        return "Good job you came first in your swimming competion."
    elif levelCode=='3D':
        return "You throwing up infected the pool and everyone is passing out. You are disqualified" 
    elif levelCode=='3E':
        return "You were to fast that you broke the laws of physics and tore the whole pool up. So you didn't win" 
    elif levelCode=='3F':
        return "Good job you came first in your swimming competion."
    elif levelCode=='3G':
        return "Too many oranges led you to explosive diareha and you missed your comeption. You are disqualified "   
    elif levelCode=='3H':
        return "Good job you came first in your swimming competion."
    

'''
returns the next game level based on the currentLevel and choice made
   choice- either 'left' or 'right'
'''
def getNextLevel(currentLevel, choice):
    if currentLevel == "2B" and choice == "left":
        return "3C"
    elif currentLevel == "1" and choice == "left":
        return random.choice(("2A", "2B"))
    elif currentLevel == "1" and choice == "right":
        return random.choice(("2C", "2D"))
    elif currentLevel == "2A" and choice == "left":
        return "3A"  
    elif currentLevel == "2A" and choice == "right":
        return "3B"
    elif currentLevel == "2B" and choice == "right":
        return "3D"
    elif currentLevel == "2C" and choice == "left":
        return "3E"
    elif currentLevel == "2C" and choice == "right":
        return "3F"
    elif currentLevel == "2D" and choice == "left":
        return "3G"
    elif currentLevel == "2D" and choice == "right":
        return "3H"   

'''
returns the 3 sentences of the text to display
pre: line must be at least 2 sentences long; 
     1st sentence must end in a period.  
     If 3 sentences, 2nd must end in a ?
     
post:  first sentence will end with a period 
       second sentence will end with a question mark (if not end of game)
       third sentence will contain any remaining text (if it exists)
'''
def splitText(line):
    period=line.find('.')
    sentence1=line[0:period+1]
    questionMark=line.find('?')
    if questionMark!=-1:  #found a ?
        sentence2=line[period+1:questionMark+1]
        sentence3=line[questionMark +1:]
    else:
        sentence2=line[period+1:]
        sentence3=""
    return sentence1,sentence2,sentence3
    
'''
draws all of the game screen
'''
def drawScreen(gameStage):
     #placement of 3 text labels
    UPPERLINE =  (w/20,35* h/48)
    MIDDLELINE = (w/20,77* h/96)
    LOWERLINE =  (w/20,42* h/48)
    
    drawBorder()
    
    #get level images and text to display
    gameText= getLevelText(gameStage)

    #split gametext to 3 lines for output using slices
    first, second, last = splitText(gameText)
    displayText(first,  UPPERLINE, 16)
    displayText(second, MIDDLELINE, 16)
    displayText(last,   LOWERLINE, 16)
    
    #returns tuple with 3 pix for that level (leftpicture, middlepicture, rightpicture)
    picsToDisplay=getPictures(gameStage) 
    displayPicture(picsToDisplay[0],LEFT) 
    displayPicture(picsToDisplay[1],MIDDLE)
    displayPicture(picsToDisplay[2],RIGHT)
     


#*------------------------------------------ MAIN PROGRAM LOOP----------------------------------*

#story starts at stage 1
stage = "1"
while(True):
    for event in pygame.event.get():
        if((event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()
            
        #add code here for mouse click detection & collision check
        #code will check collision with the LEFT and RIGHT RECT objects and getNextLevel() of the game to execute
        if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
            mousePos = pygame.mouse.get_pos()
            if LEFT.collidepoint(mousePos):
                stage = getNextLevel(stage, "left")
            if RIGHT.collidepoint (mousePos):
                stage = getNextLevel(stage, "right")
            
        
        
        #was mouse clicked inside of LEFT or RIGHT Picture?
            
           

   
    #Set Background Fill
    surface.fill(WHITE)
    
    #Drawing code goes here
    drawScreen(stage) 
   
    pygame.display.update()
