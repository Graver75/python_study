import random
import copy


class Animal:
    pass


class Fish(Animal):
    def __str__(self):
        return "F"


class Bear(Animal):
    def __init__(self):
        self.without_food = 0

    def __str__(self):
        return 'B'


class Ecosystem:
    def __init__(self, bear_dead, bear_percent, fish_percent, length_river, steps):
        self.length_river = length_river
        self.bear_number = int(0.01 * self.length_river * bear_percent)
        self.fish_number = int(0.01 * self.length_river * fish_percent)
        self.none_number = self.length_river - (self.bear_number + self.fish_number)
        self.steps = steps
        self.river = []
        self.bear_dead = bear_dead
        self.__life()

    def __str__(self):
        for i in range(self.length_river):
            if self.river[i] is None:
                print('_', end=' ')
            else:
                print(self.river[i].__str__(), end=' ')

    def __life(self):
        self.__filling()
        if self.steps > 0:
            for i in range(self.steps - 1):
                if self.fish_number == self.length_river or self.bear_number == self.length_river:
                    break
                print()
                self.__step_life()
        else:
            s = ''
            while s != 'stop' and self.fish_number != self.length_river and self.bear_number != self.length_river:
                s = input()
                if s != 'stop':
                    self.__step_life()

    def __filling(self):
        for i in range(self.bear_number):
            self.river.append(Bear())
        for i in range(self.fish_number):
            self.river.append(Fish())
        for i in range(self.fish_number + self.bear_number, self.length_river):
            self.river.append(None)
        self.__shuffle()
        self.__str__()

    def __shuffle(self):
        shuffle_list = []
        while len(self.river) != 0:
            i = random.randint(0, len(self.river) - 1)
            shuffle_list.append(self.river.pop(i))
        self.river = []
        self.river = copy.deepcopy(shuffle_list)

    def __step_life(self):
        next_step = -1
        for i in range(0, len(self.river)):
            if next_step == -1:
                if type(self.river[i]) == Bear:
                    next_step = self.__move_bear(i)
                if type(self.river[i]) == Fish:
                    next_step = self.__move_fish(i)
            else:
                next_step = -1
        self.__str__()

    def __move_bear(self, i):
        x = self.river[i].without_food
        step = self.get_step(i, self.length_river)
        if step == 0:
            if x >= self.bear_dead - 1:
                self.river[i] = None
                self.bear_number -= 1
                self.none_number += 1
            return -1
        else:
            if type(self.river[i + step]) == Fish:
                self.river[i] = None
                self.fish_number -= 1
                self.none_number += 1
                self.river[i + step] = Bear()
            elif type(self.river[i + step]) == Bear:
                self.__new_animal('bear')
                if x >= self.bear_dead - 1:
                    self.river[i] = None
                    self.bear_number -= 1
                    self.none_number += 1
                    return
                self.river[i].without_food += 1
                return -1
            else:
                self.river[i] = None
                if x >= self.bear_dead - 1:
                    self.bear_number -= 1
                    self.none_number += 1
                    return
                self.river[i + step] = Bear()
                self.river[i + step].without_food = x + 1
            return step

    def __move_fish(self, i):
        step = self.get_step(i, self.length_river)
        if step != 0:
            if type(self.river[i + step]) == Bear:
                self.river[i] = None
                self.none_number += 1
                self.fish_number -= 1
                self.river[i + step].without_food = 0
                return -1
            elif type(self.river[i + step]) == Fish:
                self.__new_animal('fish')
                return -1
            else:
                self.river[i] = None
                self.river[i + step] = Fish()
            return step
        return -1

    @staticmethod
    def get_step(i, length_river):
        if i == 0:
            return random.randint(0, 1)
        elif i == length_river - 1:
            return random.randint(-1, 0)
        else:
            return random.randint(-1, 1)

    def __new_animal(self, obj):
        index = self.__get_new_index()
        if index != -1:
            self.river[index] = Bear() if obj == 'bear' else Fish()
            self.none_number -= 1
            if obj == 'bear':
                self.bear_number += 1
            else:
                self.fish_number += 1

    def __get_new_index(self):
        if self.none_number > int(0.1 * self.length_river):
            item = random.randint(1, self.none_number)
            number = 0
            for i in range(self.length_river):
                if self.river[i] is None:
                    number += 1
                    if number == item:
                        return i
        else:
            return -1


print('River life simulation')
print('Enter values')
length_river = int(input('Length of the river: '))
dead_bear = int(input('Stamina of bear: '))
bear = int(input("Bear percent: "))
fish = int(input('Fish percent: '))
steps = int(input('Amount of life cycles(0 for default): '))
print('(10 percents are not used to reproduce)')
if steps == 0:
    print('Press enter to next life cycle, enter "stop" exit')
e = Ecosystem(dead_bear, bear, fish, length_river, steps)