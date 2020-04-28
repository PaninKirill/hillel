def parse_usr_value(usr_value: str) -> int or str:
    if not usr_value.isdigit():
        return f'Incorrect value: {usr_value}. The request must contain a number between [1, 150]'

    usr_value = int(usr_value)

    if usr_value > 150 or usr_value < 1:
        return f'Incorrect value: {usr_value}. Enter number in range [1, 150]'

    return usr_value


def parse_hum_params(hum_params: str) -> int or str:
    available_params = '1: weight/height(AVG), 2: weight/height(MIN), 3: weight/height(MAX)'
    if not hum_params.isdigit():
        return f'Incorrect input: {hum_params}. Available requests: {available_params}. ' \
               f'Chose argument between 1-3'

    hum_params = int(hum_params)

    if hum_params > 3 or hum_params < 1:
        return f'Incorrect value: {hum_params}. Enter number in range [1, 3]'

    return hum_params

