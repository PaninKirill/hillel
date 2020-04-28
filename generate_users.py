from faker import Faker


def fake_people(usr_value: int = 100):
    fake = Faker()
    data = ''
    for _ in range(usr_value):
        data += f'{fake.name()} | {fake.email()}'
    return f'Average number of users: {usr_value} ' + data

