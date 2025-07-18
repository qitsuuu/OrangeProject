#workplace_file = open("topic18_01workplace.txt", "r")
#print(workplace_file.readable())
#print(workplace_file.read())
#print(workplace_file.readline())
#print(workplace_file.readlines())
#print(workplace_file.readlines()[0])
'''for place in workplace_file:
    print(place)'''

# = open("topic18_01workplace.txt", "a")
#workplace_file.write("<p>Canon is in Kawasaki</p>")

workplace_file = open("topic18_02index.html", "w")
workplace_file.write("<p>Canon is in Kawasaki</p>")

workplace_file.close()