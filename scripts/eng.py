from decimal import *
_suffix_lookup = {
    'p': 'e-12',
    'n': 'e-9',
    'u': 'e-6',
    'm': 'e-3',
    '': 'e0',
    'k': 'e3',
    'M': 'e6',
    'G': 'e9',
    'T': 'e12'
}

_exponent_lookup_scaled = {
    '-36': 'p',
    '-33': 'n',
    '-30': 'u',
    '-27': 'm',
    '-24': '',
    '-21': 'k',
    '-18': 'M',
    '-15': 'G',
    '-12': 'T'
}

class EngNumber:
    """
    Used for easy manipulation of numbers which use engineering notation
    """

    def __init__(self, value, precision=2):
        """
        Initialize the class
        :param value: string, integer, or float representing the numeric value of the number
        :param precision: the precision past the decimal - default to 2
        """
        self.precision = precision

        if isinstance(value, str):
            suffix_keys = [key for key in _suffix_lookup.keys() if key != '']

            for suffix in suffix_keys:
                if suffix in value:
                    value = value[:-1] + _suffix_lookup[suffix]
                    break

            self.number = Decimal(value)

        elif isinstance(value, int) or isinstance(value, float):
            self.number = Decimal(str(value))

    def __repr__(self):
        """
        Returns the string representation
        :return: a string representing the engineering number
        """
        # since Decimal class only really converts number that are very small
        # into engineering notation, then we will simply make all number a
        # small number and take advantage of Decimal class
        num_str = self.number * Decimal('10e-25')
        num_str = num_str.to_eng_string().lower()

        base, exponent = num_str.split('e')

        base = str(round(Decimal(base), self.precision))
        if '.00' in base:
            base = base[:-3]

        return base + _exponent_lookup_scaled[exponent]
