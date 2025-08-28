from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import KYCModel
import random
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import KYCForm, LoginForm

from datetime import datetime, timedelta
from django.urls import reverse 
from django.db.models import Q
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.conf import settings


# Home page view
def home(request):
    return HttpResponse("KYC Home Page")


def kyc_login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            policy_no = form.cleaned_data["policy_no"]
            dob = form.cleaned_data["dob"]
            
            try:
                # Try to find the KYC record
                kyc = KYCModel.objects.get(policy_no=policy_no, date_of_birth_ad=dob)
                
                # Store kyc_id in session and redirect
                request.session["kyc_id"] = kyc.kyc_id
                request.session["policy_no"] = policy_no
                request.session["dob_ad"] = dob.isoformat()
                request.session.modified = True
                return redirect("kyc:kyc_create")
                
            except KYCModel.DoesNotExist:
                # Handle case where no matching record is found
                messages.error(request, "The policy number and date of birth combination was not found. Please check your details and try again.")
                
            except Exception as e:
                # Handle any other unexpected errors
                messages.error(request, "An error occurred during login. Please try again.")
                # You might want to log the actual error for debugging:
                # import logging
                # logger = logging.getLogger(__name__)
                # logger.error(f"Login error: {str(e)}")
    
    else:
        form = LoginForm()

    return render(request, "kyc_login.html", {"form": form})
#Create a view (validate-policy) in server side instead of getting already existing database data



@csrf_exempt
@require_POST
def validate_policy(request):
    """
    Validate policy number and date of birth against external API
    """
    try:
        # Parse the JSON data from the request body
        data = json.loads(request.body)
        policy_no = data.get('policy_no', '').strip()
        date_of_birth = data.get('date_of_birth', '').strip()
        
        # Validate that we have both required fields
        if not policy_no:
            return JsonResponse({
                'valid': False,
                'message': 'Policy number is required'
            }, status=400)
            
        if not date_of_birth:
            return JsonResponse({
                'valid': False,
                'message': 'Date of birth is required'
            }, status=400)
        
        # Call the external API to validate the policy
        # Replace with your actual API endpoint and parameters
        API_URL = "http://127.0.0.1:8001/policies"
        
        try:
            # Make request to external API
            response = requests.post(
                API_URL,
                json={
                    'policy_number': policy_no,
                    'date_of_birth': date_of_birth
                },
                timeout=10  # Set a timeout to prevent hanging
            )
            
            # Check if the API request was successful
            if response.status_code == 200:
                api_data = response.json()
                
                # Adjust this based on your API's response structure
                if api_data.get('is_valid', False):
                    return JsonResponse({
                        'valid': True,
                        'message': 'Credentials verified successfully',
                        'policy_data': api_data.get('policy_data', {})
                    })
                else:
                    return JsonResponse({
                        'valid': False,
                        'message': api_data.get('message', 'Invalid policy number or date of birth')
                    }, status=404)
            
            # Handle API errors
            elif response.status_code == 404:
                return JsonResponse({
                    'valid': False,
                    'message': 'Policy not found in the system'
                }, status=404)
                
            else:
                return JsonResponse({
                    'valid': False,
                    'message': f'Validation service error: {response.status_code}'
                }, status=response.status_code)
                
        except requests.exceptions.Timeout:
            return JsonResponse({
                'valid': False,
                'message': 'Validation service timeout. Please try again.'
            }, status=504)
            
        except requests.exceptions.ConnectionError:
            return JsonResponse({
                'valid': False,
                'message': 'Cannot connect to validation service. Please try again later.'
            }, status=503)
            
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'valid': False,
                'message': f'Error connecting to validation service: {str(e)}'
            }, status=500)
    
    except json.JSONDecodeError:
        return JsonResponse({
            'valid': False,
            'message': 'Invalid JSON data'
        }, status=400)
    
    except Exception as e:
        return JsonResponse({
            'valid': False,
            'message': 'An internal error occurred during validation'
        }, status=500)
    
# Create/Submit KYC form

def kyc_create_view(request):
    if request.method == 'POST':
        form = KYCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kyc:kyc_success')
        else:print(form.errors) 
         # Use namespaced redirect
    else:
        form = KYCForm()
    return render(request, 'kyc_form.html', {'form': form})

# Success page after form submission
def kyc_success_view(request):
   
    return render(request, 'kyc_success.html')

