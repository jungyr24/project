from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import math
from bs4 import BeautifulSoup


def main_page(request):
    if request.user.is_authenticated == True:
        return render(request, 'board/base.html', {})
    else:
        return redirect('login')


def tab_page(request):
    return render(request, 'board/tab-page.html', {})


def get_prob_number(request):
    if 'q' in request.GET:
        number = request.GET['q']
    else:
        message = 'plz enter the problem number'
        return HttpResponse(message)
    url = 'http://boj.kr/' + str(number)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    problem = {}
    similar_problem = []
    info_key = []
    info_value = []
    problem['문제번호'] = number
    for tag in soup.select('.col-md-12'):
        for title in tag.select('#problem_title'):
            problem['문제제목'] = title.text

        for prob in tag.select('#problem_description p'):
            problem['문제'] = prob.text

        for in_put in tag.select('#input p'):
            problem['입력'] = in_put.text

        for output in tag.select('#output p'):
            problem['출력'] = output.text

        for key in soup.select('.col-md-12 .table th'):
            info_key.append(key.text.replace(' ',''))

        for value in soup.select('.col-md-12 .table td'):
            info_value.append(value.text.replace(' ', ''))

        for similar_prob in tag.select('#problem_association li'):
            similar_problem.append(similar_prob.text)

    for key, value in zip(info_key, info_value):
        problem[key] = value

    input_list = []
    output_list = []

    for idx, ex in enumerate(soup.select('.col-md-12 .col-md-6 .sampledata')):
        cnt = math.floor(idx / 2) + 1

        if idx % 2 == 0:
            input_list.append(ex.text)
        else:
            output_list.append(ex.text)

    problem['입력예시'] = input_list
    problem['출력예시'] = output_list

    if len(similar_problem) != 0:
        problem['비슷한문제'] = similar_problem


    return render(request, 'board/test.html', {'problem': problem})