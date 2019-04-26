from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^hello/', "app.views.hello"),#效能較慢
    url(r'^hello/', views.hello),
    url(r'^$', views.frontpage),
    url(r'^settings$', views.setting),
    url(r'^add_category$', views.addCategory),
    url(r'^delete_category/(?P<category>\w+)', views.deleteCategory),
    url(r"add_record$" , views.addRecord),
    url(r"delete_record" , views.deleteRecord),
]