# List all KYC entries
def kyc_list_view(request):
    # Get all parameters with defaults
    order_by = request.GET.get('order_by', 'kyc_id')
    order_dir = request.GET.get('order_dir', 'asc')
    search_term = request.GET.get('search', '').strip()
    status_filter = request.GET.get('status', '').lower()
    page_number = request.GET.get('page', 1)
    
    # Validate and sanitize parameters
    valid_fields = {
        'kyc_id': 'kyc_id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'date_of_birth_ad': 'date_of_birth_ad',
        'gender': 'gender'
    }
    
    # Validate sorting parameters
    order_by = valid_fields.get(order_by, 'kyc_id')
    order_dir = 'desc' if order_dir == 'desc' else 'asc'
    
    # Base queryset
    kycs = KYCModel.objects.all()
    
    # Apply search filter if term exists
    if search_term:
        kycs = kycs.filter(
            Q(kyc_id__icontains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(mobile__icontains=search_term) |
            Q(document_number__icontains=search_term)
        )
    
    # Apply status filter if specified
    if status_filter in ['pending', 'approved', 'rejected']:
        kycs = kycs.filter(status=status_filter)
    
    # Apply sorting with direction
    order_prefix = '-' if order_dir == 'desc' else ''
    kycs = kycs.order_by(f'{order_prefix}{order_by}')
    
    # Pagination with 25 items per page
    paginator = Paginator(kycs, 20)
    
    try:
        page_obj = paginator.page(page_number)
    except:
        page_obj = paginator.page(1)
    
    # Build query string for pagination links
    query_params = []
    if search_term:
        query_params.append(f'search={search_term}')
    if status_filter:
        query_params.append(f'status={status_filter}')
    if order_by != 'kyc_id':
        query_params.append(f'order_by={order_by}')
    if order_dir != 'asc':
        query_params.append(f'order_dir={order_dir}')
    
    query_string = '&'.join(query_params)
    if query_string:
        query_string = f'&{query_string}'
    
    context = {
        'kycs': page_obj,
        'order_by': order_by,
        'order_dir': order_dir,
        'search_term': search_term,
        'status_filter': status_filter,
        'is_paginated': page_obj.has_other_pages(),
        'total_records': paginator.count,
        'query_string': query_string,
        'request': request
    }
    
    return render(request, 'kyc_list.html', context)


# kyc_lists table
FIELD_MAPPING = {
    'ClientNo': 'kyc_id',           # Maps 'ClientNo' to 'kyc_id' field
    'NewClientNo': 'new_client_no', # Add your actual field names
    'FullName': 'full_name',        # Map to existing fields in KYCModel
    'MobileNo': 'mobile',
    'IsPolicyIssued': 'is_policy_issued',
    'CreatedBy': 'created_by',
    'CreatedDate': 'created_date',
}
def kyc_lists_view(request):
    # First, determine if we're using dummy data or real data
    use_dummy = request.GET.get('dummy', 'false').lower() == 'true'
    
    if use_dummy:
        # Generate dummy data function
        def generate_dummy_kyc():
            first_names = ['John', 'Jane', 'Robert', 'Emily', 'Michael', 'Sarah', 'David', 'Lisa']
            last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis']
            mobile_prefixes = ['984', '985', '986', '974', '975']
            
            for i in range(1, 101):  # Generate 100 dummy records
                yield {
                    'kyc_id': i,
                    'ClientNo': f"CL{1000 + i}",
                    'NewClientNo': f"NCL{2000 + i}",
                    'FullName': f"{random.choice(first_names)} {random.choice(last_names)}",
                    'MobileNo': f"{random.choice(mobile_prefixes)}{random.randint(1000000, 9999999)}",
                    'IsPolicyIssued': random.choice([True, False]),
                    'CreatedBy': random.choice(['admin', 'manager', 'agent1', 'agent2']),
                    'CreatedDate': (datetime.now() - timedelta(days=random.randint(0, 365))).date()
                }

        # Paginate the dummy data
        dummy_data = list(generate_dummy_kyc())
        paginator = Paginator(dummy_data, 10)  # 10 items per page
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        context = {
            'kyc_list': page_obj,
            'is_paginated': paginator.num_pages > 1,
            'page_obj': page_obj,
            'is_dummy_data': True  # Flag for template to show this is dummy data
        }
        
    else:
        # Get parameters with defaults for real data
        order_by = request.GET.get('order_by', 'ClientNo')
        order_dir = request.GET.get('order_dir', 'asc')
        search_term = request.GET.get('search', '').strip()
        page_number = request.GET.get('page', 1)

        # Map the requested field to actual model field
        actual_field = FIELD_MAPPING.get(order_by, 'kyc_id')  # Default to kyc_id if mapping not found

        # Validate sorting direction
        order_dir = 'desc' if order_dir == 'desc' else 'asc'

        # Base queryset
        kycs = KYCModel.objects.all()

        # Search filter - update to use actual field names
        if search_term:
            kycs = kycs.filter(
                Q(kyc_id__icontains=search_term) |
                Q(new_client_no__icontains=search_term) |
                Q(full_name__icontains=search_term) |
                Q(mobile__icontains=search_term) |
                Q(created_by__username__icontains=search_term)  # Assuming created_by is a User
            )

        # Apply sorting with the actual field name
        order_prefix = '-' if order_dir == 'desc' else ''
        kycs = kycs.order_by(f'{order_prefix}{actual_field}')

        # Paginate the results
        paginator = Paginator(kycs, 20)
        try:
            page_obj = paginator.page(page_number)
        except:
            page_obj = paginator.page(1)

        # Preserve query parameters for pagination links
        query_params = []
        if search_term:
            query_params.append(f'search={search_term}')
        if order_by != 'ClientNo':
            query_params.append(f'order_by={order_by}')
        if order_dir != 'asc':
            query_params.append(f'order_dir={order_dir}')

        query_string = '&'.join(query_params)
        if query_string:
            query_string = f'&{query_string}'

        context = {
            'kyc_list': page_obj,
            'order_by': order_by,  # Keep the original order_by for UI
            'order_dir': order_dir,
            'search_term': search_term,
            'is_paginated': page_obj.has_other_pages(),
            'total_records': paginator.count,
            'query_string': query_string,
            'request': request,
            'is_dummy_data': False
        }

    return render(request, 'kyc_lists.html', context)

# Create or Update KYC form based on presence of kyc_id
def kyc_update_view(request, kyc_id):
    kyc = get_object_or_404(KYCModel, kyc_id=kyc_id)
    
    if request.method == 'POST':
        form = KYCForm(request.POST, instance=kyc)
        if form.is_valid():
           
                form.save()
                return redirect('kyc:kyc_list') 
           
            
              
        # If form is invalid or save fails, render the form with errors
        return render(request, 'kyc_update.html', {
            'form': form,
            'kyc': kyc
        })
    else:
        form = KYCForm(instance=kyc)
    
    return render(request, 'kyc_update.html', {
        'form': form,
        'kyc': kyc
    })

# Delete a KYC entry




def kyc_delete_view(request, kyc_id):
    try:
        # Try both id and kyc_id fields
        try:
            kyc = get_object_or_404(KYCModel, id=kyc_id)
        except:
            kyc = get_object_or_404(KYCModel, kyc_id=kyc_id)
            
        if request.method == 'POST':
            kyc.delete()
           
            return redirect('kyc:kyc_list')
            
    except Exception as e:
       
        return redirect('kyc:kyc_list')
    
    # GET request should not reach here if form is POST-only
    return redirect('kyc:kyc_list')

# View details of a single KYC record
def kyc_detail_view(request, kyc_id):
    kyc = get_object_or_404(KYCModel, kyc_id=kyc_id)
    return render(request, 'kyc_detail.html', {'kyc': kyc})
@csrf_exempt
@require_POST


def kyc_bulk_delete(request):
    try:
        # Try both POST form data and JSON body
        if request.content_type == 'application/json':
            import json
            data = json.loads(request.body)
            kyc_ids = data.get('kyc_ids', [])
        else:
            kyc_ids = request.POST.getlist('kyc_ids[]') or request.POST.getlist('kyc_ids')
        
        # Convert to integers - try both id and kyc_id fields
        valid_ids = []
        for id_str in kyc_ids:
            try:
                valid_ids.append(int(id_str))
            except (ValueError, TypeError):
                continue
        
        if not valid_ids:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'error': 'No valid IDs provided'
                }, status=400)
            return redirect('kyc:kyc_list')
        
        # Delete records - try both id and kyc_id fields
        deleted_count = 0
        for id in valid_ids:
            try:
                # Try deleting by id first
                kyc = get_object_or_404(KYCModel, id=id)
                kyc.delete()
                deleted_count += 1
            except:
                try:
                    # Fall back to kyc_id if id fails
                    kyc = get_object_or_404(KYCModel, kyc_id=id)
                    kyc.delete()
                    deleted_count += 1
                except Exception as e:
                    continue
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'Successfully deleted {deleted_count} records',
                'deleted_count': deleted_count
            })
        
        return redirect('kyc:kyc_list')
        
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)
        return redirect('kyc:kyc_list')
