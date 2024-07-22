import frappe

def execute():
    # Check if the new_field exists
    if not frappe.db.has_column('Gym Member', 'new_field'):
        frappe.db.add_column('Gym Member', 'new_field', 'Data')
    
    # Update existing records with the default value for new_field
    frappe.db.sql("""
        UPDATE `tabGym Member`
        SET new_field = 'default_value'
    """)
    
    # Commit the changes
    frappe.db.commit()
