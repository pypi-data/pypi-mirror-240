# This code is licensed under the MIT License

import json
from requests import Session

from .types import MailHandler
from ..types.Mail import Mail
from .exceptions import MailRequestError


class FakeMail(MailHandler):

    json_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'application/json; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.fakemail.net/',
    }

    html_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
    }

    def __init__(self):
        super().__init__()

        self.session = Session()
        self._init_session()

    def _init_session(self):

        url = "https://www.fakemail.net/"

        self.session.request("GET", url, headers=self.html_headers)
        self.update()
        self.refresh()

    def update(self):

        url = "https://www.fakemail.net/index/index"

        response = self.session.request("GET", url, headers=self.json_headers)

        if response.status_code == 200:
            data = json.loads(response.text[1:].strip())
            self.address = data["email"]
            self.password = data["heslo"]
            return {
                "mail": self.address,
                "password": self.password
            }

        raise MailRequestError("Could not get current mail!")

    def refresh(self):

        url = "https://www.fakemail.net/index/refresh"

        response = self.session.request("GET", url, headers=self.json_headers)

        if response.status_code == 200:
            data = json.loads(response.text[1:].strip())
            mails = []
            for mail in data:
                mails.append(Mail(self, mail["predmet"], mail["od"], mail["id"]))

            self.mails = mails
            return mails

        raise MailRequestError("Could not refresh mail!")

    def claim_mail(self, address_without_at: str):

        url = "https://www.fakemail.net/index/new-email/"

        if "@" in address_without_at:
            address_without_at = address_without_at.split("@")[0]

        payload = f"emailInput={address_without_at}&format=json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.fakemail.net/',
        }

        response = self.session.request("POST", url, headers=headers, data=payload)

        if "ok" in response.text:
            self.update()
            self.refresh()

            return True
        elif "bad" in response.text:
            return False
        else:
            raise MailRequestError("Could not claim mail!")

    def check_mail(self, address_without_at: str):

        url = "https://www.fakemail.net/index/email-check/"

        payload = f"email={address_without_at}&format=json"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': 'https://www.fakemail.net/',
        }

        response = self.session.request("POST", url, headers=headers, data=payload)

        if "ok" in response.text:
            return True
        elif "bad" in response.text:
            return False
        else:
            raise MailRequestError("Could not check mail!")

    def get_mail(self, email_id: int):
        url = f"https://www.fakemail.net/email/id/{email_id}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.fakemail.net/window/id/1',
        }

        response = self.session.request("GET", url, headers=headers)

        if response.status_code != 200:
            raise MailRequestError("Could not get mail!")

        email = response.text

        return email
