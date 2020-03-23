from myapp import app, db
from flask import render_template, request, redirect
import sqlite3 as sql

def weighted_product_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from weighted_product where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def liquid_product_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from liquid_product where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def cosmetics_product_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from cosmetics where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def kids_food_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from kids_food where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def packets_product_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from packets where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def spices_product_table(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT * from spices where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows

def search_product():
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	curr.execute("select product_name, shelf_no from query_product_list")
	rows = curr.fetchall();
	return rows

def delete_query_product_list():
	d_conn = sql.connect("product.db")
	d_cur = d_conn.cursor()
	d_cur.execute("delete from query_product_list")
	d_conn.commit()

def query_shelf_no(query_product):
	con = sql.connect("product.db")
	con.row_factory = sql.Row
	curr = con.cursor()
	query = """
	SELECT shelf_number from product where product_name=?
	"""
	curr.execute(query, (query_product, ))
	rows = curr.fetchall();
	return rows