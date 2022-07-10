
from logging import exception
import pygame 
import sys

class Node():
    def __init__(self,state,state_x,state_y,parent,action):
        self.state = state
        self.state_x = state_x
        self.state_y = state_y
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self,node):
        self.frontier.append(node)
    def contains_state(self,state_x,state_y):
        return any(node.state_y == state_y and node.state_x == state_x for node in self.frontier)
    def empthy(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empthy():
            raise Exception("empty stack")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
    def  stack_len(self):
        return len(self.frontier)


class QueueFrontier(StackFrontier):
    
    def remove(self):
        if self.empthy():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node



def check_move(state_x,state_y):
    moves = []
    rows = len(arr) - 1
    columns = len(arr[0])  - 2
 
        #down
    if state_x != rows:
        if arr[state_x+1][state_y] != "#":
            moves.append("Down")
    if state_x != 0:
        if arr[state_x-1][state_y] != "#":
            moves.append("Up")
    if state_y != columns:
        if arr[state_x][state_y+1] != "#":
            moves.append("Right")
    if state_y != 0:
        if arr[state_x][state_y-1] != "#":
            moves.append("Left")

    return moves

def DFS():
    start = Node(arr[start_pos_x][start_pos_y],start_pos_x,start_pos_y,None,None)
    stack = StackFrontier()
    stack.add(start)
    moves = []
    while True:
        if stack.empthy():
            print("NO SOLUTION")
            return

        node = stack.remove()
        if node.state == "B":
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent
            actions.reverse()
            #print("FOUND")
            return 
        if arr[node.state_x][node.state_y] != 'A':
            arr[node.state_x][node.state_y] = 'E'
        #up
        '''print("State:",node.state)
        print("NODE:",node.state_x,node.state_y)
        print("STACK_LEN:",stack.stack_len())
        print(moves)
        print(stack.contains_state(node.state_x,node.state_y)) '''
        moves = check_move(node.state_x,node.state_y)
        for i in range(len(moves)):
            if moves[i] == 'Down' and arr[node.state_x+1][node.state_y]  !='E'  and not stack.contains_state(node.state_x+1,node.state_y):
                child = Node(arr[node.state_x+1][node.state_y],node.state_x +1, node.state_y,node,'Down')
                stack.add(child)
            if moves[i] == 'Up' and arr[node.state_x-1][node.state_y]  !='E' and not stack.contains_state(node.state_x-1,node.state_y):
                child = Node(arr[node.state_x-1][node.state_y],node.state_x -1, node.state_y,node,'Up')
                stack.add(child)
            if moves[i] == 'Left' and arr[node.state_x][node.state_y-1] != 'E' and not stack.contains_state(node.state_x,node.state_y-1):
                child = Node(arr[node.state_x][node.state_y-1],node.state_x, node.state_y-1,node,'Left')
                stack.add(child)
            if moves[i] == 'Right' and arr[node.state_x][node.state_y+1]  != 'E' and not stack.contains_state(node.state_x,node.state_y+1):
                child = Node(arr[node.state_x][node.state_y+1],node.state_x, node.state_y+1,node,'Right')
                stack.add(child)


def BFS():
    start = Node(arr[start_pos_x][start_pos_y],start_pos_x,start_pos_y,None,None)
    stack = QueueFrontier()
    stack.add(start)
    moves = []
    while True:
        if stack.empthy():
            print("NO SOLUTION")
            return

        node = stack.remove()
        if node.state == "B":
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent
            actions.reverse()
            #print("FOUND")
            return 
        if arr[node.state_x][node.state_y] != 'A':
            arr[node.state_x][node.state_y] = 'E'
        #up
        '''print("State:",node.state)
        print("NODE:",node.state_x,node.state_y)
        moves = check_move(node.state_x,node.state_y)
        print("STACK_LEN:",stack.stack_len())
        print(moves) 
        print(stack.contains_state(node.state_x,node.state_y))'''
        moves = check_move(node.state_x,node.state_y)
        for i in range(len(moves)):
            if moves[i] == 'Down' and arr[node.state_x+1][node.state_y]  !='E'  and not stack.contains_state(node.state_x+1,node.state_y):
                child = Node(arr[node.state_x+1][node.state_y],node.state_x +1, node.state_y,node,'Down')
                stack.add(child)
            if moves[i] == 'Up' and arr[node.state_x-1][node.state_y]  !='E' and not stack.contains_state(node.state_x-1,node.state_y):
                child = Node(arr[node.state_x-1][node.state_y],node.state_x -1, node.state_y,node,'Up')
                stack.add(child)
            if moves[i] == 'Left' and arr[node.state_x][node.state_y-1] != 'E' and not stack.contains_state(node.state_x,node.state_y-1):
                child = Node(arr[node.state_x][node.state_y-1],node.state_x, node.state_y-1,node,'Left')
                stack.add(child)
            if moves[i] == 'Right' and arr[node.state_x][node.state_y+1]  != 'E' and not stack.contains_state(node.state_x,node.state_y+1):
                child = Node(arr[node.state_x][node.state_y+1],node.state_x, node.state_y+1,node,'Right')
                stack.add(child)
        
        
            



actions = []
COLOR1 = (0,0,139)
BLACK = (64,64,64)
RED = (220,20,60)
BLUE = (0,128,0)
YELLOW = (184,134,11)
GREEN = (0,128,0)
arr = []
Width = 900
Height = 900
start_pos_x = 14
start_pos_y = 1 
showExplored = False
dfs_on = True
def open_file():
    f = open("MazePathFinder\mazee.txt", "r")
    
    for line in f:
        col = []
        for character in line:
            col.append(character)
        arr.append(col)
    f.close()
       
    
def draw():
    global start_pos_x,start_pos_y
    rows = len(arr)
    columns = len(arr[0])  - 1
    Margin = 5
    block_size = Width / rows - Margin
    full_width, full_height = Margin + block_size, Margin + block_size
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == "#":
                pygame.draw.rect(Screen, BLACK,[full_width * j + Margin, 
                                         full_height * i + Margin, block_size, block_size])
            if arr[i][j] == "A":
                pygame.draw.rect(Screen, RED,[full_width * j + Margin, 
                                         full_height * i + Margin, block_size, block_size])
                
            if arr[i][j] == "B":
                pygame.draw.rect(Screen, GREEN,[full_width * j + Margin, 
                                         full_height * i + Margin, block_size, block_size])
            if arr[i][j] == "!":
                 pygame.draw.rect(Screen, YELLOW,[full_width * j + Margin, 
                                         full_height * i + Margin, block_size, block_size])
            if showExplored == True:
               if arr[i][j] == "E":
                 pygame.draw.rect(Screen, COLOR1,[full_width * j + Margin, 
                                         full_height * i + Margin, block_size, block_size])
            
def print_arr():
    counter = 0
    goal_counter = 0
    rows = len(arr)
    columns = len(arr[0])  - 1
    print("ROWS:",rows)
    print("Columns:",columns)           
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == "!" or arr[i][j] == "E":
                counter += 1
            if arr[i][j] == '!':
                goal_counter += 1 
            print(arr[i][j],end= " ")
        print()
    print("Total_moves:",counter)
    print("Moves to the Goal:",goal_counter)
    print("-------------------------------------------")
def show_actions():
    curr_x = start_pos_x
    curr_y = start_pos_y
    for i in range(len(actions)-1):
        if actions[i] == 'Up':
            arr[curr_x-1][curr_y] = "!"
            curr_x = curr_x -1
        elif actions[i] == 'Down':
            arr[curr_x+1][curr_y] = "!"
            curr_x = curr_x +1
        elif actions[i] == 'Left':
            arr[curr_x][curr_y-1] = "!"
            curr_y = curr_y - 1
        else:
            arr[curr_x][curr_y+1] = "!"
            curr_y = curr_y + 1







if __name__ == "__main__":
    pygame.init() 
    open_file()
    
    Screen = pygame.display.set_mode((Width,Height))
    Clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if dfs_on == True:
                    DFS()
                    show_actions()
                    dfs_on = False
                else:
                    actions = []
                    arr = []
                    open_file()
                    BFS()
                    show_actions()
                    
            
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    print_arr()
                if event.key == pygame.K_SPACE:
                    showExplored = True
                
        Screen.fill(('black'))
        draw()
        Clock.tick(60)
        pygame.display.update()