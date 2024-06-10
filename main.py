import re
import json
responseMessage = {"name": "John", "age": 30, "message": "aminkii"} 
y=json.dumps(responseMessage)
# print(y)
x=json.loads(y)
print(x)
z=x["message"]
user_message = input("Please enter your message:\n  Make sure you only use letters and ranging from 4-8")
if not re.match(r'^[a-zA-Z0-9]{4,8}$', user_message):
    print ("Validation Error!")
    
else:
    # print("Hello "+ user_message)
    if(user_message[0:int(len(user_message)/2)] == z[0:int(len(z)/2)]):
        if(user_message[int(len(user_message)/2):len(user_message)] == z[int(len(z)/2):len(z)]):
            print("verified")
        else:
            print("invalid")
    else:
        print("invalid")
    # match user_message[0:2] in x['message']:
    #     # pattern 1
    #     case True:
    #         match user_message[2:4] in x['message']:
    #             case True:
                    
    #     case False:
    #         print("no match")
print(user_message)

# print (user_message in message_values)