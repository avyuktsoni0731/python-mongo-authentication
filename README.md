# Python Encryption/Authentication System

The Encryption System is a Python project designed to provide a secure and reliable method for storing and verifying user passwords using cryptographic techniques. It leverages hashing algorithms, salted password storage, and MongoDB as the database backend to ensure data integrity and confidentiality.

## Features

- **Password Hashing**: User passwords are hashed using the SHA-256 algorithm with a random salt, preventing unauthorized access to sensitive information.
- **Salted Password Storage**: Hashed passwords are securely stored along with their corresponding salt values in a MongoDB collection, enhancing security by adding an additional layer of protection against password cracking techniques such as rainbow tables.
- **User Verification**: Users can securely verify their passwords by comparing the hashed passwords with the stored values in the MongoDB database, ensuring password authenticity and integrity.
- **Flexible Configuration**: The system allows for easy configuration through environment variables, enabling customization of MongoDB connection settings and other parameters to suit specific deployment environments.
- **Error Handling**: Robust error handling mechanisms are implemented to handle various edge cases and exceptions, ensuring reliable operation under diverse scenarios.

### Standard Authentication Algorithm
Normal authentication systems store the passwords of users in a standardised manner, most frequently using base64 encoding.

|Username|Password|
|-|-|
|User0|a1b2c3|
|Sam|altman|
|Bruce|wayne01|
|User96|abc123|

This is an unsecure way of storing user credentials, and are prone to get breached easily.

### Hashing Passwords (using SHA-256)
The passwords are hashed using SHA256 (PBKDF2_HMAC) cryptographic encryption algorithm, which is the most secure encryption algorithm right now (used by Bitcoin).

|Username|Password|Hashed Password
|-|-|-|
|User0|a1b2c3|e91f5eb8960f7a3452b6ac4ff4ba5924a51dea5fd070a429395fe44b1146b0a2|
|Sam|altman|2d1b40272f23de5bea32da3bbe3c20c97830043144621c6bcc3ef949ac184c1c|
|Bruce|wayne01|bf048a253fa3b967dc1e427eb709b03a62e7bdc3c892ab723baedd8685a8b3ee|
|User96|abc123|65f312413163fb0163bcc964cb642fa10bddbfdd147f847fa9198199a8a7efba|

Hashing is a one-way process, so it becomes astronomically impossible to find the pre-image of a hash function.

### Using Salt
To add an extra layer of security, we generate a random 64 byte UTF-8 salt (using urandom) and iterate the hashed password with it 100,000 times.
|Username|Salt|Salted Password
|-|-|-|
|User0|bbd4ef4d747938d243d54da0d92bf70e|e91f5eb8960f7a3452b6ac4ff4ba5924a51dea5fd070a429395fe44b1146b0a2bbd4ef4d747938d243d54da0d92bf70e|
|Sam|587384ecf5c7989a95b0a7a3e0d00a2d|2d1b40272f23de5bea32da3bbe3c20c97830043144621c6bcc3ef949ac184c1c587384ecf5c7989a95b0a7a3e0d00a2d|
|Bruce|e06db82dec005105fc95238938f812e0|bf048a253fa3b967dc1e427eb709b03a62e7bdc3c892ab723baedd8685a8b3eee06db82dec005105fc95238938f812e0|
|User96|88fb96453dfa576b0dcdedb1045abb3b|65f312413163fb0163bcc964cb642fa10bddbfdd147f847fa9198199a8a7efba88fb96453dfa576b0dcdedb1045abb3b|

### Password Storage
The UserIDs along with their hashed passwords, salts, and salted passwords are stored in a MongoDB database instead of traditional MySQL databases to ensure data integrity and prevent data leak from hardware.

![mongoDB](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/mongoDB.png?raw=true)

# Usage

### Setup

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/avyuktsoni0731/python-mongo-authentication.git
   ```

2. Install the required dependencies:

   ```python
   pip install -r requirements.txt
   ```

3. Set up a MongoDB database (cluster) and obtain the connection URI.

4. Create a `.env` file in the project directory and add your MongoDB URI as `MONGODB_URI`.

5. Run `main.py`.

# Implementation

### Create/Update a User :
1) A 64 byte cryptographic pseudorandom salt is generated.
2) The salt is then encoded to base64 (UTF-8) format.
3) The password entered by user is hashed using PBKDF2_HMAC, then iterated with 100,000 rounds of salt using SHA256 cryptographic encryption algorithm.
4) The userdata is then stored on a secure MongoDB database.

### Verify/Authenticate a User :
1) The user is asked for the username and password to verify.
2) The verification function first checks if the user exists in the database or not, and if it does, the password is passed through the same encryption algorithm used while creating a new user to verify if with the hash of the existing user. As hashes of the same strings are same.
3) If the hash matches, then the user is verified/authenticated.
4) If the user is not found in the database, the verification process does not go through, and user is faced with an error.
5) If the credentials (password) provided by the user is incorrect, then user is faced with an error of invalid credentials.

### Delete a User :
1) The user is asked for the username and password to verify.
2) The verification function first checks if the user exists in the database or not, and if it does, the password is passed through the same encryption algorithm used while creating a new user to verify if with the hash of the existing user. As hashes of the same strings are same.
3) If the hash matches, then the user is deleted.
4) If the user is not found in the database, the deletion process does not go through, and user is faced with an error.
5) If the credentials (password) provided by the user is incorrect, then user is faced with an error of invalid credentials.

# Working

### Main Interface

- Here, the user is asked if they want to create a new user, verify an existing user or delete an existing user.

![Main Interface](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/mainMenu.png?raw=true)

### Storing User Passwords

- Here, the user enters the `Username` and `Password` that they want to create and store in encrypted format.

![userCreated](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/userCreated.png?raw=true)

- The created user gets stored in the MongoDB database along with the hashed password, salt and salted password.

![createdUserMongoDB](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/createdUserMongoDB.png?raw=true)

### Verifying User Passwords

- If the user enters correct `Username` and `Password`, the user will get verified.

![verifySuccess](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/verifySuccess.png?raw=true)

- If the user enteres incorrect `Username` and `Password`, the user will be faced by an incorrect credentials error.

![verifyInvalid](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/verifyInvalid.png?raw=true)

- If the user enteres a `Username` that does not exist, the user will be faced by a User doesn't exist error.

![verifyFail](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/verifyFail.png?raw=true)

### Deleting User Accounts

- If the user does exist, and user enters correct `Username` and `Password`, the user will get deleted from the MongoDB database.

![userDeleted](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/userDeleted.png?raw=true)

### Exiting the System

- After you're done with it, exit the system to close the connection to MongoDB server.

![cxnEnd](https://github.com/avyuktsoni0731/python-mongo-authentication/blob/main/static/cxnEnd.png?raw=true)

## Requirements

- Python 3.x
- pymongo
- python-dotenv

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
