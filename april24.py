


# first program

nums=[1,2,5]
target=7
solutions=[]

def solution(nums,target):
    for i in range(len(nums)):
        cur_num=nums[i]
        for j in range(i+1, len(nums)):
            next_num=nums[j]
            if cur_num+next_num==target:
                solutions.append((i,j))
    print(solutions)
solution(nums,target)         
   
# seocnd program
    
       


# import time
# nums=[2,5,6,9]
# target=7
# start=time.perf_counter()
# def sol(nums,target):
#     dictionary={}
#     solutions=[]
#     for i in range(len(nums)):
#         dictionary[nums[i]]=i

#     for i in range(len(nums)):
#         currentnumber=nums[i]
#         remaining=target-currentnumber
#         if remaining in dictionary:
#             solutions.append((i,dictionary[remaining]))
#     return solutions
# print(sol(nums,target))
# end=time.perf_counter()
# print(end-start)
    
    
# nums=[1,2,3,1]
# def solution(nums):
#     dictionary={}
#     for i in nums:
#         if i not in dictionary:
#            dictionary[i]=1
#     else:
#        return True
#     return false

# print(solution(nums))



# nums=[1,2,3,1]
# for i in nums:
#     if nums.count(i)>1:
#        return true
# return false

# print(solution(nums))
    

