from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('add', views.add, name='add'),

    path('add/month', views.month, name='month'),
    path('view/month_', views.month_, name='month_'),

    path('add/production', views.production, name='production'),
    path('view/production_', views.production_, name='production_'),

    path('add/position', views.position, name='position'),
    path('view/position_', views.position_, name='position_'),

    path('add/history', views.history, name='history'),
    path('view/history_', views.history_, name='history_'),

    path('add/coupon', views.coupon, name='coupon'),
    path('view/comupon_', views.coupon_, name='coupon_'),

    path('add/machine', views.machine, name='machine'),
    path('view/machine_', views.machine_, name='machine_'),

    path('add/oil', views.oil, name='oil'),
    path('view/oil_', views.oil_, name='oil_'),

    path('add/breaks', views.breaks, name='breaks'),
    path('view/breaks_', views.breaks_, name='breaks_'),
    path('<id>/breaks', views.delete_breaks, name='delete'),

    path('add/subdivision', views.subdivision, name='subdivision'),
    path('view/subdivision_', views.subdivision_, name='subdivision_'),

    path('add/table', views.table, name='table'),
    path('view/table_', views.table_, name='table_'),

    path('add/employer', views.employer, name='employer'),
    path('view/employer_', views.employer_, name='employer_'),

    path('add/trip', views.trip, name='trip'),
    path('view/trip_', views.trip_, name='trip_'),

    path('add/hospital', views.hospital, name='hospital'),
    path('view/hospital_', views.hospital_, name='hospital_'),

    path('add/vacation', views.vacation, name='vacation'),
    path('view/vacation_', views.vacation_, name='vacation_'),
]


