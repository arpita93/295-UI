from flask import Flask, Response, request, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
#def hello_world():
#	return 'Hello World!'

def index():
    return render_template("page1.html")

@app.route('/ml.html', methods = ['GET', 'POST'])
def machine_learning():
    return render_template("ml.html")

@app.route('/nlp.html', methods = ['GET', 'POST'])
def nlp():
    return render_template("nlp.html")

@app.route('/cv.html', methods = ['GET', 'POST'])
def cv():
    return render_template("cv.html")

@app.route('/speech.html', methods = ['GET', 'POST'])
def speech():
    return render_template("speech.html")


@app.route('/img_domain.html', methods = ['GET', 'POST'])
def domain():
    return render_template("img_domain.html")


@app.route('/img_rec_tree.html', methods = ['GET', 'POST'])
def visual_example():
    return render_template("img_rec_tree.html")

@app.route('/text_CI.html', methods = ['GET', 'POST'])
def text_CI():
    return render_template("text_CI.html")

@app.route('/textI.html', methods = ['GET', 'POST'])
def text_input():
    return render_template("textI.html")

@app.route('/text_context.html', methods = ['GET', 'POST'])
def text_context():
    return render_template("text_context.html")

@app.route('/voice_CI.html', methods = ['GET', 'POST'])
def voice_CI():
    return render_template("voice_CI.html")

@app.route('/voice_input.html', methods = ['GET', 'POST'])
def voice_input():
    return render_template("voice_input.html")

@app.route('/voice_context.html', methods = ['GET', 'POST'])
def voice_context():
    return render_template("voice_context.html")


if __name__ == "__main__":
    app.run(debug=True)



