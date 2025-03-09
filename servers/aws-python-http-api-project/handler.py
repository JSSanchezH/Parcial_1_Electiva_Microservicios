import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response


def get_five_attributes():
    return {
        "attr1": "value1",
        "attr2": "value2",
        "attr3": "value3",
        "attr4": "value4",
        "attr5": "value5",
    }


def get_ten_attributes():
    return {
        "attr1": "value1",
        "attr2": "value2",
        "attr3": "value3",
        "attr4": "value4",
        "attr5": "value5",
        "attr6": "value6",
        "attr7": "value7",
        "attr8": "value8",
        "attr9": "value9",
        "attr10": "value10",
    }


def return_five_attributes(event, context):
    attributes = get_five_attributes()
    response = {"statusCode": 200, "body": json.dumps(attributes)}
    return response


def return_ten_attributes(event, context):
    attributes = get_ten_attributes()
    response = {"statusCode": 200, "body": json.dumps(attributes)}
    return response
