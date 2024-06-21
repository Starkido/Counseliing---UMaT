# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser, Member, FinanceOfficer

# # Register your models here.

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email','is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         # ('Personal info', {'fields': ('first_name', 'last_name')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Member)
# admin.site.register(FinanceOfficer)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Student, Counsellor

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)


# Define admin classes for Member and FinanceOfficer
@admin.register(Student)
class StudentAdmin(UserAdmin):
    list_display = ('email','first_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name', 'last_name','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'staff_id', 'full_name')
    ordering = ('email',)

@admin.register(Counsellor)
class CounsellorAdmin(UserAdmin):
    list_display = ('email', 'staff_id', 'first_name','last_name','gender','is_staff', 'year_of_experience', 'religion')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name', 'staff_id', 'gender','year_of_experience', 'religion')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'staff_id','first_name','last_name','gender','year_of_experience', 'religion','password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'staff_id')
    ordering = ('email',)