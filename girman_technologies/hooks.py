app_name = "girman_technologies"
app_title = "Girman Technologies"
app_publisher = "Sampada"
app_description = "Custom Application"
app_email = "sampadakambagi@gmail.com"
app_license = "mit"

# Apps
# ------------------

required_apps = ["hrms"]

fixtures = [
	{"dt": "Workflow", "filters": [["name", "in", ["Recruitment Workflow"]]]},
	{"dt": "Custom Field"},
	{
		"dt": "Workflow State",
		"filters": [["name", "in", ["Application", "Screening", "Interview", "Offer", "Hired"]]],
	},
	{"dt": "Dashboard", "filters": [["name", "in", ["Applicants by Source"]]]},
	{"dt": "Dashboard Chart", "filters": [["name", "in", ["Applicants by Source"]]]},
	{"dt": "Letter Head", "filters": [["name", "in", ["Girman Technologies"]]]},
	{"dt": "Print Format", "filters": [["name", "in", ["Experience Letter", "Standard Salary Slip 1"]]]},
	{"dt": "Salary Component", "filters": [["name", "in", ["Special Allowance", "Investments"]]]},
	{
		"dt": "Salary Structure",
		"filters": [["name", "in", ["GirmanTechnologies", "Old Regime", "New Regime"]]],
	},
	{
		"dt": "Report",
		"filters": [["name", "in", ["Tax Regime comparision"]]],
	},
]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "girman_technologies",
# 		"logo": "/assets/girman_technologies/logo.png",
# 		"title": "Girman Technologies",
# 		"route": "/girman_technologies",
# 		"has_permission": "girman_technologies.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/girman_technologies/css/girman_technologies.css"
# app_include_js = "/assets/girman_technologies/js/girman_technologies.js"

# include js, css files in header of web template
# web_include_css = "/assets/girman_technologies/css/girman_technologies.css"
# web_include_js = "/assets/girman_technologies/js/girman_technologies.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "girman_technologies/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "girman_technologies/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "girman_technologies.utils.jinja_methods",
# 	"filters": "girman_technologies.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "girman_technologies.install.before_install"
# after_install = "girman_technologies.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "girman_technologies.uninstall.before_uninstall"
# after_uninstall = "girman_technologies.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "girman_technologies.utils.before_app_install"
# after_app_install = "girman_technologies.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "girman_technologies.utils.before_app_uninstall"
# after_app_uninstall = "girman_technologies.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "girman_technologies.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Employee": {
		"before_save": "girman_technologies.girman_technologies.employee.before_save",
		"on_update": "girman_technologies.girman_technologies.employee.on_update",
	},
	"Salary Slip": {
		# "on_update": "girman_technologies.girman_technologies.payroll.before_save_salary_slip",
		"before_save": "girman_technologies.girman_technologies.payroll.before_save_salary_slip",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"girman_technologies.tasks.all"
# 	],
# 	"daily": [
# 		"girman_technologies.tasks.daily"
# 	],
# 	"hourly": [
# 		"girman_technologies.tasks.hourly"
# 	],
# 	"weekly": [
# 		"girman_technologies.tasks.weekly"
# 	],
# 	"monthly": [
# 		"girman_technologies.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "girman_technologies.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "girman_technologies.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "girman_technologies.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["girman_technologies.utils.before_request"]
# after_request = ["girman_technologies.utils.after_request"]

# Job Events
# ----------
# before_job = ["girman_technologies.utils.before_job"]
# after_job = ["girman_technologies.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"girman_technologies.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
