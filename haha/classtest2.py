#!/usr/bin/env python3

class UserData:
    def __init__ (self, id, name):
        self.id = id
        self._name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.id, self._name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @classmethod
    def get_group(cls):
        return cls.group
    
    @staticmethod
    def format_userdata(id, name):
        return '{}\'s id is {}'.format(name, id)

if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
