import frappe

@frappe.whitelist()
def disable_all_users():
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 1})  # Fetch only enabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            frappe.db.set_value('User', user.name, 'enabled', 0)
            frappe.db.commit()

@frappe.whitelist()
def enable_all_users():
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 0})  # Fetch only disabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            frappe.db.set_value('User', user.name, 'enabled', 1)
            frappe.db.commit()

@frappe.whitelist()
def add_to_group(): 
    role_profile_name = "ERP_NEXT_USERS"
    # Get all user accounts
    users = frappe.get_all('User', filters={'enabled': 1})  # Fetch only enabled users
    for user in users:
        # Skip Administrator and Guest
        if user.name not in ['Administrator', 'Guest']:
            if not user.role_profile_name == role_profile_name:
               
                role_profile = frappe.get_doc('Role Profile', role_profile_name)

                roles = [role.role for role in role_profile.roles]
                # Add roles to the user
                for role in roles:
                    # Insert into tabHas Role directly
                    frappe.get_doc({
                        'doctype': 'Has Role',
                        'parent': user.name,
                        'parenttype': 'User',
                        'role': role})

                # Save changes
                #user.save()

                frappe.db.set_value('User', user.name, 'role_profile_name', role_profile_name)
                
                frappe.db.commit()