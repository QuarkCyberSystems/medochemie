from . import __version__ as app_version

app_name = "medochemie"
app_title = "Medochemie"
app_publisher = "Medochemie"
app_description = "Customization for ERPNext for Medochemie-specific use cases."
app_email = "it@medochemie.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/medochemie/css/medochemie.css"
app_include_js = "/assets/medochemie/js/item-override.js"
app_include_js = "/assets/medochemie/js/form-override.js"

#app_include_js = "/assets/medochemie/js/jobcard_extensions.js"


# include js, css files in header of web template
# web_include_css = "/assets/medochemie/css/medochemie.css"
# web_include_js = "/assets/medochemie/js/medochemie.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "medochemie/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "medochemie.utils.jinja_methods",
#	"filters": "medochemie.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "medochemie.install.before_install"
# after_install = "medochemie.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "medochemie.uninstall.before_uninstall"
# after_uninstall = "medochemie.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "medochemie.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }


# on_login = "medochemie.overrides.successful_login"
# on_session_creation = "medochemie.overrides.on_session_creation"

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"medochemie.tasks.all"
#	],
#	"daily": [
#		"medochemie.tasks.daily"
#	],
#	"hourly": [
#		"medochemie.tasks.hourly"
#	],
#	"weekly": [
#		"medochemie.tasks.weekly"
#	],
#	"monthly": [
#		"medochemie.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "medochemie.install.before_tests"

# Overriding Methods
# ------------------------------
#

override_whitelisted_methods = {
	"frappe.api.resource.BOM": "medochemie.api.custom_get_bom",
 }

whitelisted = [
    # ... existing whitelisted functions ...
    'medochemie.weighing_module.jobcard_extensions.check_job_card_status',
    # 'medochemie.weighing_module.user_validation.validate_usr',
    # 'medochemie.weighing_module.user_validation.validate_usr_new',

    # 'medochemie.weighing_module.user_validation.validate_usr1',
]

#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "medochemie.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["medochemie.utils.before_request"]
# after_request = ["medochemie.utils.after_request"]

# Job Events
# ----------
# before_job = ["medochemie.utils.before_job"]
# after_job = ["medochemie.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]
# https://erpnext.medochemie.com/app/custom-field/Item-type

fixtures = [
	{
		"dt": "Custom Field", "filters": [
			[
				"name", "in", [
					'Item-misc',
					'Item-type'

				]
			]
		],
	},
	{
		"dt": "Property Setter", "filters": [
			[
				"name", "in", [
					'Item-main-field_order',
                    'Item-warranty_period-hidden',
                    'Item-valuation_method-hidden',
                    'Item-end_of_life-hidden',
                    'Item-item_name-label',
                    'Item-barcodes-hidden',
                    'Item-item_code-reqd',
                    'Item-item_code-hidden',
                    'Item-naming_series-hidden',
                    'Item-naming_series-reqd',
                    'Item-naming_series-options',
                    'Item-weight_uom-in_list_view',
                    'Item-item_group-in_list_view',
                    'Item-item_name-in_list_view',
				]
			]
		],
	},
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"medochemie.auth.validate"
# ]


fixtures = [
 	"Item Family",
]
