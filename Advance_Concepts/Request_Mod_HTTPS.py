import requests

#Get request
r =  requests.get("https://www.digikey.ca/en/products/detail/knowles-dielectric-labs/D30BJ101M1BX/9806612")
#print(r.text)
print(r.status_code)

#Post request

"""url = "shivamvasudeva.ca"
data = {
    "p1":4,
    "p2":5
}
r2 = requests.post(url=url, data=data)
print(r2.status_code)"""