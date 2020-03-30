# Copyright 2017 Dario Lodeiros - Dario Lodeiros <dariodafoz@gmail.com>
# Copyright 2018 Angel Moya
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "HelpDesk_project",
    "summary":
        "Module to Support Teams",
    "version": "13.0.0.0.1",
    "category": "Customer Relationship Management",
    "website": "",
    "author": "Carlos Soriano <csoriano@puntsistemes.es>,"
              "Puntsistemes",
    "license": "AGPL-3",
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "views/project_views.xml",
        "views/ticket_views.xml",
    ],
    "application": True,
    "installable": True,
    "depends": [
        "helpdesk_mgmt",
        "project"],
}
