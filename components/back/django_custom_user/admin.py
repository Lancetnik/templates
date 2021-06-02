from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ("email", "full_name", "is_staff",
                  'icon_color', 'password', 'about_me',
                  'portfolio')

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class MyUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email", "full_name", "is_staff", 
                    'icon_color','password', 'about_me', 
                    'portfolio')
    ordering = ("email",)
    list_filter = ("email",)

    fieldsets = (
        (None, {'fields': list_display}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'full_name',
                       'about_me', 'portfolio')}
         ),
    )
    pass


admin.site.register(MyUser, MyUserAdmin)
