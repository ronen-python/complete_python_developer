user1 = {
	'name': 'tt',
	'valid': False
}



def authenticated(fn):
	def wrapper(*args, **kwargs):
		print(args)
		print(kwargs)

		if args[0]['valid']:
			return fn(*args, **kwargs)
	return wrapper


@authenticated
def message_friends(user):
	print ('message has been sent')

message_friends(user1)

