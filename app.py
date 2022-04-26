from flask import Flask, render_template
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/i')
def i():
    return render_template('i.html')

if __name__ == "__main__":
    app.run(debug=True)