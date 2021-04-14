import sys

print("\n************Hello World, I Solve Alice Mazes************\n")

class Node:
    def __init__(self, loc, moves, d_change,  start=False, goal=False):
        self.loc = loc
        self.moves = moves
        self.d_change = d_change
        self.my_d = 0
        self.start = start
        self.goal = goal
        self.d_arrivals = {}
    
    def __repr__(self):
        return str((self.loc["row"], self.loc["col"]))

    def d_update(self):
        self.my_d += self.d_change
    
    def setMyD(self, d):
        self.my_d = d + self.d_change
    
    def getMyD(self):
        return self.my_d

def isValidCell(alice_maze, row, col, current_d):
     return (row < len(alice_maze) and col < len(alice_maze[0])) and (not current_d <= 0) \
          and (not current_d in list(alice_maze[row][col].d_arrivals.keys()))

def aliceBFS(alice_maze, start, d=1):

    # queue used to do BFS
    queue = []

    # push start cell in queue
    start_cell = alice_maze[start["row"]][start["col"]]
    start_cell.setMyD(d)
    queue.append(start_cell)

    # loop till queue is empty
    while(len(queue) != 0):

        # pop from front of queue and print it
        cell_parent = queue.pop(0)
        current_d = cell_parent.my_d
        
        # check if cell is the goal
        if(cell_parent.goal):
            print("Goal Found: "+ str(cell_parent))
            return cell_parent

        if(current_d==0):
            continue

        # do for every move (x1,y1) -> (x2, y2)
        for move in cell_parent.moves:

            # get coord of next loc/cell
            next_row = cell_parent.loc["row"] + (current_d)*move["row"]
            next_col = cell_parent.loc["col"] + (current_d)*move["col"]

            # check if cell exists in alice maze
            valid_cell = isValidCell(alice_maze, next_row, next_col, current_d)

            if(not valid_cell):
                continue

            # add next cell to the queue
            cell_child = alice_maze[next_row][next_col]
            if(not current_d in cell_child.d_arrivals.keys() and ((current_d + cell_child.d_change)>0)):
                cell_child.setMyD(current_d)
                cell_child.d_arrivals[current_d] = cell_parent
                queue.append(cell_child)

    return None

# Utility function to print path from source to destination
def printPath(goal):
    
    if goal is None:
        return 0
        
    cell_path = []

    cell_path.insert(0, goal)

    arrival_step = list((goal.d_arrivals.keys()))[0]
    cell_parent = goal.d_arrivals[arrival_step]
    cell_path.insert(0, cell_parent)

    while(not cell_parent.start):

        arrival_step = arrival_step - cell_parent.d_change
        cell_parent = cell_parent.d_arrivals[arrival_step]
        cell_path.insert(0, cell_parent)

    path =""
    indx = 0
    while(indx < len(cell_path)):
        if(indx!=len(cell_path)-1):
            path += str(cell_path[indx])+"->"
        else:
            path += str(cell_path[indx])
            break
        indx += 1
    
    print(path)
 
    length = len(cell_path)
    return length

def generateMaze():
    
    # Check for .txt file command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 Alice.py <inputfilename>")
        sys.exit()

    # open a file whose name is given as the first argument
    f = open(sys.argv[1])

    # read row
    row_num = int((f.readline().split('-')[1]).strip())

    # read col
    col_num = int((f.readline().split('-')[1]).strip())

    # read start loc
    start_str = (f.readline().split('-')[1]).strip()
    start = {"row": int((start_str.split(',')[0]).strip()), "col": int((start_str.split(',')[1]).strip())}

    # read goal loc
    goal_str = (f.readline().split('-')[1]).strip()
    goal = {"row": int((goal_str.split(',')[0]).strip()), "col": int((goal_str.split(',')[1]).strip())}

    # read d
    d = int((f.readline().split('-')[1]).strip())

    # print line header
    f.readline()

    alice_maze = []
    for row in range(0,row_num):
        row = []
        for col in range(0,col_num):

            line = f.readline()
            input_str_list = line.strip().split('|')
            
            row_col = (input_str_list[0]).strip().split(',')
            n_row = int(row_col[0])
            n_col = int(row_col[1])
            n_start = {"row": n_row, "col": n_col}

            moves_str_list = input_str_list[1].strip().split("#")
            moves = []
            
            for move_str in moves_str_list:
                if(moves_str_list[0]==''):
                    continue
                move_split = (move_str).strip().split(',')

                m_row = int(move_split[0])
                m_col = int(move_split[1])
                move = {"row": m_row, "col": m_col}
                moves.append(move)

            d_change = int(input_str_list[2])                
            
            is_start = False
            if(input_str_list[3]=='T'):
                is_start = True
            
            is_goal = False
            if(input_str_list[4]=='T'):
                is_goal = True
            
            node = Node(n_start, moves, d_change, is_start, is_goal)

            row.append(node)
        
        alice_maze.append(row)

    f.close()

    return alice_maze, start, goal, d

if __name__ == '__main__':

    alice_maze, start, goal, d = generateMaze()
    print("Start: " + "(" + str(start["row"]) + ", "+  str(start["col"]) +")")
    goal = aliceBFS(alice_maze, start, d)
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")
    
    print('\n')