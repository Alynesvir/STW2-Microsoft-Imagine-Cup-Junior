from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/suggestions', methods=['POST'])
def suggestions():
    clothing_type = request.form['type']

    suggestions = []
    if clothing_type == 'shirt':
        suggestions.append(random.choice(['t-shirt', 'button-up', 'sweater']))
    elif clothing_type == 'pants':
        suggestions.append(random.choice(['jeans', 'khakis', 'leggings']))
    elif clothing_type == 'dress':
        suggestions.append(random.choice(['maxi', 'midi', 'mini']))
    else:
        suggestions.append(random.choice(['here is our suggestion!']))

    return render_template('suggestions.html', suggestions=suggestions)
@app.route("/submit", methods=["POST"])
def submit():
  # Get the user's input
  color = request.form["color"]
  style = request.form["style"]
  design = request.form["design"]
  size = request.form["size"]

  # Render the results page
  return render_template("suggestions.html", color=color, style=style, design=design, size=size)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
