import bcrypt

password = "testtest".encode()

# สร้าง bcrypt hash ใหม่
salt = bcrypt.gensalt(rounds=12)
hashed_password = bcrypt.hashpw(password, salt)

print("Bcrypt Hashed Password:", hashed_password)
