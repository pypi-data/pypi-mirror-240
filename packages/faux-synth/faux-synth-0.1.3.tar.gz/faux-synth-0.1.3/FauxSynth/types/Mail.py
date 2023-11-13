
class Mail:

    body: str

    def __init__(self, handler, subject: str, sender: str, mail_id: int):
        self.handler = handler
        self.subject = subject
        self.sender = sender
        self.mail_id = mail_id

    def __str__(self):
        return f"<Mail {self.mail_id} | {self.subject} / {self.sender} >"

    def load_body(self):
        self.body = self.handler.get_mail(self.mail_id)
        return self.body

