"""
Given a list of numbers and a number k, 
return whether any two numbers from the list add up to k.

Runtime : O(N)
Space : O(N)


"""



class solution(object):
     

    def fun(self,nums,k):
        numset = set(nums)
        for x in nums:

            num1 = x
            num2 = k - num1

            if num2 in numset:
                return True

        return False



#Testcase 1 : empty list
x = solution()
AssertionError(x.fun([],4))

#Testcase 2 : less than 2 elements
AssertionError(x.fun([1],4))

#Testcase 3 : worstcase
assert(x.fun([1,2,2,3],4))

#Testcase 4 : no solution
AssertionError(x.fun([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],4))






