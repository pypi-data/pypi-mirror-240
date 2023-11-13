# This code is licensed under the MIT License

import requests
import time

from ..types.Mail import Mail
from .exceptions import MailWaitTimeout


class MailHandler:

    session: requests.Session

    address: str
    password: str

    mails: list[Mail] = []

    def __init__(self):
        pass

    def refresh(self):
        pass

    def update(self):
        pass

    def get_mail(self, mail_id: int) -> str:
        pass

    def wait_for_mail(self, timeout: int = 5, interval: int = 1) -> Mail:

        amount = len(self.mails)
        start_time = time.time()

        while len(self.mails) == amount:
            self.refresh()
            time.sleep(interval)

            if time.time() - start_time > timeout:
                raise MailWaitTimeout()

        mail = self.mails[0]
        return mail

    def session(self, new_cookies: dict = None):

        if new_cookies:
            # set cookies for session object
            self.session.cookies.update(new_cookies)

            # get current mail
            self.update()

        cookies = self.session.cookies.get_dict()

        return cookies


