#Name: Sushant Chaudhari
#Source: A* algorithm from wikipedia
"""This program sets up and displays a puzzle based on the game
   Ricochet Robots. The student should replace the solve() method
   with code to compute a solution to the puzzle."""

# ---------- The following code should be adapted by the student ----------

path_to_file_containing_puzzle = "E:/AI assignment/Assignment_2/ricochet_py/test"
    
def solve():
    """This method should compute and return the solution, as a list
    of (row, column) tuples, zero-based. What it currently does is
    just provide a hand-crafted solution.
    """
    rnum = number_of_rows
    cnum = number_of_columns
    l1 = block_locations
    r1 = ball_location
    g1 = goal_location
    path = []

    closedset = [] #The set of nodes already evaluated.
    current = r1
    openset = {}
    openset[r1] = abs(g1[0] - current[0]) + abs(g1[1] - current[1]) #Initially, only the start node is known.
    print(openset)

    camefrom = {} #The most effiecient previous step

    gscore = {}
    gscore[current] = 0
    fscore = {}
    fscore[current] = abs(g1[0] - current[0]) + abs(g1[1] - current[1])
    
    while( current != g1):
        #loop begins
        n1 = {}
        #del openset[current]
        if current in openset:
            del openset[current]
        #add current to closedset
        closedset.append(current)
        #Calculate all fronitier nodes
        #calculate left frontier node
        #check for blockage
        blockage_found = 0
        left_flag = 0
        l1.sort(key=lambda tup: tup[1])
        for i in l1:
            if(i[0] == current[0] and i[1] < current[1]):
                left_node = (current[0],i[1]+1)
                blockage_found = 1
                #print("Blockage found")
        if(blockage_found == 0):
            left_node = (current[0],0)
        #print("left node is ",left_node)
        if(left_node == current):
            left_flag = 1
        for i in closedset:
            if(i[0] == current[0] and i[1] < current[1]):
                left_flag = 1
        if(left_flag == 0):
            n1[left_node] = 0
        if(left_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate right frontier node
        #check for blockage
        blockage_found = 0
        right_flag = 0
        l1.sort(key=lambda tup: tup[1], reverse= True)
        for i in l1:
            if(i[0] == current[0] and i[1] > current[1]):
                right_node = (current[0],i[1]-1)
                blockage_found = 1
        if(blockage_found == 0):
            right_node = (current[0],cnum-1)
        #print(right_node)
        if(right_node == current):
            right_flag = 1
        for i in closedset:
            if(i[0] == current[0] and i[0] > current[0]):
                right_flag = 1
        if(right_flag == 0):
            n1[right_node] = 0
        if(right_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate upper frontier node
        #check for blockage
        blockage_found = 0
        upper_flag = 0
        l1.sort(key=lambda tup: tup[0])
        for i in l1:
            if(i[1] == current[1] and i[0] < current[0]):
                upper_node = (i[0]+1,current[1])
                blockage_found = 1 
        if(blockage_found == 0):
            upper_node = (0,current[1])
        #print(upper_node)
        if(upper_node == current):
            upper_flag = 1
        for i in closedset:
            if(i[1] == current[1] and i[0] < current[0]):
                upper_flag = 1
        if(upper_flag == 0):
            n1[upper_node] = 0
        if(upper_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        #calculate lower frontier node
        #check for blockage
        blockage_found = 0
        lower_flag = 0
        l1.sort(key=lambda tup: tup[0], reverse = True)
        for i in l1:
            if(i[1] == current[1] and i[0] > current[0]):
                lower_node = (i[0]-1,current[1])
                blockage_found = 1 
        if(blockage_found == 0):
            lower_node = (rnum-1,current[1])      
        for i in closedset:
            if(i[1] == current[1] and i[0] > current[0]):
                lower_flag = 1
        if(lower_node == current):
            lower_flag = 1
        if(lower_flag == 0):
            n1[lower_node] = 0
        if(lower_node == g1):
            current = g1
            path.append(current)
            #print("solution found")
            #print(path)
            continue
        
        delete = 0
        for i in n1:
            if i in closedset:
                #print("Do not consider",i)
                delete = i
                continue
            tent_gscore = gscore[current] + (abs(i[0] - current[0]) + abs(i[1] - current[1]))
            #print(tent_gscore)
            gscore[i] = tent_gscore
            n1[i] = gscore[i] + (abs(i[0] - g1[0]) + abs (i[1] - g1[1]))
            if i not in openset:
                openset[i] = gscore[i] + (abs(i[0] - g1[0]) + abs (i[1] - g1[1]))
                #print("openset is:",openset)
            elif(tent_gscore >= gscore[i]):
                continue
            camefrom[i] = current
            gscore[i] = tent_gscore
            fscore[i] = gscore[i] + (abs(i[0] - g1[0]) + abs(i[1] - g1[1])) 
        if delete in n1:
            del n1[delete]
        if not n1:
            current = min(openset, key=openset.get)
            path = []
        else:
            current = min(n1, key=n1.get) 
        path.append(current)
            
    return(path)

# -------------------------------------------------------------------------
# ----- The following code provides the GUI and should not be altered -----
    
def setup():
    """This method is called automatically once, when program starts.
    """
    global game
    size(300, 300) # arguments _must_ be literal integers, not variables!!!
    read_puzzle(path_to_file_containing_puzzle)
    game = Ricochet(number_of_rows, number_of_columns)
    game.place_blocks(block_locations)
    game.place_ball(ball_location)
    game.place_goal(goal_location)
    solution = solve()
    game.set_path(solution)
    
def draw():
    """This method is called automatically 60 times a second.
    Its job is to draw everything.
    """
    background(255)
    game.draw_grid(game.rows, game.columns)
    game.draw_blocks()
    game.draw_goal()
    game.draw_ball()
    game.move_ball()

def read_puzzle(file_path):
    """Read in a ricochet puzzle, putting results in global variables.
    Values must be one per line, in the given order. Comments,
    indicated with a # character, may occur after the value."""
    global number_of_rows, number_of_columns, block_locations
    global ball_location, goal_location
    file = open(file_path, "r")
    number_of_rows =    read_and_evaluate_line(file)
    number_of_columns = read_and_evaluate_line(file)
    block_locations =   read_and_evaluate_line(file)
    ball_location =     read_and_evaluate_line(file)
    goal_location =     read_and_evaluate_line(file)
    file.close()

def read_and_evaluate_line(file):
    line = file.readline()
    data = eliminate_comment(line)
    return eval(data)
    
def eliminate_comment(line):
    """Removes the # character (if there is one) and everything after it."""
    hash_at = line.find("#")
    if hash_at >= 0:
        return line[:hash_at]
    else:
        return line
class Ricochet:
    """This defines the display for the game. To use this display,
    create a "ricochet object" with
        game = ricochet(number of rows, number of columns)
    then call any or all of the methods
      * game.place_ball(row, column)
      * game.place_goal(row, column)
      * game.place_blocks( a list of (row, column) tuples )
      * game.set_path( a list of (row, column) tuples )
    """    
    
    def __init__(self, number_of_rows, number_of_columns):
        """This method is automatically called when you say
            game = ricochet(number of rows, number of columns)
        and should never be called explicitly. It contains a
        few constants you may wish to modify.
        """
        self.cell_size = min(width // (number_of_columns + 2),
                             height // (number_of_rows + 2))
        self.x = self.cell_size           # position of left edge of grid
        self.y = self.cell_size           # position of top edge of grid
        self.rows = number_of_rows
        self.columns = number_of_columns
        self.block_locations = []         # to be filled in
        self.path = []                    # to be filled in
        self.ball_x_y_position = (-1, -1) # to be replaced
        self.goal_location = -1           # leave alone!
        self.initial_delay = 60           # delay before ball starts to move
        ellipseMode(CORNER)
        strokeCap(ROUND)
    
    def place_ball(self, location):
        """Specifies the initial location of the red ball."""
        self.ball_x_y_position = self.row_column_to_x_y(location)
        
    def place_goal(self, location):
        """Specifies the location of the goal cell (green X)."""
        self.goal_location = location
        
    def place_blocks(self, locations):
        """Given any number of (row, column) tuples, place blocks at
           those locations. Previous blocks, if any, are forgotten.
           """
        self.block_locations = list(locations)
        
    def set_path(self, locations):
        """Given a list of (row, column) tuples, define a path
        for the red ball to follow, starting from where it has been
        placed initially. The ball will move to each location in
        turn.
        This method does NOT test whether the path is legal; it
        will simply move the ball where it is told to.
        """
        self.path = list(locations)
        self.path_index = -1 # used to keep track of red ball moves
        
    def move_ball(self):
        """Given a list of (row, column) tuples, define a path
        for the red ball to follow, starting from its current
        location. The ball will move to each location in turn.
        
        This method does NOT test whether the path is legal; it
        will simply move the ball where it is told to, even
        diagonally, through blocks, or off the screen.
        """
        if self.initial_delay > 0:
            self.initial_delay -= 1
            return # Pause before ball starts to move
        if self.path_index == -1 :
            self.path_index = 0
            return # Just starting the path
        if self.path_index >= len(self.path):
            noLoop()
            return # reached end of path
        elif self.ball_x_y_position == \
             self.row_column_to_x_y(self.path[self.path_index]):
            self.path_index += 1
            return # reached one location, ready to move to next location
        else:
            self.move_ball_toward(self.path[self.path_index])
            return # moved slightly closer to next desired location
                        
    def draw_grid(self, rows, columns):
        """Draw a rows x columns grid starting at (x, y)."""
        size = self.cell_size
        x = size
        y = size
        stroke(0)
        strokeWeight(1)
        if rows > 0:
            h_length = size * columns
            v_length = size * rows
            for i in range (0, rows + 1):
                line(x, y + i * size, x + h_length, y + i * size)
            for i in range (0, columns + 1):
                line(x + i * size, y, x + i * size, y + v_length)
        
    def draw_blocks(self):
        """Draws a black square at every location in block_locations."""
        fill(0)
        for location in self.block_locations:
            (x, y) = self.row_column_to_x_y(location)
            rect(x, y, self.cell_size, self.cell_size)
           
    def draw_ball(self):
        """Draws the red ball at the position indicated by
        ball_x_y_position, which is not necessarily exactly
        within a single cell.
        """
        fill(255, 0, 0)
        noStroke()
        (x, y) = self.ball_x_y_position
        ellipse(x + 2, y + 2, self.cell_size - 3, self.cell_size - 3)
        
    def draw_goal(self):
        """Draws a green X at goal_location."""
        stroke(0, 255, 0)
        strokeWeight(2)
        (x, y) = self.row_column_to_x_y(self.goal_location)
        line(x, y, x + self.cell_size, y + self.cell_size)
        line(x, y + self.cell_size, x + self.cell_size, y)
        
    def move_ball_toward(self, new_location):
        """Adjust the current (x, y) position of the red ball to be
        slightly closer to the new location, given as (row, column)."""
        (old_x, old_y) = self.ball_x_y_position
        (new_x, new_y) = self.row_column_to_x_y(new_location)
        self.ball_x_y_position = (self.toward(old_x, new_x),
                                  self.toward(old_y, new_y))
        
    def toward(self, frum, to): # "from" is a reserved word
        """Return one of the values frum-1, frum, or frum+1,
        whichever is closer to 'to'."""
        if frum < to: return frum + 1
        elif frum > to: return frum - 1
        else: return frum
    
    def row_column_to_x_y(self, location):
        """Convert a (row, column) tuple to the (x, y) coordinates of
        the top left corner of the cell at that location."""
        (row, column) = location
        return (self.x + column * self.cell_size, self.y + row * self.cell_size)