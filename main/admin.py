from django.contrib import admin

from main.models import Product, NetworkElement

admin.site.register(Product)


@admin.register(NetworkElement)
class NetworkElementAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'supplier')
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier(self, obj):
        if obj.supplier:
            return obj.supplier.name
        else:
            return 'Нет поставщика'

    supplier.allow_tags = True

    def clear_debt(self, request, queryset):
        for obj in queryset:
            if obj.supplier > 0:
                obj.supplier = 0
                obj.save()
        self.message_user(request, "Задолженность погашена по выбранным объектам.")

    clear_debt.short_description = "Очистить долги"
