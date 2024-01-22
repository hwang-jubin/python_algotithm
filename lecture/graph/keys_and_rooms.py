#bfs
# https://leetcode.com/problems/keys-and-rooms/submissions/1149496744/
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False]*len(rooms)

        q = deque()

        visited[0] = True
        for key in rooms[0]:
            q.append(key)
            visited[key] = True

        while q:
            keys = q.popleft()
            
            for kkey in rooms[keys]:
                if visited[kkey] == False:
                    q.append(kkey)
                    visited[key] = True

        return visited not in False
