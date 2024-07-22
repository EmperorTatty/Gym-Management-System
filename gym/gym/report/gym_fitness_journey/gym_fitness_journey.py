# Copyright (c) 2024, Emperor and contributors
# For license information, please see license.txt

# Copyright (c) 2024, Emperor and contributors
# For license information, please see license.txt

# gym_management_system/gym_management_system/report/customer_fitness_journey/customer_fitness_journey.py

import frappe
from frappe.utils import flt

def execute(filters=None):
    if not filters:
        filters = {}

    columns, data = [], []
    columns = get_columns()
    data = get_data(filters)

    chart = {
        "data": {
            "labels": [d['date'] for d in data],
            "datasets": [
                {
                    "name": "Weight",
                    "values": [flt(d['weight']) for d in data]
                },
                {
                    "name": "Calories",
                    "values": [flt(d['calories']) for d in data]
                }
            ]
        },
        "type": "line"
    }

    return columns, data, None, chart

def get_columns():
    return [
        {"label": "Date", "fieldname": "date", "fieldtype": "Date", "width": 120},
        {"label": "Weight", "fieldname": "weight", "fieldtype": "Float", "width": 120},
        {"label": "Calories", "fieldname": "calories", "fieldtype": "Float", "width": 120},
        {"label": "Member", "fieldname": "member", "fieldtype": "Link", "options": "Gym Member", "width": 120}
    ]

def get_data(filters):
    conditions = []
    if filters.get("member"):
        conditions.append(f"`member` = '{filters['member']}'")

    conditions = " AND ".join(conditions) if conditions else "1=1"

    data = frappe.db.sql(f"""
        SELECT
            date,
            weight,
            calories,
            member
        FROM
            `tabGym Fitness Tracker`
        WHERE
            {conditions}
        ORDER BY
            date ASC
    """, as_dict=True)

    return data
