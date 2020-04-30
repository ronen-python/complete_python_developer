# def hello(func):
# 	print('!!!!!!')

# greet = hello
# del hello
# print(greet())

# def hello():
# 	print ('hello')
# def my_decorator(func):
# 	def wrap_func(*args, **kwargs):
# 		print('rrrr')
# 		func(*args, **kwargs)
# 		print('eeeee')
# 	return wrap_func


# @my_decorator
# def hello(x, we='ee'):
# 	print(x, we)


# hello('hi!!!')


from time import time
def performance(func):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'took {t1-t2}')
		return result
	return wrapper
@performance
def long_time():
	for i in range(1000):
		i * 5

long_time()
