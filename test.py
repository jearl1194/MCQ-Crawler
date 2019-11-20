from mcq_crawler import get_source, get_numbers, get_ids, get_images, get_questions, get_choices, get_answers
from mcq import Question
import io

# file_source = r"results\examveda.com_transformers_sourcecode.html"
# file_source = r"results\examveda.com_ac_circuit_theorems_sourcecode.html"
# file_source = r"results\examveda.com.html"
# file_content = get_source(file_source, local=True)
# page_content = get_source(page_source)

sections = 2
pages = 14

question = Question()
# anki_format = f"{number}. {question}<br><img src="{image}"><br>{choices};{answer}"

for s in range(1, sections+1):
    # text_path = f".\\results\\examveda.com_transformer_section_{s}.txt"
    # text_path = f".\\results\\examveda.com_A.C_Fundamentals,_Circuits_And Circuit_Theory_section_{s}.txt".lower()
    text_path = f".\\results\\examveda.com_Transmission And Distribution_section_{s}.txt".lower().replace(
        ' ', '_')
    for p in range(1, pages+1):
        # page_source = f"https://www.examveda.com/electrical-engineering/practice-mcq-question-on-a.c-fundamentals,-circuits-and-circuit-theory/?section={s}&page={p}"
        page_source = f"https://www.examveda.com/electrical-engineering/practice-mcq-question-on-transmission-and-distribution/?section={s}&page={p}"
        page_content = get_source(page_source)

        numbers = get_numbers(page_content)
        ids = get_ids(page_content)
        images = get_images(page_content)
        questions = get_questions(page_content)
        choices = get_choices(page_content)
        answers = get_answers(page_content)

        source_info = ""
        source_info += f"site: {page_source}<br>"
        source_info += f"section: {s}<br>"
        source_info += f"page: {p}"

        for i in range(0, len(numbers)):
            question.number = numbers[i]
            question.id = ids[i]
            question.image = images[i]
            question.question = questions[i]
            question.choice = choices[i]
            question.answer = answers[i]

            img_filename = question.image['filename']
            answer = ""

            choices_per_num = ""
            for choice in question.choice:
                choices_per_num += choice['letter']
                choices_per_num += '. '
                choices_per_num += choice['description']
                if not choice == question.choice[-1]:
                    choices_per_num += '<br>'
                if choice['id'][-1] == answers[i]:
                    answer += choice['letter']
                    answer += '. '
                    answer += choice['description']

            if img_filename == None:
                anki_format = f"{question.question}<br><br>{choices_per_num};{answer};{source_info}\n"
            else:
                anki_format = f"{question.question}<br><br><img src=\"{img_filename}\"><br><br>{choices_per_num};{answer};{source_info}\n"

            with io.open(text_path, 'a', encoding="utf-8") as f:
                f.write(anki_format)

# numbers = get_numbers(file_content)
# ids = get_ids(file_content)
# images = get_images(file_content)
# questions = get_questions(file_content)
# choices = get_choices(file_content)
# answers = get_answers(file_content)
# get_solutions(file_content)

# print(f"numbers:\n{numbers}\n")
# print(f"ids:\n{ids}\n")
# print(f"questions:\n{questions}\n")
# print(f"images:\n{images}\n")
