from fastapi import APIRouter 

entry_root = APIRouter()

# endpoint 
@entry_root.get("/")
def apiRunning():
    res = {
        "message" : "Api is runinng"
    }
    return build_response(200, res)


def build_response(status_code, body):
    return {
        'status_code': status_code,
        'headers': {
            'Content-type':'application/json'
        },
        'body':body
    }