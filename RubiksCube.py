"""Brandon Vo
   CS 4080
   Question 4: Rubik's Cube 
"""


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
        original_topFace = [self.cube["Top"][i][:] for i in range(3)] # Store temp top face
        for i in range(3):
            if clockwise: # Rotate the top row to the right

                self.cube["Front"][0][i] = self.cube["Left"][0][i]
                self.cube["Left"][0][i] = self.cube["Back"][0][i]
                self.cube["Back"][0][i] = self.cube["Right"][0][i]
                self.cube["Right"][0][i] = temp_row[i]

                # Rotate Top face
                self.cube["Top"][0][i] = original_topFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Top"][i][2] = original_topFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Top"][2][2-i] = original_topFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Top"][2-i][0] = original_topFace[0][i] #20 10 00 -> 00 01 02

            else: # Rotate the top row to the left instead
            
                self.cube["Front"][0][i] = self.cube["Right"][0][i]
                self.cube["Right"][0][i] = self.cube["Back"][0][i]
                self.cube["Back"][0][i] = self.cube["Left"][0][i]
                self.cube["Left"][0][i] = temp_row[i]

                # Rotate Top face
                self.cube["Top"][0][i] = original_topFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Top"][2-i][0] = original_topFace[2][i] #20 10 00 -> 22 21 20
                self.cube["Top"][2][i] = original_topFace[2-i][2] #22 21 20 -> 02 12 22
                self.cube["Top"][2-i][2] = original_topFace[0][i] #02 12 22 -> 00 01 02

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
        original_bottomFace = [self.cube["Bottom"][i][:] for i in range(3)] # Store temp top face
        for i in range(3):
            if clockwise: # Rotate the bottom row to the right

                self.cube["Front"][2][i] = self.cube["Left"][2][i]
                self.cube["Left"][2][i] = self.cube["Back"][2][i]
                self.cube["Back"][2][i] = self.cube["Right"][2][i]
                self.cube["Right"][2][i] = temp_row[i]

                # Rotate Bottom face
                self.cube["Bottom"][0][i] = original_bottomFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Bottom"][2-i][0] = original_bottomFace[2][2-i] #20 10 00 -> 22 21 20
                self.cube["Bottom"][2][2-i] = original_bottomFace[i][2] #22 21 20 -> 02 12 22
                self.cube["Bottom"][i][2] = original_bottomFace[0][i] #02 12 22 -> 00 01 02

            else: # Rotate the bottom row to the left instead
            
                self.cube["Front"][2][i] = self.cube["Right"][2][i]
                self.cube["Right"][2][i] = self.cube["Back"][2][i]
                self.cube["Back"][2][i] = self.cube["Left"][2][i]
                self.cube["Left"][2][i] = temp_row[i]

                # Rotate Bottom face
                self.cube["Bottom"][0][i] = original_bottomFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Bottom"][i][2] = original_bottomFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Bottom"][2][2-i] = original_bottomFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Bottom"][i][0] = original_bottomFace[0][i] #20 10 00 -> 00 01 02


#-----------------------------------------------------------------------------------------------------------------------
    # Method 4: Rotate the left column of the front face
    def rotate_front_leftColumn(self, clockwise=True):
        temp_col = [self.cube["Top"][i][0] for i in range(3)]
        original_leftFace = [self.cube["Left"][i][:] for i in range(3)] # Store temp left face
        for i in range(3):    
            if clockwise: # Rotate front left column up
                self.cube["Top"][i][0] = self.cube["Front"][i][0]
                self.cube["Front"][i][0] = self.cube["Bottom"][i][0]
                self.cube["Bottom"][i][0] = self.cube["Back"][2 - i][2] # Reverse the sides for back
                self.cube["Back"][2 - i][2] = temp_col[i]

                # Rotate left face
                self.cube["Left"][0][i] = original_leftFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Left"][i][2] = original_leftFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Left"][2][2-i] = original_leftFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Left"][2-i][0] = original_leftFace[0][i] #20 10 00 -> 00 01 02
                
            else: # Rotate left column down
                self.cube["Top"][i][0] = self.cube["Back"][2 - i][2]
                self.cube["Back"][2 - i][2] = self.cube["Bottom"][i][0] # Reverse the sides for back
                self.cube["Bottom"][i][0] = self.cube["Front"][i][0] 
                self.cube["Front"][i][0] = temp_col[i]

                # Rotate left face
                self.cube["Left"][0][i] = original_leftFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Left"][2-i][0] = original_leftFace[2][2-i] #20 10 00 -> 22 21 20
                self.cube["Left"][2][2-i] = original_leftFace[i][2] #22 21 20 -> 02 12 22
                self.cube["Left"][i][2] = original_leftFace[0][i] #02 12 22 -> 00 01 02
