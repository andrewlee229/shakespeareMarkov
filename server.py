from bottle import post, run, route, static_file
import processing.markov

@post('/process')
def process():
	return processing.markov.process_markov("a","b")

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