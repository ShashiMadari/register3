from flask import Flask, render_template, request, redirect, url_for # type: ignore

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        full_name = request.form['fullName']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        gender = request.form['gender']
        course = request.form['course']
        address = request.form['address']
        profile_picture = request.files['profilePicture']

        # Save profile picture
        profile_picture_path = 'static/uploads/' + profile_picture.filename
        profile_picture.save(profile_picture_path)

        # Pass data to success page
        return render_template('success.html', full_name=full_name, email=email, phone=phone,
                               dob=dob, gender=gender, course=course, address=address, 
                               profile_picture_path=profile_picture_path)

    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
