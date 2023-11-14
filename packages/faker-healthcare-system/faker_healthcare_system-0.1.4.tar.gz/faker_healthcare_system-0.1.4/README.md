# Health System provider for Faker
[![Tests](https://github.com/matthttam8411/faker_education/actions/workflows/python-app.yml/badge.svg)](https://github.com/matthttam8411/faker_education/actions/workflows/python-app.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/180ddde29f8aa4e8c869/maintainability)](https://codeclimate.com/github/matthttam8411/faker_education/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/180ddde29f8aa4e8c869/test_coverage)](https://codeclimate.com/github/matthttam8411/faker_education/test_coverage)
## Acknowlegements
`faker_healthcare_system` is a provider for the `Faker` Python package, and a fork of https://github.com/kennethwsmith/faker_airtravel.

## Description

`faker_healthcare_system` provides fake data related to healthcare system for testing purposes.
## Installation

Install with pip:
``` bash
pip install faker-healthcare-system
```
Providers
---------
Each of the generator properties (such as ``individual_object``, ``person_object``, and
``person_object_by_gender``) are called "false". A fake generator has many of them,
packaged in "providers".

.. code:: python

    from faker import Faker
    from faker.providers import dddd

    fake = Faker()
 