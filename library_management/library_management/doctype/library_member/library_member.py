# Copyright (c) 2024, Aathsha Mehar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LibraryMember(Document):
    
    def before_save(self):
        self.full_name = f'{self.first_name} {self.last_name or ""}'

# python method signature
@frappe.whitelist()
def custom_query(doctype, txt, searchfield, start, page_len, filters):
    return frappe.db.sql('''
        SELECT name
        FROM `tabLibrary Member`
        WHERE membership_validation = 1
    ''')
        




