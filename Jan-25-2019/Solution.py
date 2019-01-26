"""
Given an array of integers, return a new array such that each element at 
index i of the new array is the product of all the numbers in the original 
array except the one at i


Run Time : O(N)
Space : O(1)

When not allowed to use division: use prefix and suffix product

"""


class Solution (object):

    #Using division
    def newArray(self,arr):

        prod = 1
        if len(arr)<1:
            return 0
        
        for x in arr:
            prod *= x

        for i,x in enumerate(arr):
            arr[i] =  prod//x
        return arr
    
    #without using division
    def newArray2(self,arr):

        prefix_prod = [1]*len(arr)
        suffix_prod = [1]*len(arr)

        prev = 1
        for i,x in enumerate(arr):
            prefix_prod[i] = prev*x
            prev = prev*x


        prev = 1
        for i,x in enumerate(arr[::-1]):
            suffix_prod[i] = prev*x
            prev = prev*x
        
        suffix_prod = suffix_prod[::-1]
        for i,x in enumerate(arr):
            if i == 0:
                arr[i] = suffix_prod[i+1]
                continue
            if i+1 ==  len(arr):
                arr[i] = prefix_prod[i-1]
                continue

            arr[i] = prefix_prod[i-1]*suffix_prod[i+1]
        
        return arr
            

var = Solution()


#Test Case 1
assert([120, 60, 40, 30, 24] == var.newArray([1, 2, 3, 4, 5]))

#Test Case 2
assert(([2, 3, 6]) == var.newArray([3, 2, 1]))


#### Method 2 : Using prefix product and suffix product

#Test Case 1
assert([120, 60, 40, 30, 24] == var.newArray2([1, 2, 3, 4, 5]))

#Test Case 2
assert(([2, 3, 6]) == var.newArray2([3, 2, 1]))
