# Lesson 3
#Squares Solution

#input
tiles = input("Enter the number of tiles:") #input() is string
tiles = int(tiles) #convert to integer
#square root is just the exponent of 0.5
calculation = int((tiles ** 0.5)//1) #square root

# check whole number
print(f"the maximun side length is: {calculation}")