from name_function import get_formatted_name

def test_get_formatted_name():
    formatted_name = get_formatted_name('liu', 'peijun')
    assert formatted_name == 'Liu Peijun'
    print('test_get_formatted_name pass')