from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask

app = Flask(__name__)


def score_server():
    # Open the file in read mode
    file = open(SCORES_FILE_NAME, "r")

    # Read the contents of the file
    contents = file.read()

    # Close the file
    file.close()

    title = "Scores Game"

    if BAD_RETURN_CODE != 0:
        return generate_html(title, f'<h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>')
    else:
        return generate_html(title, f'<h1>The score is <div id="score">{contents}</div></h1>')


def generate_html(title, body):
    html = "<html><head><title>{}</title></head><body>{}</body></html>".format(title, body)
    return html


@app.route('/')
def hello():
    return score_server()


app.run(host="0.0.0.0", port=80)
