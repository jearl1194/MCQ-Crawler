from mcq import Question
from bs4 import BeautifulSoup, element
import requests
import io


# page_link = f'https://www.examveda.com/electrical-engineering/practice-mcq-question-on-transformers/?section={s}&page={i}'
# page_response = requests.get(page_link, timeout=1)
# page_content = BeautifulSoup(page_response.content, "html.parser")


def get_source(page_url, local=False, time=10):
    if local:
        with open(page_url, 'r') as p:
            page_content = BeautifulSoup(
                p, "html.parser", from_encoding="utf-8")
    else:
        if 'examveda.com' in page_url:
            page_response = requests.get(page_url, timeout=time)
            page_content = BeautifulSoup(
                page_response.content, "html.parser", from_encoding="utf-8")
    return page_content


def get_ids(page_content):
    page_ids = page_content.find_all('div', 'col-xs-12')
    ids = []
    for id in page_ids:
        if 'id' in id.attrs:
            ids.append(id.attrs['id'].replace('save_alert_', ''))
    return ids


def get_numbers(page_content):
    page_question_numbers = page_content.find_all('div', 'question-number')
    numbers = []
    for n in page_question_numbers:
        numbers.append(int(n.text.strip().strip('.')))
    return numbers


def get_questions(page_content):
    page_questions = page_content.find_all('div', 'question-main')
    questions = []
    for q in page_questions:
        try:
            q.find('img').decompose()
        except AttributeError:
            pass
        questions.append(q.decode_contents().strip().strip('<br/>').strip())
    return questions


def get_images(page_content, time=10):
    images = []
    image_urls = []
    image_filenames = []
    page_questions = page_content.find_all('div', 'question-main')
    for q in page_questions:
        image = {}
        img = q.find('img')
        if isinstance(img, element.Tag):
            image_filename = img.attrs['src'].split('/')[-1]
            image_filenames.append(image_filename)
            image_url = f"https://www.examveda.com{img.attrs['src']}"
            image_urls.append(image_url)
            image_save_path = f".\\results\\images\\{image_filename}"
            response = requests.get(image_url, timeout=time)
            if response.status_code == 200:
                with open(image_save_path, 'xb') as f:
                    f.write(response.content)
            image.update({'filename': image_filename})
            image.update({'url': image_url})
        else:
            image.update({'filename': None})
            image.update({'url': None})
        images.append(image)
    return images


def get_choices(page_content):
    page_choices = page_content.find_all(
        'div', 'form-inputs clearfix question-options')
    choices = []
    choices_per_number = []
    for c in page_choices:
        choices_per_number = []
        for l in c.find_all('p'):
            try:
                letter = l.find('label').text.strip().strip('.')
                description = l.find('label').findNext().findNext().text
                id = l.find('label').attrs['for']
                choices_per_number.append(
                    {'letter': letter, 'description': description, 'id': id})
            except AttributeError:
                pass
        choices.append(choices_per_number)
    return choices


def get_answers(page_content):
    page_answers = page_content.find_all('p', 'hidden')
    answers = []
    for p in page_answers:
        answers.append(p.findChild().attrs['value'])
    return answers


def get_solutions(page_content):
    page_solution = page_content.find_all('div')
    for p in page_solution:
        print(p)


def get_page_tags(page_content):
    tags = set()
    for tag in page_content.find_all(True):
        tags.add(tag.name)
    return tags
