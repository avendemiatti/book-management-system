from flask import Flask, render_template, request, redirect, url_for
from service.category_service import CategoryService

app = Flask(__name__)
category_service = CategoryService()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/categories')
def list_categories():
    categories = category_service.list_categories()
    return render_template('categories.html', categories=categories)

@app.route('/categories/new', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form['name']
        category_service.add_category(name)
        return redirect(url_for('list_categories'))
    return render_template('new_category.html')

if __name__ == "__main__":
    app.run(debug=True)
