__author__ = 'MacUser'

from . import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello Worldj"



@app.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    return "Hello Worldj"


@app.route("/login", methods=['GET', 'POST'])
def login():
    return "Hello Worldj"


@app.route("/logout", methods=['GET'])
def logout():
    return "Hello Worldj"



# bucket list crud routes
@app.route("/create/bucket-list", methods=['GET', 'POST'])
def create_bucket_list():
    return "Hello Worldj"


@app.route("/update/bucket-list/<bucket_list_id>", methods=['GET', 'POST'])
def update_bucket_list(bucket_list_id):
    return "Hello Worldj"


@app.route("/view/bucket-lists", methods=['GET', 'POST'])
def view_bucket_list():
    return "Hello Worldj"


@app.route("/delete/bucket-list/<bucket_list_id>", methods=['POST'])
def delete_bucket_list(bucket_list_id):
    return "Hello Worldj"





# bucket list items crud routes
@app.route("/create/<bucket_list>/item", methods=['GET', 'POST'])
def create_bucket_list_item(bucket_list):
    return "Hello Worldj"


@app.route("/update/<bucket_list>/item/<item_id>", methods=['GET', 'POST'])
def update_bucket_list_item(bucket_list, item_id):
    return "Hello Worldj"


@app.route("/view/<bucket_list>/items", methods=['GET', 'POST'])
def view_bucket_list_item(bucket_list):
    return "Hello Worldj"


@app.route("/delete/bucket-list-item/<item_id>", methods=['POST'])
def delete_bucket_list_item(item_id):
    return "Hello Worldj"
