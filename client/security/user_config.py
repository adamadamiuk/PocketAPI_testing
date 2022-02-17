import json
import jwt
import pathlib
"""
Below code allows to input and hash credentials into a db.json file
That data will be encoded with JWT and decoded when logging in is necessary to proceed
"""
class UserBase:

    @staticmethod
    def input_data():
        test_user_name = input("Provide an user name ")
        test_user_pass = input("Provide a password for the test user ")

        dataload = {
            "username": test_user_name,
            "password": test_user_pass
        }

        encoded_data = jwt.encode(dataload, "secret", algorithm="HS256")

        with open("db.json", "w") as db:
            db.truncate(0)
            json.dump(encoded_data, db)
            db.close()


    @staticmethod
    def decode_user():
        path = pathlib.Path(__file__).parent.absolute()
        with open(str(path) + "\db.json", "r") as db:
            data = json.load(db)
            db.close()
            return jwt.decode(data, "secret", algorithms="HS256")

