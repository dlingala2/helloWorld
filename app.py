from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Divya Lingala! I am adding my first code change.'

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def about_css():  # put application's code here
    return render_template('about-css.html')

@app.route("/greeting")
def greeting():
    return render_template("greeting.html")

# route for favorite course page
@app.route('/favorite-course')
def favorite_course():
    # get subject and course number from query parameters
    subject = request.args.get('subject', '').strip()
    course_number = request.args.get('course_number', '').strip()
    # render the favorite-course template and pass the values
    return render_template('favorite-course.html', subject=subject, course_number=course_number)

# route for contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    # if the form was submitted, show thank you message
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    # otherwise, show the form
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run()