from django.db import models
from django.utils.translation import ugettext as _



class Patient(models.Model):
	'''
	A fully featured patient model
	'''

	first_name = models.CharField(
        _('First Name'),
        max_length=255,
        blank=False,
        null=True,
        help_text=_('First Name of the patient (including middle name)'))

	last_name = models.CharField(
        _('Last Name'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Last name of the patient'))

	birth_date = models.DateField(
		_('Date of Birth'),
		blank=False,
		null=True,
		help_text=_('Patient Date of birth'))

	full_address = models.CharField(
        _('First Address'),
        max_length=255,
        blank=False,
        null=True,
        help_text=_('Full Address of the patient'))

	city = models.CharField(
        _('City'),
        max_length=255,
        blank=False,
        null=True,
        help_text=_('City of the patient'))

	state = models.CharField(
        _('State of residence'),
        max_length=255,
        blank=False,
        null=True,
        help_text=_('State of residence of patient'))

	mobile_no = models.CharField(
        _('Mobile No'),
        max_length=10,
        blank=False,
        null=True,
        help_text=_('Mobile No of the patient'))

	landline_no = models.CharField(
        _('Landline No'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Landline no of the patient'))

	email = models.EmailField(
		_('Email ID'),
		max_length=70,
		blank=True,
		null=True,
		help_text=_('Email ID of the patient'),)

	referred_by = models.CharField(
        _('Reffered By'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('Name of the Doctor by whom the patient has been referred'))

	first_visit = models.DateTimeField(
        _('First Visit of the patient'),
        auto_now_add=True,
        help_text=_('When did the patient first visit the hospital'))

	def __unicode__(self):
		
		return '%d' % self.id
        

	





