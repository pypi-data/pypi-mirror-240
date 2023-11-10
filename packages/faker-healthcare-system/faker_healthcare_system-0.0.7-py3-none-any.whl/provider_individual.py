import random
from datetime import date, timedelta

from faker import Faker
from faker.providers import BaseProvider


class IndividualProvider(BaseProvider):

    def npi(self) -> int:
        return self.generator.random_number(digits=9, fix_len=True)

    def tin(self) -> int:
        return self.generator.random_int(min=100000000, max=999999999)

    def gender(self) -> str:
        return random.choice(["M", "F"])

    def enumeration_date(self) -> date:
        return self.generator.date_between(start_date="-5y", end_date="today")

    def person_name_by_gender(self, gender: str) -> dict:
        return {
            'first_name': self.generator.first_name_female() if gender == "F" else self.generator.first_name_male(),
            'last_name': self.generator.last_name_female() if gender == "F" else self.generator.last_name_male(),
            'name_prefix': self.generator.prefix_female() if gender == "F" else self.generator.prefix_male(),
            'name_suffix': self.generator.suffix_female() if gender == "F" else self.generator.suffix_male(),
            'type_name': 'Personal Name',
        }

    def person_married_name(self, person_object: dict) -> dict:
        new_last_name = self.generator.last_name_male()

        new_person_object = {
            'first_name': person_object['first_name'],
            'last_name': new_last_name,
            'name_prefix': person_object['name_prefix'],
            'name_suffix': person_object['name_suffix'],
            'type_name': 'Married',
        }
        return new_person_object

    def address_with_purpose(self, purpose: str = 'Mailing') -> dict:
        address_type = ["DOM", "FGN", "MIL"]
        us_states = [
            "Alabama",
            "Alaska",
            "Arizona",
            "Arkansas",
            "California",
            "Colorado",
            "Connecticut",
            "Delaware",
            "Florida",
            "Georgia",
            "Hawái",
            "Idaho",
            "Illinois",
            "Indiana",
            "Iowa",
            "Kansas",
            "Kentucky",
            "Luisiana",
            "Maine",
            "Maryland",
            "Massachusetts",
            "Míchigan",
            "Minnesota",
            "Misisipi",
            "Misuri",
            "Montana",
            "Nebraska",
            "Nevada",
            "Nuevo Hampshire",
            "Nueva Jersey",
            "Nuevo México",
            "Nueva York",
            "Carolina del Norte",
            "Dakota del Norte",
            "Ohio",
            "Oklahoma",
            "Oregón",
            "Pensilvania",
            "Rhode Island",
            "Carolina del Sur",
            "Dakota del Sur",
            "Tennessee",
            "Texas",
            "Utah",
            "Vermont",
            "Virginia",
            "Washington",
            "Virginia Occidental",
            "Wisconsin",
            "Wyoming",
        ]
        return {
            'country_code': self.generator.current_country_code(),
            'country_name': self.generator.current_country(),
            'purpose': '',
            'address_type': random.choice(address_type) if purpose != 'Main Office' else 'Physical',
            'address_1': self.generator.address(),
            'address_2': self.generator.address(),
            'city': self.generator.city(),
            'state': random.choice(us_states),
            'postal_code': self.generator.postcode(),
            'telephone_number': self.generator.phone_number(),
            'fax_number': self.generator.phone_number(),
        }

    def individual_object(self) -> dict:
        gender = self.gender()
        person_name: dict = self.generator.person_name_by_gender(gender)
        last_updated_epoch: date = self.generator.date_this_decade()
        return {
            'npi': self.npi(),
            'tin': self.tin(),
            'last_updated_epoch': last_updated_epoch,
            'created_epoch': last_updated_epoch - timedelta(365 * self.generator.random_int(min=1, max=4)),
            'enumeration_date': self.enumeration_date(),
            "status": "Active",
            "email": self.generator.email(),
            "enumeration_type": "NPI-1",
            "mailing_address": self.address_with_purpose(),
            "location_address": self.address_with_purpose(purpose='LOCATION'),
            "main_office_address": self.address_with_purpose(purpose='Main Office'),
            "taxonomies": "",
            "licenses": "",
            "identifiers": "",
            "taxonomy_qualification": "",
            "taxonomy_endpoints": "",
            "schedule": "",
            'credential': random.choice(["DMD", "PhD", "MD", "Dr"]),
            'sole_proprietor': random.choice(["YES", "NO"]),
            'gender': gender,
            'personal_name': person_name,
            'other_names': '' if gender == 'M' else self.person_married_name(person_name),
            'dea': '',
            'ethnicity_code': '',
            'date_of_birth': '',
            'languages': '',
            'gender_restriction': '',
            'malpractice': '',
            'main_office_address': '',
        }


fake = Faker()
fake.add_provider(IndividualProvider)
Faker.seed(0)

fake_person_names = [fake.individual_object() for _ in range(10)]
for i in fake_person_names:
    print(i)
