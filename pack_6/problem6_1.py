import Base


class LinkedCircularList(Base.DoublyLinkedBase):
    def __init__(self):
        self._center = Base._Node(None, None, None)
        self._center._next = self._center
        self._center._prev = self._center
        self._size = 0

    def add_right(self, e):
        self._insert_between(e, self._center, self._center._next)

    def pop_right(self):
        if self.is_empty():
            raise Base.Empty("List is empty")
        return self._delete_node(self._center._next)

    def add_left(self, e):
        self._insert_between(e, self._center._prev, self._center)

    def pop_left(self):
        if self.is_empty():
            raise Base.Empty("List is empty")
        return self._delete_node(self._center._prev)

    def next(self, node=0):
        if self.is_empty():
            raise Base.Empty("List is empty")
        if node == 0:
            node = self._center
        if node._next != self._center:
            return node._next
        else:
            return node._next._next

    def next_element(self, node=0):
        if self.is_empty():
            raise Base.Empty("List is empty")
        if node == 0:
            node = self._center
        return self.next(node)._element

    def get_element(self, node):
        if self.is_empty():
            raise Base.Empty("List is empty")
        return node._element

    def view_list(self):
        if self.is_empty():
            raise Base.Empty("List is empty")
        node = self.next()
        while node != self._center:
            print(self.get_element(node), end=' ')
            node = node._next
        print()

    def view_elements(self, iter):
        if self.is_empty():
            raise Base.Empty("List is empty")
        node = self.next()
        for i in range(iter):
            print(self.get_element(node), end=' ')
            node = self.next(node)
        print()

    def view_circle(self, iter):
        if self.is_empty():
            raise Base.Empty("List is empty")
        node = self.next()
        for i in range(self.len() * iter):
            print(self.get_element(node), end=' ')
            node = self.next(node)
        print()
