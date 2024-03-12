#Crystal Waters 10/27/2023
#This is a program to demonstrate functions by creating two functions to
#computer the area and perimeter of a rectangle.
#The user will give the dimensions

#this function computes the area of a rectangle given the length and width

def perimeter(length,width):
    return 2*(length+width)


#this function computes the area of a rectangle given the length and width
def area(length,width):
    return length*width

def main():
    #greet the user
    print("Welcome to the geometry program for rectangle !!:)")

    #ask the user to input the length and width

    Length= int(input("Enter the length: "))

    Width= int(input("Enter the width: "))

    #let the user choose which to compute, area or perimeter
    Choice='x'
    while Choice!='Q':

        Choice=input("Enter P for perimeter or A for area, Q to quit: ")
    #If P is entered call the perimeter function and is A is entered call the area function
    if Choice == 'P':
        Per= perimeter(Length,Width)
        print("The perimeter is", Per)
    elif Choice == 'A':
        Are= area(Length,Width)
        print("The area is",Are)
    elif Choice== 'Q':
        print("Thank you for using the Geometry  program")
    else:
        print("That option is not available")

main()
        

    
