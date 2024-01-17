class solution:
    def temperater(self, tem):
        answer=[0]*len(tem)
        stk = []
        for (day,temp) in enumerate(tem):
            while stk and stk[-1][1] < temp:
                pop = stk.pop()
                answer[pop[0]] = day - pop[0]
            stk.append((day, temp))

        return answer


solution_instance = solution()
# print(solution_instance.temperater([22,23,4,5,67,8,2]))

