name = 'Polina'
day = 'Friday'
print(f'Good day {name}! {day} is a perfect day to learn some python.')

greeting = 'Good day {}! {} is a perfect day to learn some python.'
print(greeting.format(name, day))

print('Good day {}! {} is a perfect day to learn some python.'.format(name, day))
print('Good day {1}! {0} is a perfect day to learn some python.'.format(day, name))
print('Good day %s! %s is a perfect day to learn some python.' % (name, day))
