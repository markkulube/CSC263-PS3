print("************Hello World, I Solve Alice Mazes************\n")

d=1
goal_found = False

class Node:
    def __init__(self, loc, moves, d_change,  start, goal):
        self.loc = loc
        self.moves = moves
        self.d_change = d_change
        self.start = start
        self.goal = goal
        self.parent = None
    
    def __repr__(self):
        return str((self.loc["row"], self.loc["col"]))


    def d_update(self, d):
        d += self.d_change

def aliceBFS(alice_maze, start, discovered):

    # queue use to do BFS
    queue = []

    # mark source cell as discovered
    discovered[start["row"]][start["col"]] = True

    # push source vertex in queue
    queue.append(alice_maze[start["row"]][start["col"]])

    # loop till queue is empty
    while(len(queue) != 0 and not goal_found):

        # pop from front of queue and print it
        cell_parent = queue.pop(0)
        print("loc: " + str(cell_parent.loc)) # DELETE

        # check if it's the goal
        if(cell_parent.goal):
            print("Goal Found\n")
            return cell_parent

        # update d
        print("d before: " + str(d))
        cell_parent.d_update(d)
        print("d after: " + str(d))
        
        # do for every move (x1,y1) -> (x2, y2)
        for move in cell_parent.moves:
            print(move)

            # get coord of next loc
            next_row = cell_parent.loc["row"] + move["row"]
            next_col = cell_parent.loc["col"] + move["col"]

            if(not discovered[next_row][next_col]):

                # mark cell discovered and push it in to the queue
                discovered[next_row][next_col] = True
                cell_child = alice_maze[next_row][next_col]
                cell_child.parent = cell_parent
                queue.append(cell_child)

        print('\n') # DELETE

    # print("goal not found")
    return None

# Utility function to print path from source to destination
def printPath(goal):
    if goal is None:
        return 0
 
    length = printPath(goal.parent)
    print(goal, end=' ')
    return length + 1

if __name__ == '__main__':
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": d, "col": 0},{"row": 0, "col": d},{"row":d, "col":d}], 0, True, False)
    node_0_0 = Node({"row": 0, "col": 0}, [{"row": d, "col": 0},{"row": 0, "col": d},{"row":d, "col":d}], 0, True, False)
    node_0_1 = Node({"row": 0, "col": 1}, [], 0, False, True)
    node_0_2 = Node({"row": 0, "col": 2}, [{"row": d, "col": -d}], -1, True, False)
    row0 = [node_0_0, node_0_1, node_0_2]

    node_1_0 = Node({"row": 1, "col": 0}, [{"row": -d, "col": d}], 0, True, False)
    node_1_1 = Node({"row": 1, "col": 1}, [{"row": -d, "col": 0}], 0, True, False)
    node_1_2 = Node({"row": 1, "col": 2}, [{"row": +d, "col": -d}], 0, True, False)
    row1 = [node_1_0, node_1_1, node_1_2]

    node_2_0 = Node({"row": 2, "col": 0}, [{"row": -d, "col": 0}, {"row": 0, "col": d}], 0, True, False)
    node_2_1 = Node({"row": 2, "col": 1}, [{"row": d, "col": 0}], 0, True, False)
    node_2_2 = Node({"row": 2, "col": 2}, [{"row": 0, "col": -d}], 0, True, False)
    row2 = [node_2_0, node_2_1, node_2_2]

    alice_maze1 = [row0, row1, row2]

    row, col = 3, 3
    discovered = [[False for x in range(row)] for y in range(col)] 

    print("solve alice maze 1\n")
    goal = aliceBFS(alice_maze1, {"row": 0, "col": 0}, discovered)

    
    if goal:
        print("The shortest path is ", end='')
        length = printPath(goal) - 1
        print("\nThe shortest path length is", length)
    else:
        print("Destination is not found")