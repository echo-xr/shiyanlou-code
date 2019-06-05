#!/usr/bin/env python3

class UserData:
    def __init__ (self, id, name):
        self.id = id
        self._name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self._name)

class NewUser(UserData):
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value


if __name__ == '__main__':
    user1 = NewUser(101, 'Jack')
    user1.set_name('Jackie')
    user2 = UserData(102, 'Louplus')
    print(user1)
    print(user2)


