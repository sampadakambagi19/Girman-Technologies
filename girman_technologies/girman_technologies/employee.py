import frappe
from frappe.utils import getdate, today
from frappe.utils.pdf import get_pdf


# Status updations
def before_save(doc, method=None):
	"""Update employee status before save based on key dates"""
	today_date = getdate(today())

	if doc.relieving_date and getdate(doc.relieving_date) <= today_date:
		doc.status = "Left"
	elif doc.final_confirmation_date and getdate(doc.final_confirmation_date) <= today_date:
		doc.status = "Active"
	elif doc.custom_probation_end_date and getdate(doc.custom_probation_end_date) > today_date:
		doc.status = "Inactive"
	else:
		doc.status = "Inactive"


# On exit attach employees' exp letter as PDF
def on_update(doc, method=None):
	"""Generate experience letter when employee leaves"""
	if doc.status == "Left" and doc.relieving_date:
		if not frappe.db.exists(
			"File",
			{
				"attached_to_doctype": "Employee",
				"attached_to_name": doc.name,
				"file_name": ["like", "%Experience Letter%.pdf"],
			},
		):
			html = frappe.get_print("Employee", doc.name, print_format="Experience Letter")
			pdf = get_pdf(html)

			file_doc = frappe.get_doc(
				{
					"doctype": "File",
					"file_name": f"Experience Letter - {doc.employee_name}.pdf",
					"attached_to_doctype": "Employee",
					"attached_to_name": doc.name,
					"content": pdf,
					"is_private": 0,
				}
			)
			file_doc.insert(ignore_permissions=True)
