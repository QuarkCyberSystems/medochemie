import frappe


def disable_all_users():
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 1})  # Fetch only enabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            frappe.db.set_value('User', user.name, 'enabled', 0)
            frappe.db.commit()

def enable_all_users():
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 0})  # Fetch only disabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            frappe.db.set_value('User', user.name, 'enabled', 1)
            frappe.db.commit()

def add_to_group(): 
    role_profile_name = "ERP_NEXT_USERS"
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 1})  # Fetch only enabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            if not user.role_profile_name == role_profile_name:
                frappe.db.set_value('User', user.name, 'role_profile_name', role_profile_name)
                frappe.db.commit()