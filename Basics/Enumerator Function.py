l1 = ["aws", "azure", "gpc", "ail_baba"]
"""i = 1
for items in l1:
    if i % 2 is 0:
        print(items)
    i += 1
"""
# we don't need to create a var and increment it
for index, item in enumerate(l1):
# it gives index and items
    if index % 2 != 0:
        print(item)