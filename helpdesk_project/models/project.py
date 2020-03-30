from odoo import api, fields, models, _


class ProjectTask(models.Model):
    _inherit = 'project.task'

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='task_id',
        string='Tickets')

    ticket_count = fields.Integer(
        compute='_compute_ticket_count',
        string="Number of Tickets"
    )

    @api.depends('ticket_ids')
    def _compute_ticket_count(self):
        for task in self:
            task.ticket_count = len(task.ticket_ids)
            

    def action_new_ticket(self):
        #nombre del modulo y el nombre de la accion (cualquiera que coincida con la vista)
        action = self.env.ref("helpdesk_project.task_action_ticket_new").read()[0]
        action['context'] = {
            'default_task_id':self.id,
            'default_project_id': self.project_id and self.project_id.id,
   
        }