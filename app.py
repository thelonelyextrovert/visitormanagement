from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def visitor():
    return render_template('visitor.html')

if __name__ == "__main__":
    app.run()
