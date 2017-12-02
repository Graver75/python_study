import random

import Base


class Domain:
    def __init__(self, url):
        self.url = url
        self.requests = 1


class Top(Base.DoublyLinkedBase):
    def add(self, url):
        self._insert_between(Domain(url), self._trailer._prev, self._trailer)

    def next(self, node=0):
        if self.is_empty():
            raise Base.Empty("Top is empty")
        if node == 0: node = self._header
        return node._next

    def new_domain(self, url):
        self.add(url)

    def search_url(self, url):
        if self.len() > 0:
            node = self.next()
            for i in range(self.len()):
                if node._element.url == url:
                    return node
                node = node._next
        return False

    def node_up(self, node):
        if self.is_empty():
            raise Base.Empty("Top is empty")
        e = self._delete_node(node._prev)
        self._insert_between(e, node, node._next)

        return node

    def upgrade_top(self, url):
        node = self.search_url(url)
        if not node:
            self.new_domain(url)
        else:
            node._element.requests += 1
            if node._prev != self._header:
                while node._prev._element.requests < node._element.requests:
                    node = self.node_up(node)
                    if node._prev == self._header:
                        break

    def get_top(self, n):
        node = self.next()
        for i in range(n):
            print(node._element.url + ' : ' + str(node._element.requests))
            if self.len() > 0:
                node = self.next(node)
            else:
                break


urls = ['google.ru', 'github.com', 'web.telegram.org', 'vk.com',
        'ya.ru', 'mail.ru', 'acer.com', 'dell.com', 'skype.com']

top = Top()

n = int(input('Amount of requests: '))
p = input('Show requests? y/n: ')

for i in range(n):
    index = random.randint(0, 8)
    if p == 'y': print(urls[index])
    top.upgrade_top(urls[index])
print()

n = int(input('Amount of services (less than 9): '))
top.get_top(n)