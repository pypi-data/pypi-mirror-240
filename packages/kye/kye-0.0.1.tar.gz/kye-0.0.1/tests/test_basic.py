from context import kye

def get_errors(text, data):
    api = kye.compile(text)
    model_name = list(api.compiled.keys())[0]
    api.from_records(model_name, data)
    return api.errors

def is_valid(text, data):
    return len(get_errors(text, data)) == 0

def test_value_is_coercible():
    USER = '''
    type UserId: Number

    model User(id) {
        id: UserId,
        name: String,
        is_admin: Boolean,
    }
    '''

    assert is_valid(USER, [{
        'id': 1,
        'name': 'Joe',
        'is_admin': True,
    }])

    assert is_valid(USER, [{
        'id': '1.0',
        'name': 1,
        'is_admin': 1,
    }])

    assert get_errors(USER, [{
        'id': 'user_01',
        'name': 'bill',
        'is_admin': 'sure',
    }]) == {
        ('Number', 'INVALID_VALUE'),
        ('Boolean', 'INVALID_VALUE'),
    }

def test_undefined_columns():
    USER = '''
    model User(id) {
        id: Number,
        name: String+,
        age: Number?,
        tags: String*,
    }
    '''

    assert is_valid(USER, [{
        'id': 1,
        'name': 'Joe',
    }])

def test_validate_cardinality():
    USER = '''
    model User(id) {
        id: Number,
        name: String+,
        age: Number?,
        tags: String*,
    }
    '''

    assert is_valid(USER, [{
        'id': 1,
        'name': 'Joe',
        'age': None,
        'tags': [],
    }])

    assert get_errors(USER, [{
        'id': 1,
        'name': None,
        'age': 21,
    }, {
        'id': 1,
        'age': 23,
    }]) == {
        ('User.name', 'NOT_NULLABLE'),
        ('User.age', 'NOT_MULTIPLE'),
    }

def test_validate_recursive():
    USER = '''
    model User(id) {
        id: Number,
        friends: User*,
    }
    '''

    assert is_valid(USER, [{
        'id': 1,
        'friends': [{
            'id': 2,
            'friends': [{ 'id': 1 }],
        },{
            'id': 3,
            'friends': [{ 'id': 1 }, { 'id': 2 }],
        }],
    }])

def test_conflicting_loads():
    api = kye.compile('''
    model User(id) {
        id: Number,
        name: String,
    }
    ''')

    api.from_records('User', [{
        'id': 1,
        'name': 'Joe',
    }, {
        'id': 2,
        'name': 'Bill',
    }])

    api.from_records('User', [{
        'id': 1,
        'name': 'Joey', # conflicting name
    }])

    assert api.errors == {
        ('User.name', 'NOT_MULTIPLE')
    }

def test_index_collision():
    USER = '''
    model User(id)(name) {
        id: Number,
        name: String,
    }
    '''

    assert get_errors(USER, [{
        'id': 1,
        'name': 'Joe',
    }, {
        'id': 2,
        'name': 'Joe', # two people are not allowed to have the same name of Joe
    }]) == {
        ('User', 'NON_UNIQUE_INDEX'),
    }