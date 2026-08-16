class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = [0] * len(temperatures)
        stack = []
        remove = 0
        for i in range(len(temperatures)) :
            num = temperatures[i]
            stack.append([num , i ])
            
            if len(stack)> 1 :
                j = len(stack) - 2
                while num > stack[j][0] :
                    diff = i - stack[j][1] 
                    array[stack[j][1]] = diff
                    stack.remove(stack[j])
                    remove = remove + 1 
                    
                    j -= 1
        return array