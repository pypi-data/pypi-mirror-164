from flask import Flask, request

app = Flask(
  __name__,
  static_url_path='',
  static_folder='./'
) 

def main():
  app.run(port=8000, host='0.0.0.0')

main()