import pygame

class DoublyLinkedStack:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        self.top = None
        self.bottom = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    def printstack(self):
        no = self.top
        temp = []
        while no is not None:
            temp.append(no.data)
            no = no.prev
            return temp
          
        return temp
    def peek(self):
        if self.is_empty():
            return None
        return self.top.data
        
    def push(self, data):
        new_node = self.Node(data, next=self.top)
        if self.is_empty():
            self.bottom = new_node
        else:
            self.top.prev = new_node
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next
        if self.top is not None:
            self.top.prev = None
        else:
            self.bottom = None
        self.size -= 1
        return data


class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = self.find_start()
        self.end = self.find_end()
        self.stack = DoublyLinkedStack()
        self.stack.push((self.start, [self.start]))
        
    def find_start(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == 'M':
                    return row, col
        return None

    def find_end(self):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                if self.maze[row][col] == 'E':
                    return row, col
        return None
    
    def is_valid_position(self, pos_r, pos_c):
        if pos_r < 0 or pos_c < 0:
            return False
        if pos_r >= len(self.maze) or pos_c >= len(self.maze[0]):
            return False
        if self.maze[pos_r][pos_c] in '.1':
            return False
        return True
    
    def print_maze(self):
        for row in self.maze:
            for item in row:
                print(item, end='')
            print()
                
    def exit_maze(self):

        while True:
            pos, path = self.stack.pop()
            pos_r, pos_c = pos
            if pos == self.find_end():
                print("Alcançou o objetivo")
                self.maze[pos_r][pos_c]="X"
                return maze
        
            if self.is_valid_position(pos_r + 1, pos_c):
                self.stack.push(((pos_r + 1, pos_c), path + [(pos_r + 1, pos_c)]))
            if self.is_valid_position(pos_r, pos_c - 1):
                self.stack.push(((pos_r, pos_c - 1), path + [(pos_r, pos_c - 1)]))
            if self.is_valid_position(pos_r - 1, pos_c):
                self.stack.push(((pos_r - 1, pos_c), path + [(pos_r - 1, pos_c)]))
            if self.is_valid_position(pos_r, pos_c + 1):
                self.stack.push(((pos_r, pos_c + 1), path + [(pos_r, pos_c + 1)]))    
            self.maze[pos_r][pos_c] = '.'

# Maze class with MazeSolver as a member

class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.solver = MazeSolver(maze)

    def display(self):
        # initialize pygame
        pygame.init()

        # Set the width and height of the screen (width, height).
        screen = pygame.display.set_mode((800, 600))
        screen2 = pygame.display.set_mode((800, 600))

        # Set the title of the window
        pygame.display.set_caption("Maze Visualization")

        # Set the color of the walls to black
        wall_color = (0, 0, 0)

        # Set the color of the path to white
        path_color = (255, 255, 255)
        start_color = (0, 255, 0)
        end_color = (255, 0, 0)
        Finished = (255, 255, 61)
        # Set the color of the path taken to gray
        path_taken_color = (128, 128, 128)
        # Run the main loop for the visualization
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen
            screen.fill((255, 255, 255))
            screen2.fill((255, 255, 255))
            # Draw the maze
            for row in range(len(self.maze)):
                for col in range(len(self.maze[0])):
                    if self.maze[row][col] == 'M':
                        pygame.draw.rect(screen2, start_color, [col * 20, row * 20, 20, 20])
                    elif self.maze[row][col] == '1':
                        pygame.draw.rect(screen2, wall_color, [col * 20, row * 20, 20, 20])
                    elif self.maze[row][col] == 'E':
                        pygame.draw.rect(screen2, end_color, [col * 20, row * 20, 20, 20])
                    else:
                        pygame.draw.rect(screen2, path_color, [col * 20, row * 20, 20, 20])
                    self.solver.print_maze()
            pygame.image.save(screen2, "maze.png")

            # Draw the path taken
            teste = self.solver.exit_maze()
            for row in range(len(teste)):
                for col in range(len(teste[0])):
                    if teste[row][col] == '.':
                        pygame.draw.rect(screen, path_taken_color, [col * 20, row * 20, 20, 20])
                    elif teste[row][col] == 'X':
                        pygame.draw.rect(screen, Finished, [col * 20, row * 20, 20, 20])
                pygame.image.save(screen, "screenshot.png")
            # Update the screen
        
            pygame.display.flip()

        # Quit pygame
        pygame.quit()        



    

maze = [
    	['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 'M', '1'],
        ['1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
        ['1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0', '1', '1', '0', '1', '1', '1', '0', '1'],
        ['E', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '1', '0', '1'],
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
    ]


mase = Maze(maze)
mase.display()

