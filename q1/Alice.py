print("\n************Hello World, I Solve Alice Mazes************\n")

class Node:
    def __init__(self, loc, moves, d_change,  start=False, goal=False):
        self.loc = loc
        self.moves = moves
        self.d_change = d_change
        self.my_d = 0
        self.start = start
        self.goal = goal
        self.parent = None
        self.d_arrivals = {}
    
    def __repr__(self):
        return str((self.loc["row"], self.loc["col"]))


    def d_update(self):
        self.my_d += self.d_change
    
    def setMyD(self, d):
        self.my_d = d + self.d_change
    
    def getMyD(self):
        return self.my_d

def isValidCell(alice_maze, row, col):
     return row < len(alice_maze) and col < len(alice_maze[0])

def aliceBFS(alice_maze, start, discovered):

    # queue used to do BFS
    queue = []

    # mark start cell as discovered
    discovered[start["row"]][start["col"]] = True

    # push start cell in queue
    start_cell = alice_maze[start["row"]][start["col"]]
    start_cell.setMyD(d)
    queue.append(start_cell)

    # loop till queue is empty
    while(len(queue) != 0 and not goal_found):

        # pop from front of queue and print it
        cell_parent = queue.pop(0)
        parent_d = cell_parent.my_d
        
        # check if cell is the goal
        if(cell_parent.goal):
            print("Goal Found: "+ str(cell_parent))
            # print(cell_parent)
            return cell_parent
        
        # do for every move (x1,y1) -> (x2, y2)
        for move in cell_parent.moves:
            # print(move)

            # get coord of next loc/cell
            next_row = cell_parent.loc["row"] + (parent_d)*move["row"]
            next_col = cell_parent.loc["col"] + (parent_d)*move["col"]

            # check if cell exists in alice maze
            valid_cell = isValidCell(alice_maze, next_row, next_col)

            if(not valid_cell):
                #print('NOT VALID child loc: {\"row\": ' + str(next_row) + ', \"col\": '+ str(next_col)+'}')
                continue

            # print('VALID child loc: {\"row\": ' + str(next_row) + ', \"col\": '+ str(next_col)+'}')

            # mark cell discovered and push it in to the queue
            discovered[next_row][next_col] = True

            # add next cell to the queue
            cell_child = alice_maze[next_row][next_col]
            cell_child.parent = cell_parent
            cell_child.setMyD(parent_d)
            if(not parent_d in cell_child.d_arrivals.keys()):
                cell_child.d_arrivals[parent_d] = cell_parent
            queue.append(cell_child)
        # print('\n') # DELETE

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
    return length + 1

