# Copyright (c) 2024, Aathsha Mehar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import nowdate


def execute(filters=None):
	columns, data = [], []

	columns = [
		{
   			"fieldname": "name",
   			"fieldtype": "data",
   			"label": "Member ID"
   		},
  		{
   			"fieldname": "full_name",
   			"fieldtype": "Data",
   			"label": "Full Name"
   		},
   		{
  			"fieldname": "email_adrdess",
	  		"fieldtype": "Data",
  			"label": "Email Adrdess"
  		},
   		{
   			"fieldname": "phone",
   			"fieldtype": "Data",
   			"label": "Phone"
   		},		
		{
   			"fieldname": "from_date",
   			"fieldtype": "Date",
   			"label": "Membership from"
   		},
		{
   			"fieldname": "to_date",
   			"fieldtype": "Date",
   			"label": "Membership to"
   		},
		{
			"fieldname": "tran_count",
			"fieldtype": "Int",
			"label": "Number of Transctions"
		},
		{
   			"fieldname": "membership_validity",
   			"fieldtype": "data",
   			"label": "Membership Validity",
		},
		{
   			"fieldname": "books_issued",
   			"fieldtype": "data",
   			"label": "Books Issued",
		},
		{
   			"fieldname": "last_tran",
   			"fieldtype": "date",
   			"label": "Date of Last Transaction",
		},
  
	]
	today = frappe.utils.getdate(nowdate())
	member_detail = frappe.db.get_all('Library Member',fields=["name","full_name","email_adrdess","phone"])
	# sub_trans = frappe.db.get_all("Library Membership",{"docstatus":1},pluck="name")
	# print(member_detail)

	for i in member_detail:
		print(i.name)
		# memberhsip_from = frappe.db.get_all("Library Membership",{"library_member":i.name},pluck="from_date",order_by = "from_date asc")
		memberhsip_from = frappe.get_last_doc("Library Membership",{"library_member":i.name, "docstatus":1}, order_by = "from_date asc").from_date
		memberhsip_to = frappe.get_last_doc("Library Membership",{"library_member":i.name, "docstatus":1}, order_by = "to_date desc").to_date
  
		# memberhsip_to = frappe.db.get_all("Library Membership",{"library_member":i.name},pluck="to_date",order_by = "to_date desc")
		# print(memberhsip_from)
		
		trans_count = frappe.db.count("Library Transaction",{"docstatus":1,"library_member":i.name})
  
		if memberhsip_from <= today and memberhsip_to >= today:
			membership_validity = "Valid"
		else:
			membership_validity = "Invalid"

		sub_trans = frappe.db.get_list("Library Transaction",{"library_member":i.name,"docstatus":1},pluck="name")
		print(sub_trans)
		print("priyanka")
		# books_issued = frappe.db.get_list("Article Child",{"type_tran":"Issue","parent":["in",sub_trans]},pluck="article")
		books_issued = ""
		for tran in sub_trans:
			issued_article = frappe.db.get_value("Article Child", {"parent": tran, "type_tran": "Issue"}, "article")

			if issued_article:
				books_issued += issued_article + ", "  # Add comma and space as separator
		
		print(books_issued)
		last= frappe.db.exists ("Library Transaction",{"library_member":i.name, "docstatus":1})
		print(last,"koi")
		if last:
			last_tran = frappe.get_last_doc("Library Transaction",{"library_member":i.name}, order_by = "date desc").date
   
		else:
			last_tran = None
		print("hai")
		print(last_tran,"t56ghyh")
        # Remove the trailing comma and space if any articles were issued
		# if books_issued:
		# 	books_issued = books_issued[:-2]
		# books_issued = []
		# for tran in sub_trans:
		# 	issued_article = frappe.db.get_value("Article Child", {"parent": tran, "type_tran": "Issue"}, "article")
		# 	if issued_article:
		# 		books_issued.append(issued_article)
		# print(books_issued)
		# Issue_count = frappe.db.count(Transaction"Article Child",{"article":i.name, "type_tran":"Issue","parent":["in",sub_trans]})
		# Return_count = frappe.db.count("Article Child",{"article":i.name, "type_tran":"Return","parent":["in",sub_trans]})
		data.append({
			'name': i.name,
            'full_name': i.full_name,
            'email_adrdess': i.email_adrdess,
            'phone': i.phone,
            'from_date': memberhsip_from,
            'to_date': memberhsip_to,
            'tran_count': trans_count,
            'membership_validity': membership_validity,
            'books_issued': books_issued,
            'last_tran': last_tran,
            #  'price': i.price,
            #  'issue_count': Issue_count,
            #  'return_count': Return_count
        })
	return columns, data
 
 
 
