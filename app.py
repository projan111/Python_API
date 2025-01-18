from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Welcome to my API'}

@app.route('/data', methods=['GET'])
def get_data():
    return {
        'name': 'John Doe',
        'age': 30,
        'occupation': 'Developer'
    }
    
@app.route('/user/<username>')
def greet_user(username):
    return {'message': f'Hello, {username}!'}


@app.route('/query')
def query_example():
    from flask import request
    name = request.args.get('name')
    age = request.args.get('age')
    return {'name': name, 'age': age}


@app.route('/create', methods=['POST'])
def create_user():
    from flask import request
    data = request.json
    return {'message': 'User created', 'data': data}




if __name__ == '__main__':
    app.run(debug=True)


