import numpy as np

def calculate(nums):
    
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.") 
    
    try:
        nums = np.array(nums)
        nums33 = nums.reshape(3,3)

        res_ls = {
            'mean': [np.mean(nums33, axis=0), np.mean(nums33, axis=1), np.mean(nums33)],
            'variance': [np.var(nums33, axis=0), np.var(nums33, axis=1), np.var(nums33)],
            'max': [np.max(nums33, axis=0), np.max(nums33, axis=1), np.max(nums33)],
            'min': [np.min(nums33, axis=0), np.min(nums33, axis=1), np.min(nums33)],
            'sum': [np.sum(nums33, axis=0), np.sum(nums33, axis=1), np.sum(nums33)]
        }
        print (res_ls)
    
    except ValueError: 
        print("List must contain nine numbers.")
    

res = calculate([0,1,2,3,4,5,6,7,8])