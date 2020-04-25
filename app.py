from flask import Flask, request, Response, render_template
from generate_users import fake_people
from spacemen import curr_spacemen
from params import hei_wei
from parser import parse_usr_value, parse_hum_params

app = Flask(__name__, template_folder="templates")


@app.route('/owner/')
def owner():
    owner_name = "Panin Kirill"
    return render_template('index.html', message=owner_name)


@app.route('/generate-users/')
def users():
    usr_value = parse_usr_value(request.args.get('usr_value', '100'))
    if type(usr_value) is str:
        return Response(usr_value)
    response = Response(fake_people(usr_value))
    return response


@app.route('/mean/')
def users_values():
    """
    Returns default data if value missing: avg height/weight for route /mean/
    Output data could be changed according to the list of params:
    available_params = '1: weight/height(AVG), 2: weight/height(MIN), 3: weight/height(MAX)'
    In this case use route /mean/?hum_params=
    """
    hum_params = parse_hum_params(request.args.get('hum_params', '1'))
    if type(hum_params) is str:
        return Response(hum_params)
    response = Response(hei_wei(hum_params))
    return response


@app.route('/space/')
def spacemen():
    response = Response(curr_spacemen())
    return response


@app.route('/requirements/')
def read_data():
    with open('req.txt', encoding='utf-8') as f:
        data = f.read()
        f.close()
        return data


if __name__ == '__main__':
    app.debug = False
    app.run()

