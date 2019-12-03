import requests

class employee:

    raises = 1.1
    def __init__(self, first, last, sal):
        self.first=first
        self.last=last
        self.salary=sal

    @property
    def email(self):
        return self.first+'.'+self.last+'@email.com'

    @property
    def fullname(self):
        return f"{self.first}.{self.last}"

    def apply_riase(self):
        return self.salary*employee.raises

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

