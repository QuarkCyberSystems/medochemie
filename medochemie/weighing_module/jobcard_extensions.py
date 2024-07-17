import json

import frappe
from frappe import _


@frappe.whitelist()
def check_job_card_status(job_card_name):
    job_card = frappe.get_doc("Job Card", job_card_name)
    if job_card.status == "Open":
        frappe.msgprint(_("Job Card {0} is Open").format(job_card_name), title=_("Job Card Status"))
    elif job_card.status == "In Process":
        frappe.msgprint(_("Job Card {0} is In Process").format(job_card_name), title=_("Job Card Status"))
    elif job_card.status == "Completed":
        frappe.msgprint(_("Job Card {0} is Completed").format(job_card_name), title=_("Job Card Status"))
    else:
        frappe.msgprint(_("Job Card {0} has an unknown status: {1}").format(job_card_name, job_card.status), title=_("Job Card Status"))

@frappe.whitelist()
def check_work_order_operation_status(work_order_name, operation):
    work_order = frappe.get_doc("Work Order", work_order_name)
    for op in work_order.operations:
        if op.operation == operation:
            if op.status == "Not Started":
                frappe.msgprint(_("Operation {0} in Work Order {1} has not started").format(operation, work_order_name), title=_("Work Order Operation Status"))
            elif op.status == "In Process":
                frappe.msgprint(_("Operation {0} in Work Order {1} is In Process").format(operation, work_order_name), title=_("Work Order Operation Status"))
            elif op.status == "Completed":
                frappe.msgprint(_("Operation {0} in Work Order {1} is Completed").format(operation, work_order_name), title=_("Work Order Operation Status"))
            else:
                frappe.msgprint(_("Operation {0} in Work Order {1} has an unknown status: {2}").format(operation, work_order_name, op.status), title=_("Work Order Operation Status"))
            break
    else:
        frappe.msgprint(_("Operation {0} not found in Work Order {1}").format(operation, work_order_name), title=_("Work Order Operation Status"))

