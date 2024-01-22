# dfs

class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False]* len(rooms)
        
        def dfs(v):
            visited[v] = True
            for key in rooms[v]:
                if visited[key] == False:
                    dfs(key)

        dfs(0)

        return all(visited)


