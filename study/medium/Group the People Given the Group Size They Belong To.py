# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

class Solution:
    def groupThePeople(self, groupSizes):
        memo = {}
        answer = []
        for index in range(len(groupSizes)):
            g_num = groupSizes[index]

            if g_num not in memo:
                memo[g_num] = []

            memo[g_num].append(index)
            
            if len(memo[g_num]) == g_num:
                value = memo[g_num]
                answer.append(value[:])
                memo[g_num].clear()

        return answer
    
solution = Solution()
print(solution.groupThePeople(groupSizes=[3,3,3,3,3,1,3]))


# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        temp = {}
        out = []

        for i, size in enumerate(groupSizes):
            if size not in temp:
                temp[size] = []
            temp[size].append(i)

            if len(temp[size]) == size:
                out.append(temp[size])
                temp[size] = []
        
        return out