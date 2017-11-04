class BracketsValidator:
    @staticmethod
    def check(string):
        curly_counter = 0
        round_counter = 0
        square_counter = 0
        for sym in string:
            if any(x < 0 for x in [curly_counter, round_counter, square_counter]):
                return False
            if sym == '{':
                curly_counter += 1
            elif sym == '}':
                curly_counter -= 1
            elif sym == '(':
                round_counter += 1
            elif sym == ')':
                round_counter -= 1
            elif sym == '[':
                square_counter += 1
            elif sym == ']':
                square_counter -= 1
        return all(x == 0 for x in [curly_counter, round_counter, square_counter])


print('String brackets checking')
print('Your string is ', 'valid' if BracketsValidator.check(input('Enter your string: ')) else 'invalid')
