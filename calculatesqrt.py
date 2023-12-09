#!/opt/homebrew/bin/python3
#Sia
#Generic script

import math

#interact with user to get input
print ("This program give you the sqrt of 2 numbers you specify.")
num1=int(input ("Enter the 1st number: "))
num2=int(input ("Enter the 2nd number: "))
response=input ("Enter Y/y to add or N/n to exit the program: ")

sqnum1=int(math.sqrt(num1))
sqnum2=int(math.sqrt(num2))

print ("You entered: ", num1, num2, response)
print ("The sqr root of num1 is: ", sqnum1)
print ("The sqr root of num2 is: ", sqnum2)

#create loop to check to run or exit program
#response="y" #set value to y to troubleshoot manually

if ( response == "Y"  or response == "y" ) and ( num1 != 0 and num2 != 0 ) :

   print ("Your response was: ", response)
   #check to make sure user doesn't enter zeroes then run program; if zeroes exit
   #if  num1 != 0 or num2 != 0 :
   yourtotal=num1+num2
   print ("Your total is: ", yourtotal )
   print ("Bye!")
   
  
#elif num1 == 0 or num2 == 0 :
    #if user enters zeroes exit
 #    print ("You entered zeroes... exiting program.")
  
#Do a last check for user entering N/n

elif response == "N" or response == "n" :
    print ("You entered N/n... exiting program.")
    exit

else:
   print("buh bye")    
