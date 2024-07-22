# Copyright (c) 2024, Emperor and contributors
# For license information, please see license.txt

import frappe




def execute(filters=None):
    if not filters:
        filters = {}

    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)

    return columns, data

def get_columns():
    return [
        {"label": "Month", "fieldname": "month", "fieldtype": "Data", "width": 120},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 120}
    ]

def get_data(filters):
    data = frappe.db.sql("""
        SELECT 
            DATE_FORMAT(start_date, '%%Y-%%m') as month,
            SUM(total_amount) as revenue
        FROM 
            `tabGym Membership`
        WHERE 
            start_date IS NOT NULL
        GROUP BY 
            DATE_FORMAT(start_date, '%%Y-%%m')
        ORDER BY 
            DATE_FORMAT(start_date, '%%Y-%%m') ASC
    """, as_dict=True)

    return data
