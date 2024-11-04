from requests import get

def get_students():
  with open('student_list') as s:
    text = s.read()
    slist = text.split('\n')
    return slist

def process_user_data(user_data):
  user_obj = {}
  user_obj['id'] = user_data['id']
  user_obj['username'] = user_data['username']
  user_obj['total_completed'] = user_data['codeChallenges']['totalCompleted']
  print(user_obj)
  return user_obj

def process_chal_data(chal_data,challenge_day='2024-11-04',hour_start = 10,hour_end=14):
  try: 
   output =  ([(item['id'],process_timestamp(item['completedAt'])) for item in chal_data['data']])
   output = list(filter(lambda x: x[1]['ymd'] == challenge_day and int(x[1]['hour'])>=hour_start and int(x[1]['hour'])<hour_end, output))
  except:
    output = []
  return output
  
def process_timestamp(timestamp):
  obj = {}
  obj['year'] = timestamp[0:4]
  obj['month'] = timestamp[5:7]
  obj['day'] = timestamp[8:10]
  obj['ymd'] = timestamp[0:10]
  obj['hour'] = timestamp[11:13]
  obj['time'] = timestamp[11:19]
  obj['timelong'] = timestamp[11:23]
  return obj

def retrieve_codewars(user):
    root = 'https://www.codewars.com/api/v1/users/'
    response = get(root+user)
    try: 
      user_obj = (response.json())
    except:
      user_obj = None
    suffix = '/code-challenges/completed'
    response_completed = get(root+user+suffix)
    try:
      completions_obj = response_completed.json()
    except:
      completions_obj = None
    return user_obj, process_chal_data(completions_obj)
