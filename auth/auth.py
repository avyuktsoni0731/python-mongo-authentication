import hashlib
import os
from db.encryptorDb import collection


def hash_password(password):
    # Generate a random salt
    salt = os.urandom(16)

    # Hash the password with SHA-256 and the salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Convert the hashed password and salt to hexadecimal strings
    hashed_password_hex = hashed_password.hex()
    salt_hex = salt.hex()

    # Concatenate hashed password and salt to create salted password
    salted_password = hashed_password_hex + salt_hex

    return hashed_password_hex, salt_hex, salted_password


def store_user(username, password):
    # Hash the password and get the hashed password, salt, and salted password
    hashed_password, salt, salted_password = hash_password(password)
    
    existing_user = collection.find_one({'username': username})

    if existing_user:
        # Update existing user data
        collection.update_one(
            {'username': username},
            {
                '$set': {
                    'hashed_password': hashed_password,
                    'salt': salt,
                    'salted_password': salted_password
                }
            }
        )
        print("\u2713 User already exists! Updated Credentials")
    else:
        userdata = {
            'username': username,
            'hashed_password': hashed_password,
            'salt': salt,
            'salted_password': salted_password
        }
        print("\u2713 User Created!")
        collection.insert_one(userdata)
  
      
def verify_user(username, password):
    
    data = collection.find_one({'username': username})

    if data:
        stored_hashed_password = data['hashed_password']
        stored_salt = bytes.fromhex(data['salt'])

        # Hash the entered password with the stored salt
        entered_password_hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, 100000)

        # Convert hashed password to hexadecimal string
        entered_password_hashed_hex = entered_password_hashed.hex()

        # Compare the stored hashed password with the entered password hashed with the same salt
        if entered_password_hashed_hex == stored_hashed_password:
            print("\u2713 User Verified!")
            return True
        else:
            print("\u274c Invalid Credentials!")
            return False
    else:
        print("\u274c User does not exist!")
        return False


def delete_user(username, password):
    # Verify the user's password
    if verify_user(username, password):
        # Delete the user from MongoDB collection
        result = collection.delete_one({'username': username})

        # Check if the user was deleted successfully
        if result.deleted_count == 1:
            print(f'\u2713 User {username} deleted successfully.')
            return True
        else:
            return False
    else:
        return False
