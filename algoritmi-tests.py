def dfs(G):
	def dfs_r(l,s,f):
		for x in l[s]:
			if f[x] == -1:
				f[x] = s
				dfs_r(l,x,f)

	fathers = [-1] * len(G)
	fathers[0] = 0
	dfs_r(G,0,fathers)


def cycles_nd(G):
	def dfs_r(l,s,v,f):
		v[s] = True
		for x in l[s]:
			if x == f[s]:
				continue
			if v[x]:
				return True
			if dfs_r(l,x,v,f):
				return True
		return False

	visited = [False] * len(G)
	dfs_r(G, 0, visited, 0)


def components_nd(G):
	def dfs_r(l,s,cc,c):
		cc[s] = c
		for x in l[s]:
			if cc[x] == 0:
				dfs_r(l,x,cc,c)


	cc = [0] * len(G)
	c = 0

	for x in G:
		if cc[x] == 0:
			c += 1
			dfs_r(G,x,cc,c)


def time_to_visit(G):
	def dfs_r(l,s,t):
		nonlocal time 
		t[s] = time
		for x in l[s]:
			if t[x] == 0:
				time += 1
				dfs_r(l,x,t)

	times = [0]*len(G)
	time = 1
	times[0] = time
	dfs_r(G, 0, times)

	return times

def dfs(l_adj, node):
	def dfs_r(l,x,v):
		v[x] = True
		for y in l[x]:
			if not v[y]:
				dfs_r(l,y,v)
	visited = [False] * len(l_adj)
	dfs_r(l_adj, node, visited)
	return visited

def transposed(l_adj):
	result = set()
	for x in l_adj:
		result[x] = []

	for x in l_adj:
		for y in l_adj[x]:
			result[y] = x
	return result


def intersected(a,b):
	if len(a) != len(b):
		raise Error()
	result = [False] * len(a)
	for x in a:
		if b[x] == a[x]:
			result[x] = True
	return result


def strongly_connected(l_adj, node):
	l_trans = transposed(l_adj)
	v1 = dfs(l_adj, node)
	v2 = dfs(l_trans, node)
	return intersected(v1,v2) 



def conta_livelli_pari(adj, start):
	q = queue()
	distances = [-1] * len(adj)
	distances[start] = 0
	stats = dict()
	stats[start] = 1
	q.push(start)
	while not q.is_empty():
		node = q.pop()
		for x in adj[node]:
			if distances[x] == -1: 
				distances[x] = distances[node]+1
				if not stats[distances[x]]: 
					stats[distances[x]] = 1
				else: 
					stats[distances[x]] += 1
				q.push(x)

	result = 0

	for dist,nodes in stats: 
		if nodes%2 == 0: 
			result+=1
	return result




def dfs_fathers(adj, start):
	def dfs_fathers_r(adj, start, fathers):
		for item in adj[start]:
			if fathers[item] == -1:
				fathers[item] = start
				dfs_fathers_r(adj, item, fathers)
	fathers = [-1 for _ in range(len(adj))]
	fathers[start] = start
	dfs_fathers_r(adj, start, fathers)
	return fathers




def cycles_nd(start, adj, father):
	def cycles_ndr(start, adj, father, visited):
		visited[start] = True
		for item in adj[start]:
			if father == item: 
				continue
			if visited[item]: 
				return True
			if cycles_ndr(item, adj, start, visited): 
				return True 
		return False
	visited = [False] * len(adj)
	return cycles_ndr(start, adj, father, visited)
	

def outdeg(vertex, adj):
	return len(adj[vertex])



def indeg(vertex):
	count = 0
	for el in adj: 
		for idx in adj[el]:
			if adj[el] == vertex:
				count += 1
	return count

def trasposto_con_lista(l_adj): 
	l_res = {}
	for index in l_adj
		l_res[index] = []
	for item in l_adj:
		for index in l_adj[item]:
			l_res[index].append(item)

	return l_res


l_adj = {
	0: [1,5],
	1: [0,5],
	2: [4],
	3: [],
	4: [2],
	5: [0,1]
}

def componente_connessa(l_adj):
	def dfs_r(x,l_adj,C,c):
		C[x] = c
		for y in G[x]:
			if C[y] == 0:
				dfs_r(y,G,C,c)
	###
	C = [0 for _ in l_adj]
	c = 0
	for x in l_adj: 
		if C[x] == 0:
			c+=1
			dfs_r(x,l_adj,C,c)
	return C



def componente_connessa(l_adj):
	def dfs_r(x, l_adj, cc, c): 
		cc[x] = c
		for item in l_adj[x]: 
			if cc[item] == 0: 
				dfs_r(item, l_adj, cc, c)

	cc = [0 for _ in l_adj]
	c = 0
	for item in l_adj: 
		if cc[item] == 0: 
			c+=1
			dfs_r(item, l_adj, cc, c)
	return cc

def sono_nello_stesso_path(x,y,z,l_adj): 
	cc = componente_connessa(l_adj)
	if cc[x] == cc[y] or cc[x] == cc[z] or cc[y] == cc[z]:
		return True

def cycles_nd(l_adj, start):
	def dfs(adj,s,v,f):
		v[s] = True
		for item in adj[s]: 
			if f == item:
				continue
			if v[item]: 
				return True
			if dfs(adj,item,v,start):
				return True
		return False
	visited = [False for _ in l_adj]
	father = start
	dfs(l_adj, start, visited, father)


def comp_conn(l_adj): 
	def dsf(adj,s,cc,c):
		cc[s] = c
		for item in adj[s]: 
			if cc[item] == 0: 
				dfs(adj, item, cc, c)
	cc = [0 for _ in l_adj]
	c = 0
	for item in l_adj: 
		if cc[item] == 0: 
			c+=1
			dfs(l_adj, item, cc, c)
	return cc


def cycles_nd(l_adj, start):
	def dfsr(l,s,f,v):
		for x in l[s]:
			if x == f:
				continue
			if v[x]: 
				return True
			if dfsr(l,x,s,v):
				return True
		return False

	visited = False * len(l_adj)
	return dfsr(l_adj, start, start, visited)
