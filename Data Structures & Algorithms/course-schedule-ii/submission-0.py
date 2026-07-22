class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0 for _ in range(numCourses)]
        queue = deque()
        # prerequisites = [[1,0], [2,0], [3,1]]

        # create adjacency list & in degree
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # add the initial one with indegree 0 
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        order = []
        while queue:
            i = queue.popleft()
            order.append(i)
            for neighbor in graph[i]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order if len(order) == numCourses else []
                

