#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:59:56 2022

@author: shimin
"""
import numpy as np
import random
from Battleships import Ship, coordinates, add_ships, guess_ship, ship_board

def ship_validation(board, ship):
    x,y = ship.pos()
    for c in ship.pos():
        if c < 0 or c > 9:
            return False
    
    if ship.size() < 1:
        return False
    
    if ship.orient() == "Horizontal":
        if x+ship.size()-1>9:
            return False
        for i in range(ship.size()):
            if board[x+i][y] != 0:
                return False
    elif ship.orient() == "Vertical":
        if y+ship.size()-1>9:
            return False
        for i in range(ship.size()):
            if board[x][y+i] != 0:
                return False
    else:
        return False
    return True
    

def ship_placement_random(l:list=[2,3,4,4]):
    board_temp = np.zeros((10,10))
    ship_arr = np.array([])
    for length in l:
        while True:
            ship_temp = Ship(length, 
                             np.array([random.randint(0,9),random.randint(0,9)]), 
                             random.choice(["Horizontal", "Vertical"]))
            if ship_validation(board_temp, ship_temp):
                break
        #while not ship_validation(board_temp, ship_temp):
        #    ship_temp = Ship(length, 
        #                     np.array([random.randint(0,9),random.randint(0,9)]), 
        #                     random.choice(["Horizontal", "Vertical"]))
        x_temp, y_temp = ship_temp.pos()
        if ship_temp.orient() == "Horizontal":
            for i in range(length):
                board_temp[x_temp+i][y_temp] = 1
        elif ship_temp.orient() == "Vertical":
            for i in range(length):
                board_temp[x_temp][y_temp+i] = 1
        ship_arr=np.append(ship_arr,ship_temp)
    print(board_temp)
    return ship_arr


s = ship_placement_random()
print(s)

def parity(board):
   for rowindex, row in enumerate(board):
       if 2 in row:
           i = list(np.where(row == 2))
           for colindex in i[0]: 
               if board[rowindex][np.max([0,colindex-1])] == 0:
                   return rowindex, np.max([0,colindex-1])
               elif board[rowindex][np.min([9,colindex+1])] == 0:
                   return rowindex, np.min([9,colindex+1])
               elif board[np.max([0,rowindex-1])][colindex] == 0:
                   return np.max([0,rowindex-1]), colindex
               elif board[np.min([9,rowindex+1])][colindex] == 0:
                   return np.min([9,rowindex+1]), colindex
               
   while True:
       rowindex=random.randint(0,9)
       colindex=random.randint(0,9)
       if board[rowindex][colindex] == 0:
           if ((rowindex + colindex) % 2 )==0:
               return rowindex, colindex


if __name__ == "__main__":
    turns=100
    l = []
    n_sim = 10
    for _ in range(n_sim):
        s=np.zeros((10,10))
        guess_board=np.zeros((10,10))
        
        ship_array=np.array([])
        
        ship1=Ship()
        
        ship_array=np.append(ship_array,ship1)
        
        
        ship2=Ship(3,np.array([]))
        
        ship_array=np.append(ship_array,ship2)
        
        ship3=Ship(4, np.array([]))
        
        ship_array=np.append(ship_array,ship3)
        
        ship4=Ship(4, np.array([]))
        
        ship_array=np.append(ship_array,ship4)
    
    
        for ship in ship_array:
            xcoord,ycoord=coordinates(ship)
            add_ships(ship_board,xcoord,ycoord)
            
        for turn in range(turns):
          print("Turn:", turn + 1, "of", turns)
          print("Ships left:", len(ship_array))
          print()
          
          
          x, y = parity(guess_board)
          
          #x = int(input("Guess an x coordinate: "))
          #y = int(input("Guess a y coordinate: "))
          
        
          guess_coord=np.array([x,y])
          #guess_coord=less_random_guess()
          
          guess_ship(guess_coord)
        
          print(guess_board)
          #print(ship_board)
          
          if np.sum(ship_board)==0:
              l += [turn]
              break
        
        # End Game
        if np.sum(ship_board)!=0:
          print("You lose!")
        else:
          print("All the ships have been sunk. You win!")
          
    
      
    import matplotlib.pyplot as plt
    plt.hist(l)
    
    cum.sum 
    
