import frappe
import erpnext

def execute():
	frappe.reload_doc('portal', 'doctype', 'homepage_featured_product')
	frappe.reload_doc('portal', 'doctype', 'homepage')
	frappe.reload_doc('portal', 'doctype', 'products_settings')

	website_settings = frappe.get_doc('Website Settings', 'Website Settings')
	if frappe.db.exists('Web Page', website_settings.home_page):
		header = frappe.db.get_value('Web Page', website_settings.home_page, 'header')
		if header and header.startswith("<div class='hero text-center'>"):
			homepage = frappe.get_doc('Homepage', 'Homepage')
			homepage.company = erpnext.get_default_company()
			homepage.tag_line = header.split('<h1>')[1].split('</h1>')[0] or 'Default Website'
			homepage.setup_items()
			homepage.save()

			website_settings.home_page = 'home'
			website_settings.save()

