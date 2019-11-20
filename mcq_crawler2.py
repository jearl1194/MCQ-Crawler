from mcq import Question
from bs4 import BeautifulSoup
import requests
import io

items = []
numbers = []
questions = []
choices = []
answers = []
tag = ['transformers']
tags = tag * 6


page_links = []
for i in range(1, 3):
    pl = f'https://www.examveda.com/electrical-engineering/practice-mcq-question-on-transformers/?section=3&page={i}'
    page_links.append(pl)

for page_link in page_links:
    page_response = requests.get(page_link, timeout=1)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    ns = page_content.find_all('div', 'question-number')
    for n in ns:
        n_replace = n.text.replace('.', '')
        n_strip = n_replace.strip()
        numbers.append(n_strip)
        print(n_strip)

    qs = page_content.find_all('div', 'question-main')
    for q in qs:
        q_strip = q.text.strip()
        questions.append(q_strip)

    cs = page_content.find_all('div', 'form-inputs clearfix question-options')
    for c in cs:
        c_replace = c.text.replace('\n\n', '')
        c_strip = c_replace.strip()
        c_split = c_strip.split('\n')
        choices.append(c_split)

    ans = page_content.find_all('input')
    for a in ans:
        if 'value' in a.attrs:
            answers.append(a['value'])

for i in range(0, 6):
    t = tags[i]
    q = questions[i]
    n = numbers[i]
    c = ''
    for choice in choices[i]:
        c = c + '<br>' + str(choice)
    a = choices[i][int(answers[i])-1]
    item = f'{t};{n}. {q}{c};{a}'
    items.append(item)

f = io.open('Examveda.txt', 'a', encoding="utf-8")
for item in items:
    f.write(item)
    f.write('\n')
    print(item)
    print('\n')

f.close()
# for n in numbers:
# print(n)
# print('')
##
# print('')
# for q in questions:
# print(q)
# print('')
##
# print('')
# for c in choices:
# print(c)
# print('')
##
# print('')
# for a in answers:
# print(a)
# print('')
