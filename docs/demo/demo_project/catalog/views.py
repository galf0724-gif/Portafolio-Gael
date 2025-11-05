from django.views.generic import ListView, View
from django.shortcuts import redirect
from django.contrib import messages
from .models import Product
import csv, io

class ProductListView(ListView):
    template_name = 'catalog/home.html'
    model = Product
    context_object_name = 'products'

class ImportView(View):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            messages.error(request, 'Seleccione un CSV.')
            return redirect('home')
        try:
            decoded = io.StringIO(file.read().decode('utf-8'))
            reader = csv.DictReader(decoded)
            created = 0; updated = 0; skipped = 0
            for row in reader:
                sku = (row.get('sku') or '').strip()
                name = (row.get('name') or '').strip()
                price = (row.get('price') or '0').strip()
                if not sku or not name:
                    skipped += 1
                    continue
                obj, is_new = Product.objects.update_or_create(
                    sku=sku,
                    defaults={'name': name, 'price': price or 0},
                )
                created += 1 if is_new else 0
                updated += 0 if is_new else 1
            messages.success(request, f'Importación OK. Nuevos: {created}, Actualizados: {updated}, Saltados: {skipped}')
        except Exception as e:
            messages.error(request, f'Error al importar: {e}')
        return redirect('home')
