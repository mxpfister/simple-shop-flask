from flask import Flask, render_template, request, session

from controller.accountcontroller import AccountController
from controller.payment import PaymentController
from controller.productcontroller import ProductController
from controller.reviewcontroller import ReviewController

app = Flask(__name__, template_folder="../templates")

ac_controller = AccountController()
pc_controller = ProductController()
rv_controller = ReviewController()
py_controller = PaymentController()

app.secret_key = "dsuigwhewiwefh"

ac_controller.initial_admin()
pc_controller.initial_products()
rv_controller.initial_reviews()


@app.route("/")
def homepage():
    return render_template("ShopHomepage.html")


@app.route("/login", methods=['POST'])
def login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    account = ac_controller.login(username=entered_username, password=entered_password)
    if account is not None:
        if account.role == "User":
            session["ID"] = account.ID
            session["role"] = account.role
            session["firstname"] = account.firstname
            session["lastname"] = account.lastname
            session["birthday"] = account.birthday
            session["username"] = account.username
            session["password"] = account.password
            session.modified = True
            return render_template("login_homepage.html")
        elif account.role == "Admin":
            session["ID"] = account.ID
            session["role"] = account.role
            session["firstname"] = account.firstname
            session["lastname"] = account.lastname
            session["birthday"] = account.birthday
            session["username"] = account.username
            session["password"] = account.password
            session.modified = True
            return render_template("admin_homepage.html")
    return render_template("ShopHomepage.html")


@app.route("/showProducts")
def all_products():
    allProducts = pc_controller.all_products
    return render_template("products.html", products=allProducts)


@app.route("/addtoCart", methods=['POST'])
def add_to_cart():
    allProducts = pc_controller.all_products
    entered_pID = request.form.get("productID")
    entered_quantity = request.form.get("quantity")
    valid_pID = pc_controller.find_product(product_id=entered_pID)
    if valid_pID is not None:
        cart = pc_controller.add_to_cart(product_id=entered_pID, quantity=entered_quantity)
        if cart:
            success = "We have added the product " + entered_pID + " " + entered_quantity + " times to your cart."
            return render_template("products.html", success=success, products=allProducts)
        else:
            error = "Sorry, please check the quantity of the product."
            return render_template("products.html", error=error, products=allProducts)
    else:
        error = "Sorry, no product found!"
        return render_template("products.html", error=error, products=allProducts)


@app.route("/showCart")
def show_cart():
    user_cart = pc_controller.user_cart
    return render_template("usercart.html", user_cart=user_cart)


@app.route("/checkout")
def checkout():
    if len(pc_controller.user_cart) >= 1:
        cart_total = round(pc_controller.cart_total(), 2)
        return render_template("checkout.html", cart_total=cart_total)
    elif len(pc_controller.user_cart) == 0:
        allProducts = pc_controller.all_products
        error = "Sorry, you need products in your cart!"
        return render_template("products.html", error=error, products=allProducts)


@app.route("/successfulCheckout", methods=['POST'])
def successful_checkout():
    entered_firstname = request.form.get("firstname")
    valid_firstname = ac_controller.firstname_validation(firstname=entered_firstname)
    entered_lastname = request.form.get("lastname")
    valid_lastname = ac_controller.lastname_validation(lastname=entered_lastname)
    entered_street = request.form.get("street")
    valid_street = py_controller.street_validation(street=entered_street)
    if valid_firstname and valid_lastname and valid_street:
        pc_controller.adapt_stock()
        pc_controller.user_cart.clear()
        success = "Your order was successful!"
        return render_template("login_homepage.html", success=success)
    else:
        cart_total = round(pc_controller.cart_total(), 2)
        error = "Sorry, please check your inputs! The placeholders give you a hint!"
        return render_template("checkout.html", cart_total=cart_total, error=error)


@app.route("/login_homepage")
def login_homepage():
    if session["role"] == "Admin":
        return render_template("admin_homepage.html")
    else:
        return render_template("login_homepage.html")


@app.route("/reviews")
def reviews():
    return render_template("reviews.html")


@app.route("/viewReviews", methods=['POST'])
def view_reviews():
    entered_pID = request.form.get("productID")
    rv_controller.found_reviews.clear()
    valid_pID = pc_controller.find_product(product_id=entered_pID)
    if valid_pID is not None:
        rv_controller.find_review(IDofproduct=entered_pID)
        if rv_controller.found_reviews is not None:
            found_reviews = rv_controller.found_reviews
            return render_template("found_reviews.html", reviews=found_reviews)
        elif rv_controller.found_reviews is None:
            error = "Sorry, no reviews for this product found"
            return render_template("reviews.html", error=error)
    if valid_pID is None:
        error = "Sorry, no product found"
        return render_template("reviews.html", error=error)


