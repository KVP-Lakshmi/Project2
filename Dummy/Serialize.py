import requests
res = requests.get("http://127.0.0.1:8000/readone")
print(res.status_code)
print(res.json())

print("====================================================================")
res = requests.get("http://127.0.0.1:8000/ones")
print(res.status_code)
print(res.json())

print("====================================================================")
res = requests.get("http://127.0.0.1:8000/onesa")
print(res.status_code)
print(res.json())

print("====================================================================")
res = requests.get("http://127.0.0.1:8000/onesaspec")
print(res.status_code)
print(res.json())

print("====================================================================")
x=input("enter id no:")
res = requests.get("http://127.0.0.1:8000/onesacon/"+x)
if res.status_code == 200:
    print(res.json())
else:
    print("Sorry... Please Enter Proper Employee IDNO")