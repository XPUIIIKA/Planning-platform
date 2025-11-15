from passlib.context import CryptContext


def hashPassword(string: str) -> str:
    pwdContext = CryptContext(schemes=["bcrypt"])
    return pwdContext.hash(string)
    
def verifyPassword(plainPassword: str, hashedPassword: str) -> bool:
    pwdContext = CryptContext(schemes=["bcrypt"])
    return pwdContext.verify(plainPassword, hashedPassword)