from pygame import *; 
from random import* 
from math import * 
from copy import*;
import pygame
pygame.init()

screen=display.set_mode((700,700))
screenRect=Rect(0,0,700,700)
gameRunning=True 
screen.fill(16777215)
backgroundTemp=image.load("connectFourBoard.png") 
background=transform.scale(backgroundTemp,(700,630)) 

columnSize= 7
rowSize= 6
board = [0] * rowSize
playerColours=[(255,0,0),(255,255,0)]

for i in range(rowSize):
    board[i] = [0] * columnSize

def return_last(board,col):
    reverse=5
    for row in range (rowSize+1):
        if (board[reverse-row][col]==0):
            return reverse-row
def update_Board(board,col,row,turn):
    board[row][col]=turn+1
def draw_Board(board):
    for row in range (rowSize):
        for col in range (columnSize):
            if (board[row][col]!=0):
                draw.circle(screen,playerColours[board[row][col]-1],(col*100+55-col*3,row*100+155-(6-row)),43)
            
def valid_pos(board,col):
    if (board[0][col]==0):
        return True
    else:
        return False

def possible_Squares(board):
    squares=[5]*columnSize
    for r in reversed(range (rowSize)):
        for c in range (columnSize):
            if ((board[r][c]==1 or board[r][c]==2) and r>=0):
                squares[c]=r-1
    return squares


       
def check3(board,turn,row,col):
    maxScore=-5
    minScore=5
    for r in range (rowSize-2):
        for c in range (columnSize):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r+1][c]==turn+1 and board[r+2][c]==turn+1):
                    if (maxScore<3):
                        if ((r==row and c==col) or (r+1==row and c==col) or (r+2==row and c==col)):
                            maxScore=3
            if (turn==1):
                if (board[r][c]==turn+1 and board[r+1][c]==turn+1 and board[r+2][c]==turn+1):
                    if (minScore<-3):
                        if ((r==row and c==col) or (r+1==row and c==col) or (r+2==row and c==col)):
                            
                            minScore=-3
    for r in range (rowSize):
        for c in range (columnSize-2):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r][c+1]==turn+1 and board[r][c+2]==turn+1):
                    if (maxScore<3):
                        if ((r==row and c==col) or (r==row and c+1==col) or (r==row and c+2==col)):
                            maxScore=3
            if (turn==1):
                if (board[r][c]==turn+1 and board[r][c+1]==turn+1 and board[r][c+2]==turn+1):
                    if (minScore>-3):
                        if ((r==row and c==col) or (r==row and c+1==col) or (r==row and c+2==col)):
                            minScore=-3
    for r in range (rowSize-2):
        for c in range (columnSize-2):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r+1][c+1]==turn+1 and board[r+2][c+2]==turn+1):
                    if (maxScore<3):
                        if ((r==row and c==col) or (r+1==row and c+1==col) or (r+2==row and c+2==col)):
                            maxScore=3
            if (turn==1):
                if (board[r][c]==turn+1 and board[r+1][c+1]==turn+1 and board[r+2][c+2]==turn+1):
                    if (minScore>-3):
                        if ((r==row and c==col) or (r+1==row and c+1==col) or (r+2==row and c+2==col)):
                            minScore=-3
    for r in range (rowSize-2):
        for c in range (columnSize-2):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r-1][c+1]==turn+1 and board[r-2][c+2]==turn+1):
                    if (maxScore<3):
                        if ((r==row and c==col) or (r-1==row and c+1==col) or (r-2==row and c+2==col)):
                            maxScore=3
            if (turn==1):
                if (board[r][c]==turn+1 and board[r-1][c+1]==turn+1 and board[r-2][c+2]==turn+1):
                    if (minScore>-3):
                         if ((r==row and c==col) or (r-1==row and c+1==col) or (r-2==row and c+2==col)):
                            minScore=-3
    if (turn==0):
        return maxScore
    else:
        return minScore
def check2(board,turn,row,col):
    maxScore=-5
    minScore=5
    for r in range (rowSize-1):
        for c in range (columnSize):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r+1][c]==turn+1):
                    if (maxScore<2):
                        if ((r==row and c==col) or (r+1==row and c==col)):
                            maxScore=2
            if (turn==1):
                if (board[r][c]==turn+1 and board[r+1][c]==turn+1):
                    if (minScore<-2):
                        if ((r==row and c==col) or (r+1==row and c==col)):
                            minScore=-2
    for r in range (rowSize):
        for c in range (columnSize-1):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r][c+1]==turn+1):
                    if (maxScore<2):
                        if ((r==row and c==col) or (r==row and c+1==col)):                
        
                            maxScore=2
            if (turn==1):
                if (board[r][c]==turn+1 and board[r][c+1]==turn+1):
                    if (minScore>-2):
                        if ((r==row and c==col) or (r==row and c+1==col)):
                            minScore=-2
    for r in range (rowSize-1):
        for c in range (columnSize-1):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r+1][c+1]==turn+1):
                    if (maxScore<2):
                        if ((r==row and c==col) or (r+1==row and c+1==col)):
                            maxScore=2
            if (turn==1):
                if (board[r][c]==turn+1 and board[r+1][c+1]==turn+1):
                    if (minScore>-2):
                        if ((r==row and c==col) or (r+1==row and c+1==col)):
                            minScore=-2
    for r in range (rowSize-1):
        for c in range (columnSize-1):
            if (turn==0):
                if (board[r][c]==turn+1 and board[r-1][c+1]==turn+1):
                    if (maxScore<2):
                        if ((r==row and c==col) or (r-1==row and c+1==col)):
                            maxScore=2
            if (turn==1):
                if (board[r][c]==turn+1 and board[r-1][c+1]==turn+1):
                    if (minScore>-2):
                        if ((r==row and c==col) or (r-1==row and c+1==col)):
                            minScore=-2
    if (turn==0):
        return maxScore
    else:
        return minScore
                
