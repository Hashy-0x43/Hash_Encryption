import hashlib

password = str(input("Password: "))

hashed_password = hashlib.md5(password.encode()).hexdigest()

print(hashed_password)
