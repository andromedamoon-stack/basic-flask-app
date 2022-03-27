from flask import Flask, render_template

app = Flask(
  __name__,
  template_folder='templates',
  static_folder = 'static'
)
@app.route('/')
def hello():
  return("Hello,World!")

if __name__ == '__main__':
  app.run(
    host='0.0.0.0',
    debug = True,
    port=8080
  )