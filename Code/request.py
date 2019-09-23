import requests
# URL
url = 'http://dzvlfi.pythonanywhere.com/predicts'

# Change the value of experience that you want to test
r = requests.post(url,json=[{"LIMIT_BAL":30000, "EDUCATION":1, "SEX":1, "AGE":22, "PAY_1":1, "PAY_2":1, "PAY_3":1}])
print(r.json())
