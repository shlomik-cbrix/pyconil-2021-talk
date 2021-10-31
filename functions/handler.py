import json
import datetime


def get(event, context):
    current_time = datetime.datetime.now().time()
    body = {"message": "Hello, the current time is " + str(current_time)}

    response = {"statusCode": 200, "body": json.dumps(body)}

    domain = input("Enter the Domain: ")
    output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding='UTF-8')
    print(output)

    secret="super secret"

    domain = input("111 the Domain:222 ")  # 123
    output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding='UTF-8')
    print(output)

    return response