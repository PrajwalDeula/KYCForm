from django.contrib import admin
from .models import KYCModel
from .forms import KYCForm  # 1. Import your custom form

class KYCAdmin(admin.ModelAdmin):
    form = KYCForm

    list_display = ('first_name', 'last_name', 'gender', 'mobile', 'email', 'nationality')
    search_fields = ('first_name', 'last_name', 'mobile', 'email')
    list_filter = ('gender', 'nationality', 'profession', 'qualification')
    ordering = ('-kyc_id',) 

    fieldsets = (
        ('Personal Information', {
            'fields': (
                'salutation', 
                ('first_name', 'middle_name', 'last_name'), 
                'nep_name',
                ('gender', 'nationality'),
                ('date_of_birth_ad', 'dob_bs'),
                'qualification',
                'profession',
            )
        }),
        ('Family Details', {
            'fields': (
                'father_name',
                'nep_father_name',              # Added
                'mother_name',
                'father_mother_name',           # Added
                'grand_father_name',
                'grandfather_in_law_name',      # Added
                'spouse_name',
                'father_in_law_name',
                'son_name',
                'daughter_name',
                'daughter_in_law_name',
                'proposer_full_name',
            )
        }),
        ('Document Details', {
            'fields': (
                'age_proof_doc', 
                'document_number', 
                'document_issued_date', 
                'issued_place',
            )
        }),
        ('Address & Contact', {
            'fields': (
                'permanent_address', 
                'temporary_address', 
                'temporary_district', 
                ('ward_no', 'house_no'),
                'local_unit', 
                'structure',
                ('email', 'mobile', 'phone_no'),
            )
        }),
        ('Income & Banking', {
            'fields': (
                'income_mode', 
                'income_amount', 
                'pan_no', 
                'bank_ac_name', 
                'bank_ac_no',
                'office_address', 
                'firm_name'
            )
        }),
        ('Declarations', {
            'fields': (
                'is_politically_involved', 
                'is_family_politically_involved',
                'is_aml_crime',
                'is_family_aml_crime',
            )
        }),
    )

admin.site.register(KYCModel, KYCAdmin)