def bestMove(board,turn,row,col):
    minScore=5
    maxScore=-5
    score1=check3(board,turn,row,col)
    score2=check2(board,turn,row,col)
    if (turn==0):
        if (score1>maxScore):
            maxScore=score1
        if (score2>maxScore):
            maxScore=score2
    if (turn==1):
        if (score1<minScore):
            minScore=score1
        if (score2<minScore):
            minScore=score2
    if (turn==0):
        return maxScore
    if (turn==1):
        return minScore
def gameOver(board,turn):
    
    winCount=0;
    for c in range (columnSize):
        for r in range (rowSize):
            if (board[r][c]==turn+1):
                winCount+=1
            else:
                winCount=0
            if (winCount==4):
                return True
    for r in range (rowSize):
        for c in range (columnSize):
            if (board[r][c]==turn+1):
                winCount+=1
            else:
                winCount=0
            if (winCount==4):
                return True
    for c in range (columnSize-3):
        for r in range (rowSize-3):
            if (board[r][c]==turn+1 and board[r+1][c+1]==turn+1 and board[r+2][c+2]==turn+1 and board[r+3][c+3]==turn+1):
                return True
    for c in range (columnSize-3):
        for r in range (3,rowSize):
            if (board[r][c]==turn+1 and board[r-1][c+1]==turn+1 and board[r-2][c+2]==turn+1 and board[r-3][c+3]==turn+1):
                return True
    
print(board)
font_1 = pygame.font.SysFont("comicsansms", 50)
font_2 = pygame.font.SysFont("comicsansms", 50)
text_1 = font_1.render("Congrats you won", True, (0, 128, 0))
text_2=font_2.render("You Lost", True, (0, 128, 0))
move=0
screen.blit(background,(0,90))
while gameRunning:
    for e in event.get():
        if e.type==QUIT:
            running=False
        if e.type==MOUSEBUTTONDOWN:
            if (move==0):
                #x=int(input("Enter a number"))
                x=e.pos[0]//100
                if (valid_pos(board,x)):
                    update_Board(board,x,return_last(board,x),0)
                    print(board)
                   #For two player Commented out 
            '''if (move==1):
               # x=int(input("Enter a number"))
                spots=possible_Squares(board)
                for i in range (columnSize):
                    if (spots[i]!=-1):
                        board[spots[i]][i]=2
                        break
                """x=e.pos[0]//100
                if (valid_pos(board,x)):
                    update_Board(board,x,return_last(board,x),1)
                    print(board)"""
               ''' 
            if (gameOver(board,move)):
                print("The game is Over")
                screen.blit(text_1,(0,0))
                gameRunning=False
                
            if (move==0):
                move=1
            else:
                move=0
            
            
        
    if (move==1 and gameRunning):
       
            # x=int(input("Enter a number"))
            spots=possible_Squares(board)
            best=5
            rowHold=-1
            colHold=-1
            for i in range (columnSize):
                if (spots[i]!=-1):
                    #board[spots[i]][i]=2
                    temp=deepcopy(board)
                    temp[spots[i]][i]=2

                    if (gameOver(temp,1)):
                        rowHold=spots[i]
                        colHold=i
                        best=-10
                    new=2*bestMove(temp,1,spots[i],i)
                    if (new !=-4 and new !=-3):
                        new+=2*(int)(ceil((i-3)/7))
                    if (best>new):
                        best=new
                        rowHold=spots[i]
                        colHold=i
                    temp[spots[i]][i]=1
                    if (gameOver(temp,0)):
                        temp[spots[i]][i]=2
                        best=-8
                        rowHold=spots[i]
                        colHold=i 
                            
                    
                    temp[spots[i]][i]=0
            if (best!=5):
                board[rowHold][colHold]=2
 

            if (best==5 and move==1):
                z=randint(0,columnSize-1)
                board[spots[z]][z]=2
                
                if (gameOver(board,1)):
                    gameRunning=False
                    

            if (gameOver(board,move)):
                    print("The game is Over")
                    gameRunning=False
                    screen.blit(text_2,(0,0))
                    
            move=0;
            
            

    screen.blit(background,(0,90))
    draw_Board(board)
    possible_Squares(board)

    display.flip()
    if (not gameRunning):
        
        time.wait(5000)

quit() 
