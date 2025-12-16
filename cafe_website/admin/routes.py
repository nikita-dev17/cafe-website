import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, session
from ..models import Meal, bcrypt, db

admin_bp = Blueprint("admin", __name__, template_folder="templates")

load_dotenv()
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD_HASH = os.getenv("ADMIN_PASSWORD_HASH")

def admin_required(f):
    from functools import wraps

    @wraps(f)
    def wrapper(*args, **kwargs):
        if not session.get("is_admin"):
            return redirect(url_for("admin.admin_login"))
        return f(*args, **kwargs)

    return wrapper


@admin_bp.route("/login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email != ADMIN_EMAIL or not bcrypt.check_password_hash(ADMIN_PASSWORD_HASH, password):
            error = "Неправильний email або пароль!"
        else:
            session["is_admin"] = True
            return redirect(url_for("admin.admin_dashboard"))

    return render_template("admin_login.html", error=error)

@admin_bp.route("/")
@admin_required
def admin_dashboard():
    meals = Meal.query.all()
    return render_template("admin_dashboard.html", meals=meals)


@admin_bp.route("/add_meal", methods=["GET", "POST"])
@admin_required
def add_meal():
    if request.method == "POST":
        meal = Meal(
            name=request.form["name"],
            description=request.form["description"],
            price=float(request.form["price"]),
            img=request.form["img"]
        )
        db.session.add(meal)
        db.session.commit()

        return redirect(url_for("admin.admin_dashboard"))

    return render_template("admin_add_meal.html")

@admin_bp.route("/edit_meal/<int:meal_id>", methods=["GET", "POST"])
@admin_required
def edit_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)

    if request.method == "POST":
        meal.name = request.form["name"]
        meal.description = request.form["description"]
        meal.price = float(request.form["price"])
        meal.img = request.form["img"]

        db.session.commit()
        return redirect(url_for("admin.admin_dashboard"))

    return render_template("admin_edit_meal.html", meal=meal)

@admin_bp.route("/delete_meal/<int:meal_id>", methods=["POST", "GET"])
@admin_required
def delete_meal(meal_id):
    meal = Meal.query.get_or_404(meal_id)
    db.session.delete(meal)
    db.session.commit()
    return redirect(url_for("admin.admin_dashboard"))



@admin_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("admin.admin_login"))

