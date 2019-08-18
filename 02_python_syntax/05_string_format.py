#positional formatting
print('This is a study about {}. {} is easy to learn and use. This year is {}.'.format('python', 'python', 2019))

#named placeholder
print('This is a study about {lang}. {lang} is easy to learn and use. This year is {year}.'.format(lang='python', year=2019))

print('This is a study about {lang}. {lang} is easy to learn and use. This year is {year:d}.'.format(lang='python', year=2019))		#	'd' means 'digit', number.

