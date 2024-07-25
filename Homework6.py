my_dict = {'Nikolay': 1998,
           'Alexander': 1996,
           'Ivan': 2000,
           'Artem': 2001}
print('Dict:', my_dict)
print('Existing Value:', my_dict.get('Nikolay'))
print('Non existing value:', my_dict.get(2003))
my_dict.update({'Ilya': 1995,
                'Sveta': 1997})
a = my_dict.pop('Ivan')
print('Deleted value:',a)
print('Modified dictionary:', my_dict)

my_set = {898,
          123,
          1002,
          898,
          1002,
          'Owl',
          'Cat'}
print('Set:', my_set)
my_set.update(['Dog'],
              [(123,456,789)])
my_set.discard('Cat')
print('Modified set:', my_set)
