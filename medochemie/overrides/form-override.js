frappe.ui.form.on('Form', {
  refresh: function(frm) {
    frm.add_custom_button(__("My Custom Button"), function() {
      // Add your custom button logic here
      frappe.msgprint("Custom button clicked!");
    });
  }
});