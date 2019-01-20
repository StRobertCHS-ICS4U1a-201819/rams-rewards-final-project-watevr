import requests
import json

def reward():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('http://localhost:8000/get_single_reward/1/')
    # we then print out the http status_code that was returned on making this request
    # you should see a successful '200' code being returned.
    print(req.status_code)
    '''
    return json.loads(req)
    '''

def student():
    # we define a request object that is equal to requests.get('API')
    req = requests.get('http://localhost:8000/get_single_reward/1/')
    # we then print out the http status_code that was returned on making this request
    # you should see a successful '200' code being returned.
    print(req.status_code)
    '''
    return json.loads(req)
    '''
    list = ["Highest Mark", "Average over 85", "Club Meeting", "Sport Team", "Activities Leader"]
    return list


if __name__ == '__main__':
    reward = reward()
    student = student()