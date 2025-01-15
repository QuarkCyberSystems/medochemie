frappe.ui.form.on('Work Order', {

    add_custom_button_to_check_job_cards: function(frm) {

       // alert('Work Order')

        // frm.add_custom_button(__('Check Job Card Status'), function() {
        //     frappe.call({
        //         method: 'erpnext.manufacturing.doctype.work_order.work_order.check_job_card_status',
        //         args: {
        //             work_order: frm.doc.name
        //         },
        //         callback: function(r) {
        //             frappe.msgprint(r.message);
        //         }
        //     });
        // }, __('Actions'));

        frm.add_custom_button(__("Check Job Card Status"), function() {

            frappe.call({
                method: 'medochemie.weighing_module.jobcard_extensions.check_job_card_status',
                args: {
                    job_card_name: frm.doc.name
                },
                callback: function(r) {
                    frappe.msgprint(r.message);
                }
            });

		 }).css({"color":"white", "background-color": "#14141f", "font-weight": "800"});

    },
    onload_post_render: function(frm) {

        //frm.trigger("add_custom_button_to_check_job_cards");

    }

});