import json,requests,time,os

def get_headers():
  headers = {
    "Content-Type": "application/vnd.github+json",
    "Authorization": f"Bearer {os.environ['GH']}"  # Include any necessary headers
  }
  return headers

def extract_students():
  slist = []
  for file in ['students.json','students2.json','students3.json']:
    with open(file) as f:
      d = json.load(f)
      slist = slist + [student['login'] for student in d]
  return slist

slist = extract_students()
with open('student_list','w+') as s:
  s.write("\n".join(slist))
  s.close


def add_student_to_repo(student):
  url = f"https://api.github.com/orgs/LCIOT/teams/2024/memberships/{student}"
  data = {"role": "member"}
  print(url)

  response = requests.put(url, json=data, headers=get_headers())

# Check the response
  if response.status_code == 200:
    print("PUT request successful")
    print("Response:", response.json())
  else:
    print("PUT request failed")
    print("Status code:", response.status_code)
    print("Response:", response.text)

def loop_through_and_add_students():
  slist = extract_students()
  for student in slist:
    time.sleep(0.2)
    add_student_to_repo(student)
