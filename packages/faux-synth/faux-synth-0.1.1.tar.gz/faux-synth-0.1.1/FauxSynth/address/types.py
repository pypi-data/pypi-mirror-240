# This code is licensed under the MIT License

from ..types.Country import Country
from ..types.Address import Address


class AddressGenerator:

    country: Country

    def __init__(self, country: Country):
        self.country = country

    def get_address(self) -> Address:
        pass

    def get_addresses(self, amount) -> list[Address]:
        pass
