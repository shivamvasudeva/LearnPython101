s = set()
s_from_list = set([1, 2, 3, 4, 5, 6])
"""
print(type(s_from_list))
print(s_from_list)
"""
'''
Question: Why Sets and not list ?????
Ans:  Set keeps unique values only there is no repeat element'''
s.add(1)
s1= s.union({2,3,4,5,6,7})
s2= s1.intersection({8,9,10})
s3 = s1.isdisjoint(s2)
"""
print(s)
print(s3)
print(s1)
print(s2)
print(len(s2))
"""