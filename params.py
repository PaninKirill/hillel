def hei_wei(hum_params: int = 1):
    with open('hw.csv', encoding='utf-8') as f:
        read_data = f.read()
        data = read_data.split('\n')
        headers = data[0].split(',')
        data = data[1:]

        result = {}
        for row in data:
            hei = row.split(',')[1]
            hei_res = float(hei.strip()) * 2.54
            wei = row.split(',')[2]
            wei_res = float(wei.strip()) * 0.453592
            result[hei_res] = result.get(hei_res, wei_res)
        f.close()

    if hum_params == 1:
        return f'Weight(AVG): {round(sum(result.values()) / len(result), 2)} kg, ' \
               f'Height(AVG): {round(sum(result.keys()) / len(result), 2)} cm'
    elif hum_params == 2:
        return f'Weight(MIN): {round(min(result.values()), 2)} kg, ' \
               f'Height(MIN): {round(min(result.keys()), 2)} cm'
    elif hum_params == 3:
        return f'Weight(MAX): {round(max(result.values()), 2)} kg, ' \
               f'Height(MAX): {round(max(result.keys()), 2)} cm'
