# KYCForm
This repository is for KYC Form that uses django primarily focuses on Python. The web application is primarily based on CRUD operation and uses APIs to make it more important.

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KYC Record Form</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #007bff;
            --secondary-color: #f8f9fa;
            --accent-color: #28a745;
            --header-bg-color: #f0f0f0;
            --text-color: #333;
        }

        body {
            background-color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: var(--text-color);
            margin: 0;
            padding: 0;
        }

        .top-nav {
            background-color: white;
            padding: 10px 20px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .top-nav .nav-tabs .nav-link {
            border: none;
            border-bottom: 3px solid transparent;
            color: #555;
            padding: 10px 20px;
            font-weight: 500;
        }

        .top-nav .nav-tabs .nav-link.active {
            color: var(--primary-color);
            border-color: var(--primary-color);
            background-color: transparent;
        }

        .form-container {
            background: white;
            border-radius: 0;
            box-shadow: none;
            padding: 30px;
            margin-top: 0;
            margin-bottom: 0;
            min-height: calc(100vh - 60px);
            padding-left: 5%;
            padding-right: 5%;
            box-sizing: border-box;
        }

        .section-header {
            color: var(--primary-color);
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 1.2rem;
            font-weight: 600;
        }

        .form-label {
            font-weight: 500;
            margin-bottom: 0;
            color: #555;
            font-size: 0.85rem;
            width: 150px;
        }

        .form-control, .form-select {
            border-radius: 4px;
            padding: 7px 10px;
            border: 1px solid #ced4da;
            transition: all 0.2s ease-in-out;
            font-size: 0.85rem;
            flex-grow: 1;
        }

        .form-control:focus, .form-select:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        }

        .input-group .form-control {
            border-right: none;
        }
        .input-group .btn {
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
            background-color: #007bff;
            color: white;
            border-color: #007bff;
        }
        .input-group .btn:hover {
            background-color: #0056b3;
            border-color: #0056b3;
        }

        .btn-submit {
            background-color: var(--accent-color);
            border: none;
            padding: 10px 25px;
            font-weight: 500;
            transition: all 0.3s;
            border-radius: 5px;
        }

        .btn-submit:hover {
            background-color: #218838;
            transform: translateY(-1px);
        }

        .error-message {
            color: #dc3545;
            font-size: 0.8rem;
            margin-top: 5px;
        }

        .form-group {
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
        }

        .form-check.form-group {
            justify-content: flex-start;
            gap: 5px;
        }

        .form-check-label {
            font-size: 0.85rem;
            margin-left: 0;
        }

        @media (max-width: 768px) {
            .form-container {
                padding: 20px;
            }
            .top-nav {
                flex-direction: column;
                align-items: flex-start;
                padding: 10px 15px;
            }
            .top-nav .nav-tabs {
                margin-bottom: 10px;
            }
            .form-group {
                flex-direction: column;
                align-items: flex-start;
                gap: 5px;
            }
            .form-label {
                width: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container-fluid top-nav">
        <ul class="nav nav-tabs mb-0">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">KYC Update</a>
            </li>
        </ul>
    </div>

    <div class="form-container">
        <h4 class="text-center sm-4 text-primary">KYC Record Form</h4>

        <div class="row mb-3">
    {% comment %} <div class="col-md-12 text-center">
        <small class="text-muted">
            {% if form.instance.created_date %}
                Created on: {{ form.instance.created_date|date:"M d, Y H:i" }}
            {% else %}
                New KYC Application
            {% endif %}
        </small>
    </div> {% endcomment %}
</div>

        <form method="POST" action="{% url 'kyc:kyc_create' %} ">


            {% csrf_token %}
            
            <h5 class="section-header">Personal Details</h5>
            <div class="row">
                <!-- Left Column -->
                <div class="col-md-5 offset-md-1">
                    <!-- First Name -->
                    <div class="form-group">
                        <label for="{{ form.first_name.id_for_label }}" class="form-label">
                            {{ form.first_name.label }} {% if form.first_name.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.first_name }}
                        {% if form.first_name.errors %}
                            <div class="error-message">{{ form.first_name.errors }}</div>
                        {% endif %}
                    </div>

                    <!-- Last Name -->
                    <div class="form-group">
                        <label for="{{ form.last_name.id_for_label }}" class="form-label">
                            {{ form.last_name.label }} {% if form.last_name.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.last_name }}
                        {% if form.last_name.errors %}
                            <div class="error-message">{{ form.last_name.errors }}</div>
                        {% endif %}
                    </div>

                    <!-- Father Name -->
                    <div class="form-group">
                        <label for="{{ form.father_name.id_for_label }}" class="form-label">
                            {{ form.father_name.label }} {% if form.father_name.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.father_name }}
                        {% if form.father_name.errors %}
                            <div class="error-message">{{ form.father_name.errors }}</div>
                        {% endif %}
                    </div>

                    <!-- Mobile -->
                    <div class="form-group">
                        <label for="{{ form.mobile.id_for_label }}" class="form-label">
                            {{ form.mobile.label }} {% if form.mobile.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.mobile }}
                        {% if form.mobile.errors %}
                            <div class="error-message">{{ form.mobile.errors }}</div>
                        {% endif %}
                    </div>

                    <!-- Age Proof Doc -->
                    <div class="form-group">
                        <label for="{{ form.age_proof_doc.id_for_label }}" class="form-label">
                            {{ form.age_proof_doc.label }}
                        </label>
                        {{ form.age_proof_doc }}
                    </div>

                    <!-- Structure -->
                    <div class="form-group">
                        <label for="{{ form.structure.id_for_label }}" class="form-label">
                            {{ form.structure.label }}
                        </label>
                        {{ form.structure }}
                    </div>

                    <!-- Local Unit -->
                    <div class="form-group">
                        <label for="{{ form.local_unit.id_for_label }}" class="form-label">
                            {{ form.local_unit.label }}
                        </label>
                        {{ form.local_unit }}
                    </div>

                    <!-- Address -->
                    <div class="form-group">
                        <label for="{{ form.address.id_for_label }}" class="form-label">
                            {{ form.address.label }}
                        </label>
                        {{ form.address }}
                    </div>

                    <!-- Temporary Address -->
                    <div class="form-group">
                        <label for="{{ form.temporary_address.id_for_label }}" class="form-label">
                            {{ form.temporary_address.label }}
                        </label>
                        {{ form.temporary_address }}
                    </div>

                    <!-- Phone No -->
                    <div class="form-group">
                        <label for="{{ form.phone_no.id_for_label }}" class="form-label">
                            {{ form.phone_no.label }}
                        </label>
                        {{ form.phone_no }}
                    </div>

                    <!-- Profession -->
                    <div class="form-group">
                        <label for="{{ form.profession.id_for_label }}" class="form-label">
                            {{ form.profession.label }} {% if form.profession.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.profession }}
                    </div>

                    <!-- Office Address -->
                    <div class="form-group">
                        <label for="{{ form.office_address.id_for_label }}" class="form-label">
                            {{ form.office_address.label }}
                        </label>
                        {{ form.office_address }}
                    </div>

                    <!-- Income Mode -->
                    <div class="form-group">
                        <label for="{{ form.income_mode.id_for_label }}" class="form-label">
                            {{ form.income_mode.label }} {% if form.income_mode.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.income_mode }}
                    </div>

                    <!-- PAN No -->
                    <div class="form-group">
                        <label for="{{ form.pan_no.id_for_label }}" class="form-label">
                            {{ form.pan_no.label }}
                        </label>
                        {{ form.pan_no }}
                    </div>

                    <!-- Bank Ac Name -->
                    <div class="form-group">
                        <label for="{{ form.bank_ac_name.id_for_label }}" class="form-label">
                            {{ form.bank_ac_name.label }}
                        </label>
                        {{ form.bank_ac_name }}
                    </div>

                    <!-- Nep Name -->
                    <div class="form-group">
                        <label for="{{ form.nep_name.id_for_label }}" class="form-label">
                            {{ form.nep_name.label }}
                        </label>
                        {{ form.nep_name }}
                    </div>

                    <!-- Gender -->
                    <div class="form-group">
                        <label for="{{ form.gender.id_for_label }}" class="form-label">
                            {{ form.gender.label }} {% if form.gender.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.gender }}
                    </div>

                    <!-- Qualification -->
                    <div class="form-group">
                        <label for="{{ form.qualification.id_for_label }}" class="form-label">
                            {{ form.qualification.label }} {% if form.qualification.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.qualification }}
                    </div>

                    <!-- Politically Involved -->
                    <div class="form-group form-check">
                        {{ form.is_politically_involved }}
                        <label for="{{ form.is_politically_involved.id_for_label }}" class="form-check-label">
                            {{ form.is_politically_involved.label }} {% if form.is_politically_involved.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="col-md-5 offset-md-1">
                    <!-- Salutation -->
                    <div class="form-group">
                        <label for="{{ form.salutation.id_for_label }}" class="form-label">
                            {{ form.salutation.label }}
                        </label>
                        {{ form.salutation }}
                    </div>

                    <!-- Middle Name -->
                    <div class="form-group">
                        <label for="{{ form.middle_name.id_for_label }}" class="form-label">
                            {{ form.middle_name.label }}
                        </label>
                        {{ form.middle_name }}
                    </div>

                    <!-- Date of Birth BS/AD -->
                    <div class="form-group d-flex align-items-center justify-content-between gap-3">
                        <div class="d-flex flex-column flex-grow-1">
                            <label for="{{ form.dob_bs.id_for_label }}" class="form-label">
                                {{ form.dob_bs.label }} {% if form.dob_bs.field.required %}<span class="text-danger">*</span>{% endif %}
                            </label>
                            {{ form.dob_bs }}
                        </div>

                        <div class="d-flex flex-column flex-grow-1">
                            <label for="{{ form.date_of_birth_ad.id_for_label }}" class="form-label">
                                {{ form.date_of_birth_ad.label }} {% if form.date_of_birth_ad.field.required %}<span class="text-danger">*</span>{% endif %}
                            </label>
                            {{ form.date_of_birth_ad }}
                        </div>
                    </div>

                    <!-- Nep Father Name -->
                    <div class="form-group">
                        <label for="{{ form.nep_father_name.id_for_label }}" class="form-label">
                            {{ form.nep_father_name.label }}
                        </label>
                        {{ form.nep_father_name }}
                    </div>

                    <!-- Birth Place -->
                    <div class="form-group">
                        <label for="{{ form.birth_place.id_for_label }}" class="form-label">
                            {{ form.birth_place.label }}
                        </label>
                        {{ form.birth_place }}
                    </div>

                    <!-- Document Number -->
                    <div class="form-group">
                        <label for="{{ form.document_number.id_for_label }}" class="form-label">
                            {{ form.document_number.label }} {% if form.document_number.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.document_number }}
                    </div>

                    <!-- Issued Place -->
                    <div class="form-group">
                        <label for="{{ form.issued_place.id_for_label }}" class="form-label">
                            {{ form.issued_place.label }} {% if form.issued_place.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.issued_place }}
                    </div>

                    <!-- Issued Date -->
                    <div class="form-group">
                        <label for="{{ form.document_issued_date.id_for_label }}" class="form-label">
                            {{ form.document_issued_date.label }} {% if form.document_issued_date.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.document_issued_date }}
                    </div>

                    <!-- Father/Mother Name -->
                    <div class="form-group">
                        <label for="{{ form.father_mother_name.id_for_label }}" class="form-label">
                            {{ form.father_mother_name.label }}
                        </label>
                        {{ form.father_mother_name }}
                    </div>

                    <!-- Ward No -->
                    <div class="form-group">
                        <label for="{{ form.ward_no.id_for_label }}" class="form-label">
                            {{ form.ward_no.label }}
                        </label>
                        {{ form.ward_no }}
                    </div>

                    <!-- Temporary District -->
                    <div class="form-group">
                        <label for="{{ form.temporary_district.id_for_label }}" class="form-label">
                            {{ form.temporary_district.label }}
                        </label>
                        {{ form.temporary_district }}
                    </div>

                    <!-- House No -->
                    <div class="form-group">
                        <label for="{{ form.house_no.id_for_label }}" class="form-label">
                            {{ form.house_no.label }}
                        </label>
                        {{ form.house_no }}
                    </div>

                    <!-- Email -->
                    <div class="form-group">
                        <label for="{{ form.email.id_for_label }}" class="form-label">
                            {{ form.email.label }}
                        </label>
                        {{ form.email }}
                    </div>

                    <!-- Firm Name -->
                    <div class="form-group">
                        <label for="{{ form.firm_name.id_for_label }}" class="form-label">
                            {{ form.firm_name.label }}
                        </label>
                        {{ form.firm_name }}
                    </div>

                    <!-- Income Amount -->
                    <div class="form-group">
                        <label for="{{ form.income_amount.id_for_label }}" class="form-label">
                            {{ form.income_amount.label }} {% if form.income_amount.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.income_amount }}
                    </div>

                    <!-- Bank Ac No -->
                    <div class="form-group">
                        <label for="{{ form.bank_ac_no.id_for_label }}" class="form-label">
                            {{ form.bank_ac_no.label }}
                        </label>
                        {{ form.bank_ac_no }}
                    </div>

                    <!-- Address Nepali -->
                    <div class="form-group">
                        <label for="{{ form.address_nepali.id_for_label }}" class="form-label">
                            {{ form.address_nepali.label }}
                        </label>
                        {{ form.address_nepali }}
                    </div>

                    <!-- Proposer Full Name -->
                    <div class="form-group">
                        <label for="{{ form.proposer_full_name.id_for_label }}" class="form-label">
                            {{ form.proposer_full_name.label }}
                        </label>
                        {{ form.proposer_full_name }}
                    </div>

                    <!-- Nationality -->
                    <div class="form-group">
                        <label for="{{ form.nationality.id_for_label }}" class="form-label">
                            {{ form.nationality.label }} {% if form.nationality.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                        {{ form.nationality }}
                    </div>

                    <!-- AML Crime -->
                    <div class="form-group form-check">
                        {{ form.is_aml_crime }}
                        <label for="{{ form.is_aml_crime.id_for_label }}" class="form-check-label">
                            {{ form.is_aml_crime.label }}
                        </label>
                    </div>
                </div>
            </div>

            <h5 class="section-header mt-4">Family Details</h5>
            <div class="row">
                <!-- Left Column -->
                <div class="col-md-5 offset-md-1">
                    <!-- Spouse Name -->
                    <div class="form-group">
                        <label for="{{ form.spouse_name.id_for_label }}" class="form-label">
                            {{ form.spouse_name.label }}
                        </label>
                        {{ form.spouse_name }}
                    </div>

                    <!-- Mother Name -->
                    <div class="form-group">
                        <label for="{{ form.mother_name.id_for_label }}" class="form-label">
                            {{ form.mother_name.label }}
                        </label>
                        {{ form.mother_name }}
                    </div>

                    <!-- Son Name -->
                    <div class="form-group">
                        <label for="{{ form.son_name.id_for_label }}" class="form-label">
                            {{ form.son_name.label }}
                        </label>
                        {{ form.son_name }}
                    </div>

                    <!-- Daughter/InLaw Name -->
                    <div class="form-group">
                        <label for="{{ form.daughter_in_law_name.id_for_label }}" class="form-label">
                            {{ form.daughter_in_law_name.label }}
                        </label>
                        {{ form.daughter_in_law_name }}
                    </div>

                    <!-- GrandFather/InLaw Name -->
                    <div class="form-group">
                        <label for="{{ form.grandfather_in_law_name.id_for_label }}" class="form-label">
                            {{ form.grandfather_in_law_name.label }}
                        </label>
                        {{ form.grandfather_in_law_name }}
                    </div>

                    <!-- Family Politically Involved -->
                    <div class="form-group form-check">
                        {{ form.is_family_politically_involved }}
                        <label for="{{ form.is_family_politically_involved.id_for_label }}" class="form-check-label">
                            {{ form.is_family_politically_involved.label }} {% if form.is_family_politically_involved.field.required %}<span class="text-danger">*</span>{% endif %}
                        </label>
                    </div>
                </div>

                <!-- Right Column -->
                <div class="col-md-5 offset-md-1">
                    <!-- Grand Father Name -->
                    <div class="form-group">
                        <label for="{{ form.grand_father_name.id_for_label }}" class="form-label">
                            {{ form.grand_father_name.label }}
                        </label>
                        {{ form.grand_father_name }}
                    </div>

                    <!-- Daughter Name -->
                    <div class="form-group">
                        <label for="{{ form.daughter_name.id_for_label }}" class="form-label">
                            {{ form.daughter_name.label }}
                        </label>
                        {{ form.daughter_name }}
                    </div>

                    <!-- Father/InLaw Name -->
                    <div class="form-group">
                        <label for="{{ form.father_in_law_name.id_for_label }}" class="form-label">
                            {{ form.father_in_law_name.label }}
                        </label>
                        {{ form.father_in_law_name }}
                    </div>

                    <!-- Family AML Crime -->
                    <div class="form-group form-check">
                        {{ form.is_family_aml_crime }}
                        <label for="{{ form.is_family_aml_crime.id_for_label }}" class="form-check-label">
                            {{ form.is_family_aml_crime.label }}
                        </label>
                    </div>
                </div>
            </div>

            <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                <button type="submit" class="btn btn-submit btn-lg">
                    Submit
                </button>
            </div>
        </form>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.6/jquery.inputmask.min.js"></script>
    <script>
        $(document).ready(function(){
            // Apply input mask for mobile number
            $('#{{ form.mobile.id_for_label }}').inputmask('999-9999999');
        });
    </script>
</body>
</html>

Before update

{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KYC and Policy Management</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #007bff;
            --secondary-color: #f8f9fa;
            --accent-color: #28a745;
            --header-bg-color: #f0f0f0;
            --text-color: #333;
        }

        body {
            background-color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: var(--text-color);
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden;
        }

        .main-container {
            display: flex;
            height: calc(100vh - 60px);
        }

        .form-section {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            height: 100%;
        }

        .top-nav {
            background-color: white;
            padding: 10px 20px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .top-nav .nav-tabs .nav-link {
            border: none;
            border-bottom: 3px solid transparent;
            color: #555;
            padding: 10px 20px;
            font-weight: 500;
        }

        .top-nav .nav-tabs .nav-link.active {
            color: var(--primary-color);
            border-color: var(--primary-color);
            background-color: transparent;
        }

        .form-container {
            background: white;
            border-radius: 0;
            box-shadow: none;
            padding: 30px;
            margin-top: 0;
            margin-bottom: 0;
            min-height: calc(100vh - 60px);
            padding-left: 5%;
            padding-right: 5%;
            box-sizing: border-box;
        }

        .section-header {
            color: var(--primary-color);
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 10px;
            margin-bottom: 25px;
            font-size: 1.2rem;
            font-weight: 600;
        }

        .form-label {
            font-weight: 500;
            margin-bottom: 0;
            color: #555;
            font-size: 0.85rem;
            width: 150px;
        }

        .form-control, .form-select {
            border-radius: 4px;
            padding: 7px 10px;
            border: 1px solid #ced4da;
            transition: all 0.2s ease-in-out;
            font-size: 0.85rem;
            flex-grow: 1;
        }

        .form-control:focus, .form-select:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
        }

        .input-group .form-control {
            border-right: none;
        }
        .input-group .btn {
            border-top-left-radius: 0;
            border-bottom-left-radius: 0;
            background-color: #007bff;
            color: white;
            border-color: #007bff;
        }
        .input-group .btn:hover {
            background-color: #0056b3;
            border-color: #0056b3;
        }

        .btn-submit {
            background-color: var(--accent-color);
            border: none;
            padding: 10px 25px;
            font-weight: 500;
            transition: all 0.3s;
            border-radius: 5px;
        }

        .btn-submit:hover {
            background-color: #218838;
            transform: translateY(-1px);
        }

        .error-message {
            color: #dc3545;
            font-size: 0.8rem;
            margin-top: 5px;
        }

        .form-group {
            margin-bottom: 0.75rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
        }

        .form-check.form-group {
            justify-content: flex-start;
            gap: 5px;
        }

        .form-check-label {
            font-size: 0.85rem;
            margin-left: 0;
        }

        /* Custom scrollbar */
        .form-section::-webkit-scrollbar {
            width: 8px;
        }
        
        .form-section::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        
        .form-section::-webkit-scrollbar-thumb {
            background: #888;
            border-radius: 4px;
        }
        
        .form-section::-webkit-scrollbar-thumb:hover {
            background: #555;
        }

        @media (max-width: 768px) {
            .main-container {
                flex-direction: column;
            }
            
            .form-container {
                padding: 20px;
            }
            .top-nav {
                flex-direction: column;
                align-items: flex-start;
                padding: 10px 15px;
            }
            .top-nav .nav-tabs {
                margin-bottom: 10px;
            }
            .form-group {
                flex-direction: column;
                align-items: flex-start;
                gap: 5px;
            }
            .form-label {
                width: auto;
            }
        }
    </style>
</head>
<body>
    <div class="container-fluid top-nav">
        <ul class="nav nav-tabs mb-0">
            <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">KYC and Policy Management</a>
            </li>
        </ul>
    </div>

    <div class="main-container">
        <!-- KYC Update Form Section -->
        <div class="form-section" style="border-right: 1px solid #eee;">
            <div class="form-container">
                <h4 class="text-center sm-4 text-primary">KYC Record Form</h4>

                <form method="POST" action="{% url 'kyc:kyc_create' %}">
                    {% csrf_token %}
                    
                    <h5 class="section-header">Personal Details</h5>
                    <div class="row">
                        <!-- Left Column -->
                        <div class="col-md-5 offset-md-1">
                            <!-- First Name -->
                            <div class="form-group">
                                <label for="{{ form.first_name.id_for_label }}" class="form-label">
                                    {{ form.first_name.label }} {% if form.first_name.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.first_name }}
                                {% if form.first_name.errors %}
                                    <div class="error-message">{{ form.first_name.errors }}</div>
                                {% endif %}
                            </div>

                            <!-- Last Name -->
                            <div class="form-group">
                                <label for="{{ form.last_name.id_for_label }}" class="form-label">
                                    {{ form.last_name.label }} {% if form.last_name.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.last_name }}
                                {% if form.last_name.errors %}
                                    <div class="error-message">{{ form.last_name.errors }}</div>
                                {% endif %}
                            </div>

                            <!-- Father Name -->
                            <div class="form-group">
                                <label for="{{ form.father_name.id_for_label }}" class="form-label">
                                    {{ form.father_name.label }} {% if form.father_name.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.father_name }}
                                {% if form.father_name.errors %}
                                    <div class="error-message">{{ form.father_name.errors }}</div>
                                {% endif %}
                            </div>

                            <!-- Mobile -->
                            <div class="form-group">
                                <label for="{{ form.mobile.id_for_label }}" class="form-label">
                                    {{ form.mobile.label }} {% if form.mobile.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.mobile }}
                                {% if form.mobile.errors %}
                                    <div class="error-message">{{ form.mobile.errors }}</div>
                                {% endif %}
                            </div>

                            <!-- Age Proof Doc -->
                            <div class="form-group">
                                <label for="{{ form.age_proof_doc.id_for_label }}" class="form-label">
                                    {{ form.age_proof_doc.label }}
                                </label>
                                {{ form.age_proof_doc }}
                            </div>

                            <!-- Structure -->
                            <div class="form-group">
                                <label for="{{ form.structure.id_for_label }}" class="form-label">
                                    {{ form.structure.label }}
                                </label>
                                {{ form.structure }}
                            </div>

                            <!-- Local Unit -->
                            <div class="form-group">
                                <label for="{{ form.local_unit.id_for_label }}" class="form-label">
                                    {{ form.local_unit.label }}
                                </label>
                                {{ form.local_unit }}
                            </div>

                            <!-- Address -->
                            <div class="form-group">
                                <label for="{{ form.address.id_for_label }}" class="form-label">
                                    {{ form.address.label }}
                                </label>
                                {{ form.address }}
                            </div>

                            <!-- Temporary Address -->
                            <div class="form-group">
                                <label for="{{ form.temporary_address.id_for_label }}" class="form-label">
                                    {{ form.temporary_address.label }}
                                </label>
                                {{ form.temporary_address }}
                            </div>

                            <!-- Phone No -->
                            <div class="form-group">
                                <label for="{{ form.phone_no.id_for_label }}" class="form-label">
                                    {{ form.phone_no.label }}
                                </label>
                                {{ form.phone_no }}
                            </div>

                            <!-- Profession -->
                            <div class="form-group">
                                <label for="{{ form.profession.id_for_label }}" class="form-label">
                                    {{ form.profession.label }} {% if form.profession.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.profession }}
                            </div>

                            <!-- Office Address -->
                            <div class="form-group">
                                <label for="{{ form.office_address.id_for_label }}" class="form-label">
                                    {{ form.office_address.label }}
                                </label>
                                {{ form.office_address }}
                            </div>

                            <!-- Income Mode -->
                            <div class="form-group">
                                <label for="{{ form.income_mode.id_for_label }}" class="form-label">
                                    {{ form.income_mode.label }} {% if form.income_mode.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.income_mode }}
                            </div>

                            <!-- PAN No -->
                            <div class="form-group">
                                <label for="{{ form.pan_no.id_for_label }}" class="form-label">
                                    {{ form.pan_no.label }}
                                </label>
                                {{ form.pan_no }}
                            </div>

                            <!-- Bank Ac Name -->
                            <div class="form-group">
                                <label for="{{ form.bank_ac_name.id_for_label }}" class="form-label">
                                    {{ form.bank_ac_name.label }}
                                </label>
                                {{ form.bank_ac_name }}
                            </div>

                            <!-- Nep Name -->
                            <div class="form-group">
                                <label for="{{ form.nep_name.id_for_label }}" class="form-label">
                                    {{ form.nep_name.label }}
                                </label>
                                {{ form.nep_name }}
                            </div>

                            <!-- Gender -->
                            <div class="form-group">
                                <label for="{{ form.gender.id_for_label }}" class="form-label">
                                    {{ form.gender.label }} {% if form.gender.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.gender }}
                            </div>

                            <!-- Qualification -->
                            <div class="form-group">
                                <label for="{{ form.qualification.id_for_label }}" class="form-label">
                                    {{ form.qualification.label }} {% if form.qualification.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.qualification }}
                            </div>

                            <!-- Politically Involved -->
                            <div class="form-group form-check">
                                {{ form.is_politically_involved }}
                                <label for="{{ form.is_politically_involved.id_for_label }}" class="form-check-label">
                                    {{ form.is_politically_involved.label }} {% if form.is_politically_involved.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                            </div>
                        </div>

                        <!-- Right Column -->
                        <div class="col-md-5 offset-md-1">
                            <!-- Salutation -->
                            <div class="form-group">
                                <label for="{{ form.salutation.id_for_label }}" class="form-label">
                                    {{ form.salutation.label }}
                                </label>
                                {{ form.salutation }}
                            </div>

                            <!-- Middle Name -->
                            <div class="form-group">
                                <label for="{{ form.middle_name.id_for_label }}" class="form-label">
                                    {{ form.middle_name.label }}
                                </label>
                                {{ form.middle_name }}
                            </div>

                            <!-- Date of Birth BS/AD -->
                            <div class="form-group d-flex align-items-center justify-content-between gap-3">
                                <div class="d-flex flex-column flex-grow-1">
                                    <label for="{{ form.dob_bs.id_for_label }}" class="form-label">
                                        {{ form.dob_bs.label }} {% if form.dob_bs.field.required %}<span class="text-danger">*</span>{% endif %}
                                    </label>
                                    {{ form.dob_bs }}
                                </div>

                                <div class="d-flex flex-column flex-grow-1">
                                    <label for="{{ form.date_of_birth_ad.id_for_label }}" class="form-label">
                                        {{ form.date_of_birth_ad.label }} {% if form.date_of_birth_ad.field.required %}<span class="text-danger">*</span>{% endif %}
                                    </label>
                                    {{ form.date_of_birth_ad }}
                                </div>
                            </div>

                            <!-- Nep Father Name -->
                            <div class="form-group">
                                <label for="{{ form.nep_father_name.id_for_label }}" class="form-label">
                                    {{ form.nep_father_name.label }}
                                </label>
                                {{ form.nep_father_name }}
                            </div>

                            <!-- Birth Place -->
                            <div class="form-group">
                                <label for="{{ form.birth_place.id_for_label }}" class="form-label">
                                    {{ form.birth_place.label }}
                                </label>
                                {{ form.birth_place }}
                            </div>

                            <!-- Document Number -->
                            <div class="form-group">
                                <label for="{{ form.document_number.id_for_label }}" class="form-label">
                                    {{ form.document_number.label }} {% if form.document_number.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.document_number }}
                            </div>

                            <!-- Issued Place -->
                            <div class="form-group">
                                <label for="{{ form.issued_place.id_for_label }}" class="form-label">
                                    {{ form.issued_place.label }} {% if form.issued_place.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.issued_place }}
                            </div>

                            <!-- Issued Date -->
                            <div class="form-group">
                                <label for="{{ form.document_issued_date.id_for_label }}" class="form-label">
                                    {{ form.document_issued_date.label }} {% if form.document_issued_date.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.document_issued_date }}
                            </div>

                            <!-- Father/Mother Name -->
                            <div class="form-group">
                                <label for="{{ form.father_mother_name.id_for_label }}" class="form-label">
                                    {{ form.father_mother_name.label }}
                                </label>
                                {{ form.father_mother_name }}
                            </div>

                            <!-- Ward No -->
                            <div class="form-group">
                                <label for="{{ form.ward_no.id_for_label }}" class="form-label">
                                    {{ form.ward_no.label }}
                                </label>
                                {{ form.ward_no }}
                            </div>

                            <!-- Temporary District -->
                            <div class="form-group">
                                <label for="{{ form.temporary_district.id_for_label }}" class="form-label">
                                    {{ form.temporary_district.label }}
                                </label>
                                {{ form.temporary_district }}
                            </div>

                            <!-- House No -->
                            <div class="form-group">
                                <label for="{{ form.house_no.id_for_label }}" class="form-label">
                                    {{ form.house_no.label }}
                                </label>
                                {{ form.house_no }}
                            </div>

                            <!-- Email -->
                            <div class="form-group">
                                <label for="{{ form.email.id_for_label }}" class="form-label">
                                    {{ form.email.label }}
                                </label>
                                {{ form.email }}
                            </div>

                            <!-- Firm Name -->
                            <div class="form-group">
                                <label for="{{ form.firm_name.id_for_label }}" class="form-label">
                                    {{ form.firm_name.label }}
                                </label>
                                {{ form.firm_name }}
                            </div>

                            <!-- Income Amount -->
                            <div class="form-group">
                                <label for="{{ form.income_amount.id_for_label }}" class="form-label">
                                    {{ form.income_amount.label }} {% if form.income_amount.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.income_amount }}
                            </div>

                            <!-- Bank Ac No -->
                            <div class="form-group">
                                <label for="{{ form.bank_ac_no.id_for_label }}" class="form-label">
                                    {{ form.bank_ac_no.label }}
                                </label>
                                {{ form.bank_ac_no }}
                            </div>

                            <!-- Address Nepali -->
                            <div class="form-group">
                                <label for="{{ form.address_nepali.id_for_label }}" class="form-label">
                                    {{ form.address_nepali.label }}
                                </label>
                                {{ form.address_nepali }}
                            </div>

                            <!-- Proposer Full Name -->
                            <div class="form-group">
                                <label for="{{ form.proposer_full_name.id_for_label }}" class="form-label">
                                    {{ form.proposer_full_name.label }}
                                </label>
                                {{ form.proposer_full_name }}
                            </div>

                            <!-- Nationality -->
                            <div class="form-group">
                                <label for="{{ form.nationality.id_for_label }}" class="form-label">
                                    {{ form.nationality.label }} {% if form.nationality.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                                {{ form.nationality }}
                            </div>

                            <!-- AML Crime -->
                            <div class="form-group form-check">
                                {{ form.is_aml_crime }}
                                <label for="{{ form.is_aml_crime.id_for_label }}" class="form-check-label">
                                    {{ form.is_aml_crime.label }}
                                </label>
                            </div>
                        </div>
                    </div>

                    <h5 class="section-header mt-4">Family Details</h5>
                    <div class="row">
                        <!-- Left Column -->
                        <div class="col-md-5 offset-md-1">
                            <!-- Spouse Name -->
                            <div class="form-group">
                                <label for="{{ form.spouse_name.id_for_label }}" class="form-label">
                                    {{ form.spouse_name.label }}
                                </label>
                                {{ form.spouse_name }}
                            </div>

                            <!-- Mother Name -->
                            <div class="form-group">
                                <label for="{{ form.mother_name.id_for_label }}" class="form-label">
                                    {{ form.mother_name.label }}
                                </label>
                                {{ form.mother_name }}
                            </div>

                            <!-- Son Name -->
                            <div class="form-group">
                                <label for="{{ form.son_name.id_for_label }}" class="form-label">
                                    {{ form.son_name.label }}
                                </label>
                                {{ form.son_name }}
                            </div>

                            <!-- Daughter/InLaw Name -->
                            <div class="form-group">
                                <label for="{{ form.daughter_in_law_name.id_for_label }}" class="form-label">
                                    {{ form.daughter_in_law_name.label }}
                                </label>
                                {{ form.daughter_in_law_name }}
                            </div>

                            <!-- GrandFather/InLaw Name -->
                            <div class="form-group">
                                <label for="{{ form.grandfather_in_law_name.id_for_label }}" class="form-label">
                                    {{ form.grandfather_in_law_name.label }}
                                </label>
                                {{ form.grandfather_in_law_name }}
                            </div>

                            <!-- Family Politically Involved -->
                            <div class="form-group form-check">
                                {{ form.is_family_politically_involved }}
                                <label for="{{ form.is_family_politically_involved.id_for_label }}" class="form-check-label">
                                    {{ form.is_family_politically_involved.label }} {% if form.is_family_politically_involved.field.required %}<span class="text-danger">*</span>{% endif %}
                                </label>
                            </div>
                        </div>

                        <!-- Right Column -->
                        <div class="col-md-5 offset-md-1">
                            <!-- Grand Father Name -->
                            <div class="form-group">
                                <label for="{{ form.grand_father_name.id_for_label }}" class="form-label">
                                    {{ form.grand_father_name.label }}
                                </label>
                                {{ form.grand_father_name }}
                            </div>

                            <!-- Daughter Name -->
                            <div class="form-group">
                                <label for="{{ form.daughter_name.id_for_label }}" class="form-label">
                                    {{ form.daughter_name.label }}
                                </label>
                                {{ form.daughter_name }}
                            </div>

                            <!-- Father/InLaw Name -->
                            <div class="form-group">
                                <label for="{{ form.father_in_law_name.id_for_label }}" class="form-label">
                                    {{ form.father_in_law_name.label }}
                                </label>
                                {{ form.father_in_law_name }}
                            </div>

                            <!-- Family AML Crime -->
                            <div class="form-group form-check">
                                {{ form.is_family_aml_crime }}
                                <label for="{{ form.is_family_aml_crime.id_for_label }}" class="form-check-label">
                                    {{ form.is_family_aml_crime.label }}
                                </label>
                            </div>
                        </div>
                    </div>

                    <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                        <button type="submit" class="btn btn-submit btn-lg">
                            Submit
                        </button>
                    </div>
                </form>
            </div>
        </div>

        <!-- Policy Number Form Section -->
        <div class="form-section">
            <div class="form-container">
                <h4 class="text-center sm-4 text-primary">Policy Number Form</h4>

                <form method="POST" action="{% url 'policy:policy_create' %}">
                    {% csrf_token %}
                    
                    <h5 class="section-header">Policy Details</h5>
                    <div class="row">
                        <!-- Left Column -->
                        <div class="col-md-6">
                            <!-- Policy Number -->
                            <div class="form-group mb-3">
                                <label for="policy_number" class="form-label">
                                    Policy Number <span class="text-danger">*</span>
                                </label>
                                <input type="text" class="form-control" id="policy_number" name="policy_number" required>
                            </div>

                            <!-- Policy Type -->
                            <div class="form-group mb-3">
                                <label for="policy_type" class="form-label">
                                    Policy Type <span class="text-danger">*</span>
                                </label>
                                <select class="form-select" id="policy_type" name="policy_type" required>
                                    <option value="">Select Policy Type</option>
                                    <option value="life">Life Insurance</option>
                                    <option value="health">Health Insurance</option>
                                    <option value="auto">Auto Insurance</option>
                                    <option value="property">Property Insurance</option>
                                </select>
                            </div>

                            <!-- Start Date -->
                            <div class="form-group mb-3">
                                <label for="start_date" class="form-label">
                                    Start Date <span class="text-danger">*</span>
                                </label>
                                <input type="date" class="form-control" id="start_date" name="start_date" required>
                            </div>

                            <!-- Premium Amount -->
                            <div class="form-group mb-3">
                                <label for="premium_amount" class="form-label">
                                    Premium Amount <span class="text-danger">*</span>
                                </label>
                                <input type="number" class="form-control" id="premium_amount" name="premium_amount" step="0.01" required>
                            </div>

                            <!-- Sum Assured -->
                            <div class="form-group mb-3">
                                <label for="sum_assured" class="form-label">
                                    Sum Assured
                                </label>
                                <input type="number" class="form-control" id="sum_assured" name="sum_assured" step="0.01">
                            </div>
                        </div>

                        <!-- Right Column -->
                        <div class="col-md-6">
                            <!-- Customer ID -->
                            <div class="form-group mb-3">
                                <label for="customer_id" class="form-label">
                                    Customer ID <span class="text-danger">*</span>
                                </label>
                                <input type="text" class="form-control" id="customer_id" name="customer_id" value="{{ kyc.kyc_id }}" readonly>
                            </div>

                            <!-- Policy Status -->
                            <div class="form-group mb-3">
                                <label for="policy_status" class="form-label">
                                    Policy Status <span class="text-danger">*</span>
                                </label>
                                <select class="form-select" id="policy_status" name="policy_status" required>
                                    <option value="active">Active</option>
                                    <option value="pending">Pending</option>
                                    <option value="expired">Expired</option>
                                    <option value="cancelled">Cancelled</option>
                                </select>
                            </div>

                            <!-- End Date -->
                            <div class="form-group mb-3">
                                <label for="end_date" class="form-label">
                                    End Date
                                </label>
                                <input type="date" class="form-control" id="end_date" name="end_date">
                            </div>

                            <!-- Payment Frequency -->
                            <div class="form-group mb-3">
                                <label for="payment_frequency" class="form-label">
                                    Payment Frequency
                                </label>
                                <select class="form-select" id="payment_frequency" name="payment_frequency">
                                    <option value="monthly">Monthly</option>
                                    <option value="quarterly">Quarterly</option>
                                    <option value="yearly">Yearly</option>
                                    <option value="single">Single Payment</option>
                                </select>
                            </div>

                            <!-- Beneficiary -->
                            <div class="form-group mb-3">
                                <label for="beneficiary" class="form-label">
                                    Beneficiary
                                </label>
                                <input type="text" class="form-control" id="beneficiary" name="beneficiary">
                            </div>
                        </div>
                    </div>

                    <h5 class="section-header mt-4">Additional Information</h5>
                    <div class="row">
                        <div class="col-md-12">
                            <!-- Agent/Broker -->
                            <div class="form-group mb-3">
                                <label for="agent_broker" class="form-label">
                                    Agent/Broker
                                </label>
                                <input type="text" class="form-control" id="agent_broker" name="agent_broker">
                            </div>

                            <!-- Underwriting Notes -->
                            <div class="form-group mb-3">
                                <label for="underwriting_notes" class="form-label">
                                    Underwriting Notes
                                </label>
                                <textarea class="form-control" id="underwriting_notes" name="underwriting_notes" rows="2"></textarea>
                            </div>

                            <!-- Special Conditions -->
                            <div class="form-group mb-3">
                                <label for="special_conditions" class="form-label">
                                    Special Conditions
                                </label>
                                <textarea class="form-control" id="special_conditions" name="special_conditions" rows="2"></textarea>
                            </div>
                        </div>
                    </div>

                    <div class="d-grid gap-2 d-md-flex justify-content-md-end mt-4">
                        <button type="submit" class="btn btn-primary">
                            <i class="fas fa-save me-1"></i> Save Policy
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.inputmask/5.0.6/jquery.inputmask.min.js"></script>
    <script>
        $(document).ready(function(){
            // Apply input mask for mobile number
            $('#{{ form.mobile.id_for_label }}').inputmask('999-9999999');
            
            // Set today's date as default for start date
            document.getElementById('start_date').valueAsDate = new Date();
        });
    </script>
</body>
</html>
