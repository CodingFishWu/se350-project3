from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^user/login', views.login),
    url(r'^user/signup', views.sign),
    url(r'^order', views.order),
    url(r'^product', views.product),
    url(r'^marketDepth/product/(?P<code>.+)', views.market_depth),
    url(r'^transaction', views.transaction),
    url(r'^trader', views.trader),
]
