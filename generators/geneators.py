range(100)
list(range(100))



def make_list(num):
	result = []
	for i in range(num):
		result.append(i*2)
	return result


# my_list = make_list(100)
# print(my_list)


# yield keeps waiting till next(g) is executed
def generator_function(num):
  for i in range(num):
	  yield i*2

g = generator_function(100)
next(g)
next(g)
print(next(g))


def special_for(iterable):
	iterator = iter(itrerable)
