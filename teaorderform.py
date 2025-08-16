from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index.html')
@app.route('/')
def tea():
    return render_template('tea_form.html')


@app.route('/order', methods=['POST'])
def order():
    print("order route called")
    print("form data:", request.form)
    user = request.form.get('user', '無名')
    sugar = request.form.get('sugar', '無糖')
    area = request.form.get('area', '無區域')
    mix = request.form.getlist('mix')

    print("user:", user)
    print("sugar:", sugar)
    print("area:", area)
    print("mix:", mix)

    return render_template("result.html",
                           user=user,
                           sugar=sugar,
                           mix=mix,
                           area=area)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)