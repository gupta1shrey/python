from flask import Flask, request

app = Flask(__name__)

@app.route('/save_data', methods=['POST'])
def save_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with open('data.txt', 'a') as file:
        file.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n")

    return 'Data saved successfully!'

if __name__ == '__main__':
    app.run()