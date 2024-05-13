import requests
from datetime import datetime
from dateutil import relativedelta

def get_data(people_id):
  auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiYmNiOTg2MzFjNDlhMDZjYWYzNWZhNzkwOWUwMjdiY2U2NzA5ZTA3MDM5ODVhMjRjMzdkYTVkZmYwYjYyNmNjNGUzYzYzZDU4ZDkzNDBiMWEiLCJpYXQiOjE3MTM4NzE2MTEuNjk0MzQ1LCJuYmYiOjE3MTM4NzE2MTEuNjk0MzQ5LCJleHAiOjE3NDU0MDc2MTEuNjg5NTYsInN1YiI6IjE5NjQyNzciLCJzY29wZXMiOltdfQ.yTCvDB8ppenqt5cGL_jDL6IYRr-bexKvubDmIsF2MPMNuqPW0uojTVbuzsYNYrjbYJJ2UG8t6-Yz-uu98dhumNKNo2mJ63nvrKIgDcCNUbyt6FwyQWHuPbYP00J1yPs6wVfqrNlta-ctad-U474uKq_HUaRqMYH2xt81-PHnkdjO5hXk6kpFdgaaUvjTPes727EjmdReg3UQAPaoT-khM4YTUgxwbYGhqcXcMMx909t1qNPE8uuiL-NJ-sWyaAU5ny0srGK7ctAG9ka8A4vd2OImnCtSHZ9epqQz1qt79ibdDFEez6vDVaMNq2Q_MyP-0EgS92uU9uh-P90HKn8ji54UfzQkNaEOFJSEtwnD5xikTPB_3Nwdw4vD_DsMRRnmIPbjFvf8JakrDKCC8bxuygVfYqc0rLQ-2AYa0qKCtvsKFSusOxFL7Ze-oitCaDMseNIfaq3Dy8KJib3JVkVzK-FJsgQi_RtaK2i1GO6Mxi8udhx4oWJRNgcAorVcZlTX994p9GRjgRpVp4qVjZlCEOI270ufkXFQt_gG9mOsht1BTY1B96qxbAHoH3StACmLbYP2l72YaHV8KJNsUWrXSSTVVaT1Qo_neZTlEGA2UHUMQ-SnIMozNZpyUQZyL4zcFtcJY0vt2Ec6X9QRNFgQ4TKmuhcxh_677LXKKHs6SKs"
  response = requests.get(f'https://ezekia.com/api/v2/people/{people_id}', headers={'Authorization': auth})
  raw_data = response.json()
  return raw_data

data = get_data(PID)

person_name = data['data']['name']
designation = data['data']['profile']['positions'][0]['title']
company = data['data']['profile']['positions'][0]['company']['name']
position_summary = data['data']['profile']['positions'][0]['summary']
key_responsibilities, key_achievements = extract_responsibilities_and_achievements(position_summary)
email =  data['data']['emails'][0]['address']
phone_number =  data['data']['phones'][0]['number']
try:
  location = data['data']['profile']['positions'][0]['location']['name']
except:
  location = 'NA'

start_date = data['data']['profile']['positions'][0]['startDate']
end_date = data['data']['profile']['positions'][0]['endDate']
current_date = str(datetime.now().date())
start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
current_date_dt = datetime.strptime(current_date, "%Y-%m-%d")
delta = relativedelta.relativedelta(current_date_dt, start_date_dt)
exp_years = delta.years
exp_months = delta.months
summary = data['data']['summary']
dob = 'not given'
nationality = 'not given'
education = 'need to discuss'
language= 'not given'
ctc = 'not given'
pref_loc = 'not given'
add_edu = 'not given'

arr_comp = []
arr_loc = []
arr_desig = []
arr_month_start = []
arr_month_end = []
arr_year_start = []
arr_year_end = []
arr_comp_prof = [] #discuss
arr_resp = []
arr_ach = []

for info in data['data']['profile']['positions']:
  try:
    arr_comp.append(info['company']['name'])
  except:
    arr_comp.append('NA')

  try:
    arr_comp.append(info['location']['name'])
  except:
    arr_comp.append('NA')

  try:
    arr_desig.append(info['title'])
  except:
    arr_desig.append('NA')

  arr_year_start.append(info['startDate'][:4])
  arr_year_end.append(info['startDate'][:4])
  arr_month_start.append(info['startDate'][5:7])
  arr_month_end.append(info['startDate'][5:7])

  try:
    arr_comp_prof.append(info['industry']['value'])
  except:
    arr_comp_prof.append('NA')

  arr_resp.append(info['summary'])
  arr_ach.append(info['achievements'])
