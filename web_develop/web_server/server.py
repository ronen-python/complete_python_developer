from flask import Flask, render_template, request, redirect
import csv
app=Flask(__name__)
print(__name__)


# @app.route('/')
# def hello_world():
# 	return 'Hello World!'


@app.route('/')
def my_home():
	return render_template('index.html')

# @app.route('/about.html')
# def about_html():
# 	return render_template('about.html')

# @app.route('/works.html')
# def work():
# 	return render_template('works.html')

# @app.route('/contact.html')
# def work():
# 	return render_template('contact.html')


@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)


def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file=database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	with open('database.csv', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer=csv.writer(database)
		csv_writer.writerow([email,subject,message])

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			print(data)
			write_to_file(data)
			write_to_csv(data)

			return redirect('/thankyou.html')

			return 'form submitted'
		except:
			return 'did not save to database'

	else:
		return 'something went wrong'

    # return 'form submitted'