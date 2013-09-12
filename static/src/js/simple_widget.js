openerp.simple_note = function(openerp)
{
    var QWeb = openerp.web.qweb;
    var _t = openerp._t;

	openerp.web.form.widgets.add('simple_widget', 'openerp.simple_note.SimpleNoteWidget');
	openerp.simple_note.SimpleNoteWidget = openerp.web.form.FieldChar.extend({
		template: "simple_widget",
		init: function(view, code){
			this._super(view, code);
			console.log('loading...');
		}
	});
}
