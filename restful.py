from flask import Flask, jsonify, request
app = Flask(__name__)

# picture a list of items from the db
languages = [{'name': 'py'}, {'name': 'js'}, {'name': 'php'}]


# using get request -- for reading date e.g. from db
@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': "Here we go! You can open the endpoints '/lang' and '/lang/<string:name>' in the browser OR these on Postman POST '/lang', PUT '/lang/<string:name>', DELETE '/lang/<string:name>'"})

@app.route('/lang', methods=['GET'])
def get_all():
    # return a dict of languages
    return jsonify({'languages': languages})

# route to <datatype:key>
@app.route('/lang/<string:name>', methods=['GET'])
def get_one(name):
    # get dict for and return value of a key in the dict
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'languages': langs[0]})


# using post request -- for data insertion
@app.route('/lang', methods=['POST'])
def create_one():
    # append a supplied language to the languages dict
    language = {'name': request.json['name']}
    languages.append(language)

    return jsonify({'languages': languages})


# using put request -- for data update
@app.route('/lang/<string:name>', methods=['PUT'])
def edit_one(name):
    # get dict for and return value of a key in the dict
    langs = [language for language in languages if language['name'] == name]

    # edit the lang -- this updates the languages dict as well
    langs[0]['name'] = request.json['name']

    # so a put request in postman, say on py, 
    # and supplying a json of name:Python 
    # should return the updated value as stated below
    # and update the languages dict as well
    return jsonify({'language': langs[0]})


# using delete request -- for data deletion
@app.route('/lang/<string:name>', methods=['DELETE'])
def remove_one(name):
    # get dict for the key to be deleted
    lang = [language for language in languages if language['name'] == name]
    languages.remove(lang[0])
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
