class UnionFindQuickFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.parent)):
                if self.parent[i] == root_x:
                    self.parent[i] = root_y

class UnionFindQuickUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

# Example usage:
n = 10  # Number of elements
uf_quickfind = UnionFindQuickFind(n)
uf_quickunion = UnionFindQuickUnion(n)

uf_quickfind.union(0, 1)
uf_quickfind.union(2, 3)
uf_quickfind.union(1, 3)

uf_quickunion.union(4, 5)
uf_quickunion.union(6, 7)
uf_quickunion.union(5, 7)

print("Quick Find:")
print(uf_quickfind.find(0) == uf_quickfind.find(2))  # Should be True
print(uf_quickfind.find(1) == uf_quickfind.find(3))  # Should be True
print(uf_quickfind.find(0) == uf_quickfind.find(7))  # Should be False

print("Quick Union:")
print(uf_quickunion.find(4) == uf_quickunion.find(6))  # Should be True
print(uf_quickunion.find(5) == uf_quickunion.find(7))  # Should be True
print(uf_quickunion.find(4) == uf_quickunion.find(1))  # Should be False
