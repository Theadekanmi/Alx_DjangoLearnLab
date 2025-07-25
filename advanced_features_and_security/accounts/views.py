from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Document
from .forms import DocumentForm


@login_required
def profile_view(request):
    """Display user profile with custom fields."""
    return render(request, 'accounts/profile.html', {'user': request.user})


# STEP 3: Views with permission checks
@login_required
@permission_required('accounts.can_view', raise_exception=True)
def document_list_view(request):
    """View to list all documents - requires can_view permission."""
    documents = Document.objects.all()
    return render(request, 'accounts/document_list.html', {'documents': documents})


@login_required
@permission_required('accounts.can_view', raise_exception=True)
def document_detail_view(request, pk):
    """View to display a single document - requires can_view permission."""
    document = get_object_or_404(Document, pk=pk)
    return render(request, 'accounts/document_detail.html', {'document': document})


@login_required
@permission_required('accounts.can_create', raise_exception=True)
def document_create_view(request):
    """View to create a new document - requires can_create permission."""
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.author = request.user
            document.save()
            messages.success(request, 'Document created successfully!')
            return redirect('accounts:document_detail', pk=document.pk)
    else:
        form = DocumentForm()
    
    return render(request, 'accounts/document_form.html', {
        'form': form, 
        'title': 'Create Document'
    })


@login_required
@permission_required('accounts.can_edit', raise_exception=True)
def document_edit_view(request, pk):
    """View to edit a document - requires can_edit permission."""
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, 'Document updated successfully!')
            return redirect('accounts:document_detail', pk=document.pk)
    else:
        form = DocumentForm(instance=document)
    
    return render(request, 'accounts/document_form.html', {
        'form': form, 
        'title': 'Edit Document',
        'document': document
    })


@login_required
@permission_required('accounts.can_delete', raise_exception=True)
def document_delete_view(request, pk):
    """View to delete a document - requires can_delete permission."""
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == 'POST':
        document.delete()
        messages.success(request, 'Document deleted successfully!')
        return redirect('accounts:document_list')
    
    return render(request, 'accounts/document_confirm_delete.html', {'document': document})


def permission_denied_view(request):
    """Custom view for permission denied."""
    return render(request, 'accounts/permission_denied.html', status=403)
