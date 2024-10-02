from django import forms

from .models import Vendor, Food

class VendorForm(forms.ModelForm):
    class Meta:
        # model : 我要使用哪一個 Model
        # fileds : 使用 Model 的哪些欄位
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': '攤販名稱',
            'store_name' : '店名',
            'phone_number' : '電話',
            'address' : '地址',
        }

# 創建一個 Raw Form
class RawVendorForm(forms.Form):
    vendor_name = forms.CharField()
    store_name = forms.CharField()
    phone_number = forms.CharField()