# Copyright (c) 2024, Aathsha Mehar and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns, data = [], []


	columns = [
		{
			'fieldname': 'account',
			'label': _('Account'),
			'fieldtype': 'Data',
		},
		{
			'fieldname': 'currency',
			'label': _('Currency'),
			'fieldtype': 'Link',
			'options': 'Currency'
		},
		{
			'fieldname': 'balance',
			'label': _('Balance'),
			'fieldtype': 'Currency',
			'options': 'currency'
		}
	]
 
	data = [
		{
			'account': 'Application of Funds (Assets)',
			'currency': 'INR',
			'balance': '15182212.738'
		},
		{
			'account': 'Current Assets - GTPL',
			'currency': 'INR',
			'balance': '17117932.738'
		},
		
	]
	return columns, data

	
 
 		



