eat = ["roti", 'sabzi', 'chawal']

# we can only use else with for loop if the for loop is ending normaly and not with break
for i in eat:
    if i == "test":
        break
else:
    print("This for loop ended properly")