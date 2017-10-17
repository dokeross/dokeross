from django.shortcuts import render

def warehouse_page(request):
    return render(request, 'warehousePage/warehouse.html', {})

def warehouse_warm(request):
    return render(request, 'warehousePage/warehouse_warm.html', {})

def warehouse_cold(request):
    return render(request, 'warehousePage/warehouse_cold.html', {})

def warehouse_manufacture(request):
    return render(request, 'warehousePage/warehouse_manufacture.html', {})

def warehouse_open(request):
    return render(request, 'warehousePage/warehouse_open.html', {})

