from django.shortcuts import render, redirect
from .forms import InputIndexForm
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Index


def output_index_list_view(request):
    indexes = Index.objects.all()
    indexes = list(reversed(indexes))
    return render(request, 'index/list_index.html', {'indexes': indexes})


def delete_index_list_view(request):
    indexes = Index.objects.all()
    indexes = list(reversed(indexes))
    return render(request, 'index/delete_index.html', {'indexes': indexes})


def delete_index_list_ordered_by_click_times_view(request):
    indexes = Index.objects.all().order_by('-click_times')

    return render(request, 'index/delete_index.html', {'indexes': indexes})


def delete_index_list_ordered_by_date_created_view(request):
    indexes = Index.objects.all().order_by('-date_created')

    return render(request, 'index/delete_index.html', {'indexes': indexes})


def delete_index_list_ordered_by_last_click_date_view(request):
    indexes = Index.objects.all().order_by('-last_click_date')

    return render(request, 'index/delete_index.html', {'indexes': indexes})


def delete_index_list_ordered_by_key_words_view(request):
    indexes = Index.objects.all().order_by('key_words')

    return render(request, 'index/delete_index.html', {'indexes': indexes})


def input_index_view(request):
    context = {}

    form = InputIndexForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = InputIndexForm()
        return redirect('output_list')

    context['form'] = form

    return render(request, 'index/input_index.html', context)


def record_click(request, index_id):
    try:
        index = Index.objects.get(pk=index_id)
        if index.click_times is not None:
            index.click_times += 1
        else:
            index.click_times = 1
        index.last_click_date = timezone.now()
        index.save()
        return JsonResponse({'success': True})
    except ObjectDoesNotExist:
        return JsonResponse({'success': False, 'error': 'Index not found'})


def delete_selected_rows(request):
    if request.method == 'POST':
        selected_row_ids = request.POST.getlist('selected_rows')
        if selected_row_ids:
            # Delete selected rows using the model's delete method
            Index.objects.filter(id__in=selected_row_ids).delete()

    return redirect('output_list')  # Redirect to the list view after deletion
