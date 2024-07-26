# Copyright (c) 2024, Emperor and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



def get_gym_settings():
    return frappe.get_single("Gym Setting")

def get_membership_plans():
    settings = get_gym_settings()
    return settings.cost

