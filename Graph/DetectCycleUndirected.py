# -*- coding: utf-8 -*-
# @Author: Pankaj Goyal
# @Date:   2018-04-01 12:01:10
# @Last Modified by:   Pankaj Goyal
# @Last Modified time: 2018-04-01 22:18:00
# Disjoint Set (Or Union-Find) | Set 1 (Detect Cycle in an Undirected Graph)
# 

from collections import defaultdict

class Graph:
	
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v):
		self.graph[u].append(v)


	def find_parent(self,parent,i):
		if parent[i] == -1:
			return i
		if parent[i] != -1:
			return self.find_parent(parent,parent[i])

	def union(self,parent,x,y):
		X_set = self.find_parent(parent,x)
		Y_set = self.find_parent(parent,y)
		parent[X_set] = Y_set

	def isCyclic(self):
		parent = [-1]*(self.V)
		for i in self.graph:
			for j in self.graph[i]:
				x = self.find_parent(parent,i)
				y = self.find_parent(parent,j)
				if x == y:
					return True
				self.union(parent,x,y)


g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)

if g.isCyclic():
	print "Graph contains cycle"
else:
	print "Graph doesn't contain graph"


