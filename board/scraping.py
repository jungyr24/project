import requests
import math
from bs4 import BeautifulSoup

def problem_scraping(number):
    url = 'http://boj.kr/' + str(number)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    problem = {}
    similar_problem = []
    info_key = []
    info_value = []

    for tag in soup.select('.col-md-12'):
        for prob in tag.select('#problem_description p'):
            problem['문제'] = prob.text

        for in_put in tag.select('#input p'):
            problem['입력'] = in_put.text

        for output in tag.select('#output p'):
            problem['출력'] = output.text

        for key in soup.select('.col-md-12 .table th'):
            info_key.append(key.text)

        for value in soup.select('.col-md-12 .table td'):
            info_value.append(value.text.replace(' ', ''))

        for similar_prob in tag.select('#problem_association li'):
            similar_problem.append(similar_prob.text)

    for key, value in zip(info_key, info_value):
        problem[key] = value

    input_dict = {}
    output_dict = {}

    for idx, ex in enumerate(soup.select('.col-md-12 .col-md-6 .sampledata')):
        cnt = math.floor(idx / 2) + 1

        if idx % 2 == 0:
            input_dict[cnt] = ex.text
        else:
            output_dict[cnt] = ex.text

    problem['입력예시'] = input_dict
    problem['출력예시'] = output_dict

    if len(similar_problem) != 0:
        problem['비슷한 문제'] = similar_problem

    return problem