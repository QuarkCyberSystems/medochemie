frappe.ui.form.on('Item', {
    onload_post_render: function(frm) {
            console.log('Load Form');

        console.log(frm);
            if (frm.doc.item_group != "Products") {
                document.querySelector('div[data-doctype="BOM"]').remove()
            }

    }
});

// Filter items based on product groups
frappe.ui.form.on('BOM', {
    onload_post_render: function(frm) {
        // Filter items with product group "Materials" or "API"
        
        frappe.msgprint({
            title: __('Diactivating BOM`s'),
            indicator: 'green',
            message: 'All active R&D BOM`s will be deactivated'
        });
        

        frm.set_query("item_code", "items", function() {
            return {
                filters: [
                    ['item_group', 'in', ['Raw Material', 'API', 'BOM Materials']]
                ]
            };
        });

    }
});




// Filter items based on product groups
frappe.ui.form.on('User', {
    onload_post_render: function(frm) {
        // Filter items with product group "Materials" or "API"
        


    }
});


