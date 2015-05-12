from bottle import post, request, route, run, static_file
import json, processing.markov

#When user clicks submit, this is called to generate the line
@post('/generate_markov')
def process():
	play = request.forms.get('play')
	persona = request.forms.get('persona')
	return processing.markov.process_markov(play, persona)

#When a play is chosen, this is called to get all of the personas
@post('/get_personas')
def process():
	play = request.forms.get('play')
	return json.dumps(processing.markov.grab_personas(play))

@route('/')
def root():
    return static_file('index.html', root='./resources')

@route('/about')
def root():
    return static_file('about.html', root='./resources')

@route('/css/<filename>')
def server_static(filename):
        return static_file(filename, root='./css')

@route('/js/<filename>')
def server_static(filename):
        return static_file(filename, root='./js')

@route('/plays/<filename>')
def server_static(filename):
        return static_file(filename, root='./plays')

run(host='localhost', port=8080)