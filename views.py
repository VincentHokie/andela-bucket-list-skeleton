__author__ = 'MacUser'

from . import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello Worldj"


@app.route("/index")
def index():
    return "Hello Worldj"


@app.route("/sign-up", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/login", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/logout", methods=['GET'])
def index():
    return "Hello Worldj"



#bucket list crud routes
@app.route("/create/bucket-list", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/update/bucket-list/<bucketListId>", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/view/bucket-lists", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/delete/bucket-list/<bucketListId>", methods=['POST'])
def index():
    return "Hello Worldj"





#bucket list items crud routes
@app.route("/create/<bucketList>/item", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/update/<bucketList>/item/<itemId>", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/view/<bucketList>/items", methods=['GET', 'POST'])
def index():
    return "Hello Worldj"


@app.route("/delete/bucket-list-item/<itemId>", methods=['POST'])
def index():
    return "Hello Worldj"
