from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list to represent the course dependencies.
        adjacency = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adjacency[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue for BFS.
        queue = deque()

        # Find courses with no prerequisites and add them to the queue.
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            numCourses -= 1
            for neighbor in adjacency[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # If all courses can be removed from the graph, return True.
        return numCourses == 0
