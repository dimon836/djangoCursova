from .models import *
from django.forms import ModelForm, TextInput


class MonthForm(ModelForm):
    class Meta:
        model = Month
        fields = ["name", "num_of_workday"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name month'
            }),
            "num_of_workday": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Amount of work day'
            })
        }


class CouponForm(ModelForm):
    class Meta:
        model = Coupon
        fields = ["type_of_transport", "cost_road", "cost_housing"]
        widgets = {
            "type_of_transport": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type of transport'
            }),
            "cost_road": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cost of road'
            }),
            "cost_housing": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cost of housing'
            })
        }


class EmployerForm(ModelForm):
    class Meta:
        model = Employer
        fields = ["name", "surname", "last_name", "id_position", "id_status", "id_subdivision"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Surname'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            "id_subdivision": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id subdivision'
            }),
            "id_status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id status'
            }),
            "id_position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id position'
            })
        }


class HistoryForm(ModelForm):
    class Meta:
        model = HistoryPromotions
        fields = ["name", "date_up"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "date_up": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date up'
            })
        }


class HospitalForm(ModelForm):
    class Meta:
        model = HospitalTrip
        fields = ["date_start", "disease", "num_days", "id_employer"]
        widgets = {
            "date_start": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date start'
            }),
            "disease": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Disease'
            }),
            "num_days": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number days'
            }),
            "id_employer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id employer'
            })
        }


class MachineForm(ModelForm):
    class Meta:
        model = WorkingMachine
        fields = ["name", "model", "year_creation"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name'
            }),
            "model": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'model'
            }),
            "year_creation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Year creation'
            }),
        }


class OilForm(ModelForm):
    class Meta:
        model = OilChange
        fields = ["amount_oil", "date_change", "id_machine"]
        widgets = {
            "amount_oil": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'amount oil'
            }),
            "date_change": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'data change'
            }),
            "id_machine": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id machine'
            })
        }


class PositionForm(ModelForm):
    class Meta:
        model = PositionEm
        fields = ["name", "date_up", "id_rate"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name'
            }),
            "date_up": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'date up'
            }),
            "id_rate": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id rate'
            })
        }


class ProductionForm(ModelForm):
    class Meta:
        model = ProductionRate
        fields = ["det_per_hour", "amount_h"]
        widgets = {
            "det_per_hour": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'detail per hour'
            }),
            "amount_h": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'amount hours'
            })
        }


class SubdivisionForm(ModelForm):
    class Meta:
        model = Subdivision
        fields = ["name", "id_machine"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name'
            }),
            "id_machine": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id machine'
            })
        }


class TableForm(ModelForm):
    class Meta:
        model = TableSheet
        fields = ["id_employer", "id_month", "nhd", "ntd", "nvd"]
        widgets = {
            "id_employer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id employer'
            }),
            "id_month": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id month'
            }),
            "nhd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'numbers of hospital days'
            }),
            "ntd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'numbers of trip days'
            }),
            "nvd": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'numbers of vacation days'
            })
        }


class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ["date", "location", "num_days", "id_employer", "id_talon"]
        widgets = {
            "date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "location": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'location'
            }),
            "num_days": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'amount of days'
            }),
            "id_talon": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id talon'
            }),
            "id_employer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id employer'
            })
        }


class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ["date_start", "num_days", "id_employer"]
        widgets = {
            "date_start": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'date start'
            }),
            "num_days": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'amount of days'
            }),
            "id_employer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id employer'
            })
        }


class BreaksForm(ModelForm):
    class Meta:
        model = MachineBreakdowns
        fields = ["date_breakdown", "num_breakdown", "cost", "id_machine"]
        widgets = {
            "date_breakdown": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "num_breakdown": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'num of breakdown'
            }),
            "cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'cost'
            }),
            "id_machine": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'id machine'
            })
        }
