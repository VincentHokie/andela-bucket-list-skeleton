__author__ = 'MacUser'

from flask import render_template
from . import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello Worldj"



@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return render_template("auth/sign-up.html",
                           title='Create Profile')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("auth/login.html",
                           title='Login')


@app.route("/logout", methods=['GET'])
def logout():
    return render_template("auth/logout.html",
                           title='Logout')



# bucket list crud routes
@app.route("/create/bucket-list", methods=['GET', 'POST'])
def create_bucket_list():
    return render_template("bucket-list/create.html",
                           title='Create Bucket List')


@app.route("/update/bucket-list/<bucket_list_id>", methods=['GET', 'POST'])
def update_bucket_list(bucket_list_id):
    return render_template("bucket-list/update.html",
                           title='Update Bucket List')


@app.route("/view/bucket-lists", methods=['GET', 'POST'])
def view_bucket_list():
    return render_template("bucket-list/view.html",
                           title='View Bucket Lists')


@app.route("/delete/bucket-list/<bucket_list_id>", methods=['POST'])
def delete_bucket_list(bucket_list_id):
    return "Hello Worldj"





# bucket list items crud routes
@app.route("/create/<bucket_list>/item", methods=['GET', 'POST'])
def create_bucket_list_item(bucket_list):
    return render_template("bucket-list-item/view.html",
                           title='View Bucket Lists')


@app.route("/update/<bucket_list>/item/<item_id>", methods=['GET', 'POST'])
def update_bucket_list_item(bucket_list, item_id):
    return render_template("bucket-list-item/view.html",
                           title='View Bucket Lists')


@app.route("/view/<bucket_list>/items", methods=['GET', 'POST'])
def view_bucket_list_item(bucket_list):
    return render_template("bucket-list-item/view.html",
                           title='View Bucket Lists')


@app.route("/delete/bucket-list-item/<item_id>", methods=['POST'])
def delete_bucket_list_item(item_id):
    return "Hello Worldj"
