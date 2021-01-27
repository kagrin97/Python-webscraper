import requests # 사이트 정보를 가져오는 라이브러리


indeed_result = requests.get("https://www.indeed.com/jobs?as_and=python&limit=50")
print(indeed_result.text) # 사이트 html 정보를 보여줌