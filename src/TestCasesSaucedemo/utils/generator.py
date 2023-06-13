from faker import Faker


class DataGenerator:
    def __init__(self, seed=None):
        self.fake = Faker()
        if seed:
            self.fake.seed(seed)

    def first_name(self):
        return self.fake.first_name()

    def last_name(self):
        return self.fake.last_name()

    def zip_code(self):
        return self.fake.postcode()