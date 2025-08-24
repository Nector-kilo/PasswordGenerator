"""Creates a random number generated password for websites and
applications.

imports random.randint:
imports random.choice:

method get: Returns the password.
method generate: Builds a password and returns it. Raises a ValueError.
method build_string: Builds the generated array to a string.
method clear: Clears the private password variables.
"""
from random import randint, choice


class Password:
    def __init__(self):
        self._LOWER = 'abcdefghijklmnopqrstuvwxyz'
        self._CAPITAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._NUMBERS = '1234567890'
        self._SYMBOLS = '!@#$%&*-=_+?'
        self._password_array = []
        self._password = ''

    def get(self):
        """Return the generated password"""
        return self._password

    def clear(self):
        """Clears the current password."""
        self._password_array = []
        self._password = ''

    def build_string(self):
        """Converts a password array to a string."""
        self._password = ''.join(i for i in self._password_array)

    def generate(self, length=12):
        """Builds a random number generated password into an array and
        checks if password has at least one capital letter, one
        lowercase letter, one number, and one symbol.

        :param length: The length of the password as string.
        :raise ValueError: Cannot be less than 4 in length.
        :returns: The password as a string
        """
        if length < 4:
            raise ValueError('Cannot be less than 4 in length.')

        for i in range(length):
            key_switch = randint(0, 2)
            if key_switch == 0:
                lower_cap_switch = randint(0, 1)
                if lower_cap_switch == 0:
                    self._password_array.append(choice(self._LOWER))
                if lower_cap_switch == 1:
                    self._password_array.append(choice(self._CAPITAL))
            elif key_switch == 1:
                self._password_array.append(choice(self._NUMBERS))
            else:
                self._password_array.append(choice(self._SYMBOLS))

        lower = []
        capital = []
        numbers = []
        symbols = []

        for i in self._password_array:
            if i in self._LOWER:
                lower.append(i)
            elif i in self._CAPITAL:
                capital.append(i)
            elif i in self._NUMBERS:
                numbers.append(i)
            else:
                symbols.append(i)

        if len(lower) == 0:
            self.clear()
            self.generate(length)
        elif len(capital) == 0:
            self.clear()
            self.generate(length)
        elif len(numbers) == 0:
            self.clear()
            self.generate(length)
        elif len(symbols) == 0:
            self.clear()
            self.generate(length)

        self.build_string()
        return self._password
