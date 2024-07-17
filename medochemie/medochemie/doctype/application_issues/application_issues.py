# Copyright (c) 2024, Medochemie and contributors
# For license information, please see license.txt

# import frappe
import json
from datetime import timedelta
from datetime import date

import frappe
from frappe import _
from frappe.core.utils import get_parent_doc
from frappe.email.inbox import link_communication_to_document
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc
from frappe.query_builder import Interval
from frappe.query_builder.functions import Now
from frappe.utils import date_diff, get_datetime, now_datetime, time_diff_in_seconds
from frappe.utils.user import is_website_user



class ApplicationIssues(Document):

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		opening_date: DF.Date | None
	# end


	def before_save(self) : 
		self.opening_date = date.today()
		return