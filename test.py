def Create_3_dim_array(array):
    for i in range(0, 6):
        array.append([])
        for j in range(0, 3):
            array[i].append([])
            for k in range(0, 3):
                array[i][j].append(i + j + k)

def shift(a, b, c, d):
    a, b ,c ,d = b, c, d, a


if __name__ == "__main__":
    a, b, c, d = 1, 2, 3, 4
    e, f, g, h = 5, 6, 7, 8

    shift(a, b, c, d)
    print(a,b,c,d)

    '''
    for i in range(0, 6):
        for j in range(0, 3):
            for k in range(0, 3):
                print(str(i) + str(j) + str(k) + ':=>' + str(array[i][j][k]))
    '''
