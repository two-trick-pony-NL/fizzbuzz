#Fizzbuz
for i in range(1,101):
    output = "" #Empty string that we'll output at the end
    flag = False #Set a flag to see if we had any special condition
    if i % 3 == 0: # Check if we can devide by 3
        output += "Fizz" #Add Fizz to the output
        flag = True #Set the flag to True -
    if i % 5 == 0: # Check if we can devide by 5
        output += "Buzz" #Add buzz to the output
        flag = True #Set flag to true
    if flag == False: # If no flag was set it's "just a number"
        print(i) #So we print the number and not the output
    else: 
        print(output + "("+str(i)+")") #Print the output


#BONUS: Palindrome test
word = "lepel"
test = word[::-1]
if word == test: 
    print("This is a palindrome: " +word)
else: 
    print("This is not a palindrome: " +word)
