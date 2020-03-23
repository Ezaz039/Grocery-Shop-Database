from myapp import app, db
from flask import render_template, request, redirect, flash, url_for
import sqlite3 as sql
from sql_query import packets_product_table, spices_product_table, search_product, delete_query_product_list, query_shelf_no
from sql_query import weighted_product_table, liquid_product_table, cosmetics_product_table, kids_food_table

global product_added_to_query
product_added_to_query = []

@app.route('/product_list', methods=['GET', 'POST'])
def query_list():
	rows = search_product()
	delete_query_product_list()
	return render_template('product.html', rows = rows)

@app.route('/productLocation/<string:query_product>', methods=['GET', 'POST'])
def location_of_product(query_product):
	rows = query_shelf_no(query_product)
	if len(rows) > 0:
		conn1 = sql.connect("product.db")
		cur1 = conn1.cursor()
		cur1.execute("insert into query_product_list (product_name, shelf_no) values(?, ?)", (query_product, rows[0][0]))
		conn1.commit()
		product_added_to_query.append(query_product)
	else:
		rows = search_product()
		flash("Something not right!!!")
		return render_template('index.html', rows = rows)
	rows = search_product()
	return redirect(url_for('home'))

@app.route('/')
def home():
	global product_added_to_query
	rows = search_product()
	product_added_to_query = []
	return render_template('index.html', rows=rows)

@app.route('/', methods=['GET', 'POST'])
def product_type():
	query = request.form['productName']
	query_product = query.title()

	if query_product == "":
		return query_list()

	if query_product[len(query_product)-1] == ' ':
		query_product = query_product[:-1]
	if query_product[len(query_product)-1] == ',':
		query_product = query_product[:-1]
	
	if query_product in product_added_to_query:
		rows = search_product()
		flash("You have searched the product before!!!")
		return render_template('index.html', rows = rows)
	weighted_product_list = ["Rice", "Masoor Dal", "Moong Dal", "Arahar Dal", "Rajma", "Matar Dal", "Chana Dal", "Biriyani Rice", "Besan", "Atta", "Maida"]
	liquid_product_list = ["Mustard Oil", "Refined Oil", "Coconut Oil", "Cold Drinks", "Soyabean Oil", "Milk"]
	cosmetics_list = ["Soap", "Face Wash", "Deodrent", "Shower Gel", "Shampoo", "Moisturizer"]
	kids_food_list = ["Chips", "Chocolate", "Baby Food", "Corn Flakes", "Biscuit"]
	packets_list = ["Tea", "Coffee", "Bhujia", "Sauce", "Toothpaste", "Soyabean", "Milk Powder"]
	spices_list = ["Chili Powder", "Turmaric", "Black Paper", "Chiken Masala", "Meat Masala", "Jeera", "Methi", "Clover", "Cinamon"]
	if query_product in weighted_product_list:
		rows = weighted_product_table(query_product)
		return render_template("weighted_product.html",rows = rows, query_product=query_product)
	elif query_product in liquid_product_list:
		rows = liquid_product_table(query_product)
		return render_template("liquid_product.html",rows = rows, query_product=query_product)
	elif query_product in cosmetics_list:
		rows = cosmetics_product_table(query_product)
		return render_template("cosmetics_product.html", rows = rows, query_product=query_product)
	elif query_product in kids_food_list:
		rows = kids_food_table(query_product)
		return render_template("kids_food.html", rows = rows, query_product=query_product)
	elif query_product in packets_list:
		rows = packets_product_table(query_product)
		return render_template("packets_product.html", rows = rows, query_product=query_product)
	elif query_product in spices_list:
		rows = spices_product_table(query_product)
		return render_template("spices_product.html", rows = rows, query_product=query_product)
	else:
		if query_product == "":
			return query_list()
		else:
			rows = search_product()
			flash("Your Product is currently not available in the shop")
			return render_template('index.html', rows = rows)