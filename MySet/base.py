class SetBase():
    def add(self, e):raise NotImplementedError
    def remove(self, e):raise NotImplementedError
    def contains(self, e):raise NotImplementedError
    def isEmpty(self):raise NotImplementedError
    def getSize(self):raise NotImplementedError


class MapBase():
    def add(self, key, value):raise NotImplementedError
    def remove(self, key):raise NotImplementedError
    def contains(self, key):raise NotImplementedError
    def get(self, key):raise NotImplementedError
    def set(self, key, value):raise NotImplementedError
    def getSize(self):raise NotImplementedError
    def isEmpty(self):raise NotImplementedError
