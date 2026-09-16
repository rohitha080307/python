#output function:the function is used to print the output on the screen
# syntax:"print()"

#example:1
#print("hello world")

#example:2
#print("hello","world")

#from example 1 and 2 we have observed that it gave same output
#in example 1 we gave single string and specified the space between the words
#but in example 2 we didnt specified the space yet it printed space 
#due to comma (automatically adds space) between the 2 strings

#example:3
#print(3)

#example:4
#print(3+5)

#example:5
#print("8+5")


#example 3 printed the value of 3
#example 4 printed the sum value of 3+5 that is"8"
#example 5 printed the string "8+5" not the sum value of 8+5
# because "" or '' indicate that it as a string 


#to avoid such conditions in example 5 we use formatted string to print the output in a specific format

#example:6
#print(f"{8+5}")

#in this case it will print the sum value of 8+5 that is "13" because we used formatted string




#input function:the function is used to take input from the user
#syntax:"input()"

#example:1
#input("enter your name:")

#in example 1 it will take the input from the user but it will not print the output on the screen

#example:2
#name=input("enter your name:")
#print(name)

#example:3
#age=input("enter your age:")
#print(age)

#in example 2 it will take the input from the user and print the output on the screen


#input function always takes the input in string format only
#in example 3 even if we give the input in integer format it will take it as a string only

#here we use "type casting" to convert the string input into integer format
#type casting:the process of converting one data type into another data type

#example:4
#age=int(input("enter your age:"))
#print(age)

#in example 4 it will take input from the user in string and coverts in into integer

#example:5
#height=float(input("enter your height:"))
#print(height)

#in example 5 it will take input from the user in string and convert it into float

#"type conversion":the process of converting one data type into another data type

#example:6 
#a=1
#b=2.3
#c=a+b
#print(c)

# in example 6 we get output in float that is 3.3
#we observed that without specifying the type format of the output python itself gave output in float

#difference between type casting and type conversion is that type casting is done by the user and type conversion is done by the python itself



