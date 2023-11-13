# This code is licensed under the MIT License

from .Country import Country


class Address:

    def __init__(self, country: Country, city: str, street: str,
                 state: str, zip_code: str, calling_code: str):
        self.country = country
        self.city = city
        self.street = street
        self.state = state
        self.zip_code = zip_code
        self.calling_code = calling_code

    def __str__(self):
        return f"{self.street}\n{self.zip_code} {self.city}\n{self.country}"

    def __repr__(self):
        return f"{self.street}\n{self.zip_code} {self.city}\n{self.country}"

    def __dict__(self):
        return {
            "country": self.country,
            "city": self.city,
            "street": self.street,
            "state": self.state,
            "zip_code": self.zip_code,
            "calling_code": self.calling_code
        }
