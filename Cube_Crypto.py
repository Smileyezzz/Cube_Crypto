'''
The function name is the cubik notation
Reference : https://ruwix.com/the-rubiks-cube/notation/
'''
class Movement():
    # For x direction in world, it's z-axis in the computer.
    def x_direct_clockwise(array, layer):
        for x in range(0,3):
            for y in range(0,3):
                count = Check_position(x, y, layer)
                #The change of [center] after rotating
                if count == 2:
                    if layer == 1:
                        temp_1 = array[1][0][layer].position 
                        temp_2 = array[0][1][layer].position 
                        temp_3 = array[1][2][layer].position
                        temp_4 = array[2][1][layer].position
                        [temp_1, temp_2, temp_3, temp_4] = [temp_2, temp_3, temp_4, temp_1]
                        array[1][0][layer].position = temp_1
                        array[0][1][layer].position = temp_2
                        array[1][2][layer].position = temp_3
                        array[2][1][layer].position = temp_4
                #The change of [edge] after rotating
                if count == 1:
                    # Layer-1 is the middle layer, others are front & back layers
                    if layer == 1:
                        temp_1 = array[0][0][layer].position 
                        temp_2 = array[0][2][layer].position 
                        temp_3 = array[2][2][layer].position
                        temp_4 = array[2][0][layer].position
                        temp_1, temp_2, temp_3, temp_4 = temp_2, temp_3, temp_4, temp_1
                        array[0][0][layer].position = temp_1
                        array[0][2][layer].position = temp_2
                        array[2][2][layer].position = temp_3
                        array[2][0][layer].position = temp_4
                    else:
                        temp_1 = array[1][0][layer].position 
                        temp_2 = array[0][1][layer].position 
                        temp_3 = array[1][2][layer].position
                        temp_4 = array[2][1][layer].position
                        [temp_1, temp_2, temp_3, temp_4] = [temp_2, temp_3, temp_4, temp_1]
                        array[1][0][layer].position = temp_1
                        array[0][1][layer].position = temp_2
                        array[1][2][layer].position = temp_3
                        array[2][1][layer].position = temp_4
                #The change of [angle] after rotating
                if count == 0:
                    if layer != 1:
                        temp_1 = array[0][0][layer].position 
                        temp_2 = array[0][2][layer].position 
                        temp_3 = array[2][2][layer].position
                        temp_4 = array[2][0][layer].position
                        [temp_1, temp_2, temp_3, temp_4] = [temp_2, temp_3, temp_4, temp_1]
                        array[0][0][layer].position = temp_1
                        array[0][2][layer].position = temp_2
                        array[2][2][layer].position = temp_3
                        array[2][0][layer].position = temp_4
    
    # Function F_inverse is x-axis counter-clockwise rotation
    def x_direct_counter_clockwise(array, layer):
        for i in range(0,3):
            x_direct_clockwise(array, layer)

    # For the y direction in world, it's x-axis in the computer
    # Function R is y-axis clockwise rotation
    def y_direct_clockwise(array, layer):
        for y in range(0,3):
            for z in range(0,3):
                count == Check_position(layer, y, z)
                # The change of [center] after rotation
                if count == 2:
                    if layer == 1:
                        temp_1 = array[layer][0][1].position 
                        temp_2 = array[layer][1][0].position 
                        temp_3 = array[layer][2][1].position
                        temp_4 = array[layer][1][2].position
                        temp_1, temp_2, temp_3, temp_4 = temp_2, temp_3, temp_4, temp_1
                        array[layer][0][1].position = temp_1
                        array[layer][1][0].position = temp_2
                        array[layer][2][1].position = temp_3
                        array[layer][1][2].position = temp_4

                # The change of [edge] after rotation
                if count == 1:
                    if layer == 


    def y_direct_counter_clockwise(array, layer):

    # For the z direction in world, it's y-axis in the computer
    def z_direct_clockwise(array, layer):
    def z_direct_counter_clockwise(array, layer):

class Angle():
    def __init__(self, color, position, value, neighbor):
        '''
        color : [frontside_color, rightside_color, topside_color]
        position : [x, y, z]
        value : [frontside_value, rightside_value, topside_value]
        neighbor : [backdirection_neighbor, leftdirection_neighbor, downside_neighbor]
        '''
        self.color = color
        self.position = position
        self.value = value
        self.neighbor = neighbor

class Edge():
    def __init__(self, color, position, value, neighbor):
        '''
        color : [frontside_color, topside_color]
        position : [x, y, z]
        value : [frontside_value, topside_value]
        neighbor : [leftdirection_neighbor, backdirection_neighbor, rightdirection_neighbor, downside_neighbor]
        '''
        self.color = color
        self.position = position
        self.value = value
        self.neighbor = neighbor

class Center():
    def __init__(self, color, position, value, neighbor):
        '''
        color : [frontside_color]
        position : [x, y, z]
        value : [frontside_value]
        neighbor : [leftside_neighbor, topside_neighbor, rightside_neighbor, downside_neightbor]
        '''
        self.color = color
        self.position = position
        self.value = value
        self.neighbor = neighbor

class Origin():
    def __init__(self, descrpition):
        '''
        It's just for fun
        '''
        self.color = descrpition

class Cube():
    def __init__(self):
        size = 3
        magic_cube = []
        Create_3_dim_array(magic_cube, size)

#Define which block should be angle or center or edge, by it's position
def Check_position(x, y, z):
    count = 0
    if (x-1) == 0:
        count += 1
    if (y-1) == 0:
        count += 1
    if (z-1) == 0:
        count += 1
    return count

#Initialize the cube, and setting it's structure by Check_position()
def Initialize_the_cube(array, size):
    for i in range(0, size):
        for j in range(0, size):
            for k in range(0, size):
                count = Check_position(i, j, k)
                if count == 3:
                    array[i][j][k] = Origin("I'm origin")
                elif count == 2:
                    array[i][j][k] = Center('center', [i, j, k], None, None)
                elif count == 1:
                    array[i][j][k] = Edge('edge', [i, j, k], None, None)
                else:
                    array[i][j][k] = Angle('angle', [i, j, k], None, None)

#Simply create the 3 dim array (Cube)
def Create_3_dim_array(array, size):
    for i in range(0, size):
        array.append([])
        for j in range(0, size):
            array[i].append([])
            for k in range(0, size):
                array[i][j].append(None)


if __name__ == "__main__":
    #plaintext = input("kkk")
    magic_cube = []
    size = 3
    Create_3_dim_array(magic_cube, size)
    Initialize_the_cube(magic_cube, size)

    #Below is the testing
    for x in range(0,size):
        for y in range(0,size):
            for z in range(0,size):
                if (x==1) and (y==1) and (z==1):
                    print(magic_cube[x][y][z].color)
                    break
                print('memory[' + str(x) + '][' + str(y) + '][' + str(z) + ']=' + str(magic_cube[x][y][z].position))
                

    '''
    memory[0][1][2] = Edge([3,2],0,0,0)
    print(memory[0][1][2].color)
    '''
