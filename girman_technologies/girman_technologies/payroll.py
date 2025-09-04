import frappe


# Check employees' tax regime preference
def before_save_salary_slip(doc, method):
	employee = frappe.get_doc("Employee", doc.employee)
	if employee.custom_tax_regime_preference == "Old Regime":
		doc.salary_structure = frappe.db.get_value("Salary Structure", {"name": "Old Regime"})
	elif employee.custom_tax_regime_preference == "New Regime":
		doc.salary_structure = frappe.db.get_value("Salary Structure", {"name": "New Regime"})
	else:
		doc.salary_structure = frappe.db.get_value("Salary Structure", {"name": "GirmanTechnologies"})

	#  Investments
	investment = frappe.db.get_value(
		"Employee Investment Declaration",
		{"employee": doc.employee},
		["section_80c", "section_80d", "other_exemptions"],
		as_dict=True,
	)

	if investment:
		total_exemptions = investment.section_80c + investment.section_80d + investment.other_exemptions
		doc.append("deductions", {"salary_component": "Investments", "amount": total_exemptions})

		# doc.total_deduction += total_exemptions
		# doc.gross_pay -= total_exemptions
