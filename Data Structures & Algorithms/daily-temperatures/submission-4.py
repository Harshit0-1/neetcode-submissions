class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)) :
            num = temperatures[i]
            
            if len(stack)> 0 :
                j = len(stack) - 1
                while len(stack) > 0 and  num > stack[-1][0] :
                    diff = i - stack[j][1] 
                    array[stack[j][1]] = diff
                    stack.pop()
                    
                    
                    j -= 1
            stack.append([num , i ])
            
        return array