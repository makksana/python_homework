print('Task 1', end='\n\n')

# Create a class method named `validate`,
# which should be called from
# the `__init__` method
# to validate parameter email,
# passed to the constructor.
# The logic inside the `validate` method
# could be to check if the passed email parameter
# is a valid email string.

# Email validations:

# https://help.xmatters.com/ondemand/trial/valid_email_format.htm

# https://en.wikipedia.org/wiki/Email_address
import re

class Email:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise ValueError('Invalid email')

    @classmethod
    def validate(cls, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex, email)


m1 = Email('abrakadabra@gmail.com')
m2 = Email('abrakadabra@gmailcom')