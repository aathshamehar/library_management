# # Copyright (c) 2024, Aathsha Mehar and contributors
# # For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _



def execute(filters=None):
	columns, data = [], []

	columns = [		
  		{
   			'fieldname': 'name',
   			'fieldtype': 'Link',
   			'label': _('Article Name'),
			'options': 'Article'
  		},
  		{
			'fieldname': 'image',
			'fieldtype': 'Attach Image',
			'label': _('Image')
		},
		{
			'fieldname': 'author',
			'fieldtype': 'Data',
			'label': _('Author')
		},
		{
			'fieldname': 'description',
   			'fieldtype': 'Text Editor',
   			'label': _('Description')
		},
		{
			'fieldname': 'isbn',
   			'fieldtype': 'Data',
			'label':_('ISBN')
		},
		{
			'fieldname': 'status',
			'fieldtype': 'Select',
			'label':  _('Status'),
			'options': "\n Issued\n Available"
		},
		{
			'fieldname': 'publisher',
			'fieldtype': 'Data',
			'label': _('Publisher')
		},
	
		{
			'fieldname': 'route',
			'fieldtype': 'Data',
			'label': _('Route')
		},
	
		{
			'fieldname': 'price',
			'fieldtype': 'Int',
   			'label': _('Price')
		},
  		{
			'fieldname': 'issue_count',
			'fieldtype': 'Int',
   			'label': _('Number of Times Issued')
		},
		{
			'fieldname': 'return_count',
			'fieldtype': 'Int',
   			'label': _('Number of Times Returned')
		}

	]
	# frappe.db.get_list("Article", fields=["name","image","author","description","isbn","status","publisher","route","price"])

	# articles = frappe.db.get_all(
    #     	'Article',
    #         pluck="article_name",
    # 		)
	# print("hai")
	# print(articles)
	
	# issued_transactions = frappe.db.get_all(
    # 		"Library Transaction",
    #     	filters={"docstatus": 1},
    #     	fields=["name"]
	# 		)
	# issue_count = None
	# return_count = None
	# for i in articles:
	# 	issue_count = frappe.db.count("Article Child", {"article":i.article_name, "type_tran": "Issue", "parent":["in",issued_transactions]})
	# 	print("here?")
	# 		# issue_count = transaction["date"]
	# 	print(issue_count)
		
	# 	return_count = frappe.db.count("Article Child", {"article":i.article_name, "type_tran": "Return", "parent":["in",issued_transactions]})
	# 	print("here?")
	# 		# return_count = transaction["date"]
	# 	print(return_count)
			
		
                    
                    
    #     #  "issue_count","return_count"
	# 	data = ({
    #      'name': i.name,
    #      'image': i.image,
    #      'author': i.author,
    #      'description': i.description,
    #      'isbn': i.isbn,
    #      'status': i.status,
    #      'publisher': i.publisher,
    #      'route': i.route,
    #      'price': i.price,
    #      'issue_count': issue_count,
    #      'return_count': return_count
    # })
	
	# return columns, data

	article_list = frappe.db.get_all('Article',fields=["name","image","author","description","isbn","status","publisher","route","price"])
	sub_trans = frappe.db.get_list("Library Transaction",{"docstatus":1},pluck="name")

	for i in article_list:
		Issue_count = frappe.db.count("Article Child",{"article":i.name, "type_tran":"Issue","parent":["in",sub_trans]})
		Return_count = frappe.db.count("Article Child",{"article":i.name, "type_tran":"Return","parent":["in",sub_trans]})
    
		data.append({
             'name': i.name,
             'image': i.image,
             'author': i.author,
             'description': i.description,
             'isbn': i.isbn,
             'status': i.status,
             'publisher': i.publisher,
             'route': i.route,
             'price': i.price,
             'issue_count': Issue_count,
             'return_count': Return_count
        })
	return columns, data