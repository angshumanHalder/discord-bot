class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size cannot be less than or equal to 0")

        self.size = size
        self.num_components = size
        self.id = [None] * size
        self.sz = [None] * size
        for i in range(size):
            self.id[i] = i
            self.sz[i] = 1

    def find(self, p):
        root = p
        while self.id[root] != root:
            root = self.id[root]
        
        while p != root:
            nxt = self.id[p]
            self.id[p] = root
            p = nxt
        return root
    
    def _connected(self, p, q):
        return self.find(p) == self.find(q)
    
    def component_size(self):
        return self.size
    
    def components(self):
        return self.num_components

    def unify(self, p, q):
        if self._connected(p, q):
            return
        
        root_p = self.find(p)
        root_q = self.find(q)

        if self.sz[root_p] < self.sz[root_q]:
            self.sz[root_p] += self.sz[root_q]
            self.id[root_p] = root_q
        else:
            self.sz[root_q] += self.sz[root_p]
            self.id[root_q] = root_p
        self.num_components -= 1

