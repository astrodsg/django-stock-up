from django.contrib import admin

from stock_manager.models import StockUpUser, Portfoilo, Stock

class StockUpUserAdmin (admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name','email')

class PortfolioAdmin (admin.ModelAdmin):
    list_display = ('stock_up_user_id','name','creation_date')

class StockAdmin (admin.ModelAdmin):
    list_display = ('portfolio_id','symbol','name','unit_price','nstocks','total_price','creation_date')

admin.site.register(StockUpUser,StockUpUserAdmin)
admin.site.register(Portfoilo,PortfolioAdmin)
admin.site.register(Stock,StockAdmin)
