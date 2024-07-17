// Copyright (c) 2024, Aathsha Mehar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Daily Food Detail", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on('Daily Food Detail', {
//     refresh: function(frm) {
//       // Get the parent document
//       var parent = frm.doc.parent;
      
//       // Check if parent document is available and has a rate
//       if (parent && parent.rate) {
//         // Set the rate in the child table based on parent
//         frm.doc.daily_food_count_detail.forEach(function(d) {
//           d.rate = parent.rate;
//         });
        
//         // Refresh the child table to display the updated rate
//         frm.refresh_field('daily_food_count_detail');
//       }
//     }
// //   });
// frappe.ui.form.on('Daily Food Detail', {
//     count: function(frm, cdt, cdn) {
//         // Calculate amount when count changes
//         let row = locals[cdt][cdn];
//         row.amount = row.count * row.rate;
//         frm.refresh_field('daily_food_count_detail');
//     },
//     rate: function(frm, cdt, cdn) {
//         // Calculate amount when rate changes
//         let row = locals[cdt][cdn];
//         row.amount = row.count * row.rate;
//         frm.refresh_field('daily_food_count_detail');
//     }
// });

