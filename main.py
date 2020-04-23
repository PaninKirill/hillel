def parse(query: str) -> dict:
    result = {}
    try:
        query = query.split('?')[1]
        for j in query.split('&'):
            try:
                key, val = j.split('=')
                result[key] = val
            except (ValueError, IndexError):
                if len(j) >= 1:
                    key, val = j, None
                    result[key] = ''
    except (ValueError, IndexError):
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
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}


