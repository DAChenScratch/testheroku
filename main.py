import bottle
@bottle.route('/') 
def index():
  return 'You can write html here'
bottle.run(host='0.0.0.0', port=1234)
