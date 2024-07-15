import requests
import randam
from datetime import datetime
url = 'https://docs.google.com/forms/d/e/1FAIpQLSfzeUzQiGqGETLNbmcVLFqB91mPGnDAKTwWSnO-KXAnQRv6Gg/formResponse'
today_date =
datetime.today().strftime('%Y-%m-%d')
if today_date == '2024-07-21':
  run_distance = 0
else:
  run_distance = random.uniform(20,25)
  number_option = '74'
  injury_option = '〇'
  form_date = {
    'entry.1482692254': today_date,
    'entry.2010531061':
    number_option,
    'entry.1208168648': '鈴木健真',
    'entry.275531236':
    f'{run_distance:.2f}',
    'entry.394754842': injury_option,
  }
  response = requests.post(url,data=form_data)
  if response.status_code == 200:
    print("データが正常に送信されました")
  else:
    print(f"エラーが発生しました:
    {response.statuss_code}")
