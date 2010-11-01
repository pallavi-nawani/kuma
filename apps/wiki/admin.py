from django.contrib import admin

from wiki.models import Document


class DocumentAdmin(admin.ModelAdmin):
    list_filter = ('is_template', 'is_localizable', 'category', 'locale')
    list_display = ('locale', 'title', 'category', 'is_localizable')
    list_display_links = ('title',)
    raw_id_fields = ('parent',)
    readonly_fields = ('id', 'current_revision')


admin.site.register(Document, DocumentAdmin)
