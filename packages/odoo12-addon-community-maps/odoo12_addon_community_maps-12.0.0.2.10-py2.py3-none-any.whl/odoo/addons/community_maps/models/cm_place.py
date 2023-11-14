import json
from jinja2 import Template
from odoo import models, api, fields
from odoo.tools.translate import _
from odoo.addons.community_maps.models.cm_utils import CmUtils
from odoo.exceptions import ValidationError

class CmPlace(models.Model):
  _name = 'crm.team'

  _inherit = ["crm.team","cm.slug.id.mixin","mail.thread"]

  _labeled_meta_formats = ['uri','progress']

  # TODO: How to manage this in a better
  _color_schema = {
    'brand': {
      'text': 'text-brand-button',
      'border': 'border-brand-base',
      'bg': 'bg-brand-button'
    },
    'black': {
      'text': 'text-gray-700',
      'border': 'border-gray-800',
      'bg': 'bg-gray-700/30'
    },
    'pink': {
      'text': 'text-pink-900',
      'border': 'border-pink-800',
      'bg': 'bg-pink-300'
    },
    'lime': {
      'text': 'text-lime-800',
      'border': 'border-lime-800',
      'bg': 'bg-lime-500'
    },
    'green': {
      'text': 'text-green-800',
      'border': 'border-green-800',
      'bg': 'bg-green-500'
    },
    'blue': {
      'text': 'text-blue-900',
      'border': 'border-blue-900',
      'bg': 'bg-blue-300'
    },
    'violet': {
      'text': 'text-violet-800',
      'border': 'border-violet-800',
      'bg': 'bg-violet-300'
    },
    'yellow': {
      'text': 'text-yellow-800',
      'border': 'border-yellow-800',
      'bg': 'bg-yellow-500'
    },
    'red': {
      'text': 'text-red-900',
      'border': 'border-red-800',
      'bg': 'bg-red-400'
    },
    'gray': {
      'textColor': 'text-neutral-800',
      'border': 'border-neutral-800',
      'bg': 'bg-neutral-400'
    },
  }

  _order = "id desc"

  lat = fields.Char(string=_("Latitude"))
  lng = fields.Char(string=_("Longitude"))
  status = fields.Selection(selection=[
    ('draft', 'Draft'), 
    ('published', 'Published')
    ], default='draft', required=True, string=_("Status"))
  map_id = fields.Many2one('cm.map',string=_("Related map"))
  form_model_id = fields.Many2one('cm.form.model',string=_("Form"))
  place_category_id = fields.Many2one('cm.place.category',string=_("Category"))
  presenter_model_id = fields.Many2one('cm.presenter.model',string=_("Presenter"))
  place_presenter_metadata_ids = fields.One2many(
    'cm.place.presenter.metadata',
    'place_id',
    string=_("Presenter metadata"))
  team_type = fields.Selection(
    selection_add=[('map_place', _("Map Place")),('map_place_proposal',_("Map Place Proposal"))])
  crowdfunding_type = fields.Selection(
    selection=CmUtils.get_system_crowdfunding_types_selection(),
    string=_("Crowdfunding type"),
    compute="_get_crowdfunding_type",
    store=False)
  form_submission_ids = fields.One2many(
    'crm.lead',
    'team_id',
    string=_("Submissions"),
    domain=[('submission_type','=','place_submission')]
  )
  completed_percentage = fields.Integer(
    string=_("% Completed"),
    compute="_get_completed_percentage",
    store=True)
  completed_percentage_live = fields.Integer(
    string=_("% Completed"),
    compute="_get_completed_percentage_live",
    store=False)
  submissions_target = fields.Integer(string=_("Submission target"))
  has_active_service = fields.Boolean(string=_("Place with active service"))
  address_txt = fields.Char(string=_("Address text"))
  allow_filter_by_status = fields.Boolean(
    string=_('"Active" filter'),
    compute="_get_allow_filter_by_status",
    store=False)
  total_committed_invoicing = fields.Float(
    string=_("Total amount commited (invoicing)"),
    compute="_get_total_committed_invoicing",
    store=True)
  total_committed_submissions = fields.Float(
    string=_("Total amount commited (submissions)"),
    compute="_get_total_committed_submissions",
    store=True)
  proposal_form_submission_id = fields.Many2one(
    'crm.lead',
    string=_("Proposal submission"),
    ondelete='restrict')
  submission_ok_message = fields.Text(
    string=_("Successful message"),
    compute='_get_submission_ok_message',
    store=False)
  submission_ok_email_template_id = fields.Many2one(
    'mail.template',
    compute='_get_submission_ok_email_template_id',
    string=_("Successful email template"),
    store=False)
  crowdfunding_notification_ids = fields.One2many(
    'cm.crowdfunding.notification',
    'team_id',
    string=_("Notifications"))
  filter_mids = fields.Many2many(
    'cm.filter',
    'cm_places_filters', 'place_id', 'filter_id',string=_("Custom filters"))
  # Interaction method
  interaction_method = fields.Selection(selection=[
    ('none', _('None')),
    ('form', _('Form')),
    ('external_link', _('External link')),
    ], default='form', required=True, string=_("Interaction method"))
  external_link_url = fields.Char(string=_("External link URL"),translate=True)
  external_link_target = fields.Selection(selection=[
    ('_blank', _('Open in a new tab')),
    ('_top', _('Open in the same page'))
    ], default='_blank', required=True, string=_("Target link"))

  # system
  @api.multi
  def unlink(self):
    for record in self:
      form_submission_ids = self.env['crm.lead'].search([('team_id','=',record.id)])
      if form_submission_ids.exists() or record.proposal_form_submission_id:
        raise ValidationError(_("You can't delete. Some submissions relate on this info. Archive instead."))
      super(CmPlace,record).unlink()

  @api.constrains('team_type')
  def _setup_crm_defaults_for_map_team_type(self):
    for record in self:
      if record.team_type in ['map_place','map_place_proposal']:
        data = {
          'use_opportunities': True,
          'use_quotations': True,
          'use_leads': True,
          'dashboard_graph_model': 'crm.lead',
          'dashboard_graph_period_pipeline': 'month',
          'dashboard_graph_group_pipeline': 'month'
        }
        if record.crowdfunding_type == 'invoicing_amount':
          data['use_invoices'] = True
        record.write(data)

  @api.constrains('user_id')
  def _add_team_leader_as_follower(self):
    for record in self:
      if record.user_id:
        self.message_subscribe([self.user_id.partner_id.id])

  @api.constrains('invoiced_target')
  def _recompute_place_progress(self):
    for record in self:
      self._get_total_committed_invoicing()
      self._get_completed_percentage()
      for submission in self.form_submission_ids:
        submission.update_probability()

  @api.depends('form_submission_ids')
  def _get_total_committed_invoicing(self):
    for record in self:
      total = 0
      if record.form_submission_ids:
        for submission in record.form_submission_ids:
            total += submission.planned_revenue
      record.total_committed_invoicing = total

  @api.depends('form_submission_ids')
  def _get_total_committed_submissions(self):
    for record in self:
      record.total_committed_submissions = len(record.form_submission_ids.filtered(lambda submission: submission.submission_type == 'place_submission'))

  @api.depends('form_submission_ids')
  def _get_completed_percentage(self):
    for record in self:
      if record.crowdfunding_type == 'invoicing_amount':
        if record.invoiced_target:
          record.completed_percentage = int(record.total_committed_invoicing/record.invoiced_target*100)
      if record.crowdfunding_type == 'submission_amount':
        if record.submissions_target:
          record.completed_percentage = int(record.total_committed_submissions/record.submissions_target*100)

  @api.depends('form_submission_ids')
  def _get_completed_percentage_live(self):
    for record in self:
      if record.crowdfunding_type == 'invoicing_amount':
        if record.invoiced_target:
          record._get_total_committed_invoicing()
          record.completed_percentage_live = int(record.total_committed_invoicing/record.invoiced_target*100)
      if record.crowdfunding_type == 'submission_amount':
        if record.submissions_target:
          record._get_total_committed_submissions()
          record.completed_percentage_live = int(record.total_committed_submissions/record.submissions_target*100)

  @api.depends('map_id')
  def _get_crowdfunding_type(self):
    for record in self:
      if record.map_id:
        record.crowdfunding_type = record.map_id.crowdfunding_type

  @api.depends('map_id')
  def _get_allow_filter_by_status(self):
    for record in self:
      if record.map_id:
        record.allow_filter_by_status = record.map_id.allow_filter_by_status

  # place config preselection
  @api.onchange('map_id')
  def _get_config_relations_attrs(self):
    self.ensure_one()
    allowed_form_model_ids = self.map_id.allowed_form_model_mids 
    allowed_place_category_ids = self.map_id.allowed_place_category_mids
    allowed_presenter_model_ids = self.map_id.allowed_presenter_model_mids 
    allowed_filter_group_mids_map =  \
      self.map_id.allowed_filter_group_mids.mapped(
        lambda r: r.filter_ids.mapped('id'))
    allowed_filter_group_mids = []
    for filter_group in allowed_filter_group_mids_map:
      allowed_filter_group_mids += filter_group
    return_dict = {
      'domain':{
        'form_model_id': [('id', 'in',allowed_form_model_ids.mapped('id'))],
        'place_category_id': [('id', 'in',allowed_place_category_ids.mapped('id'))],
        'presenter_model_id': [('id', 'in',allowed_presenter_model_ids.mapped('id'))],
        'filter_mids': [('id','in',allowed_filter_group_mids)]
      }
    }
    if allowed_form_model_ids:
      self.form_model_id = allowed_form_model_ids[0].id
    if allowed_place_category_ids:
      self.place_category_id = allowed_place_category_ids[0].id
    if allowed_presenter_model_ids:
      self.presenter_model_id = allowed_presenter_model_ids[0].id
    return return_dict

  def _get_filters_data_datamodel_dict(self):
    filters = []
    for filter in self.filter_mids:
      filters.append({
        'title': filter.name,
        'group': filter.filter_group_id.slug_id,
        'icon_class': filter.icon.replace('_', '-'),
        'color': self._color_schema[filter.color],
        'markerColor': {
          'markerText': filter.marker_text_color,
          'markerColor': filter.marker_color,
          'markerBg': filter.marker_bg_color,
          'markerBorder': filter.marker_border_color
        }
      })
      return filters

  def _get_category_data_datamodel_dict(self):
    return {
      'title': self.place_category_id.name,
      'icon_class': self.place_category_id.icon.replace('_', '-'),
      'color': self._color_schema[self.place_category_id.color],
      'markerColor': {
        'markerText': self.place_category_id.marker_text_color,
        'markerColor': self.place_category_id.marker_color,
        'markerBg': self.place_category_id.marker_bg_color,
        'markerBorder': self.place_category_id.marker_border_color
      }
    }

  # PRESENTER
  def _get_create_place_meta(self,key,type,format,sort_order,place_id,dataschema,uischema):
    return self._get_create_place_meta_dmodel(
      'cm.place.presenter.metadata',
      key,type,format,sort_order,place_id,dataschema,uischema)

  def _get_create_place_meta_dmodel(self,model,key,type,format,sort_order,place_id,dataschema,uischema):
    creation_data = {
      'type' : type,
      'key' : key,
      'format' : format,
      'sort_order' : sort_order,
      'place_id': place_id
    }
    # default values
    if key in dataschema.keys():
      creation_data['value'] = dataschema[key]
    # default labels
    if ".label" in key:
      if 'elements' in uischema.keys():
        for element in uischema['elements']:
          if element['type'] == 'Links':
            for sub_element in element['elements']:
              label = self._get_schema_meta_label_from_key(sub_element,key)
              if label:
                creation_data['value'] = label
          else:
            label = self._get_schema_meta_label_from_key(element,key)
            if label:
              creation_data['value'] = label
    query = [
      ('place_id', '=', place_id),
      ('key','=',key),
      ('type','=',type),
      ('format','=',format)
    ]
    return CmUtils.get_create_existing_model(
      self.env[model],
      query,
      creation_data
    )
  
  def _get_schema_meta_label_from_key(self,element,key):
    meta_key = key.replace('.label','')
    if element['scope'] == '#/properties/'+meta_key:
      if "label" in element.keys():
        return element['label']
    return False

  # public method to be called from erppeek after import
  def build_presenter_metadata_ids(self):
    self._build_presenter_metadata_ids()
    return True

  @api.onchange('presenter_model_id')
  def _build_presenter_metadata_ids(self,presenter_model_relation='presenter_model_id',metas_relation='place_presenter_metadata_ids'):
    self.ensure_one()
    try:
      place_id = self._origin.id
    except:
      place_id = self.id
    place_presenter_metadata_ids = []
    presenter_model_id = getattr(self,presenter_model_relation)
    if presenter_model_id:
      presenter_json_schema = json.loads(presenter_model_id.json_schema)
      presenter_json_dataschema = json.loads(presenter_model_id.json_dataschema)
      presenter_json_uischema = json.loads(presenter_model_id.json_uischema)
      current_meta_ids = []
      sort_order = 0
      for meta_key in presenter_json_schema['properties'].keys():
        meta_format = ''
        if 'format' in presenter_json_schema['properties'][meta_key].keys():
          meta_format = presenter_json_schema['properties'][meta_key]['format']
        if meta_format in self._labeled_meta_formats:
          place_meta = self._get_create_place_meta(
            meta_key+'.label',
            'string',
            meta_format+'.label',
            sort_order,
            place_id,
            presenter_json_dataschema,
            presenter_json_uischema
          )
          current_meta_ids.append(place_meta.id)
          place_presenter_metadata_ids.append((4,place_meta.id))
          sort_order += 1
        if meta_format != 'progress':
          place_meta = self._get_create_place_meta(
            meta_key,
            presenter_json_schema['properties'][meta_key]['type'],
            meta_format,
            sort_order,
            place_id,
            presenter_json_dataschema,
            presenter_json_uischema
          )
          current_meta_ids.append(place_meta.id)
          place_presenter_metadata_ids.append((4,place_meta.id))
          sort_order += 1
      # delete metas not in presenter
      for metadata in self.place_presenter_metadata_ids:
        if metadata.id not in current_meta_ids:
          place_presenter_metadata_ids.append((2,metadata.id))
    else:
      # delete all metas
      for metadata in self.place_presenter_metadata_ids:
        place_presenter_metadata_ids.append((2,metadata.id))
    # create metas
    setattr(self,metas_relation,place_presenter_metadata_ids)

  # DATAMODEL / API
  def _build_base_datamodel(self):
    place_dict = {
      'name': self.name,
      'slug': self.slug_id,
      'map_slug': self.map_id.slug_id,
      'category_slug': self.place_category_id.slug_id,
      'category_data': self._get_category_data_datamodel_dict(),
      'category_': self.place_category_id.name,
      'interaction_method': self.interaction_method,
      'form_slug': None,
      'external_link_url': None,
      'external_link_target': None,
      'external_link_cta_txt': None,
      'filters': self._get_filters_datamodel_dict(),
      'filters_data': self._get_filters_data_datamodel_dict(),
      'lat': self.lat,
      'lng': self.lng,
      'address': None,
      'submission_number': int(self.total_committed_submissions)
    }
    if self.address_txt:
      place_dict['address'] = self.address_txt
    if self.allow_filter_by_status:
      place_dict['active'] = self.has_active_service
    if self.crowdfunding_type != 'none':
      if self.completed_percentage > 100:
        completed_percentage_return = 100
      else:
        completed_percentage_return = self.completed_percentage
      place_dict['goalProgress'] = completed_percentage_return
    if self.interaction_method == 'form' and self.form_model_id:
      place_dict['form_slug'] = self.form_model_id.slug_id
    elif self.interaction_method == 'external_link':
      place_dict['external_link_url'] = self.external_link_url
      place_dict['external_link_target'] = self.external_link_target
      place_dict['external_link_cta_txt'] = self.map_id.external_link_cta_txt
    return place_dict

  def _get_filters_datamodel_dict(self):
    filters = []
    for filter in self.filter_mids:
      filters.append(filter.slug_id)
    if not filters:
      return False
    return filters

  def _build_presenter_schemadata_json(self,presenter_model_relation='presenter_model_id',metas_relation='place_presenter_metadata_ids'):
    presenter_model_id = getattr(self,presenter_model_relation)
    if presenter_model_id:
      presenter_schemadata_dict = {}
      presenter_json_schema = json.loads(presenter_model_id.json_schema)
      for meta_key in presenter_json_schema['properties'].keys():
        if presenter_json_schema['properties'][meta_key]['format'] == 'progress':
          if self.completed_percentage > 100:
            completed_percentage_return = 100
          else:
            completed_percentage_return = self.completed_percentage
          presenter_schemadata_dict['progress'] = completed_percentage_return
        else:
          place_meta_ids = getattr(self,metas_relation)
          place_meta = place_meta_ids.filtered(lambda r: r.key == meta_key)
          if place_meta.exists():
            if place_meta[0].value:
              meta_val_template = Template( place_meta[0].value )
              presenter_schemadata_dict[meta_key] = meta_val_template.render(self._build_base_datamodel())
            else:
              presenter_schemadata_dict[meta_key] = None
      return presenter_schemadata_dict
    return False

  def _build_presenter_schema_json(self,presenter_model_relation='presenter_model_id'):
    presenter_model_id = getattr(self,presenter_model_relation)
    if presenter_model_id:
      return json.loads(presenter_model_id.json_schema)
    return False
  
  def _build_presenter_uischema_json(self,presenter_model_relation='presenter_model_id'):
    presenter_model_id = getattr(self,presenter_model_relation)
    if presenter_model_id:
      presenter_json_schema = json.loads(presenter_model_id.json_schema)
      presenter_json_uischema = json.loads(presenter_model_id.json_uischema)
      for element in presenter_json_uischema['elements']:
        if element['type'] == 'Links':
          for sub_element in element['elements']:
            meta_label = self._get_meta_label_from_scope(presenter_json_schema,sub_element['scope'])
            if meta_label:
              meta_label_template = Template(meta_label)
              sub_element['label'] = meta_label_template.render(self._build_base_datamodel())
        else:
          meta_label = self._get_meta_label_from_scope(presenter_json_schema,element['scope'])
          if meta_label:
            meta_label_template = Template(meta_label)
            element['label'] = meta_label_template.render(self._build_base_datamodel())
      return presenter_json_uischema
    return False

  def _get_meta_label_from_scope(self,json_schema,scope):
    meta_key = scope.replace('#/properties/','')
    meta_format = json_schema['properties'][meta_key]['format']
    if meta_format in self._labeled_meta_formats:
      place_meta = self.place_presenter_metadata_ids.filtered(lambda r: r.key == meta_key+'.label')
      if place_meta.exists():
        return place_meta[0].value
    return False

  # api datamodel
  def get_datamodel_dict(self,single_view=False):
    place_dict = self._build_base_datamodel()
    if single_view:
      place_dict['schemaData'] = self._build_presenter_schemadata_json()
      place_dict['jsonSchema'] = self._build_presenter_schema_json()
      place_dict['uiSchema'] = self._build_presenter_uischema_json()
    return place_dict

  # UI actions
  def accept_place_proposal_workflow_action(self):
    # TODO: Do we mark the lead as won?!?
    for record in self:
      record.write({'team_type':'map_place'})

  def publish_place_workflow_action(self):
    for record in self:
      record.write({'status':'published'})

  def unpublish_place_workflow_action(self):
    for record in self:
      record.write({'status':'draft'})

  # Form Submission
  def submit_place_form(self,data,submission_fields_map=False):
    # Submission creation
    submission = self.env['crm.lead'].create({
      'name': self.name + " (Place Submission)",
      'submission_type': 'place_submission',
    })
    # Shareable_url
    first_overwrite = {}
    try:
      shareable_url_base = data['shareable_url_base']
    except:
      shareable_url_base = False
    if shareable_url_base:
      first_overwrite['shareable_url_base'] = shareable_url_base
    # Force team_id after everything happens on crm lead creation.
    first_overwrite['team_id'] = self.id
    # First overwrite
    submission.write(first_overwrite)
    # Metadata creation
    if(submission_fields_map):
      fields_map = submission_fields_map
    else:
      fields_map = self.form_model_id.json_submission_fields_map
    submission.create_submission_metadata(
      data=data,
      fields_map= fields_map
    )
    # Second overwrite
    submission.write({
      'name': submission.name + " #" + str(submission.id)
    })
    # Constrain probability
    submission.constrain_revenue()
    
    
    if self.form_model_id.follower_partner_id:
      submission.message_subscribe([self.form_model_id.follower_partner_id.id])
    submission.message_post(
      subject=submission.name+" notification",
      body="New place submission has been made!",
      message_type="comment",
      subtype="mail.mt_comment"
    )
    return submission

  def crowdfunding_notify_if_must(self):
    for request in self.map_id.crowdfunding_notification_request_ids:
      if self.completed_percentage >= request.percentage:
        existing_notification = self.env['cm.crowdfunding.notification'].search([
          ('team_id', '=', self.id),
          ('percentage', '=', request.percentage)
        ])
        if existing_notification.exists():
          return False
        else:
          self.message_post(
            subject=self.name+" notification",
            body="Place reached percentage: %s" % self.completed_percentage,
            message_type="comment",
            subtype="mail.mt_comment"
          )
          notification = self.env['cm.crowdfunding.notification'].create({
            'team_id': self.id,
            'percentage': request.percentage
          })
          return True
    return False

  @api.depends('form_model_id')
  def _get_submission_ok_message(self):
    for record in self:
      try:
        ok_message = record.form_model_id.submission_ok_message
      except:
        ok_message = False
      record.submission_ok_message = ok_message

  @api.depends('form_model_id')
  def _get_submission_ok_email_template_id(self):
    for record in self:
      try:
        email_template = record.form_model_id.submission_ok_email_template_id
      except:
        email_template = False
      record.submission_ok_email_template_id = email_template.id
