from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register', views.register, name='register'),
    
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('sale_invoices', views.sale_invoices, name='sale_invoices'),
    path('estimate_quotation', views.estimate_quotation, name='estimate_quotation'),
    path('payment_in', views.payment_in, name='payment_in'),
    path('sale_order', views.sale_order, name='sale_order'),
    path('delivery_challan', views.delivery_challan, name='delivery_challan'),
    path('sale_return_cr', views.sale_return_cr, name='sale_return_cr'),

    # created by athul
    path('settings', views.settings, name='settings'),
    path('hide_options', views.hide_options, name='hide_options'),

    path('staffhome', views.staffhome, name='staffhome'),
    path('adminhome', views.adminhome, name='adminhome'),
    
    
    path('staff_register', views.staff_register, name='staff_register'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('company_reg', views.company_reg, name='company_reg'),
    path('company_reg2', views.company_reg2, name='company_reg2'),
    path('add_company', views.add_company, name='add_company'),
    path('log_page', views.log_page, name='log_page'),
    path('login', views.login, name='login'),
    path('adminaccept/<id>', views.adminaccept, name='adminaccept'),
    path('adminreject/<id>', views.adminreject, name='adminreject'),
    path('View_staff', views.View_staff, name='View_staff'),
    path('companyaccept/<id>', views.companyaccept, name='companyaccept'),
    path('companyreject/<id>', views.companyreject, name='companyreject'),
    path('client_request', views.client_request, name='client_request'),
    path('client_details', views.client_details, name='client_details'),
    path('staff_request', views.staff_request, name='staff_request'),
    path('payment_term', views.payment_term, name='payment_term'),
    path('add_payment_terms', views.add_payment_terms, name='add_payment_terms'),
    path('Allmodule/<uid>', views.Allmodule, name='Allmodule'),
    path('addmodules/<uid>', views.addmodules, name='addmodules'),
    path('client_request_overview/<id>', views.client_request_overview, name='client_request_overview'),
    path('client_details_overview/<id>', views.client_details_overview, name='client_details_overview'),


    
    path('companyreport', views.companyreport, name='companyreport'),
    path('Companyprofile', views.Companyprofile, name='Companyprofile'),
    path('editcompanyprofile', views.editcompanyprofile, name='editcompanyprofile'),
    path('editcompanyprofile_action', views.editcompanyprofile_action, name='editcompanyprofile_action'),
    path('editmodule', views.editmodule, name='editmodule'),
    path('editmodule_action', views.editmodule_action, name='editmodule_action'),
    path('admin_notification', views.admin_notification, name='admin_notification'),
    path('module_updation_details/<mid>', views.module_updation_details, name='module_updation_details'),
    path('module_updation_ok/<mid>', views.module_updation_ok, name='module_updation_ok'),
    path('staff_profile', views.staff_profile, name='staff_profile'),
    path('editstaff_profile', views.editstaff_profile, name='editstaff_profile'),
    path('editstaff_profile_action', views.editstaff_profile_action, name='editstaff_profile_action'),

    path('distributor_home', views.distributor_home, name='distributor_home'),
    path('distributor_reg', views.distributor_reg, name='distributor_reg'),
    path('distributor_reg_action', views.distributor_reg_action, name='distributor_reg_action'),
    path('distributors', views.distributors, name='distributors'),
    path('clients', views.clients, name='clients'),
    path('distributor_request', views.distributor_request, name='distributor_request'),
    path('admin_distributor_accept/<id>', views.admin_distributor_accept, name='admin_distributor_accept'),
    path('admin_distributor_reject/<id>', views.admin_distributor_reject, name='admin_distributor_reject'),
    path('distributor_request_overview/<id>', views.distributor_request_overview, name='distributor_request_overview'),
    path('distributor_details', views.distributor_details, name='distributor_details'),
    path('distributor_details_overview/<id>', views.distributor_details_overview, name='distributor_details_overview'),
    path('dcompany_request', views.dcompany_request, name='dcompany_request'),
    path('dcompany_details', views.dcompany_details, name='dcompany_details'),
    path('dcompany_request_overview/<id>', views.dcompany_request_overview, name='dcompany_request_overview'),
    path('distributor_accept_company/<id>', views.distributor_accept_company, name='distributor_accept_company'),
    path('distributor_reject_company/<id>', views.distributor_reject_company, name='distributor_reject_company'),
    path('dcompany_details_overview/<id>', views.dcompany_details_overview, name='dcompany_details_overview'),
    path('distributor_profile', views.distributor_profile, name='distributor_profile'),
    
    # ========================================   ASHIKH V U (START) ======================================================

    path('item_create', views.item_create, name='item_create'),
    path('items_list/<int:pk>', views.items_list, name='items_list'),
    path('item_create_new', views.item_create_new, name='item_create_new'),
    path('item_delete/<int:pk>', views.item_delete, name='item_delete'),
    path('item_view_or_edit/<int:pk>', views.item_view_or_edit, name='item_view_or_edit'),
    path('item_unit_create', views.item_unit_create, name='item_unit_create'),
    path('item_update/<int:pk>', views.item_update, name='item_update'),
    path('item_search_filter', views.item_search_filter, name='item_search_filter'),
    path('item_get_detail/<int:pk>', views.item_get_detail, name='item_get_detail'),
    path('item_get_details_for_modal_target/<int:pk>', views.item_get_details_for_modal_target, name='item_get_details_for_modal_target'),
    path('ajust_quantity/<int:pk>', views.ajust_quantity, name='ajust_quantity'),
    path('transaction_delete/<int:pk>', views.transaction_delete, name='transaction_delete'),
    path('item_transaction_view_or_edit/<int:pk>/<int:tran>', views.item_transaction_view_or_edit, name='item_transaction_view_or_edit'),
    path('update_adjusted_transaction/<int:pk>/<int:tran>', views.update_adjusted_transaction, name='update_adjusted_transaction'),
    path('item_delete_open_stk/<int:pk>',views.item_delete_open_stk,name='item_delete_open_stk'),

    path('bank_create',views.bank_create,name='bank_create'),
    path('banks_list/<int:pk>',views.banks_list,name='banks_list'),
    path('get_bank_to_bank',views.get_bank_to_bank,name='get_bank_to_bank'),
    path('get_bank_to_cash',views.get_bank_to_cash,name='get_bank_to_cash'),
    path('get_cash_to_bank',views.get_cash_to_bank,name='get_cash_to_bank'),
    path('get_adjust_bank_balance',views.get_adjust_bank_balance,name='get_adjust_bank_balance'),
    path('bank_create_new',views.bank_create_new,name='bank_create_new'),
    path('bank_delete/<int:pk>',views.bank_delete,name='bank_delete'),
    path('account_num_check',views.account_num_check,name='account_num_check'),
    path('account_num_check_for_edit/<int:pk>',views.account_num_check_for_edit,name='account_num_check_for_edit'),
    path('bank_ifsc_check',views.bank_ifsc_check,name='bank_ifsc_check'),
    path('bank_view_or_edit/<int:pk>',views.bank_view_or_edit,name='bank_view_or_edit'),
    path('bank_update/<int:pk>',views.bank_update,name='bank_update'),
    path('bank_to_bank_transaction_create',views.bank_to_bank_transaction_create,name='bank_to_bank_transaction_create'),
    path('bank_to_cash_transaction_create',views.bank_to_cash_transaction_create,name='bank_to_cash_transaction_create'),
    path('cash_to_bank_transaction_create',views.cash_to_bank_transaction_create,name='cash_to_bank_transaction_create'),
    path('get_adjust_bank_balance_create',views.get_adjust_bank_balance_create,name='get_adjust_bank_balance_create'),
    path('delete_bank_open_balance/<int:pk>',views.delete_bank_open_balance,name='delete_bank_open_balance'),
    path('delete_bank_transaction/<int:pk>/<int:bank_id>',views.delete_bank_transaction,name='delete_bank_transaction'),
    path('view_or_edit_bank_transaction/<int:pk>/<int:bank_id>',views.view_or_edit_bank_transaction,name='view_or_edit_bank_transaction'),
    path('update_bank_transaction/<int:pk>/<int:bank_id>',views.update_bank_transaction,name='update_bank_transaction'),
    path('import_from_excel/<int:pk>',views.import_from_excel,name='import_from_excel'),
    path('import_statement_from_excel/<int:pk>',views.import_statement_from_excel,name='import_statement_from_excel'),
    path('transaction_history/<int:pk>/<int:bank_id>',views.transaction_history,name='transaction_history'),
    path('bank_transaction_statement/<int:bank_id>',views.bank_transaction_statement,name='bank_transaction_statement'),
    
    # ========================================   ASHIKH V U (END) ======================================================
    
    #______________Parties(new)_________________Antony Tom___________________________

    path('add_parties', views.add_parties, name='add_parties'),
    path('save_parties', views.save_parties, name='save_parties'),
    path('view_parties', views.view_parties, name='view_parties'),
    path('view_party/<int:id>', views.view_party, name='view_party'),
    path('edit_party/<int:id>', views.edit_party, name='edit_party'),
    path('edit_saveparty/<int:id>', views.edit_saveparty, name='edit_saveparty'),
    path('deleteparty/<int:id>', views.deleteparty, name='deleteparty'),
    #End
    
    path('view_purchasebill',views.view_purchasebill,name='view_purchasebill'),
    path('add_purchasebill',views.add_purchasebill,name='add_purchasebill'), 
    path('create_purchasebill',views.create_purchasebill,name='create_purchasebill'),
    path('edit_purchasebill/<int:id>',views.edit_purchasebill,name='edit_purchasebill'),
    path('update_purchasebill/<int:id>',views.update_purchasebill,name='update_purchasebill'),
    path('details_purchasebill/<int:id>',views.details_purchasebill,name='details_purchasebill'),
    path('history_purchasebill/<int:id>',views.history_purchasebill,name='history_purchasebill'),
    path('delete_purchasebill/<int:id>',views.delete_purchasebill,name='delete_purchasebill'), 
    path('import_purchase_bill',views.import_purchase_bill,name='import_purchase_bill'), 
    path('billhistory',views.billhistory,name='billhistory'), 
    path('bankdata',views.bankdata,name='bankdata'), 
    path('savecustomer',views.savecustomer,name='savecustomer'),
    path('cust_dropdown',views.cust_dropdown,name='cust_dropdown'),
    path('saveitem',views.saveitem,name='saveitem'),
    path('item_dropdown',views.item_dropdown,name='item_dropdown'),
    path('custdata',views.custdata,name='custdata'),
    path('itemdetails',views.itemdetails,name='itemdetails'),
    path('add_purchaseorder',views.add_purchaseorder,name='add_purchaseorder'),
    path('view_purchaseorder',views.view_purchaseorder,name='view_purchaseorder'),
    
    # =========== estimate & delivery challan=========== shemeem - start =======================================
    path('create_estimate',views.create_estimate, name='create_estimate'),
    path('add_new_party',views.addNewParty, name='addNewParty'),
    path('add_new_item',views.addNewItem, name='addNewItem'),
    path('get_party_details',views.getPartyDetails, name='getPartyDetails'),
    path('get_item_data',views.getItemData, name='getItemData'),
    path('create_new_estimate',views.createNewEstimate, name='createNewEstimate'),
    path('get_party_list',views.getPartyList, name= 'getPartyList'),
    path('get_item_list',views.getItemList, name = 'getItemList'),
    path('estimate_filter_with_date',views.estimateFilterWithDate, name='estimateFilterWithDate'),
    path('estimate_filter_with_ref',views.estimateFilterWithRef, name='estimateFilterWithRef'),
    path('estimate_filter_with_name',views.estimateFilterWithName, name='estimateFilterWithName'),
    path('estimate_filter_with_total',views.estimateFilterWithTotal, name='estimateFilterWithTotal'),
    path('estimate_filter_with_bal',views.estimateFilterWithBal, name='estimateFilterWithBal'),
    path('estimate_filter_with_stat',views.estimateFilterWithStat, name='estimateFilterWithStat'),
    path('estimate_in_between', views.estimateInBetween, name='estimateInBetween'),
    path('edit_estimate/<int:id>',views.editEstimate, name='editEstimate'),
    path('update_estimate/<int:id>',views.updateEstimate, name= 'updateEstimate'),
    path('delete_estimate_quotation/<int:id>',views.deleteEstimate, name = 'deleteEstimate'),
    path('estimate_transaction_history/<int:id>',views.estimateTransactionHistory, name='estimateTransactionHistory'),
    path('import_estimate_form_excel',views.importEstimateFromExcel, name='importEstimateFromExcel'),
    path('download_estimate_sample_file',views.downloadEstimateSampleImportFile, name = 'downloadEstimateSampleImportFile'),
    path('estimate_bill_pdf_view/<int:id>',views.estimateBillPdf, name='estimateBillPdf'),
    path('view_estimate_bill/<int:id>',views.viewEstimate, name='viewEstimate'),


    path('create_delivery_challan',views.createDeliveryChallan, name='createDeliveryChallan'),
    path('create_new_delivery_challan',views.createNewDeliveryChallan, name='createNewDeliveryChallan'),
    path('challan_in_between', views.challanInBetween, name='challanInBetween'),
    path('challan_filter_with_date',views.challanFilterWithDate, name='challanFilterWithDate'),
    path('challan_filter_with_duedate',views.challanFilterWithDueDate, name='challanFilterWithDueDate'),
    path('challan_filter_with_challan_no',views.challanFilterWithChallanNo, name='challanFilterWithChallanNo'),
    path('challan_filter_with_name',views.challanFilterWithName, name='challanFilterWithName'),
    path('challan_filter_with_total',views.challanFilterWithTotal, name='challanFilterWithTotal'),
    path('challan_filter_with_bal',views.challanFilterWithBal, name='challanFilterWithBal'),
    path('challan_filter_with_stat',views.challanFilterWithStat, name='challanFilterWithStat'),
    path('delete_delivery_challan/<int:id>',views.deleteChallan, name = 'deleteChallan'),
    path('edit_challan/<int:id>',views.editChallan, name='editChallan'),
    path('update_challan/<int:id>',views.updateChallan, name= 'updateChallan'),
    path('challan_transaction_history/<int:id>',views.challanTransactionHistory, name='challanTransactionHistory'),
    path('import_challan_form_excel',views.importChallanFromExcel, name='importChallanFromExcel'),
    path('download_challan_sample_file',views.downloadChallanSampleImportFile, name = 'downloadChallanSampleImportFile'),
    path('challan_bill_pdf_view/<int:id>',views.challanBillPdf, name='challanBillPdf'),
    path('view_challan_bill/<int:id>',views.viewChallan, name='viewChallan'),


    # ===================================== shemeem - end ==================================================




      #______________sales return(new)_________________Keerthana___________________________

    # path('sales_first', views.sales_first, name='sales_first'),
    path('create_sale', views.create_sale, name='create_sale'),
    path('new_creditnote_item', views.new_creditnote_item, name='new_creditnote_item'),
    path('get_hsn_for_item',views.get_hsn_for_item,name='get_hsn_for_item'),
   
    path('creditnote_list',views.creditnote_list,name='creditnote_list'),
    path('party_dropdown',views.party_dropdown,name='party_dropdown'),
    path('saveparty',views.saveparty,name='saveparty'),
    path('credit_bankdetails',views.credit_bankdetails,name='credit_bankdetails'),
    path('add_creditnote',views.add_creditnote,name='add_creditnote'),
    path('detail_creditnote/<int:id>/',views.detail_creditnote,name='detail_creditnote'),
    #path('creditnotehistory',views.creditnotehistory,name='creditnotehistory'),
    path('import_creditnote',views.import_creditnote,name='import_creditnote'),
    path('delete_CreditNote/<int:id>/', views.delete_CreditNote, name='delete_CreditNote'),
    path('creditnote_item_unit',views.creditnote_item_unit,name='creditnote_item_unit'),
    path('edit_creditnote/<int:id>/',views.edit_creditnote,name='edit_creditnote'),
    path('salesinvoicedata',views.salesinvoicedata,name='salesinvoicedata'),
  
    path('update_creditnote/<int:id>/',views.update_creditnote,name='update_creditnote'),
    path('history_creditnote/<int:id>',views.history_creditnote,name='history_creditnote'),
    path('credititemdetails',views.credititemdetails,name='credititemdetails'),
    path('creditnote_item_dropdown',views.creditnote_item_dropdown,name='creditnote_item_dropdown'),
    path('sharecreditnoteToEmail/<int:id>',views.sharecreditnoteToEmail,name='sharecreditnoteToEmail'),
    path('get_Invoice_date',views.get_Invoice_date,name='get_Invoice_date'),



    #end     
    
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)