
# d = {
# 	'word':('slovo','slova','etc'),
# 	'world':('mir','shar zemnoy'),
# }

# word = 'world'

# if word in d:
# 	tem =(", ").join(d[word])
# 	print(tem)
# 	tem =(tem).split(' ')
# 	print(tem)
import random
from mini_hole.models import *

ab = 'qwertyuioplkjhgfdsazxcvbnm'

count = 0

while count < 4:
	a = ''
	b = ''
	len1 = random.randrange(3,10)
	len2 = random.randrange(3,10)

	for i in range(len1):
		a+=random.choice(ab)

	for i in range(len2):
		b+=random.choice(ab)

	s = str(random.randrange(12000))

	print(a,b,s)

	#Mini_hole.objects.create(name = a, surname = b, salary = s)

	count+=1