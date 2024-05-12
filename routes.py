from flask import render_template, abort, session, app


class Car:
    pass


@app.route('/cars-list/<int:id>')
def car_detail(id):
    car = session.query(Car).get(id)
    if car:
        return render_template("car_detail.html", car=car)
    else:
        abort(404)



