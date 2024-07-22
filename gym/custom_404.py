import frappe
from frappe.website.render import render_page

def custom_404():
    path = "404.html"
    response = render_page(path)
    response.status_code = 404
    return response
