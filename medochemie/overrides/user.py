import frappe
from frappe.model.document import Document
import erpnext
from erpnext.stock.doctype.item.item import Item

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def user_query(doctype, txt, searchfield, start, page_len, filters):
	from frappe.desk.reportview import get_filters_cond, get_match_cond

	doctype = "User"
	conditions = []

	user_type_condition = "and user_type != 'Website User'"
	if filters and filters.get("ignore_user_type") and frappe.session.data.user_type == "System User":
		user_type_condition = ""
		filters.pop("ignore_user_type")

	txt = f"%{txt}%"
	return frappe.db.sql(
		"""SELECT `name`, CONCAT_WS(' ', first_name, middle_name, last_name)
		FROM `tabUser`
		WHERE `enabled`=1
			{user_type_condition}
			AND `docstatus` < 2
			AND `name` NOT IN ({standard_users})
			AND ({key} LIKE %(txt)s
				OR CONCAT_WS(' ', first_name, middle_name, last_name) LIKE %(txt)s)
			{fcond} {mcond}
		ORDER BY
			CASE WHEN `name` LIKE %(txt)s THEN 0 ELSE 1 END,
			CASE WHEN concat_ws(' ', first_name, middle_name, last_name) LIKE %(txt)s
				THEN 0 ELSE 1 END,
			NAME asc
		LIMIT %(page_len)s OFFSET %(start)s
	""".format(
			user_type_condition=user_type_condition,
			standard_users=", ".join(frappe.db.escape(u) for u in STANDARD_USERS),
			key=searchfield,
			fcond=get_filters_cond(doctype, filters, conditions),
			mcond=get_match_cond(doctype),
		),
		dict(start=start, page_len=page_len, txt=txt),
	)
