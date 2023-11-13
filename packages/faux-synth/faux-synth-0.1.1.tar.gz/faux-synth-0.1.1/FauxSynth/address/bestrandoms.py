# This code is licensed under the MIT License

import requests
from bs4 import BeautifulSoup

from .types import AddressGenerator
from ..types.Address import Address


class BestRandoms(AddressGenerator):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
    }

    def get_address(self) -> Address:
        addresses = self._get_addresses()
        return addresses[0]

    def get_addresses(self, amount) -> list[Address]:

        if amount > 20:
            raise ValueError("Amount must be less than 20")

        addresses = self._get_addresses()
        return addresses[:amount]

    def _get_addresses(self) -> list[Address]:
        print(f"Getting addresses for {self.country.name}...")

        url = f"https://www.bestrandoms.com/random-address-in-{self.country.value}?quantity=20"
        response = requests.request("GET", url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        addresses = []
        raw_addresses = soup.find_all("li", {"class": "col-sm-6"})

        for raw_address in raw_addresses:
            entries = raw_address.find_all("p")
            # print(entries)

            # separate street and number
            street = entries[0].find("span").find(text=True, recursive=False).strip()

            city = entries[1].find("span").find(text=True, recursive=False).strip()

            if len(entries) == 5:
                index = 3
                state = None
            elif len(entries) == 4:
                index = 2
                state = None
                postcode = None
            else:
                index = 4

            if len(entries) > 4:
                postcode = entries[index].find("span").find(text=True, recursive=False).strip()
            if len(entries) > 5:
                state = entries[2].find("span").find(text=True, recursive=False).strip()

            calling_code = entries[index + 1].find("span").find(text=True, recursive=False).strip()

            address = Address(self.country, city, street, state, postcode, calling_code)
            addresses.append(address)

        return addresses
