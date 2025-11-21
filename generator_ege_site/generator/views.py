from django.shortcuts import render

# Create your views here.
def generator(request):
    return render(request, 'generator/generator.html')

def generate_variant(request, variant_id):
    # Логика генерации конкретного варианта
    context = {
        'variant_id': variant_id,
        'variant_data': f'Данные для варианта {variant_id}'
    }
    return render(request, 'generator/generate_variant.html', context)