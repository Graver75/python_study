class Polynomial:
    def __init__(self, s):
        self.degree = []
        self.coef = []
        self.value = s
        self.parse()

    def parse(self):
        pol = []
        if self.value[0] != '-':
            self.value = '+' + self.value
        while len(self.value) != 0:
            if self.value.rfind('+') < self.value.rfind('-'):
                pol.append(self.value[self.value.rfind('-'):])
                self.value = self.value[:self.value.rfind('-')]
            else:
                pol.append(self.value[self.value.rfind('+'):])
                self.value = self.value[:self.value.rfind('+')]
        for i in range(len(pol)):
            a = pol.pop()
            if a.find('x') == -1:
                self.degree.append(0)
                self.coef.append(float(a))
            elif a.find('^') != -1:
                self.degree.append(int(a[a.find('^') + 1:]))
                self.coef.append(float(a[:a.find("x") - 1]))
            else:
                self.degree.append(1)
                self.coef.append(float(a[:a.find("x") - 1]))

    def get_derivation(self):
        diff_coef = []
        diff_degree = []
        for i in range(len(self.coef)):
            diff_coef.append(self.coef[i] * (self.degree[i]))
            diff_degree.append(self.degree[i] - 1)
        dif = ''

        for i in range(len(diff_coef)):
            diff_coef[i] = explicit_float_to_int(diff_coef[i])

        for i in range(len(diff_coef)):
            if diff_coef[i] == 0:
                pass
            elif diff_degree[i] == 0:
                if diff_coef[i] > 0:
                    dif += '+' + str(diff_coef[i])
                else:
                    dif += str(diff_coef[i])
            elif diff_degree[i] == 1:
                if diff_coef[i] > 0:
                    dif += '+' + str(diff_coef[i]) + '*x'
                else:
                    dif += str(diff_coef[i]) + '*x'
            else:
                if diff_coef[i] > 0:
                    dif += '+' + str(diff_coef[i]) + '*x^' + str(diff_degree[i])
                else:
                    dif += str(diff_coef[i]) + '*x^' + str(diff_degree[i])
        if dif[0] == '+':
            dif = dif[1:]
        return dif


def explicit_float_to_int(x):
    if x - int(x) == 0:
        return int(x)
    else:
        return x


print('Calculating polynomial derivations')
z = input('Enter polynomial: ')
y = Polynomial(z)
print(y.get_derivation())
