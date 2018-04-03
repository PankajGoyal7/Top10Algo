# -*- coding: utf-8 -*-
# @Author: Pankaj Goyal
# @Date:   2018-03-19 00:33:15
# @Last Modified by:   Pankaj Goyal
# @Last Modified time: 2018-03-19 00:47:55
#
from collections import defaultdict
class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)

	def DFSUtil(self,s,visited):

		visited[s] =  True
		print s,

		for i in self.graph[s]:
			if visited[i] == False:
				self.DFSUtil(i,visited)


	def DFS(self,s):

		l = len(self.graph)

		visited = [False]*(l)

		# for disconnted nodes to process as well
		for i in range(l):
			if visited[i] == False:
				self.DFSUtil(s,visited)


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.DFS(2)
#Time  complexity = O(V+E)
