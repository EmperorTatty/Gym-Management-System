import datetime
import frappe

@frappe.whitelist(allow_guest=True)
def get_all_gym_memberships():
    gym_memberships = frappe.get_all('Gym Membership', fields=['*'])
    return gym_memberships



@frappe.whitelist(allow_guest=True)
def get_active_plan_for_member(member):
    active_plan = frappe.get_all(
        'Gym Membership',
        filters={
            'member': member,
            'is_active': 1
        },
        fields=['*']
    )
    if active_plan:
        return active_plan[0]['workout_plan']
    else:
        return None
    
    




@frappe.whitelist(allow_guest=True)
def remaining_days_in_subscription(member):
    try:
        # Fetch the gym membership details for the member
        membership = frappe.get_doc('Gym Membership', {"member": member})
        
        if membership:
            # Check if the end_date is set
            if membership.end_date:
                # Convert end_date to date object (assuming end_date is in 'YYYY-MM-DD' format)
                end_date = membership.end_date
                
                # Get current date
                current_date = datetime.date.today()
                
                # Calculate remaining days
                remaining_days = (end_date - current_date).days
                
                # Return the remaining days in the subscription
                return {
                    "status": "success",
                    "remaining_days": remaining_days
                }
            else:
                return {
                    "status": "error",
                    "message": "Subscription end date is not set."
                }
        else:
            return {
                "status": "error",
                "message": "Gym membership not found."
            }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }




@frappe.whitelist(allow_guest=True)
def get_trainer_and_past_plans(member):
    try:
        memberships = frappe.get_all(
            'Gym Membership',
            filters={'member': member},
            fields=['member', 'start_date', 'end_date', 'workout_plan', 'allocated_trainer'],
            order_by='end_date desc'
        )
        if not memberships:
            return {
                "status": "error",
                "message": f"No memberships found for member '{member}'"
            }
        allocated_trainer_id = memberships[0]['allocated_trainer']
        trainer_details = frappe.get_doc('Gym Trainer', allocated_trainer_id)
        result = {
            "status": "success",
            "trainer": {
                "name": trainer_details.full_name,
                "contact_info": {
                    "phone": trainer_details.phone_no,
                    "email": trainer_details.email
                }
            },
            "past_plans": [
                {
                    "membership_id": membership['member'],
                    "start_date": membership['start_date'],
                    "end_date": membership['end_date'],
                    "workout_plan": membership['workout_plan']
                } for membership in memberships
            ]
        }
        return result
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
