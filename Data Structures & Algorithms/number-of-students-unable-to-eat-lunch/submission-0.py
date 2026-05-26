from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        students: deque = deque(students)
        sandwiches: deque = deque(sandwiches)
        # student and sandwiches queues are not empty.
        count = 0
        while students and sandwiches:
            if count == len(students):
                return count
            if students[0] == sandwiches[0]:
                count = 0 # reset
                students.popleft()
                sandwiches.popleft()
            else:
                count += 1 # increment counter
                popped = students.popleft()
                students.append(popped)
        return 0
        
# students = [1,1,1,0,0,1]
# sandwiches = [1,0,0,0,1,1]
# solution = Solution()
# print(solution.countStudents(students, sandwiches))
        
        
        
# students = list([1, 2, 3])
# for std in students:
#     print(std)
# myqueue = deque(students)
# print(myqueue.popleft())
# print(myqueue[0])
# print(myqueue[1])
# print(myqueue.popleft())
# print(myqueue.popleft())
# print(myqueue.popleft())
