# Learn-to-program
Solution to the programming assignments of course Learn to Program - The Fundamentals which is being offered in Coursera. All the assignments are in Python.
#####Largest sub-array problem####

#You have an array containing positive and negative numbers (no zeros). How will you find the sub-array with the largest sum.
#Example: If the array is: 1, 5, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5 
#The largest sub-array is: 8, 1, -4, 5, -3, 1, -1, 6
#NOTE: You've to print the largest sub-array (with all integers), NOT the largest numeric sum total.
#Boundary condition: For an array with all negative numbers, the largest number is the answer. For an array with all positive numbers, the whole array is the answer.

#array=[1, 5, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5]
array=[1, 5, -7, 8, 1, -4, 5, -3, 1, -15, 6, -5]
def lar_subarray(array):
    larSum=array[0]
    larArray = []
    for i in range(len(array)):
        #print("i : ", i)
        last = len(array)-1
        
        sum=0
        while (last>i):
            sub=array[i:last]
            #print ("last : ", last)
            sum=sumArray(sub)
            #print("Inner Sum ::", sum)
            if ((sum==larSum) and (len(sub)<len(larArray))):
                larArray=sub
            elif ((sum>larSum) and sorted(sub)!=sorted(array)):
                larSum=sum
                larArray=sub 
            last-=1
    print("Array : ", larArray)
    print("Sum : ", larSum)
    return larArray

def sumArray(list):
    sum=0
    for n in list:
        sum+=n
    return sum

lar_subarray(array)



###########################################################################################################

###Palindromes in a string###
#Given an input string str with N characters in it, print out all occurrences of palindromes in it.
#Example: For the string I O M K I L O L I K T C J I O P L L P O
#The answer would be:
#O P L L P O and K I L O L I K
#Please note that every palindrome that is more than 3 characters in length can be broken down into more palindromes.
#but you just need to print out the largest size possible for each set (so, for the example string, you SHOULD NOT print LOL, LL , PLLP and ILOLI )

str="I O M K I L O L I K T C J I O P L L P O O O O"

def palindromes_string(str):
    #str = str.replace(" ","")
    N = len(str)
    pal = []
    for i in range(N):
        last = N
        while(last-i>2):
            sub = str[i:last]
            if((check_palindrome(sub)) and (check_list(sub,pal)==False)):
                pal.append(sub.strip())
            last-=1
    #print(pal)
    kl = remove_smaller(pal)
    finalList = []
    for each in kl:
        pl = [j for j in kl]
        pl.remove(each)
        re = check_list(each, pl)
        if (re==False):
            finalList.append(each)
    return (finalList)


def check_palindrome(str):
    rev = str[-1::-1]
    return (rev==str)

def check_list(sub, li):
    flag = False
    for each in li:
        if (sub in each):
            flag = True
    return flag

def remove_smaller(list):
    new_list = []
    for each in list:
        if len(each)>=5:
            new_list.append(each)
    return new_list
    

print(palindromes_string(str))
#print(check_palindrome(str))
