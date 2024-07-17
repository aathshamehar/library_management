// Copyright (c) 2024, Aathsha Mehar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Library Transaction", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on("Library Transaction", {
//     onload(frm) {
        
//         frm.set_query('library_member', () => {
//             return {
//                 filters: {
//                     "membership_validation": 1
//                 }
//             }
//         })
        
//     },
// });

// frm.set_query('article','add_articles',() => {
//     return {
//         filters: {
//             status: 'Available'
//         }
//     }
// })
frappe.ui.form.on("Library Transaction", {
    onload(frm) {
        
        frm.set_query('library_member', () => {
            return {
                query: 'library_management.library_management.doctype.library_transaction.library_transaction.custom_query',
                
                
            }
        })
        
    },
});

// frm.set_query('library_member', () => {
//     return {
//         query: 'library_management.library_management.doctype.library_member.library_member.custom_query',
//     }
// })