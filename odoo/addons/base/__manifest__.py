# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Base',
    'version': '1.3',
    'category': 'Hidden',
    'description': """
The kernel of Odoo, needed for all installation.
===================================================
""",
    'depends': [],
    'data': [
        'data/res.lang.csv',
        'data/base_data.xml',
        'data/res_currency_data.xml',
        'data/res_country_data.xml',
        'security/base_security.xml',
        'views/base_menus.xml',
        'views/res_config_views.xml',
        'data/res.country.state.csv',
        'views/ir_actions_views.xml',
        'views/ir_config_parameter_views.xml',
        'views/ir_cron_views.xml',
        'views/ir_filters_views.xml',
        'views/ir_mail_server_views.xml',
        'views/ir_model_views.xml',
        'views/ir_attachment_views.xml',
        'views/ir_rule_views.xml',
        'views/ir_sequence_views.xml',
        'views/ir_translation_views.xml',
        'views/ir_ui_menu_views.xml',
        'views/ir_ui_view_views.xml',
        'views/ir_default_views.xml',
        'data/ir_cron_data.xml',
        'report/ir_model_report.xml',
        'report/ir_model_templates.xml',
        'views/ir_logging_views.xml',
        'views/ir_qweb_widget_templates.xml',
        'views/ir_module_views.xml',
        'data/ir_module_category_data.xml',
        'report/ir_module_reports.xml',
        'report/ir_module_report_templates.xml',
        'wizard/base_module_update_views.xml',
        'wizard/base_language_install_views.xml',
        'wizard/base_import_language_views.xml',
        'wizard/base_module_upgrade_views.xml',
        'wizard/base_module_uninstall_views.xml',
        'wizard/base_export_language_views.xml',
        'wizard/base_update_translations_views.xml',
        'data/ir_actions_data.xml',
        'views/res_company_views.xml',
        'views/res_lang_views.xml',
        'views/res_partner_views.xml',
        'views/res_bank_views.xml',
        'views/res_country_views.xml',
        'views/res_currency_views.xml',
        'views/res_users_views.xml',
        'data/res_partner_data.xml',
        'views/ir_property_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_paperformat_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
        'data/res_company_demo.xml',
        'data/res_users_demo.xml',
        'data/res_partner_bank_demo.xml',
        'data/res_currency_rate_demo.xml',
        'data/res_bank_demo.xml',
        'data/res_partner_demo.xml',
        'data/res_partner_image_demo.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': True,
    'post_init_hook': 'post_init',
}
