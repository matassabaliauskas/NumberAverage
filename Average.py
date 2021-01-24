num =1000;
count = 0;
sum = 0;

print("This program will calculate an average. Please enter a negative number to exit.")
while num>0:
    num = int(input("Please input a number: "))
    if num < 0:
        print();
        
    else:
        #print("The sum before equation is: ", sum)
        sum = sum + num;
        #print("The sum after equation is: ", sum)
        count = count +1


#print("You have entered",count,"numbers")

##print("The sum is: ", sum)
##print("The count is: ", count);
average=sum/count

print ("The average is: ", average)
