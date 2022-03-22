from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense', views.add_expense, name="add-expense"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('search-expenses', csrf_exempt(views.search_expenses), name="search_expenses"),
    path('expense_category_summary', views.expense_category_summary, name="expense_category_summary"),
    # path('income_source_summary', views.income_source_summary, name="income_source_summary"),
    path('stats', views.stats_view, name="stats"),
    # path('stats_income', views.stats_view_income, name="stats-income"),
    path('export_csv', views.export_csv, name="export-csv"),
    path('export_excel', views.export_excel, name="export-excel"),
    path('export_pdf', views.export_pdf, name="export-pdf"),
]
