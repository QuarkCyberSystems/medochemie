import frappe
import frappe.utils
from frappe import _


def get_user_by_email(email):
    users = frappe.get_doc("User", email)
    return users

# https://erpnext.medochemie.com/api/resource/Social%20Login%20Key?filters=[[%22owner%22,%22=%22,%22Administrator%22]]&fields=[%22*%22]


def get_social_login_keys():
    sl = frappe.get_doc("Social Login Key","office_365")
    return sl

def on_after_login(login_manager):
	frappe.msgprint("Test")
     
def successful_login(login_manager): 
    frappe.msgprint("Test")

def on_session_creation(login_manager):
    # allocate free credits to frappe.session.user
    user = frappe.session.user
    
    # Check if the user logged in via Social Login (Office 365)
    social_logins = get_social_login_keys()
    # frappe.get_doc('Social Login Key', filters={'owner': user}, fields=['provider'])
    is_office_365_login = social_logins
    
    if is_office_365_login:
        # Check if the user has the "ERP_NEXT_USERS" Role Profile
        role_profile_name = "ERP_NEXT_USERS"
        
        # https://erpnext.medochemie.com/api/resource/User?filters=[["email","=","admin@example.com"]]&fields=["*"]

        #print(frappe.session.user_email)
        user_doc = get_user_by_email(frappe.session.user_email) # frappe.get_doc("User", user)
        
        if not user_doc.role_profile_name == role_profile_name:
            # Assign the "ERP_NEXT_USERS" Role Profile if not assigned
            user_doc.role_profile_name = role_profile_name
            user_doc.save(ignore_permissions=True)
            frappe.msgprint(f"Assigned {role_profile_name} role profile to user {user}.")
    pass
