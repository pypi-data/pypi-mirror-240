import random

from faker import Faker
from faker.providers import BaseProvider

from faker_healthcare_system.person_name import PersonNameProvider

fake = Faker()
fake.add_provider(PersonNameProvider)


class IndividualProvider(BaseProvider):
    def individual_object(self) -> dict:
        gender = random.choice(["M", "F"])
        person_name:dict = self.generator.person_object_by_gender(gender)
        return {
            'credential': random.choice(["DMD", "PhD", "MD", "Dr"]),
            'sole_proprietor': random.choice(["YES", "NO"]),
            'gender': gender,
            'personal_name': self.generator.person_object_by_gender(gender),
            'other_names': '' if gender == 'M' else self.generator.person_object_married(person_name),
            'credential': '',
            'credential': '',
            'credential': '',
            'credential': ''
        }


fake.add_provider(IndividualProvider)
Faker.seed(0)

fake_person_names = [fake.individual_object() for _ in range(10)]
for i in fake_person_names:
    print(i)
