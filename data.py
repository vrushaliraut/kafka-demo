from faker import Faker

fake = Faker()

def get_registered_user() :
    return {
        "name": fake.name(),
        "address": fake.address(),
        "created_at": fake.year()
    }

if __name__ == "_main_":
    print(get_registered_user())