from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import KYCModel
from django.http import JsonResponse
from django.core.paginator import Paginator
from .forms import KYCForm
from django.urls import reverse 
from django.db.models import Q
from django.views import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


# Home page view
def home(request):
    return HttpResponse("KYC Home Page")

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
