number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print("\nUsing manual method:")
print(number_grid[0])
print(number_grid[0][0])
print(number_grid[1])
print(number_grid[1][1])
print(number_grid[2])
print(number_grid[2][2])

print("\nUsing for loop to display all:")
for row in number_grid: #any name is okay for row
    for col in row: #any name is okay for col
        print(col)