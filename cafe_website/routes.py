from flask import Blueprint, render_template
from .models import Meal

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/about")
def about():
    return render_template("about.html")

@main_bp.route("/menu")
def menu():
    meals = Meal.query.all()
    return render_template("menu.html", meals=meals)
