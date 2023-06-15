#Fizzbuzz code: given a number n, for each integer i in the range from 1 to n exclusive
#a.if 3 and 5 are multiple of i print fizzbuzz
#a.if 3 is multiple and 5 isnt multiple of i print fizz
#a.if 3 is not multiple  and 5 is multiple of i print buzz
#b. otherwise return i

#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    # Write your code here
    for i in range (1,n + 1):
        
        if i % 3 == 0 & i % 5 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0 & i % 5 != 0:
            print ("Fizz")
        elif i % 3 != 0 & i % 5 == 0:
            print("Buzz")
        else:
            print(i)       
    
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
