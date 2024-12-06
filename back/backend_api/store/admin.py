from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title', 
        'description', 
        'is_subcategory'
    ]
    list_filter = [
        'is_subcategory'
    ]
    prepopulated_fields = {
        'slug': ('title',)
    }
admin.site.register(Category, CategoryAdmin)

import boto3
from django import forms
from django.conf import settings
from django.contrib import admin

from .models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def save(self, commit=True):
        """
        Переопределяем метод save для загрузки фотографии в S3 через boto3.
        """
        instance = super().save(commit=False)

        # Проверяем, есть ли новое фото для загрузки
        if self.cleaned_data.get("photo"):
            photo_file = self.cleaned_data['photo']
            s3_client = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            )

            # Определяем путь в S3
            s3_path = f"/{photo_file.name}"

            try:
                # Загружаем файл в S3
                s3_client.upload_fileobj(
                    photo_file.file,  # Передаем файл
                    settings.AWS_STORAGE_BUCKET_NAME,  # Имя бакета
                    s3_path,  # Путь внутри бакета
                )
                # Сохраняем URL фотографии в поле модели
                instance.photo = f"{settings.AWS_S3_ENDPOINT_URL}{s3_path}"
            except Exception as e:
                raise forms.ValidationError(f"Ошибка загрузки в S3: {e}")

        if commit:
            instance.save()

        return instance


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title', 'price', 'category', 'is_available', 'photo')
