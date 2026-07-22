class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        visited = 0
        while queue:
            course = queue.popleft()
            visited += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return True if visited == numCourses else False
        