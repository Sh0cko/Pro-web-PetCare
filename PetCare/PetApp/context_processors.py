from django.utils import timezone

def nav_counters(request):
    """Provide sidebar counters for badges: low stock, expiring/expired, recent movements.
    Safe to fail (returns zeros) if tables aren't migrated yet.
    """
    data = {
        'low_stock_count': 0,
        'exp_count': 0,
        'movimientos_recent_count': 0,
    }
    try:
        from django.db.models import OuterRef, Subquery, IntegerField, Value, F
        from django.db.models.functions import Coalesce
        from .models import Producto, ProductMeta, InventoryMovement

        # Low stock: cantidad <= (meta.threshold or 5)
        threshold_subq = ProductMeta.objects.filter(producto=OuterRef('pk')).values('low_stock_threshold')[:1]
        productos_ann = (
            Producto.objects
            .annotate(umbral=Coalesce(Subquery(threshold_subq, output_field=IntegerField()), Value(5)))
        )
        data['low_stock_count'] = productos_ann.filter(cantidad__lte=F('umbral')).count()

        # Expiration: expired or within 30 days
        today = timezone.now().date()
        metas = ProductMeta.objects.filter(expiration_date__isnull=False)
        expired = metas.filter(expiration_date__lt=today).count()
        soon = metas.filter(expiration_date__gte=today, expiration_date__lte=today + timezone.timedelta(days=30)).count()
        data['exp_count'] = expired + soon

        # Movements in last 24 hours
        since = timezone.now() - timezone.timedelta(hours=24)
        data['movimientos_recent_count'] = InventoryMovement.objects.filter(timestamp__gte=since).count()
    except Exception:
        # Fail-safe: if DB tables are missing or any error occurs, keep zeros
        pass

    return { 'nav_badges': data }

def user_permissions(request):
    return {
        'is_admin': request.user.is_authenticated and request.user.is_superuser,
        'is_staff': request.user.is_authenticated and request.user.is_staff,
        'is_normal_user': request.user.is_authenticated and not request.user.is_staff and not request.user.is_superuser,
    }
