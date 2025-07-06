flowers = ["iris", "hydrangea", "daisy", "peony", "sunflower", "tulip"]
print(flowers)
print(len(flowers))
print(flowers[0])

random_numbers= [1, 2, 6, 8, 4,8,32,64,2]
flowers.extend(random_numbers)
print(flowers)
print(len(flowers))
flowers.append("rose")
flowers.remove("sunflower")
flowers.pop()
print(flowers.count("iris"))
random_numbers.sort()
random_numbers.reverse()
print(random_numbers)

flowers2 = flowers.copy()
flowers2[1] = "dahlia"
print(flowers2[1])