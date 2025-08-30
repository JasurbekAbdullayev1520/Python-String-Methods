username = input("Username kiriting: ")

username = username.strip()

clean = username.replace("-", "")

if clean and clean.isalnum():
    print(True)
else:
    print(False)
