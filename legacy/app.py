from flask import Flask, request, Response, render_template
from generate_users import fake_people
from spacemen import curr_spacemen
from params import hei_wei
from parser import parse_usr_value, parse_hum_params
from db import run_query, ordering, filter_and

app = Flask(__name__, template_folder="templates")


@app.route('/owner/')
@app.route('/')
def owner():
    owner_name = "Panin Kirill"
    return render_template('st_index.html', message=owner_name)


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


@app.route('/customers/')
def customers():
    query = '''
    SELECT * FROM customers
    '''

    country = request.args.get('country')
    if country:
        param = f" WHERE Country = '{country}'"
        query += param

    fil_and = request.args.get('filter')
    if fil_and:
        param = f" WHERE {filter_and(fil_and)}"
        query += param

    order = request.args.get('ordering')
    if order:
        param = f" ORDER BY {ordering(order)}"
        query += param

    query += ';'
    return str(run_query(query))


@app.route('/employees/')
def employees():
    query = '''
        SELECT * FROM employees;
    '''
    return str(run_query(query))


@app.route('/f/')
def foo():
    query = '''
        SELECT UnitPrice, Quantity FROM invoice_items;
    '''
    results = run_query(query)
    sum_ = 0
    for price, quantity in results:
        sum_ += price * quantity

    return str(sum_)


@app.route('/f2/')
def foo2():
    query = '''
        SELECT SUM(UnitPrice * Quantity) FROM invoice_items;
    '''
    return str(run_query(query))


@app.route('/tracks/')
def tracks():
    query = '''
        SELECT COUNT(*) FROM tracks;
    '''
    return f'Tracks: {run_query(query)}'


@app.route('/names/')
def names():
    query = '''
        SELECT COUNT (DISTINCT FirstName) FROM customers;
    '''
    return f'Distinguished names: {run_query(query)}'


@app.route('/tracks-sec/')
def tracks_sec():
    query = '''
        SELECT Name, Milliseconds FROM  tracks;
    '''
    return f'Songs: {run_query(query)}'


if __name__ == '__main__':
    app.debug = True
    app.run()