@app.route("/createReview", methods=['POST'])
def create_review():
    entered_pID = request.form.get("product_id")
    entered_heading = request.form.get("heading")
    entered_text = request.form.get("text")
    valid_pID = pc_controller.find_product(product_id=entered_pID)
    if valid_pID is not None:
        rv_controller.create_review(headline=entered_heading, review_text=entered_text, product_id=entered_pID)
        success = session["firstname"] + ", your review was created"
        return render_template("reviews.html", success=success)
    else:
        error = "Sorry, no product found"
        return render_template("reviews.html", error=error)


@app.route("/addProduct")
def add_product():
    return render_template("addProduct.html")


@app.route("/submitProduct", methods=['POST'])
def submit_product():
    entered_id = int(request.form.get("id"))
    valid_id = pc_controller.find_product(product_id=entered_id)
    entered_category = request.form.get("category")
    entered_name = request.form.get("name")
    entered_description = request.form.get("description")
    entered_net_price = int(request.form.get("price_excl_tax"))
    entered_gross_price = int(request.form.get("price_incl_tax"))
    entered_stock = int(request.form.get("stock"))
    if valid_id is None:
        pc_controller.create_product(ID=entered_id, category=entered_category, name=entered_name,
                                     description=entered_description, price_excl_tax=entered_net_price,
                                     price_incl_tax=entered_gross_price, stock=entered_stock)
        success = "The product " + entered_name + " was added."
        return render_template("addProduct.html", success=success)
    if valid_id is not None:
        error = "Sorry, the product id already exists."
        return render_template("addProduct.html", error=error)


@app.route("/showAccount")
def account_overview():
    return render_template("account.html")


@app.route("/changeAccount")
def change_account():
    return render_template("ChangeUserData.html")


@app.route("/updateAccount", methods=['POST'])
def update_account():
    entered_attribute = request.form.get("change_attribute")
    entered_data = request.form.get("change_data")

    if entered_attribute == "first name":
        valid_attribute = ac_controller.firstname_validation(firstname=entered_data)
    elif entered_attribute == "last name":
        valid_attribute = ac_controller.lastname_validation(lastname=entered_data)
    elif entered_attribute == "password":
        valid_attribute = ac_controller.password_validation(password=entered_data)
    elif entered_attribute == "username" or entered_attribute == "birthday":
        valid_attribute = True
    else:
        return render_template("account.html")

    if valid_attribute is True:
        if entered_attribute == "first name":
            session["firstname"] = entered_data
        elif entered_attribute == "last name":
            session["lastname"] = entered_data
        elif entered_attribute == "birthday":
            session["birthday"] = entered_data
        elif entered_attribute == "username":
            session["username"] = entered_data
        elif entered_attribute == "password":
            session["password"] = entered_data

        ac_controller.change_user(change_attribute=entered_attribute, new_value=entered_data)
        return render_template("account.html")
    else:
        error = "Sorry, please use correct input!"
        return render_template("ChangeUserData.html", error=error)


@app.route("/logout")
def logout():
    pc_controller.user_cart.clear()
    ac_controller.logged_in_user.clear()
    session.clear()
    return render_template("ShopHomepage.html")


@app.route("/createAccount")
def new_account():
    return render_template("createAccount.html")


@app.route("/submitAccount", methods=['POST'])
def create_account():
    entered_firstname = request.form.get("firstname")
    valid_firstname = ac_controller.firstname_validation(firstname=entered_firstname)
    entered_lastname = request.form.get("lastname")
    valid_lastname = ac_controller.lastname_validation(lastname=entered_lastname)
    birthday = request.form.get("birthday")
    username = request.form.get("username")
    entered_password = request.form.get("password")
    valid_password = ac_controller.password_validation(password=entered_password)
    if valid_firstname and valid_lastname and valid_password:
        ac_controller.create_user(firstname=entered_firstname, lastname=entered_lastname, birthday=birthday,
                                  username=username, password=entered_password)
        return render_template("ShopHomepage.html")
    else:
        error = "Please use correct inputs!"
        return render_template("createAccount.html", error=error)


app.run(debug=True)
