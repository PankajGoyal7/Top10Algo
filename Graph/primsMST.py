# -*- coding: utf-8 -*-
# @Author: Pankaj Goyal
# @Date:   2018-04-01 22:45:48
# @Last Modified by:   Pankaj Goyal
# @Last Modified time: 2018-04-01 22:54:51

import sys

class Graph(object):
	"""docstring for Graph"""
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

	def printMST(self,parent):
		print "Edge \t weight"
		for i in range(1,self.V):
			print parent[i],"-",i,"\t",self.graph[i][parent[i]]


	def minKey(self,key,mstSet):
		min = sys.maxint
		for v in range(self.V):
			if key[v] < min and mstSet[v] == False:
				min = key[v]
				min_index = v
		return min_index


	def primMST(self):
		key = [sys.maxint] * self.V
		parent = [None] * self.V
		key[0] = 0
		mstSet = [False] * self.V

		parent[0] = -1

		for count in range(self.V):
			u = self.minKey(key,mstSet)

			mstSet[u] = True

			for v in range(self.V):
				if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
					key[v] = self.graph[u][v]
					parent[v] = u

		self.printMST(parent)

g = Graph(5)
g.graph = [[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]
g.primMST()

