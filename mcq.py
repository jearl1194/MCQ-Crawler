class Question(object):
    def __init__(self):
        self._question = ""
        self._image = {}
        self._choices = []
        self._answer = ""
        self._solution = ""
        self._tags = []
        self._url = ""
        self._title = ""
        self._section = 0
        self._page = 0
        self._number = 0

    def __str__(self):
        question = self._question
        image = self._image['filename']
        choices = ""
        answer = ""
        for c in self._choices:
            if self._answer == c['id'][-1]:
                letter = c['letter']
                description = c['description']
                answer = f"{letter}. {description}"
        for c in self._choices:
            letter = c['letter']
            description = c['description']
            choices += f"{letter}. {description}"
            if not c == self._choices[-1]:
                choices += '<br>'
        anki_format = f"{question}<br><img src=\"{image}\"><br>{choices};{answer}"
        return anki_format

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, value):
        assert isinstance(value, str)
        self._question = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        assert isinstance(value, dict)
        self._image = value

    @property
    def choices(self):
        return self._choices

    @choices.setter
    def choices(self, value):
        assert isinstance(value, list)
        self._choices = value

    @property
    def answer(self):
        answer = ""
        for c in self._choices:
            print(c['letter'])
            print(c['description'])
            print(c['id'][-1])
            if self._answer['id'][-1] == c:
                letter = c['letter']
                description = c['description']
                answer = f"{letter}. {description}"
        return answer

    @answer.setter
    def answer(self, value):
        assert isinstance(value, str)
        self._answer = value

    @property
    def solution(self):
        return self._solution

    @solution.setter
    def solution(self, value):
        assert isinstance(value, str)
        self._solution = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        assert isinstance(value, list)
        self._tags = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        assert isinstance(value, str)
        self._url = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        assert isinstance(value, str)
        self._title = value

    @property
    def section(self):
        return self._section

    @section.setter
    def section(self, value):
        assert isinstance(value, int)
        self._section = value

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        assert isinstance(value, int)
        self._page = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        assert isinstance(value, int)
        self._number = value
