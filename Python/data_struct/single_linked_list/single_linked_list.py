class Node:
    def __init__(self, data = None):
        self.__data = data
        self.link = None

    @property
    def data(self):
        return self.data


    @data.setter
    def data(self, data):
        self.data = data

    @property
    def link(self):
        return self.link

    @link.setter
    def link(self, link):
        self.link = link