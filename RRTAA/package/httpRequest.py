import requests
import json

def main():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('http://get_single_reward/1/')
    # we then print out the http status_code that was returned on making this request
    # you should see a successful '200' code being returned.
    print(req.status_code)
    data = json.loads(req)
    print(data)


if __name__ == '__main__':
    main()