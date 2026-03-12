
import bcrypt


class HashPassword:

    def hash_password(self, password:str) -> str:
        # bcrypt only accepts bytes, encode password string to bytes
        encoded_password = password.encode("utf-8")

        # Generate salt, this is stored within the hash (algo, salt, hashed string)
        salt = bcrypt.gensalt()
        # hash the password
        hashed_password = bcrypt.hashpw(encoded_password, salt)
        # return the hashed_password as a string using decode
        return hashed_password.decode("utf-8")
    
    def validate_password(self, provided_password:str, stored_hash:str):
        # encode both provided password and stored hash into bytes
        encoded_provided_password = provided_password.encode("utf-8")

        encoded_stored_hash = stored_hash.encode("utf-8")

        # return true/false result from checkpw() when checking if both hashes are the same
        return bcrypt.checkpw(encoded_provided_password, encoded_stored_hash)