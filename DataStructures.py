#Finding Area of the Circle
# r is the Radius of the circle

r=float(input("Input the Radius of the circle: "))
Area = (22/7)*r*r
print("The area of the circle with radius r is :", Area)





#Second Task

#Accept a filename from the user and print the extension of that
Filename=input("Input the filename: ")
File_extension=Filename.split(".")
print("The extension of the file is: ", repr(File_extension[-1]))
