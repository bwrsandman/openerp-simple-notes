from openerp.osv import fields, osv
from openerp.tools.translate import _


class sn_note(osv.Model):
    """
    A very simple note
    """
    _name = 'sn.note'
    _description = 'A very simple note'
    _columns = {
        'title': fields.char(_('Title'), size=255, require=True),
        'content': fields.text(_('Content')),
        'user_id': fields.many2one('res.users', string=_('Owner'),
                                   ondelete='cascade', required=True,
                                   select=1),
    }
