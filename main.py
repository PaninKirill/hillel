def parse(query: str) -> dict:
    result = {}
    try:
        query = query.split('?')[1]
        for j in query.split('&'):
            if len(j) != 0:
                if len(j.split('=')) == 1 and j != '':
                    key, val = j, None
                    result[key] = ''
                else:
                    key, val = j.split('=')
                    result[key] = val
    except IndexError:
        pass
    return result


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://maps.googleapis.com/'
                 'maps/api/staticmap?size=600x400&zoom=8&center=42,-70') == {'size': '600x400', 'zoom': '8',
                                                                             'center': '42,-70'}
    assert parse(
        'https://www.google.com/search?sxsrf=ALeKk03...&q=some+query&oq=some+query&gs_lcp=CgZwc...&sclient=psy-ab') == {
               'sxsrf': 'ALeKk03...', 'q': 'some+query', 'oq': 'some+query', 'gs_lcp': 'CgZwc...', 'sclient': 'psy-ab'}
    assert parse('https://maps.googleapis.com/maps/api/staticmap?size=600x400') == {'size': '600x400'}
    assert parse('http://www.foo.bar/image-2.html?w=100&h=50') == {'w': '100', 'h': '50'}
    assert parse('https://someurl.com/with/query_string?i=main&mode=front&sid=12ab&enc=Hello') == {'i': 'main',
                                                                                                   'mode': 'front',
                                                                                                   'sid': '12ab',
                                                                                                   'enc': 'Hello'}
    assert parse('https://someurl.com/with/query_string?a=1&b=2&b=3') == {'a': '1', 'b': '3'}
    assert parse('http://www.example.com/t.html?a=1&b=3&c=m2-m3-m4-m5&self') == {'a': '1', 'b': '3', 'c': 'm2-m3-m4-m5',
                                                                                 'self': ''}
    assert parse('http://example.com/a=1&b=2&c') == {}
    assert parse('http://example.com/?a=1&b=2&c') == {'a': '1', 'b': '2', 'c': ''}
    assert parse('http://example.com/foo?a=1&b=2&c') == {'a': '1', 'b': '2', 'c': ''}


def parse_cookie(query: str) -> dict:
    result = {}

    for j in query.split(';'):
        if len(j) != 0:
            if len(j.split('=')) >= 3:
                res = [j for j in j.split('=')]
                key = res[0]
                index = j.index('=')
                result[key] = j[index + 1:]
            if len(j.split('=')) == 2:
                key, val = j.split('=')
                result[key] = val
            if len(j.split('=')) == 1:
                key, val = j, None
                result[key] = ''
    return result


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima=User=Super;age=28;') == {'name': 'Dima=User=Super', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;Gender=male') == {'name': 'Dima', 'age': '28', 'Gender': 'male'}
    assert parse_cookie(
        'NAME=VALUE;expires=DATE;path=PATH;domain=DOMAIN_NAME;secure=;') == {
               'NAME': 'VALUE', 'expires': 'DATE', 'path': 'PATH', 'domain': 'DOMAIN_NAME', 'secure': ''}
    assert parse_cookie(
        '__Secure-name=value;max-age=31536000;domain=example.com;path=/') == {
               '__Secure-name': 'value', 'max-age': '31536000', 'domain': 'example.com', 'path': '/'}
    assert parse_cookie('name=new_value;temperature=20"Celsius"') == {'name': 'new_value', 'temperature': '20"Celsius"'}
    assert parse_cookie('encoding=utf-8;') == {'encoding': 'utf-8'}
    assert parse_cookie('lang=en-US;Path=/;Domain=example.com;SID=31d4d96e407aad42') == {'lang': 'en-US', 'Path': '/',
                                                                                         'Domain': 'example.com',
                                                                                         'SID': '31d4d96e407aad42'}
    assert parse_cookie(
        'name=1P_JAR;Content=2020-4-22-20;Domain=.google.com;Path=/;Send for=Secure connections only;Created=Wednesday,'
        ' April 22, 2020 at 11:26:13 PM; Expires=Friday, May 22, 2020 at 11:26:13 PM') == {
               'name': '1P_JAR', 'Content': '2020-4-22-20', 'Domain': '.google.com', 'Path': '/',
               'Send for': 'Secure connections only', 'Created': 'Wednesday, April 22, 2020 at 11:26:13 PM',
               ' Expires': 'Friday, May 22, 2020 at 11:26:13 PM'}
    assert parse_cookie('123') == {'123': ''}
    assert parse_cookie('name=;secure;httponly') == {'name': '', 'secure': '', 'httponly': ''}
