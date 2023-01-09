import bcrypt

class Encryption:
    def encrypt(password):
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        return hashed_password.decode("utf-8")
    
    def check_password(password, hashed_password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)