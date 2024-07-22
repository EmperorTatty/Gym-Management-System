// Copyright (c) 2024, Emperor and contributors
// For license information, please see license.txt

frappe.query_reports["Revenue Report by Month"] = {
    "filters": [
        {
            "fieldname": "start_date",
            "label": ("Start Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.add_months(frappe.datetime.get_today(), -12),
            "reqd": 1
        },
        {
            "fieldname": "end_date",
            "label": ("End Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        }
    ],

    onload: function(report) {
        // Add any custom onload logic here
        console.log("Report Loaded: Revenue Report by Month");
    },

    refresh: function(report) {
        // Add any custom refresh logic here
        console.log("Report Refreshed: Revenue Report by Month");
    },

    formatter: function(value, row, column, data, default_formatter) {
        // Custom formatting logic
        value = default_formatter(value, row, column, data);
        if (column.fieldname == "total_revenue" && data && data.total_revenue > 10000) {
            value = `<span style="color:green;">${value}</span>`;
        }
        return value;
    }
};
