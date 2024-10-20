class RubiksCube:
    def __init__(self):
        # Define the color structure for each face
        self.colors = {
            "Top": "⬜",
            "Bottom": "🟨",
            "Left": "🟩",
            "Right": "🟦",
            "Front": "🟥",
            "Back": "🟧"
        }
        
        # Create a 3D array to represent the cube
        # Each face should be 3x3 and have the same color arrangement (white-yellow, green-blue, red-orange)
        self.cube = {
            "Front": [[self.colors["Front"]] * 3 for _ in range(3)],
            "Right": [[self.colors["Right"]] * 3 for _ in range(3)],
            "Back": [[self.colors["Back"]] * 3 for _ in range(3)],
            "Left": [[self.colors["Left"]] * 3 for _ in range(3)],
            "Top": [[self.colors["Top"]] * 3 for _ in range(3)],
            "Bottom": [[self.colors["Bottom"]] * 3 for _ in range(3)]
        }

    def display(self):
        # Display the cube's current state
        for face in self.cube:
            print(f"{face} Face:")
            # Display current face/side
            for row in self.cube[face]:
                print(" ".join(row))
            print()

    # Reset all sides to normal
    def reset(self):
        self.cube = {
            "Front": [[self.colors["Front"]] * 3 for _ in range(3)],
            "Right": [[self.colors["Right"]] * 3 for _ in range(3)],
            "Back": [[self.colors["Back"]] * 3 for _ in range(3)],
            "Left": [[self.colors["Left"]] * 3 for _ in range(3)],
            "Top": [[self.colors["Top"]] * 3 for _ in range(3)],
            "Bottom": [[self.colors["Bottom"]] * 3 for _ in range(3)]
        }


