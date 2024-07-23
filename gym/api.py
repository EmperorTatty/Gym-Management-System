import frappe

@frappe.whitelist()
def get_customer_profile(member):
    member = frappe.get_doc("Gym member", member)
    active_plan = frappe.db.get_value("Gym Membership", {"member": member, "docstatus": 1, "end_date": [">", frappe.utils.nowdate()]}, ["plan", "end_date"], as_dict=True)
    past_plans = frappe.get_all("Gym Membership", filters={"member": member, "docstatus": 1, "end_date": ["<", frappe.utils.nowdate()]}, fields=["plan"])

    profile = {
        "full_name": f"{member.first_name} {member.last_name}",
        "email": member.email,
        "active_plan": active_plan.plan if active_plan else "No Active Plan",
        "remaining_days": (frappe.utils.getdate(active_plan.end_date) - frappe.utils.nowdate()).days if active_plan else 0,
        "trainer": frappe.db.get_value("Gym Trainer Subscription", {"member": member, "docstatus": 1}, "trainer"),
        "past_plans": [plan.plan for plan in past_plans]
    }

    return profile
