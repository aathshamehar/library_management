import frappe

def after_migrate():
    print("Migrated Successfully")
    
def after_insert(doc, method):
    if doc.doctype == "User":
        frappe.msgprint(f"New user created: {doc.first_name}, {doc.last_name}, {doc.email}")

def before_insert(doc, method):
    if doc.doctype == "Library Member":
        if doc.last_name == "P":
            doc.last_name = "KPP"