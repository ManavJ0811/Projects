import requests

base = input("From: ").upper()
target = input("To: ").upper()
amount = float(input("Amount: "))

url = f"https://api.exchangerate-api.com/v4/latest/{base}"
res = requests.get(url)

if res.status_code != 200:
    print("Wrong currency!")
else:
    data = res.json()
    rate = data['rates'].get(target)
    if rate:
        print(f"{amount} {base} = {amount * rate:.2f} {target}")
    else:
        print("Wrong currency!")