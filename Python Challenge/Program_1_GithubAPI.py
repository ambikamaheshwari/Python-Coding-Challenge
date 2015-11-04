__author__ = 'Ambika'

import urllib.request
import json
import sys
import string

if sys.version_info[0] < 3:
    input = raw_input

def print_github_graph(search_term):

    github_url = "https://api.github.com/search/users?q=%s"%search_term
    response = urllib.request.urlopen(github_url)
    data = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
    alphabet = string.ascii_lowercase #alphabet contains lower a-z as string
    dict_alpha = dict() # Creating empty dictionary
    data_str = ""
    output = ""
    ast = '*'
    data_login = []
    temp = 0
    dict_alpha['others'] = ""

    for k in range(0,len(data['items'])):
        # Checking for type as User
        if (data['items'][k]['type']) == 'User':
            str_data = data['items'][k]['login']
            data_login.append(str_data.lower())
    # Sort over the results by login attribute.
    data_login = sorted(data_login)
    # if users are greater than 5, then limiting it upto 5
    if len(data_login) >= 5:
        for i in data_login:
            if temp < 5:
                data_str += str(i)
                temp = temp + 1
    else:
        for i in data_login:
                data_str += str(i)
    # creating dictionary for all the alphabet in the login name
    for d in data_str.lower():
        if d in alphabet:
            if d not in dict_alpha:
               dict_alpha[d] = ast
            else:
               dict_alpha[d] = dict_alpha[d] + ast
        else:
            dict_alpha['others'] = dict_alpha['others'] + ast
    # updating character as null if it doesnt contain in login
    for a in alphabet:
        if a not in dict_alpha:
            dict_alpha[a] = ""
    others = ['others']
    # sorting the alphabets and printing
    for key, value in sorted(dict_alpha.items()):
        if key not in others:
            output += ("{} : {}".format(key, value)) + "\n"
    output += "others:"+dict_alpha['others']

    return output

print(print_github_graph(input('Search Term: ')))
