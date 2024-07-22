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
        {"label": "Class", "fieldname": "class", "fieldtype": "Data", "width": 200},
        {"label": "Total Bookings", "fieldname": "total_bookings", "fieldtype": "Int", "width": 120}
    ]

def get_data(filters):
    conditions = ""
    if filters.get("start_date") and filters.get("end_date"):
        conditions = f"WHERE booking_date BETWEEN '{filters['start_date']}' AND '{filters['end_date']}'"

    data = frappe.db.sql(f"""
        SELECT
            class,
            COUNT(*) as total_bookings
        FROM
            `tabGym Class Booking`
        {conditions}
        GROUP BY
            class
        ORDER BY
            total_bookings DESC
    """, as_dict=True)

    return data
