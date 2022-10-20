    # odoo manifeast file
{
    'name': 'Water Purification Plant Managent Dashboard',
    'version' : "1.0",
    'author' : "Chetan Rathod",
    'summary': "Dashboard to manager water purification plant",
    'description': "Dashboard to manager water purification plant",
    'depends' : ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/user_account.xml',
        'views/distribution.xml',
        'views/employee.xml',
        # 'views/read_mail_trigger.xml',

        'report/customer_card.xml',
    ],
    
    'installable': True,
    'application' : True,
    "sequence":-100,
    'license': 'LGPL-3',
}
