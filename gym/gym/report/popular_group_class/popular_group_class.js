// Copyright (c) 2024, Emperor and contributors
// For license information, please see license.txt

frappe.query_reports["Popular Group Class"] = {
	"filters": [
		{
            "fieldname": "start_date",
            "label": "Start Date",
            "fieldtype": "Date",
            "default": frappe.utils.nowdate()
        },

		{
            "fieldname": "end_date",
            "label": "End Date",
            "fieldtype": "Date",
            "default": frappe.utils.nowdate()
        }

	]
};
