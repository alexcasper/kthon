from requests import get

def get_students():
  with open('student_list') as s:
    text = s.read()
    slist = text.split('\n')
    return slist
  
output = {}
existing = []
def retrieve_codewars_all(iteration=1):
  slist = get_students()
  
  for student in slist:
    data,chal_data = None,None
    if student not in output:
      output[student]= {}
    try:
      user_data,chal_data = retrieve_codewars(student)
      if 'success' in chal_data and chal_data['success']==False:
        print(f'{student} not found')
      elif 'totalItems' in chal_data and chal_data['totalItems']==0:
        print(f'{student} found but no completions')
      else:
        print(f"retrieved for {student} - {user_data['codeChallenges']['totalCompleted']} completions")
    except:
      print(f'error for {student}')
    finally:
      output[student][iteration] = {'user':user_data,
                         'chal':chal_data}
    return output    
      

def retrieve_codewars(user):
    root = 'https://www.codewars.com/api/v1/users/'
    response = get(root+user)
    try: 
      user_obj = (response.json())
      print(user_obj)
      #completed = user_obj['codeChallenges']['totalCompleted']
    except:
      user_obj = None
    suffix = '/code-challenges/completed'
    response_completed = get(root+user+suffix)
    try:
      completions_obj = response_completed.json()
      print(completions_obj)
    except:
      completions_obj = None
    return user_obj, completions_obj

retrieve_codewars('alexcasper')
