// Copyright (c) 2024, Aathsha Mehar and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Monthly Transaction", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Monthly Transaction', {
    refresh: function(frm) {
        calculate_totals(frm);
    },
    validate: function(frm) {
        calculate_totals(frm);
    },
    refresh: function(frm, cdt, cdn) {
        update_rate_and_amount(frm, cdt, cdn);
    },
    fooddetail_remove: function(frm) {
        calculate_totals(frm);
    }
});

frappe.ui.form.on('Daily Food Detail', {
    food_type: function(frm, cdt, cdn) {
        update_rate_and_amount(frm, cdt, cdn);
    },
    count: function(frm, cdt, cdn) {
        update_amount_and_totals(frm, cdt, cdn);
    },
    rate: function(frm, cdt, cdn) {
        update_amount_and_totals(frm, cdt, cdn);
    }
});

function update_rate_and_amount(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let rate = 0;

    if (row.food_type === 'Normal') {
        rate = frm.doc.normal_rate;
    } else if (row.food_type === 'Special') {
        row.rate = frm.doc.special_rate;
    }
    else  {
        rate = frm.doc.normal_rate;
    }
    // else if (row.food_type === "select") {
    //     rate = 0;
    // }

    frappe.model.set_value(cdt, cdn, 'rate', rate);

    update_amount_and_totals(frm, cdt, cdn);
}

function update_amount_and_totals(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    let amount = 0;
    row.amount = row.count * row.rate;
    // frappe.model.set_value(cdt, cdn, 'amount', row.amount);
    frm.refresh_fields();  


    calculate_totals(frm, cdt, cdn);
}

function calculate_totals(frm) {
    let total_count = 0;
    let total_amount = 0;

    frm.doc.daily_food_count_detail.forEach(function(row) {
        total_count += row.count;
        total_amount += row.amount;
    });

    frm.set_value('total_count', total_count);
    frm.set_value('total_amount', total_amount);
}

