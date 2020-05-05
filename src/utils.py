def parse_usr_value(usr_value: str):
    if not usr_value.replace('.', ' ', 1).isdigit() and '-' not in usr_value:
        return f'Incorrect value: {usr_value}. Number has to be integer not float'

    if not usr_value.isdigit():
        return f'Incorrect value: {usr_value}. Enter a number between [1, 100]'

    usr_value = int(usr_value)

    if usr_value > 100 or usr_value < 1:
        return f'Incorrect value: {usr_value}. Enter a number in range [1, 100]'

    return usr_value


def clear_table_parser(request, param):
    available_params = '1: Clear sheet, 2: Get sheet name'
    if param == 'digit':
        if not request.isdigit():
            return f'Incorrect input: {request}. Available requests: {available_params}. '
        request = int(request)
        if request > 2 or request < 1:
            return f'Incorrect value: {request}. Select an option <br/> {available_params}'
    if param == 'alpha':
        if not request.isalpha():
            return f'Incorrect input: {request}. Available requests: {available_params}. '
        request = request.capitalize()
    if param == 'id':
        if not request.isdigit():
            return f'Incorrect input: {request}. Enter valid value. '
        request = int(request)
    return request
