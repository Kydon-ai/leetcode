class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        required_courses = []
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in required_courses:
                required_courses.append(prerequisites[i][1] )
            else:   
                return False
        return True

s = Solution()

numCourses = 2; prerequisites = [[1,0]]

print(s.canFinish(numCourses,prerequisites))