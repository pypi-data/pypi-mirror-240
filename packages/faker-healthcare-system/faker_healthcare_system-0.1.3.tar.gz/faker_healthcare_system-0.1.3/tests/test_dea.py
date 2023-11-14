from datetime import date

import pytest
from faker import Faker

from faker_healthcare_system.dea import DeaProvider


@pytest.fixture
def fake():
    fake_instance = Faker()
    fake_instance.add_provider(DeaProvider)
    return fake_instance


def test_dea_object(fake):
    dea_data = fake.dea_object()

    assert 'number' in dea_data
    assert isinstance(dea_data['number'], str)

    assert 'allow_prescribe' in dea_data
    assert isinstance(dea_data['allow_prescribe'], bool)

    assert 'start_date' in dea_data
    assert isinstance(dea_data['start_date'], date)

    assert 'expiration_date' in dea_data
    assert isinstance(dea_data['expiration_date'], date)

    assert 'supervising_number' in dea_data
    assert isinstance(dea_data['supervising_number'], str)

    assert 'supervising_license' in dea_data
    assert isinstance(dea_data['supervising_license'], int)