if __name__ == '__main__':

    # MAZE 1
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row": 0, "col": 1},{"row":1, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": d, "col": -d}], -1)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": -1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 1, "col": -1}], 0)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": -1, "col": 0}, {"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze1 = [row0, row1, row2]
    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 1")
    goal = aliceBFS(alice_maze1, {"row": 0, "col": 0}, discovered)

    
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 2
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":d, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}], -1)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": -1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": +1, "col": -1}], 0)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": -1, "col": 0}, {"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze2 = [row0, row1, row2]
    d=1
    goal_found = False
    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 2")
    goal = aliceBFS(alice_maze2, {"row": 0, "col": 0}, discovered)

    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 3
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":1, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}, {"row": 0, "col": -1}], -1)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": 1},{"row": 1, "col": -1},{"row": 1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": +1, "col": -1}], 0)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": -1, "col": 0}, {"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 0, "col": 1}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 1)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze3 = [row0, row1, row2]
    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 3")
    goal = aliceBFS(alice_maze3, {"row": 0, "col": 0}, discovered)

    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 4
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":1, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}, {"row": 0, "col": -1}], -1)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0},{"row": 1, "col": 1}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": -1},{"row": 1, "col": 1}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 1, "col": -1}], 0)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 1)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": -1, "col": 0}], 1)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze4 = [row0, row1, row2]
    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 4")
    goal = aliceBFS(alice_maze4, {"row": 0, "col": 0}, discovered)

    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')
    
    # # MAZE 5
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":1, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}, {"row": 0, "col": -1}], -1)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": -1},{"row": 1, "col": 1},{"row": 1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 1, "col": -1}], 0)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 1)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": -1, "col": 0}], 1)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze5 = [row0, row1, row2]
    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 5")
    goal = aliceBFS(alice_maze5, {"row": 0, "col": 0}, discovered)

    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 6
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":0, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}], 0)
    row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": 1},{"row": -1, "col": 1}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_1_3 = Node({"row": 1, "col": 3}, [], 0, False, True)
    row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_2_3 = Node({"row": 2, "col": 3}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2, node_2_3]


    node_3_0 = Node({"row": 3, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_3_1 = Node({"row": 3, "col": 1}, [{"row": 0, "col": -1}, {"row": 0, "col": 1}], 0)
    node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0)
    row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    alice_maze6 = [row0, row1, row2, row3]
    row, col = 4, 4
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 6")
    goal = aliceBFS(alice_maze6, {"row": 0, "col": 0}, discovered)

    
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # maze 7
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":0, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}], 0)
    row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 0, "col": -1},{"row": 1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_1_3 = Node({"row": 1, "col": 3}, [], 0, False, True)
    row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_2_3 = Node({"row": 2, "col": 3}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2, node_2_3]

    node_3_0 = Node({"row": 3, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_3_1 = Node({"row": 3, "col": 1}, [{"row": 0, "col": -1}, {"row": 0, "col": 1}], 0)
    node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0)
    row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    alice_maze7 = [row0, row1, row2, row3]
    row, col = 4, 4
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 7")
    goal = aliceBFS(alice_maze7, {"row": 0, "col": 0}, discovered)

    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 8
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":0, "col":1}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}], 0)
    row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 0, "col": 1}], 1)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_1_3 = Node({"row": 1, "col": 3}, [], 0, False, True)
    row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 0)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_2_3 = Node({"row": 2, "col": 3}, [{"row": -1, "col": 0}], 0)
    row2 = [node_2_0, node_2_1, node_2_2, node_2_3]


    node_3_0 = Node({"row": 3, "col": 0}, [{"row": -1, "col": 0}], 0)
    node_3_1 = Node({"row": 3, "col": 1}, [{"row": 0, "col": -1}, {"row": 0, "col": 1}], 0)
    node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], 0)
    node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0)
    row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    alice_maze8 = [row0, row1, row2, row3]
    row, col = 4, 4
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 8\n")
    goal = aliceBFS(alice_maze8, {"row": 0, "col": 0}, discovered)

    
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")

    print('\n')

    # # MAZE 9
    # d=1
    # goal_found = False
    # node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":0, "col":1}], 0, True, False)
    # node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}], 1)
    # node_0_2 = Node({"row": 0, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}], 0)
    # row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    # node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    # node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": 1},{"row": 1, "col": 0}], 0)
    # node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_1_3 = Node({"row": 1, "col": 3}, [], 0, False, True)
    # row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    # node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 0)
    # node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], -1)
    # node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_2_3 = Node({"row": 2, "col": 3}, [{"row": -1, "col": 0}], 0)
    # row2 = [node_2_0, node_2_1, node_2_2, node_2_3]

    # node_3_0 = Node({"row": 3, "col": 0}, [{"row": -1, "col": 0}], 0)
    # node_3_1 = Node({"row": 3, "col": 1}, [{"row": 0, "col": 1}], 1)
    # node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0)
    # row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    # alice_maze9 = [row0, row1, row2, row3]
    # row, col = 4, 4
    # discovered = [[False for x in range(row)] for y in range(col)] 

    # print("solve alice maze 9")
    # goal = aliceBFS(alice_maze9, {"row": 0, "col": 0}, discovered)

    
    # if goal:
    #     print("The shortest path is ", end='')
    #     length = printPath(goal) - 1
    #     print("The shortest path length is", length)
    # else:
    #     print("Destination is not found")

    # print('\n')

    # # MAZE 10
    # d=1
    # goal_found = False
    # node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":1, "col":1}], 0, True, False)
    # node_0_1 = Node({"row": 0, "col": 1}, [], 0)
    # node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}, {"row": 0, "col": -1}], -1)
    # row0 = [node_0_0, node_0_1, node_0_2]

    # node_1_0 = Node({"row": 1, "col": 0}, [{"row": -1, "col": 0}], 0)
    # node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": 1},{"row": 1, "col": -1},{"row": 1, "col": 0}], 0)
    # node_1_2 = Node({"row": 1, "col": 2}, [{"row": +1, "col": -1}], 0)
    # row1 = [node_1_0, node_1_1, node_1_2]

    # node_2_0 = Node({"row": 2, "col": 0}, [{"row": -1, "col": 0}, {"row": 0, "col": 1}], 0)
    # node_2_1 = Node({"row": 2, "col": 1}, [{"row": 0, "col": 1}], 0)
    # node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 1)
    # row2 = [node_2_0, node_2_1, node_2_2]

    # alice_maze10 = [row0, row1, row2]
    # row, col = 3, 3
    # discovered = [[False for x in range(row)] for y in range(col)] 

    # print("solve alice maze 10")
    # goal = aliceBFS(alice_maze10, {"row": 0, "col": 0}, discovered)

    
    # if goal:
    #     print("The shortest path is ", end='')
    #     length = printPath(goal) - 1
    #     print("The shortest path length is", length)
    # else:
    #     print("Destination is not found")


    # print('\n')

    # # MAZE 11
    # d=1
    # goal_found = False
    # node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":1, "col":1}], 0, True, False)
    # node_0_1 = Node({"row": 0, "col": 1}, [], 0)
    # node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": -1}, {"row": 0, "col": -1}], -1)
    # row0 = [node_0_0, node_0_1, node_0_2]

    # node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    # node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": -1},{"row": 1, "col": 1},{"row": 1, "col": 0}], 0)
    # node_1_2 = Node({"row": 1, "col": 2}, [{"row": 1, "col": -1}], 0)
    # row1 = [node_1_0, node_1_1, node_1_2]

    # node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 1)
    # node_2_1 = Node({"row": 2, "col": 1}, [{"row": -1, "col": 0}], 1)
    # node_2_2 = Node({"row": 2, "col": 2}, [{"row": -1, "col": 0}], 0)
    # row2 = [node_2_0, node_2_1, node_2_2]

    # alice_maze11 = [row0, row1, row2]
    # row, col = 3, 3
    # discovered = [[False for x in range(row)] for y in range(col)] 

    # print("solve alice maze 11")
    # goal = aliceBFS(alice_maze11, {"row": 0, "col": 0}, discovered)

    
    # if goal:
    #     print("The shortest path is ", end='')
    #     length = printPath(goal) - 1
    #     print("The shortest path length is", length)
    # else:
    #     print("Destination is not found")

    # print('\n')

    # # MAZE 12
    # d=1
    # goal_found = False
    # node_0_0 = Node({"row": 0, "col": 0}, [{"row": 1, "col": 0},{"row":0, "col":1}], 0, True, False)
    # node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}], 1)
    # node_0_2 = Node({"row": 0, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}], 0)
    # row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    # node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 0)
    # node_1_1 = Node({"row": 1, "col": 1}, [{"row": 1, "col": 1},{"row": 1, "col": 0}], 0)
    # node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_1_3 = Node({"row": 1, "col": 3}, [], 0)
    # row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    # node_2_0 = Node({"row": 2, "col": 0}, [{"row": 0, "col": 1}], 0)
    # node_2_1 = Node({"row": 2, "col": 1}, [{"row": 1, "col": 0}], -1)
    # node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_2_3 = Node({"row": 2, "col": 3}, [{"row": -1, "col": 0}], 0)
    # row2 = [node_2_0, node_2_1, node_2_2, node_2_3]

    # node_3_0 = Node({"row": 3, "col": 0}, [{"row": -1, "col": 0}], 0)
    # node_3_1 = Node({"row": 3, "col": 1}, [{"row": 0, "col": 1}], 1)
    # node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], 0)
    # node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0)
    # row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    # alice_maze12 = [row0, row1, row2, row3]
    # row, col = 4, 4
    # discovered = [[False for x in range(row)] for y in range(col)] 

    # print("solve alice maze 12")
    # goal = aliceBFS(alice_maze12, {"row": 0, "col": 0}, discovered)

    
    # if goal:
    #     print("The shortest path is ", end='')
    #     length = printPath(goal) - 1
    #     print("The shortest path length is", length)
    # else:
    #     print("Destination is not found")

    # print('\n')

