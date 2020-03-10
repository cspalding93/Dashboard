import requests

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00502/online_retail_II.xlsx"

response = requests.get(url)

with open("Online_Retail_2.xlsx", "wb") as output:
    output.write(response.content)
    output.close()
