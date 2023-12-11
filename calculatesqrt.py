#!/opt/homebrew/bin/python3
#Sia
#Generic script

#import math to use the sqrt function
import math

#interact with user to get input
print ("This program give you the sqrt of 2 numbers you specify.")

#wrap it in int to make sure user enters integers only.
num1=int(input ("Enter the 1st integer: "))
num2=int(input ("Enter the 2nd integer: "))
response=input ("Enter Y/y to math or N/n to exit the program: ")

#verifying user input
print ("You entered: ", num1, num2, response)


#create loop to run or exit program
#check to make sure user doesn't enter zeroes then run program; if zeroes exit

if ( response == "Y"  or response == "y" ) and ( num1 != 0 and num2 != 0 ) :

   #print ("Your response was: ", response)

   sqnum1=int(math.sqrt(num1))
   sqnum2=int(math.sqrt(num2))
   print ("The sqr root of num1 is: ", sqnum1)
   print ("The sqr root of num2 is: ", sqnum2)
   yourtotal=num1+num2
   print ("Your total is: ", yourtotal )
   print ("Bye!")
   
#Do a last check for user entering N/n

elif response == "N" or response == "n" :
    print ("You entered N/n... exiting program.")
    exit

else:
   print("Toodeloo! You entered zeroes and Y/y.")    
