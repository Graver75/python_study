class Converter(int):
    roman_map = (('M', 1000),
           ('CM', 900),
           ('D', 500),
           ('CD', 400),
           ('C', 100),
           ('XC', 90),
           ('L', 50),
           ('XL', 40),
           ('X', 10),
           ('IX', 9),
           ('V', 5),
           ('IV', 4),
           ('I', 1))

    def check(self, value):
        try:
            int(value)
        except Exception:
            return value
        return int(value)

    def convert(self, value):
        value = self.check(value)
        type_of_value = type(value)
        res = 0 if type_of_value is str else ''
        i = 0
        for numeral, integer in self.roman_map:
            if type_of_value is str:
                while value[i:i + len(numeral)] == numeral:
                    res += integer
                    i += len(numeral)
            else:
                while value >= integer:
                    res += numeral
                    value -= integer
        return res

converter = Converter()
print('Converting to roman and from')
print('Your result is: ', converter.convert(input('Enter your number: ')))