#-----------------------------------------------------------------------------------------------------------------------
    # Method 5: Rotate the middle column of the front face
    def rotate_front_middleColumn(self, clockwise=True):
        temp_col = [self.cube["Top"][i][1] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate front middle column up
                self.cube["Top"][i][1] = self.cube["Front"][i][1]
                self.cube["Front"][i][1] = self.cube["Bottom"][i][1]
                self.cube["Bottom"][i][1] = self.cube["Back"][2 - i][1] # Reverse the sides for back
                self.cube["Back"][2 - i][1] = temp_col[i]
                
            else: # Rotate front middle column down
                self.cube["Top"][i][1] = self.cube["Back"][2 - i][1]
                self.cube["Back"][2 - i][1] = self.cube["Bottom"][i][1] # Reverse the sides for back
                self.cube["Bottom"][i][1] = self.cube["Front"][i][1]
                self.cube["Front"][i][1] = temp_col[i]       

#-----------------------------------------------------------------------------------------------------------------------
    # Method 6: Rotate the right column of the front face
    def rotate_front_rightColumn(self, clockwise=True):
        original_rightFace = [self.cube["Right"][i][:] for i in range(3)] # Store temp right face
        temp_col = [self.cube["Top"][i][2] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate front right column up
                self.cube["Top"][i][2] = self.cube["Front"][i][2]
                self.cube["Front"][i][2] = self.cube["Bottom"][i][2]
                self.cube["Bottom"][i][2] = self.cube["Back"][2 - i][0] # Reverse the sides for back
                self.cube["Back"][2 - i][0] = temp_col[i]
                # Rotate right face
                self.cube["Right"][0][i] = original_rightFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Right"][2-i][0] = original_rightFace[2][2-i] #20 10 00 -> 22 21 20
                self.cube["Right"][2][2-i] = original_rightFace[i][2] #22 21 20 -> 02 12 22
                self.cube["Right"][i][2] = original_rightFace[0][i] #02 12 22 -> 00 01 02
                
            else: # Rotate right column down
                self.cube["Top"][i][2] = self.cube["Back"][2 - i][0] # Reverse the sides for back
                self.cube["Back"][2 - i][0] = self.cube["Bottom"][i][2]
                self.cube["Bottom"][i][2] = self.cube["Front"][i][2]
                self.cube["Front"][i][2] = temp_col[i]
                # Rotate right face
                self.cube["Right"][0][i] = original_rightFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Right"][i][2] = original_rightFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Right"][2][2-i] = original_rightFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Right"][2-i][0] = original_rightFace[0][i] #20 10 00 -> 00 01 02
                

#---------------------------------------------------Top Face Rotations------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
    # Method 7: Rotate the top row of the top face
    def rotate_top_topRow(self, clockwise=True):
        # Save the top row
        temp_row = [self.cube["Top"][0][i] for i in range(3)]
        original_backFace = [self.cube["Back"][i][:] for i in range(3)] # Store temp back face
        for i in range(3):
            if clockwise: # Rotate the top row to the right
                self.cube["Top"][0][i] = self.cube["Left"][2-i][0]
                self.cube["Left"][2-i][0] = self.cube["Bottom"][2][2-i]  # Inverse left face (vertical)
                self.cube["Bottom"][2][2-i] = self.cube["Right"][i][2] # Inverse bottom face (horizontal)
                self.cube["Right"][i][2] = temp_row[i] # Inverse right face (vertical)

                # Rotate Back face
                self.cube["Back"][0][i] = original_backFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Back"][i][2] = original_backFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Back"][2][2-i] = original_backFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Back"][2-i][0] = original_backFace[0][i] #20 10 00 -> 00 01 02

            else: # Rotate the top row to the left instead
                self.cube["Top"][0][i] = self.cube["Right"][i][2] 
                self.cube["Right"][i][2] = self.cube["Bottom"][2][2-i] # Inverse right face (vertical)
                self.cube["Bottom"][2][2-i] = self.cube["Left"][2-i][0] # Inverse bottom face (horizontal)
                self.cube["Left"][2-i][0] = temp_row[i] # Inverse left face (vertical)

                # Rotate Back Face
                self.cube["Back"][0][i] = original_backFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Back"][2-i][0] = original_backFace[2][i] #20 10 00 -> 22 21 20
                self.cube["Back"][2][i] = original_backFace[2-i][2] #22 21 20 -> 02 12 22
                self.cube["Back"][2-i][2] = original_backFace[0][i] #02 12 22 -> 00 01 02

