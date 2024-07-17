// Copyright (c) 2024, Aathsha Mehar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Membership", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Library Membership', {
    from_date: function(frm) {
  
      if (frm.doc.from_date && frm.doc.to_date && (frm.doc.from_date > frm.doc.to_date)) {
        frm.set_value('from_date',"");
        frappe.throw('To Date cannot be before From Date!');
      }
    },


    to_date: function(frm) {
  
      if (frm.doc.from_date && frm.doc.to_date && (frm.doc.from_date > frm.doc.to_date)) {
        frm.set_value('to_date',"");
        frappe.throw('To Date cannot be before From Date!');
      }
    }
  });







  /*frappe.ui.form.on('Library Membership', {
    validate: function(frm) {
      var to_date = frm.doc.to_date;
      var from_date = frm.doc.from_date;
  
      if (from_date && to_date && new Date(from_date) > new Date(to_date)) {
        frappe.throw('To Date cannot be before From Date!');
      }
    }
  });
  
  */
