import requests
import json
import pickle

r = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
saved_text = r.text
splited = saved_text.splitlines()
data = [[i] for i in splited] #what it is doing ?
file = 'list_of_lists.pkl'
#Pickel

f = open(file,'wb')
pickle.dump(data,f)
f.close()

#De-Pickel
file = "list_of_lists.pkl"
f = open(file,'rb')
depickled = pickle.load(f)
f = open("Result_of_Pickle.txt",'wb')
pickle.dump(depickled,f)
f.close()




