class Data(object):
    def __str__(self):
        return 'str'
    def __repr__(self):
        return 'repr'
print ('{0!s} {0!r}'.format(Data()))