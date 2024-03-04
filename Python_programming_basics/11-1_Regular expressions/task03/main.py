import re

with open('job.txt', 'r') as file:
    content = file.read()
    job_pattern = r'\b[К-С][а-яА-Я]{5}к\b'
    jobs = re.findall(job_pattern, content)
    for job in jobs:
        print(job)
