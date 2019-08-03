# Unit is one small square in surface, one surface has 9 units
class Unit():
    def __init__(self, color, value):
        self.color = color
        self.value = value

# There are several rotating functions in this class, which is the official activation in mini cube
# Reference : https://ruwix.com/the-rubiks-cube/notation/
class Rotation():
    def l_shift(a, b, c, d):
        a, b, c, d = b, c, d, a
        return a, b, c, d

    def r_shift(a, b, c, d):
        a, b, c, d = d, a, b, c
        return a, b, c, d

    def F(cube):
        l_shift(cube[0][2][1], cube[4][1][0], cube[2][0][1], cube[5][1][2])
        cube[0][2][:], cube[4][:][0], cube[2][0][:], cube[5][:][2] = cube[4][:][0], cube[2][0][:], cube[5][:][2], cube[0][2][:]
        return 

    def F_inverse(cube):
        return 
    
    def R(cube):
        cube[1][2][:], cube[4][2][:], cube[3][0][:], cube[5][2][:] = cube[4][2][:], cube[3][0][:], cube[5][2][:], cube[1][2][:]
        return 

    def R_inverse(cube):
        return 

    def L(cube):
        cube[1][0][:], cube[5][0][:], cube[3][2][:], cube[4][0][:] = cube[4][0][:], cube[1][0][:], cube[3][2][:], cube[1][0][:]
        return 

    def L_inverse(cube):
        return 

    def U(cube):
        cube[0][:][2], cube[1][:][2], cube[2][:][2], cube[3][:][2] = cube[1][:][2], cube[2][:][2], cube[3][:][2], cube[0][:][2]
        return 

    def U_inverse(cube):
        return 
    
    def B(cube):
        cube[0][0][:], cube[5][:][0], cube[2][2][:], cube[4][:][2] = cube[4][:][2], cube[0][0][:], cube[5][:][0], cube[2][2][:]
        return 

    def B_inverse(cube):
        return 

    def D(cube):
        cube[0][:][0], cube[1][:][0], cube[2][:][0], cube[3][:][0] = cube[3][:][0], cube[0][:][0], cube[1][:][0], cube[2][:][0]
        return 
    
    def D_inverse(cube):
        return 

    def M(cube):
        cube[1][1][:], cube[4][1][:], cube[3][1][:], cube[5][1][:] = cube[4][1][:], cube[3][1][:], cube[5][1][:], cube[1][1][:]
        return 
    
    def M_inverse(cube):
        return 

    def E(cube):
        cube[0][:][1], cube[1][:][1], cube[2][:][1], cube[3][:][1] = cube[3][:][1], cube[0][:][1], cube[1][:][1], cube[2][:][1]
        return 

    def E_inverse(cube):
        return 

    def S(cube):
        cube[0][1][:], cube[4][:][1], cube[2][1][:], cube[5][:][1] = cube[5][:][1], cube[0][1][:], cube[4][:][1], cube[2][1][:]
        return 
    
    def S_inverse(cube):
        return 
    




# Make the surface of the cube, which contains 9 units 
def create_surface():
    array = []
    for i in range(0, 3):
        array.append([])
        for j in range(0, 3):
            array[i].append(Unit('', ''))

    return array

# Padding the plaintext to 54 units
def padding(data):
    lack = 54 - len(data)
    pad = random_pick(lack)
    data = data + pad
    return data

# [Almost]Random pick values from the dictionary
def random_pick(num):
    dictionary = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pickup = []
    for i in range(0, num):
        pickup.append(dictionary[random()])
    return pickup


# Input the plaintext to the cube
def input_file(struct, data):
    count = 0
    if len(data) <= 54:
        data = padding(data)

    for i in range(0, 6):
        for j in range(0, 3):
            for k in range(0, 3):
                struct[i][j][k].value = data[count]
                count += 1
    
    return struct

# Extract the cipher from the cube
def extract_file(struct):
    cipher = []
    for i in range(0, 6):
        for j in range(0, 3):
            for k in range(0, 3):
                cipher.append(struct[i][j][k].value)
    return cipher

# Fill the color to the cube
def fill_in_color(struct):
    color_map = ['O', 'G', 'R', 'B', 'W', 'Y']
    for i in range(0, 6):
        for j in range(0, 3):
            for k in range(0, 3):
                struct[i][j][k].color = color_map[i]
                print('memory[' + str(i) + '][' + str(j) + '][' + str(k) + ']=' + str(struct[i][j][k].color)) 
                
    
    '''
    for j in range (0,3):
        for k in range (0,3):
            struct[0][j][k].color = color_map[1]
    
    for j in range (0,3):
        for k in range (0,3):
            struct[1][j][k].color = color_map[1]
    '''
    return struct

# main function is HERE
if __name__ == "__main__":
    #plaintext =  input()
    # Create the cube first 
    surface = create_surface()
    cube = []
    for i in range(0,6):
        cube.append(surface)
    cube = fill_in_color(cube)
    cube = input_file(cube, plaintext)
    '''
    Here is the rotation
    '''

    cipher = extract_file(cube)




    '''
    #Below is the testing
    for x in range(0,6):
        for y in range(0,3):
            for z in range(0, 3):
                print('memory[' + str(x) + '][' + str(y) + '][' + str(z) + ']=' + str(cube[x][y][z].color))
    '''