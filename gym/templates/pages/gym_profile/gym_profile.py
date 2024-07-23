# gym/gym/page/gym_profile/gym_profile.py
import frappe

def get_context(context):
    member = frappe.get_doc("Gym Member", frappe.session.user)
    memberships = frappe.get_all("Gym Membership", filters={"member": member.name}, fields=["name", "start_date", "end_date"])
    subscriptions = frappe.get_all("Gym Trainer Subscription", filters={"member": member.name}, fields=["trainer", "rating"])
    
    context.member = member
    context.memberships = memberships
    context.subscriptions = subscriptions