# MAZE 13
    d=1
    goal_found = False
    node_0_0 = Node({"row": 0, "col": 0}, [{"row":0, "col":1}], 0)
    node_0_1 = Node({"row": 0, "col": 1}, [{"row": 1, "col": 0}, {"row": 0, "col": -1}, {"row": 0, "col": 1}], 0)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": 1, "col": 0}], -1)
    node_0_3 = Node({"row": 0, "col": 3}, [{"row": 1, "col": -1}, {"row": 1, "col": 0}, {"row": 0, "col": -1}], 0)
    row0 = [node_0_0, node_0_1, node_0_2, node_0_3]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": 1, "col": 0}], 1)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": 0, "col": -1},{"row": 1, "col": 0}], 0)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": 0, "col": 1}, {"row": 0, "col": -1}], 0)
    node_1_3 = Node({"row": 1, "col": 3}, [{"row": -1, "col": 0}, {"row": 1, "col": 0}], 0)
    row1 = [node_1_0, node_1_1, node_1_2, node_1_3]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": -1, "col": 0}], -1)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": 0, "col": 1}], 0)
    node_2_2 = Node({"row": 2, "col": 2}, [], 0, False, True)
    node_2_3 = Node({"row": 2, "col": 3}, [{"row": 0, "col": -1}], 1)
    row2 = [node_2_0, node_2_1, node_2_2, node_2_3]

    node_3_0 = Node({"row": 3, "col": 0}, [{"row": 0, "col": 1}], 0)
    node_3_1 = Node({"row": 3, "col": 1}, [{"row": -1, "col": 0}], 1)
    node_3_2 = Node({"row": 3, "col": 2}, [{"row": 0, "col": 1}], -1)
    node_3_3 = Node({"row": 3, "col": 3}, [{"row": -1, "col": 0}], 0, True, False)
    row3 = [node_3_0, node_3_1, node_3_2, node_3_3]
    

    alice_maze13 = [row0, row1, row2, row3]
    row, col = 4, 4
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 13")
    goal = aliceBFS(alice_maze13, {"row": 3, "col": 3}, discovered)

    
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("The shortest path length is", length)
    else:
        print("Destination is not found")
