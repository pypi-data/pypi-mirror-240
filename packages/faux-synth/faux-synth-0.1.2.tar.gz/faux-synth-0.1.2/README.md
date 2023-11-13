# FauxSynth
[![GitHub issues](https://img.shields.io/github/issues/Alok-joseph/Fake-stuff-generator)](https://github.com/Alok-joseph/Fake-stuff-generator/issues) [![GitHub stars](https://img.shields.io/github/stars/Alok-joseph/Fake-stuff-generator)](https://github.com/Alok-joseph/Fake-stuff-generator/stargazers)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

The Python package for generating addresses, temporary emails, fake names, fake credit card numbers, fake phone numbers, fake jobs, fake profiles, fake companies, fake credit reports, fake identities, and more.
It scrapes the data from the internet and generates fake data for you.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Random Address](#random-address)
  - [Temporary Email](#temporary-email)
    - [Receive Emails](#receive-emails) 


## Installation

Download this repository and run the following command in the terminal to install the required packages.

```bash
pip install -r requirements.txt
```

## Usage

### Random Address

FauxSynth provides multiple `AddressGenerators` present in `FauxSynth.address` module. 
Each `AddressGenerator` can generate multiple addresses from different countries.

In this example we will use the `BestRandoms` address generator to generate random addresses from the United States.

```python
from FauxSynth.address import BestRandoms
from FauxSynth.types import Country

# Create an instance of the AddressGenerator
address_generator = BestRandoms(Country.UnitedStates)

# Generate a random address
address = address_generator.get_address()
print(address)

# Generate multiple addresses
addresses = address_generator.get_addresses(5)
print(addresses)

# Access the address fields
print(address.street)

```

### Temporary Email

FauxSynth provides multiple `MailHandler` present in `FauxSynth.mail` module.
Each `MailHandler` can generate temporary emails.

In this example we will use the `FakeMail` mail handler to generate a temporary email.

```python
from FauxSynth.mail import FakeMail

mail_handler = FakeMail()
# FakeMail automatically has a random address. 
# You can access it using the `address` property.
print(mail_handler.address)

# You can also generate a new random address by creating a new generator.
# Or claim a new address with `claim_mail()`
# Also check if the address is available with `check_mail()`
new_address = "max.mustermann"
if mail_handler.check_mail(new_address):
    mail_handler.claim_mail(new_address)
    print(mail_handler.address)
else:
    print("Address already taken")
```

#### Receive Emails

To receive Emails using a `MailHandler` you can use the `refresh()` method.
This method will refresh the inbox and saves the new emails in the `mails` property.

The `mails` property is a list of `Mail` objects. Each `Mail` object has the following properties:

- `sender`: The sender of the email
- `subject`: The subject of the email
- `body`: The body of the email (Needs to be loaded with `load_body()`)

```python
from FauxSynth.mail import FakeMail

mail_handler = FakeMail()
print(f"Current Mail Address: {mail_handler.address}")

# Refresh the inbox
mail_handler.refresh()

# Print the mails
for mail in mail_handler.mails:
    print(f"Sender: {mail.sender}")
    print(f"Subject: {mail.subject}")
    
    mail.load_body()
    print(f"Body: {mail.body}")
    print("")
```

There is also the `wait_for_mail()` method. 
This method will automatically refresh and wait for a new email to arrive.

```python
from FauxSynth.mail import FakeMail

mail_handler = FakeMail()

# Wait for a new email
new_mail = mail_handler.wait_for_mail(timeout=60, interval=2)
```




