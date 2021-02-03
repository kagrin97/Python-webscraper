import csv

def save_to_file(jobs):
    file = open("jobs_scrapper/jobs.csv", mode="w", encoding = "utf-8")
    # 'w'를 사용할경우 원래 내용을 사라지고 새로운 내용이 생긴다 'a'를 사용할경우 추가만 된다
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return