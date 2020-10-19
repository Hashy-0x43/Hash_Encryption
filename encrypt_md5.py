import hashlib

password = str(input("Password: "))

hashed_password = hashlib.md5(password.encode()).hexdigest()

print("Your Password as MD5: " + hashed_password)
