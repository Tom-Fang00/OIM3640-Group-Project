from flask import Flask, render_template, request
from recipe import fetch
import recipe

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        category = request.form.get('category')
        area = request.form.get('area')
        ingredient = format(request.form['text'])
        food = fetch(category, area, ingredient)
        imageId = food[0]
        foodName = food[1]
        return render_template("index.html", imageId=imageId, category=category, area=area, ingredient=ingredient, foodName = foodName)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
