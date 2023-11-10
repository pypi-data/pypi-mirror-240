import random

from faker import Faker
from faker.providers import BaseProvider


class IndividualProvider(BaseProvider):

    def npi(self) -> int:
        return self.generator.random_number(digits=9, fix_len=True)

    def tin(self) -> int:
        return self.generator.random_int(min=100000000, max=999999999)

    def individual_object(self) -> dict:
        gender = random.choice(["M", "F"])
        # person_name: dict = self.generator.person_object_by_gender(gender)
        return {
            'npi': self.npi(),
            'credential': random.choice(["DMD", "PhD", "MD", "Dr"]),
            'sole_proprietor': random.choice(["YES", "NO"]),
            'gender': gender,
            'personal_name': '',
            'other_names': '',
            'credential': '',
            'credential': '',
            'credential': '',
            'credential': ''
        }


fake = Faker()
fake.add_provider(IndividualProvider)
Faker.seed(0)

fake_person_names = [fake.individual_object() for _ in range(10)]
for i in fake_person_names:
    print(i)
