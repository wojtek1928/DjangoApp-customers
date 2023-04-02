from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from customers.models import Customer
from customers.ui.forms import CustomerAddForm, CustomerEditForm, PostalAddressAddForm, PostalAddressEditForm

# UI Views
#################################################################
# UI customer addition and customers list view


def customer_add_list_view(request):
    customers = Customer.objects.all()
    args = {}
    args['object_list'] = customers

    # Collapse form handling
    args['aria_expanded'] = 'false'
    args['show_form'] = ''

    # Form handling
    if request.method == 'POST':
        args['form_customer'] = CustomerAddForm(request.POST)
        args['form_address'] = PostalAddressAddForm(request.POST)

        # Data validation
        if args['form_customer'].is_valid() and args['form_address'].is_valid():
            address = args['form_address'].save()
            customer = args['form_customer'].save(commit=False)
            customer.address = address  # Linking the address to the customer record
            customer.save()
            return redirect('customers-add-list-ui')

        else:
            args['aria_expanded'] = 'true'
            args['show_form'] = 'show'
    else:
        args['form_customer'] = CustomerAddForm
        args['form_address'] = PostalAddressAddForm

    return render(request, 'index.html', args)


# UI customer edition view
def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    args = {}
    args['main_site'] = reverse('customers-add-list-ui')

    # Form handling
    if request.method == 'POST':
        args['form_customer'] = CustomerEditForm(
            request.POST, instance=customer)
        args['form_address'] = PostalAddressEditForm(
            request.POST, instance=customer.address)

        # Data validation
        if args['form_customer'].is_valid() and args['form_address'].is_valid():
            args['form_customer'].save()
            args['form_address'].save()
            return redirect('customers-add-list-ui')
    else:
        args['form_customer'] = CustomerEditForm(instance=customer)
        args['form_address'] = PostalAddressEditForm(instance=customer.address)

    return render(request, 'edit.html', args)


# UI customer deletion view
def customer_delete(request, id):
    args = {}
    # URI for Cancel button
    args['main_site'] = reverse('customers-add-list-ui')
    # Customer selection
    customer = get_object_or_404(Customer, id=id)
    args['customer_name'] = customer.name
    # URI for confirmation button
    args['delete'] = reverse('customer-delete-ui', kwargs={'id': customer.id})

    # Delete confirmation handling
    if 'confirmed' in request.GET:
        customer.delete()
        return redirect('customers-add-list-ui')

    return render(request, 'delete.html', args)
