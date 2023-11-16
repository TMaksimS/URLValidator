"""unit for making requests to endpoint /get_form"""

import requests

from settings import APP_HOST, APP_PORT

URL = f"http://{APP_HOST}:{APP_PORT}/api/hb/get_form?"
MSG1 = "I look forward to requests from you in the format 'f_name1=value1&f_name2=value2'"
MSG2 = "To finish the job, enter 'exit'"


def main():
    """Head method for making requests"""
    while True:
        values = str(input("Please enter your values: "))
        if values.lower() == "exit":
            break
        req = requests.post(f"{URL}{values}", timeout=60)
        print(f"status code: {req.status_code}")
        print(f"response {req.json()}")


if __name__ == "__main__":
    print(f"{MSG1}\n{MSG2}")
    main()
