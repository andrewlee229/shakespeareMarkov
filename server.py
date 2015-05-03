from bottle import post, request, route, run, static_file
import json, processing.markov

@post('/generate_markov')
def process():
	play = request.forms.get('play')
	persona = request.forms.get('persona')
	return processing.markov.process_markov(play, persona)

@post('/get_personas')
def process():
	play = request.forms.get('play')
	return json.dumps(processing.markov.grab_personas(play))

@route('/')
def root():
    print("root!") 
    return static_file('index.html', root='./resources')

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