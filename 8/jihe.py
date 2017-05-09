#coding:utf-8

aSet = set(['a','c','b','d'])
bSet = set(['c','e','d','f'])

print aSet
print bSet

print "#交集"
print aSet.intersection(bSet)
print "#并集"
print aSet.union(bSet)
print bSet.union(aSet)
print "#差集"
print aSet.difference(bSet)
print bSet.difference(aSet)
print "#对称差"
print aSet.intersection(bSet)
print bSet.intersection(aSet)

print "#超级，子集"
smallSet = set(['a','c','b'])
print smallSet
bigSet = set(['a','c','b','e','d','f'])
print bigSet
print smallSet.issubset(bigSet)
print bigSet.issubset(smallSet)



