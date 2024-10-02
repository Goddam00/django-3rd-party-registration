from django.shortcuts import render
from .models import Vendor
from .forms import VendorForm, RawVendorForm # 要記得 import 相對應的 Model Form 唷!
from django.http import Http404
from django.shortcuts import get_object_or_404 # 新增
from django.views.generic import ListView, DetailView # 新增
from django.views.generic import CreateView
from django.forms import ModelForm
from django.views.generic import UpdateView # 新增

# Create your views here.
'''
def showtemplate(request):
    vendor_list = Vendor.objects.all()
    context = {'vendor_list': vendor_list}
    # print(vendor_list)
    return render(request, 'vendors/detail.html', context)

def singleVendor(request, id): #加了一個 id 這個參數是對應到 urls.py 裡面 <int:id>
    # try:
    #     vendor_list = Vendor.objects.get(id=id)
    # except Vendor.DoesNotExist:
    #     raise Http404
    vendor_list = get_object_or_404(Vendor, id=id)
    context = {
        'vendor_list': vendor_list
    }
    return render(request, 'vendors/vendor_detail.html', context)
'''
'''
# 針對 vendor_create.html
def vendor_create_view(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VendorForm() # 清空 form

    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)
'''

# 新增
'''
def vendor_create_view(request):
    form = RawVendorForm(request.POST or None)
    if form.is_valid():
        Vendor.objects.create(**form.cleaned_data) # 新增
        form = VendorForm()
    context = {
        'form' : form
    }
    return render(request, "vendors/vendor_create.html", context)
'''
# 繼承 ListView
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendors/vendor_list.html'

# 繼承 DetailView
class VendorDetailView(DetailView):
    model = Vendor # 它與 queryset = Vendor.objects.all()是同義的
    # queryset = Vendor.objects.all()
    template_name = 'vendors/vendor_detail.html'



# modelForm 
class VendorModelForm(ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
            # fields = (
            #         'vendor_name',
            #         'store_name',
            #         'phone_number',
            #         'address',
            # )
        labels = {
            'vendor_name': '攤販名稱',
            'store_name' : '店名',
            'phone_number' : '電話',
            'address' : '地址',
        }

# CreateView
class VendorCreateView(CreateView):
    form_class = VendorModelForm
    # model = Vendor
    # fields= ['vendor_name', 'store_name']
    template_name = 'vendors/vendor_create.html'


class VendorUpdateView(UpdateView):
    form_class = VendorModelForm
    template_name = 'vendors/vendor_create.html'
    queryset = Vendor.objects.all() # 這很重要