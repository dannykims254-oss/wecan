array_1d =  [10, 20, 30, 40, 50]
array_1d.append(60)
array_1d.remove(30)
array_1d[2] =  35
print(" \n1D array:")
print(array_1d)


array_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
array_2d.append([10, 11, 12])
array_2d[1][1]  = 55
array_2d.remove([7, 8, 9])
print(" \n2D array:")
print(array_2d)


array_3d = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print(" \n3D array:")
print(array_3d)