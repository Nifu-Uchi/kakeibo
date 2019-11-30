from django import forms
from .models import Suitoh

class SuitohForm(forms.ModelForm):
   """
   新規データ登録画面用のフォーム定義
   """
   class Meta:
       model = Suitoh
       fields =['data', 'cat', 'out_cost', 'meimoku','rank']