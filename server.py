from bottle import run, route, static_file

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


run(host='localhost', port=8080)