class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        array = []

        for i in range(len(temperatures)) :
            temp = temperatures[i]
            warm_temp = float('-inf')
            next_temp_index = i + 1 
            while temp > warm_temp  :
                if next_temp_index > len(temperatures)-1 :
                    array.append(0)
                    break 
                check = temperatures[next_temp_index] > temp
                print("this is the check : " , check)
                if check :
                    diff = next_temp_index - i
                    warm_temp = temperatures[next_temp_index]
                    array.append(diff)
                next_temp_index += 1
            print("this is the array : " , array)
        return array

                


