import jwt


SECRET = "mybankai"


token = jwt.encode(
    {"id": "1",
     "name": "daramz",
     "job": "back_dev"},
    SECRET,
    algorithm="HS256"
)
print("Token: ", token)


data = jwt.decode(token, SECRET, algorithms=["HS256"])
# print("Decoded: ", data)




try:
    fake = jwt.decode(token, "wrongsecret", algorithms=["HS256"])
except jwt.InvalidTokenError as e:
    print("Error:", e)