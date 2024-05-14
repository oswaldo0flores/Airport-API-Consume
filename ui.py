# HW8 - Consume API    Oswaldo Flores
"""
To handle input and output.

The run method will start the application and ask data from the user. The display data
method will display the data to the user and ask if they would like to see more of their data.
The display given text will tell the user that a certain parameter contains data. The description
method will tell the user how to use this application properly. The user input method just
get data from the user, zero validation. The validate id method will only get validate ids entered
by the user. The validate yes no method will validate the user input if they enter a yes or a no.
The format string method will properly format the given string.

RESULT_MAXIMUM_DISPLAY: The amount of results the user should see at a time.
ZERO_LENGTH: The length of a collection or a string is zero.
"""
from objects import Results

RESULT_MAXIMUM_DISPLAY = 999
ZERO_LENGTH = 0


def run() -> None:
    """
    To start the application.

    To start the application. This application will ask the user for 7 inputs
    to be entered. It is okay if the user enter nothing. I assume the user will
    not properly format their enter values. So I properly format the user input
    because the user input will build my api call. Building the actucally api
    url and calling the api does not happen in this module. It happens in the dal
    module. Once I get the data from the api call, display the data to the user.
    """
    description()
    valid_ids = validate_id()
    display_given_text(valid_ids, 'id')
    name = format_string(user_input('Enter name(s) > '))
    display_given_text(name, 'name')
    city = format_string(user_input('Enter city > '))
    display_given_text(city, 'city')
    country = format_string(user_input('Enter country > '))
    display_given_text(country, 'country')
    types = format_string(user_input('Enter type(s) > '))
    display_given_text(types, 'type')
    iata = format_string(user_input('Enter iata(s) > '))
    display_given_text(iata, 'iata')
    icao = format_string(user_input('Enter icao(s) > '))
    display_given_text(icao, 'icao')
    url = Results.build_url(valid_ids, name, city, country, types, iata, icao)
    results = Results.load(url)
    display_data(results)


def display_data(results: list):
    """
    To display the given results to the user.

    To display the given results to the user. When I first ran this application,
    I realize pycharm has an output limit. Pycharm will display the newest
    output only. So, I decided the user should only see 1000 of the results at a
    time. I will ask the user if they would like to see the next 1000 results.
    It is okay if the given results has no data. It means the api call could not find
    any results.

    :param results: A list of data given by the api call.
    :type results: list
    """
    print()
    counter = 0
    if results is None:
        print('An error has occur.')
        return
    if len(results) != ZERO_LENGTH:
        maximum_length = len(results)
        for index in range(maximum_length):
            print(results[index])
            counter += 1
            if counter == RESULT_MAXIMUM_DISPLAY:
                answer = validate_yes_no()
                if answer == 'yes':
                    counter = 0
                else:
                    return
    else:
        print('No Data Found')


def display_given_text(text: str, text_type: str) -> None:
    """
    To display if the user provide data.

    To display if the user provide data. Tell the user that whether they provide
    data or no data at all. The given text will determine if the user provide data.

    :param text: Represents what the user entered.
    :type text: str
    :param text_type: Represent what the text is about.
    :type text_type: str
    """
    if text != '':
        print(f'Values given for {text_type}. Moving on.')
    else:
        print(f'Empty string for {text_type}. Moving on.')


def description() -> None:
    """
    To display the description of this application.

    To display the description of this application. This will tell the user how
    to enter the data. This should tell what type of data the user should enter.
    """
    print('You will be ask to enter 7 text box entries. It is okay if you enter nothing.')
    print('An entry can have multiple values as long they are separated by a comma.')
    print('Example: id > 1,2,3,1221')
    print('If a comma belongs to a word, enclose the comma with double quotes.')
    print('Example: name > Name1,"Name2_1, Name2_2"')
    print('------------------------------------------------------------------------------')
    print('ID(s): Unique Identifier')
    print('Name(s): The name of an airport, station, port, etc...')
    print('City: The city name')
    print('Country: The country name')
    print('Type: Airport, station, port, etc...')
    print('IATA: 3-letter IATA code')
    print('ICAO: 4-letter ICAO code')
    print('------------------------------------------------------------------------------')


def user_input(prompt: str) -> str:
    """
    Prompt the user for something.

    Prompt the user for something. This method should not validate the
    user input.

    :param prompt: Tells the user what to enter.
    :type prompt: str
    :return: Anything the user type. Can be empty.
    """
    return input(prompt)


def validate_id(prompt: str = 'Enter ID(s) > ') -> str:
    """
    To validate user id.

    To validate user id. Separate the given value by a comma and determine if the
    user enter an integer for each "id". This method will not ask the user to enter
    a new set of ids if they enter an invalid id. Instead, I will take the valid
    ids and put it into a new string.

    :param prompt: To tell the user to enter ID(s).
    :type prompt: str
    :return: A string of valid id(s)
    """
    valid_ids = ''
    user_ids = user_input(prompt)
    ids = user_ids.split(',')
    for single_id in ids:
        if single_id.strip(' ').isdigit():
            valid_ids = f'{int(single_id)},{valid_ids}'
    return valid_ids.strip(',')


def validate_yes_no(prompt: str = 'Would you like to see your next 1000 results? ') -> str:
    """
    Validate user input.

    Validate user input if the enter a yes or a no. Casing should not matter. Keep
    asking the user the same question until they enter a yes or a no.

    :param prompt: Ask the user for a yes or no question.
    :type prompt: str
    :return: A yes or a no.
    """
    while True:
        answer = user_input(prompt)
        if answer.lower() == 'yes' or answer.lower() == 'no':
            return answer.lower()


def format_string(line: str, delimiter: str = ',', enclose: str = '"', new_whitespace: str = '_') -> str:
    """
    To format the user enter string properly.

    To format the user enter string properly. The delimiter is used to parse a string.
    Enclose means that everything within enclose belongs to that word. The new whitespace
    will remove every whitespace and converted to this new whitespace character.

    :param line: User input string.
    :type line: str
    :param delimiter: What separates a string.
    :type delimiter: str
    :param enclose: What enclose a word in a string.
    :type enclose: str
    :param new_whitespace: To remove whitespace with this new "whitespace".
    :type new_whitespace: str
    :return: A proper format string.
    """
    valid_line = ''
    word = ''
    is_enclose = False
    for character in line:
        word = f'{word}{character}'
        if character == enclose:
            is_enclose = not is_enclose
        elif character == delimiter and not is_enclose:
            word = word.strip(' ')
            word = word.replace(' ', new_whitespace)
            word = word.rstrip(delimiter)
            valid_line = f'{word},{valid_line}'
            word = ''
    word = word.strip(' ').replace(' ', new_whitespace)
    word = word.rstrip(delimiter)
    if word != '' and word != delimiter:
        valid_line = f'{word},{valid_line}'
    return valid_line.lower().strip(delimiter)
