from django.db import models
from nepali_datetime_field.models import NepaliDateField
from django.utils import timezone
import datetime

SALUTATION_CHOICES = [
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr'),
]

NATIONALITY_CHOICES=[
    ('Nepalese','Nepalese'),
    ('Indian','Indian'),
    ('Other','Other'),
]

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

AGE_PROOF_DOC_CHOICES = [
    ('Citizenship', 'Citizenship'),
    ('Passport', 'Passport'),
    ('Birth Certificate', 'Birth Certificate'),
    ('Other', 'Other'),
]

INCOME_MODE_CHOICES = [
    ('Salary', 'Salary'),
    ('Business', 'Business'),
    ('Investment', 'Investment'),
    ('Other', 'Other'),
]

QUALIFICATION_CHOICES = [
    ('SLC', 'SLC'),
    ('Bachelor', 'Bachelor'),
    ('Master', 'Master'),
    ('Other', 'Other'),
]

ISSUED_PLACE_CHOICES = [
    ('Kathmandu', 'Kathmandu'),
    ('Bhaktapur', 'Bhaktapur'),
    ('Lalitpur', 'Lalitpur'),
]

PROFESSION_CHOICES = [
    ('Service', 'Service'),
    ('Business', 'Business'),
    ('Other', 'Other'),
]


STRUCTURE_CHOICES = [
    ('Metropolitan City', 'Metropolitan City'),
    ('Sub-Metropolitan City', 'Sub-Metropolitan City'),
    ('Municipality', 'Municipality'),
    ('Rural Municipality', 'Rural Municipality'),
    ('Ward', 'Ward'),
]

LOCAL_UNIT_CHOICES = [
    ('Kathmandu Metropolitan City', 'Kathmandu Metropolitan City'),
    ('Pokhara Metropolitan City', 'Pokhara Metropolitan City'),
    ('Lalitpur Metropolitan City', 'Lalitpur Metropolitan City'),
    ('Biratnagar Metropolitan City', 'Biratnagar Metropolitan City'),
    ('Bharatpur Metropolitan City', 'Bharatpur Metropolitan City'),
    ('Birgunj Metropolitan City', 'Birgunj Metropolitan City'),
]


class KYCModel(models.Model):
    kyc_id = models.AutoField(primary_key=True)
    salutation = models.CharField(max_length=10, choices=SALUTATION_CHOICES, default='Mr')
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    nep_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Male')
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES,default='Nepalese')
    date_of_birth_ad = models.DateField(blank=True, null=True, default=datetime.date.today)
    dob_bs = NepaliDateField(blank=True, null=True)
    qualification = models.CharField(max_length=100, choices=QUALIFICATION_CHOICES, blank=True, null=True)
    profession = models.CharField(max_length=50, choices=PROFESSION_CHOICES, default='Service') 
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    nep_father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    grand_father_name = models.CharField(max_length=100, blank=True, null=True)
    grandfather_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    father_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    father_mother_name = models.CharField(max_length=100, blank=True, null=True)
    son_name = models.CharField(max_length=100, blank=True, null=True)
    daughter_name = models.CharField(max_length=100, blank=True, null=True)
    daughter_in_law_name = models.CharField(max_length=100, blank=True, null=True)
    proposer_full_name = models.CharField(max_length=100, blank=True, null=True)
    is_family_politically_involved = models.BooleanField(default=False)
    is_aml_crime = models.BooleanField(default=False)

    age_proof_doc = models.CharField(max_length=50, choices=AGE_PROOF_DOC_CHOICES, default='Citizenship')
    document_number = models.CharField(max_length=50, blank=True, null=True)
    document_issued_date = models.DateField(blank=True, null=True, default=datetime.date.today)
    issued_place = models.CharField(max_length=100,choices=ISSUED_PLACE_CHOICES, blank=True, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_nepali = models.CharField(max_length=255, blank=True, null=True)

    permanent_address = models.CharField(max_length=255, blank=True, null=True)
    temporary_address = models.CharField(max_length=255, blank=True, null=True)
    temporary_district = models.CharField(max_length=100, blank=True, null=True)
    ward_no = models.CharField(max_length=10, blank=True, null=True)
    house_no = models.CharField(max_length=10, blank=True, null=True, default='0')
    local_unit = models.CharField(max_length=50, choices=LOCAL_UNIT_CHOICES, default='Municipality')
    structure = models.CharField(max_length=50, choices=STRUCTURE_CHOICES, default='Metropolitan City')

    email = models.EmailField(blank=True, null=True, default='test@example.com')
    mobile = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=20, blank=True, null=True)

    income_mode = models.CharField(max_length=50, choices=INCOME_MODE_CHOICES, default='Salary')
    income_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, default=0.00)
    pan_no = models.CharField(max_length=20, blank=True, null=True)
    bank_ac_name = models.CharField(max_length=100, blank=True, null=True)
    bank_ac_no = models.CharField(max_length=50, blank=True, null=True)
    office_address = models.CharField(max_length=255, blank=True, null=True)
    firm_name = models.CharField(max_length=100, blank=True, null=True)

    is_politically_involved = models.BooleanField(default=False)
    is_family_aml_crime = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