#-----------------------------------------------------------------------------------------------------------------------
    # Method 8: Rotate the middle row of the top face
    def rotate_top_middleRow(self, clockwise=True):
        # Save the middle row
        temp_row = [self.cube["Top"][1][i] for i in range(3)]
        for i in range(3):
            if clockwise: # Rotate the middle row to the right
                self.cube["Top"][1][i] = self.cube["Left"][i][1]
                self.cube["Left"][i][1] = self.cube["Bottom"][1][i] # Inverse left face (vertical)
                self.cube["Bottom"][1][i] = self.cube["Right"][i][1]
                self.cube["Right"][i][1] = temp_row[i] # Inverse right face (vertical)


            else: # Rotate the middle row to the left instead
                self.cube["Top"][1][i] = self.cube["Right"][i][1]
                self.cube["Right"][i][1] = self.cube["Bottom"][1][i] # Inverse right face (vertical)
                self.cube["Bottom"][1][i] = self.cube["Left"][i][1]
                self.cube["Left"][i][1] = temp_row[i] # Inverse left face (vertical)

#-----------------------------------------------------------------------------------------------------------------------
    # Method 9: Rotate the bottom row of the top face
    def rotate_top_bottomRow(self, clockwise=True):
        # Save the top row
        temp_row = [self.cube["Top"][2][i] for i in range(3)]
        original_frontFace = [self.cube["Front"][i][:] for i in range(3)] # Store temp front face
        for i in range(3):
            if clockwise: # Rotate the bottom row to the right
                self.cube["Top"][2][i] = self.cube["Left"][2-i][2]
                self.cube["Left"][2-i][2] = self.cube["Bottom"][0][i] # Inverse left face (vertical)
                self.cube["Bottom"][0][i] = self.cube["Right"][2-i][0] # Inverse bottom face (horizontal)
                self.cube["Right"][2-i][0] = temp_row[i] # Inverse right face (vertical)

                # Rotate Front Face
                self.cube["Front"][0][i] = original_frontFace[2-i][0] #00 01 02 -> 20 10 00
                self.cube["Front"][2-i][0] = original_frontFace[2][2-i] #20 10 00 -> 22 21 20
                self.cube["Front"][2][2-i] = original_frontFace[i][2] #22 21 20 -> 02 12 22
                self.cube["Front"][i][2] = original_frontFace[0][i] #02 12 22 -> 00 01 02

            else: # Rotate the bottom row to the left instead
                self.cube["Top"][2][i] = self.cube["Right"][i][0]  
                self.cube["Right"][i][0] = self.cube["Bottom"][0][i] # Inverse right face (vertical)
                self.cube["Bottom"][0][i] = self.cube["Left"][i][2] # Inverse bottom face (horizontal)
                self.cube["Left"][i][2] = temp_row[i] # Inverse left face (vertical)

                # Rotate Front face
                self.cube["Front"][0][i] = original_frontFace[i][2] #00 01 02 -> 02 12 22
                self.cube["Front"][i][2] = original_frontFace[2][2-i] #02 12 22 -> 22 21 20
                self.cube["Front"][2][2-i] = original_frontFace[2-i][0] #22 21 20 -> 20 10 00
                self.cube["Front"][2-i][0] = original_frontFace[0][i] #20 10 00 -> 00 01 02

# Example of using the RubiksCube class
if __name__ == "__main__":
    cube = RubiksCube()
    print("Initial Cube State:")
    cube.display()


    print("1) After rotating the top row right:")
    cube.rotate_front_topRow()
    cube.display()

    print("\n--------------\n2) After rotating the left column down:")
    cube.rotate_front_leftColumn(clockwise=False)
    cube.display()
    
    print("\n--------------\n3) After rotating the top row right:")
    cube.rotate_top_topRow()
    cube.display()

# These references were used to help faciliate this program
# https://towardsdatascience.com/rubiks-cube-solver-96fa6c56fbe4 (understanding 3D array representation)
# https://medium.com/@ekollie324/how-to-build-a-rubiks-cube-in-python-c3bd19cbcd73 (understanding rotation logic)