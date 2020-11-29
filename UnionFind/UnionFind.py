from collections import defaultdict

class UnionFind():
    def __init__(self,n):
        # n が集合の総数
        # parents につながっている親要素を入れる
        # parents が負のやつが root 
        self.n = n
        self.parents = [-1]*n
    
    # x の root 要素を探す
    def find(self,x):
        # 親要素が負ならそれが root 
        if self.parents[x] < 0:
            return x
        else:
            # 親要素で find して更新
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # x,y をつなげる
    def union(self,x,y):
        # それぞれの root 要素を検索
        x = self.find(x)
        y = self.find(y)

        # root が一緒なら何もしない（既につながっている）
        if x == y:
            return
        
        # x を値が小さい方にしとく（ root につながってる数が多いのを x にする）
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        # x の root に y の root を併合する
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    # x が所属する集合のサイズを返す
    # root の負の大きさがサイズを表す
    def size(self, x):
        return -self.parents[self.find(x)]

    # x と y がおなじ集合に所属するかを判断
    def same(self,x,y):
        return self.find(x) == self.find(y)

    # 同じ root のものをリストで返す
    def members(self,x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    # root である要素を一覧で返す
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    # group の数を返す
    def group_count(self):
        return len(self.roots())

    # 集合内すべての要素を group ごとに返す
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    # print 用
    # group ごとに集計して返す
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
