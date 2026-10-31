'''
My solution

1. Create a recursive algorithm, NO LOOPS ALLOWED, that takes in an array of numbers, and a `position` input, and it adds up the values from `position` to the end of the array.

'''
def recursion1(nums, position, index):
    if index>=len(nums): # base case
        return 0
    
    if index<position: #skipping
        return recursion1(nums,position,index + 1) # move one ahead 

    return nums[index]+recursion1(nums,position,index + 1)

'''
Lian's solution
'''
def sumPos(lisA, position):
    if position>=len(lisA):
        return 0
    else:
        return lisA[position]+sumPos(lisA, position+1)

'''
2. Create a recursive algorithm that takes in a string and prints all the non-vowels. 
Use recursion, not looping, and simplify the string itself by making it smaller each time.

''' 
def print_nonvowels(letters):
    if len(letters)==0: # base case
        print("")
    else: 
        if letters[0] not in "aeiou" and letters[0] not in "AEIOU":
            print(letters[0])
        print_nonvowels(letters[1:]) # recursive call = pass on rest of the string


'''
3. (Optional) Create a recursive algorithm that takes in three integers, 
`low`, `high`, and `step`, and it uses recursion to build a list or array 
containing the integers from `low` to `high`, skipping `step` integers each time. 
Build the list by appending new values to it. Again, no loops!

Base case:
low+step
if high>low
'''
def build_list(low, high, step):
    if low>high: #base case
        return []
    else:
        return [low]+build_list(low+step, high, step)

if __name__ == '__main__':
    nums=[1,2,3,4,5]
    position=2
    index=0
    print(recursion1(nums, position, index))
    print(sumPos(nums, position))


'''
problems on recursion
TIP 103: https://courses.codepath.org/courses/tip103/unit/3#!session_one
week 3 session 1
'''
    