
# user_validation

import frappe
from frappe import _
import json

from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from frappe.utils.password import check_password, get_password_reset_limit
from frappe.exceptions import AuthenticationError
from frappe.core.doctype.user.user import User


@frappe.whitelist(allow_guest=True)
def validate_usr_new(usr, pwd):
# Script Name: Validate User
# Script Type: API
# API Endpoint: validate_usr
# Allow Guest: Yes

    
    try:
        # Extract parameters from URL
        usr = frappe.form_dict.get('usr')
        pwd = frappe.form_dict.get('pwd')
        

        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)

        # If no exception is raised, the credentials are correct
        frappe.response['message'] = "Credentials are correct"
        frappe.response['success'] = True
        
        # Return user details
        frappe.response.http_status_code = 200

    except frappe.AuthenticationError:
        frappe.log_error(f"usr: {usr}, pwd: {pwd}", "Debug")
        frappe.response['message'] = "Credentials are incorrect [AuthenticationError]"
        frappe.response['success'] = False

    except frappe.DoesNotExistError:
        frappe.log_error(f"usr: {usr}, pwd: {pwd}", "Debug")
        frappe.response['message'] = "User does not exist"
        frappe.response['success'] = False

    except Exception as e:
        frappe.response['message'] = e
        frappe.response['success'] = False


@frappe.whitelist(allow_guest=True)
def validate_usr(usr, pwd):

    frappe.log_error(f"---")

    try:
        # Fetch the user document
        user_doc = frappe.get_doc("User", usr)

        
        frappe.local.response.http_status_code = 200

        # Return user details
        frappe.response['user'] = {
            "full_name": user_doc.full_name,
            "email": user_doc.email,
            "roles": [role.role for role in user_doc.get("roles")],
            # Add any other user fields you want to return here
        }
        
        # Check if the provided password matches the stored password
        check_password(user_doc.name, pwd)
        
        # If no exception is raised, the credentials are correct
        frappe.response['message'] = "Credentials are correct"
        frappe.response['success'] = True

    except frappe.AuthenticationError:
        frappe.response['message'] = "Credentials are incorrect [AuthenticationError]"
        frappe.response['success'] = False

    except frappe.DoesNotExistError:
        frappe.response['message'] = "User does not exist"
        frappe.response['success'] = False

    except Exception as e:
        frappe.response['message'] = frappe.get_traceback()
        frappe.response['success'] = False
        frappe.log_error(message=frappe.get_traceback(), title='Unexpected Error')