#-----------------------------------------------------Rotating Methods------------------------------------------------
#---------------------------------------------------Front Face Rotations------------------------------------------------
    # Method 1: Rotate the top row of the front face
    def rotate_front_topRow(self, clockwise=True):
        # Save the top front row
        temp_row = [self.cube["Front"][0][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the top row to the right

                self.cube["Front"][0][i] = self.cube["Left"][0][i]
                self.cube["Left"][0][i] = self.cube["Back"][0][i]
                self.cube["Back"][0][i] = self.cube["Right"][0][i]
                self.cube["Right"][0][i] = temp_row[i]

            else: # Rotate the top row to the left instead
            
                self.cube["Front"][0][i] = self.cube["Right"][0][i]
                self.cube["Right"][0][i] = self.cube["Back"][0][i]
                self.cube["Back"][0][i] = self.cube["Left"][0][i]
                self.cube["Left"][0][i] = temp_row[i]

#-----------------------------------------------------------------------------------------------------------------------
    # Method 2: Rotate the middle row of the front face
    def rotate_front_middleRow(self, clockwise=True):
        # Save the middle front row
        temp_row = [self.cube["Front"][1][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the middle row to the right

                self.cube["Front"][1][i] = self.cube["Left"][1][i]
                self.cube["Left"][1][i] = self.cube["Back"][1][i]
                self.cube["Back"][1][i] = self.cube["Right"][1][i]
                self.cube["Right"][1][i] = temp_row[i]

            else: # Rotate the middle row to the left instead
            
                self.cube["Front"][1][i] = self.cube["Right"][1][i]
                self.cube["Right"][1][i] = self.cube["Back"][1][i]
                self.cube["Back"][1][i] = self.cube["Left"][1][i]
                self.cube["Left"][1][i] = temp_row[i]

#-----------------------------------------------------------------------------------------------------------------------
    # Method 3: Rotate the bottom row of the front face
    def rotate_front_bottomRow(self, clockwise=True):
        # Save the bottom front row
        temp_row = [self.cube["Front"][2][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the bottom row to the right

                self.cube["Front"][2][i] = self.cube["Left"][2][i]
                self.cube["Left"][2][i] = self.cube["Back"][2][i]
                self.cube["Back"][2][i] = self.cube["Right"][2][i]
                self.cube["Right"][2][i] = temp_row[i]

            else: # Rotate the bottom row to the left instead
            
                self.cube["Front"][2][i] = self.cube["Right"][2][i]
                self.cube["Right"][2][i] = self.cube["Back"][2][i]
                self.cube["Back"][2][i] = self.cube["Left"][2][i]
                self.cube["Left"][2][i] = temp_row[i]


#-----------------------------------------------------------------------------------------------------------------------
    # Method 4: Rotate the left column of the front face
    def rotate_front_leftColumn(self, clockwise=True):
        temp_col = [self.cube["Top"][i][0] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate front left column up
                self.cube["Top"][i][0] = self.cube["Front"][i][0]
                self.cube["Front"][i][0] = self.cube["Bottom"][i][0]
                self.cube["Bottom"][i][0] = self.cube["Back"][2 - i][2]
                self.cube["Back"][2 - i][2] = temp_col[i]
                
            else: # Rotate left column down
                self.cube["Top"][i][0] = self.cube["Back"][2 - i][2]
                self.cube["Back"][2 - i][2] = self.cube["Bottom"][i][0]
                self.cube["Bottom"][i][0] = self.cube["Front"][i][0]
                self.cube["Front"][i][0] = temp_col[i]
#-----------------------------------------------------------------------------------------------------------------------
    # Method 5: Rotate the middle column of the front face
    def rotate_front_middleColumn(self, clockwise=True):
        temp_col = [self.cube["Top"][i][1] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate front middle column up
                self.cube["Top"][i][1] = self.cube["Front"][i][1]
                self.cube["Front"][i][1] = self.cube["Bottom"][i][1]
                self.cube["Bottom"][i][1] = self.cube["Back"][2 - i][1]
                self.cube["Back"][2 - i][1] = temp_col[i]
                
            else: # Rotate front middle column down
                self.cube["Top"][i][1] = self.cube["Back"][2 - i][1]
                self.cube["Back"][2 - i][1] = self.cube["Bottom"][i][1]
                self.cube["Bottom"][i][1] = self.cube["Front"][i][1]
                self.cube["Front"][i][1] = temp_col[i]       

#-----------------------------------------------------------------------------------------------------------------------
    # Method 6: Rotate the right column of the front face
    def rotate_front_rightColumn(self, clockwise=True):
        temp_col = [self.cube["Top"][i][2] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate front left column up
                self.cube["Top"][i][2] = self.cube["Front"][i][2]
                self.cube["Front"][i][2] = self.cube["Bottom"][i][2]
                self.cube["Bottom"][i][2] = self.cube["Back"][2 - i][0]
                self.cube["Back"][2 - i][0] = temp_col[i]
                #self.cube["Left"][0][i] = self.cube["Bottom"][2-i][0]
                
            else: # Rotate left column down
                self.cube["Top"][i][2] = self.cube["Back"][2 - i][0]
                self.cube["Back"][2 - i][0] = self.cube["Bottom"][i][2]
                self.cube["Bottom"][i][2] = self.cube["Front"][i][2]
                self.cube["Front"][i][2] = temp_col[i]

#---------------------------------------------------Top Face Rotations------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
    # Method 7: Rotate the top row of the top face
    def rotate_top_topRow(self, clockwise=True):
        # Save the top row
        temp_row = [self.cube["Top"][0][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the top row to the right
                self.cube["Top"][0][i] = self.cube["Left"][i][0]
                self.cube["Left"][i][0] = self.cube["Bottom"][2][i]
                self.cube["Bottom"][2][i] = self.cube["Right"][i][2]
                self.cube["Right"][i][2] = temp_row[i]


            else: # Rotate the top row to the left instead
                self.cube["Top"][0][i] = self.cube["Right"][i][0]
                self.cube["Right"][i][0] = self.cube["Bottom"][2][i]
                self.cube["Bottom"][2][i] = self.cube["Left"][i][2]
                self.cube["Left"][i][2] = temp_row[i]

#-----------------------------------------------------------------------------------------------------------------------
    # Method 8: Rotate the middle row of the top face
    def rotate_top_middleRow(self, clockwise=True):
        # Save the top row
        temp_row = [self.cube["Top"][1][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the top row to the right
                self.cube["Top"][1][i] = self.cube["Left"][i][1]
                self.cube["Left"][i][1] = self.cube["Bottom"][1][i]
                self.cube["Bottom"][1][i] = self.cube["Right"][i][1]
                self.cube["Right"][i][1] = temp_row[i]


            else: # Rotate the top row to the left instead
                self.cube["Top"][1][i] = self.cube["Right"][i][1]
                self.cube["Right"][i][1] = self.cube["Bottom"][1][i]
                self.cube["Bottom"][1][i] = self.cube["Left"][i][1]
                self.cube["Left"][i][1] = temp_row[i]

#-----------------------------------------------------------------------------------------------------------------------
    # Method 9: Rotate the bottom row of the top face
    def rotate_top_bottomRow(self, clockwise=True):
        # Save the top row
        temp_row = [self.cube["Top"][2][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the top row to the right
                self.cube["Top"][2][i] = self.cube["Left"][i][2]
                self.cube["Left"][i][2] = self.cube["Bottom"][0][i]
                self.cube["Bottom"][0][i] = self.cube["Right"][i][0]
                self.cube["Right"][i][0] = temp_row[i]


            else: # Rotate the top row to the left instead
                self.cube["Top"][2][i] = self.cube["Right"][i][2]
                self.cube["Right"][i][2] = self.cube["Bottom"][0][i]
                self.cube["Bottom"][0][i] = self.cube["Left"][i][0]
                self.cube["Left"][i][0] = temp_row[i]

# Example of using the RubiksCube class
if __name__ == "__main__":
    cube = RubiksCube()
    print("Initial Cube State:")
    cube.display()

    # Rotate the top row
    print("1) After rotating the top row right:")
    cube.rotate_front_topRow()
    cube.display()

    print("\n--------------\n2) After rotating the middle row left:")
    cube.rotate_front_middleRow(clockwise=False)
    cube.display()

    print("\n--------------\n3) After rotating the bottom row right:")
    cube.rotate_front_bottomRow()
    cube.display() 

    cube.reset()

    print("\n--------------\n4) After rotating the left column up:")
    cube.rotate_front_leftColumn()
    cube.display()

    print("\n--------------\n5) After rotating the middle column down:")
    cube.rotate_front_middleColumn(clockwise=False)
    cube.display()

    print("\n--------------\n6) After rotating the right column up:")
    cube.rotate_front_rightColumn()
    cube.display()

    cube.reset()
    
    print("\n--------------\n7) After rotating the top row right:")
    cube.rotate_top_topRow()
    cube.display()

    print("\n--------------\n8) After rotating the middle row left:")
    cube.rotate_top_middleRow(clockwise=False)
    cube.display()

    print("\n--------------\n9) After rotating the bottom row right:")
    cube.rotate_top_bottomRow()
    cube.display()


# https://towardsdatascience.com/rubiks-cube-solver-96fa6c56fbe4 (understanding 3D array representation)
# https://medium.com/@ekollie324/how-to-build-a-rubiks-cube-in-python-c3bd19cbcd73 (understanding rotation logic)