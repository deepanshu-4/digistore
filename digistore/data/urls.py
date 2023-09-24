from django.urls import path
from . import views
app_name="data"
urlpatterns = [
    path("",views.index,name="index"),
    path("otp",views.otp,name="otp"),
    path("checkotp",views.checkotp,name="checkotp"),
    path("newf",views.newf,name="newf"),
    path("about",views.about,name="about"),
    path("register",views.register,name="register"),
    path("login",views.log_in,name="log_in"),
    path("logout",views.log_out,name="log_out"),
    path('blog', views.blog_view, name='blog'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('addim/<int:id>/', views.addimage, name='addimage'),
    path('addfolder', views.addfolder, name='addfolder'),
    path('yvideo', views.yvideo, name='yvideo'),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('deleteimage/<int:id>/',views.deleteimage,name="deleteimage"),
    path('deletefolder/<int:id>/',views.deletefolder,name="deletefolder"),
    path('gallery', views.gallery, name='gallery'),
    #for gallery
    path('pblog', views.pblog_view, name='pblog'),
    path('p/<int:id>/', views.pdetail_view, name='pdetail'),
    path('paddim/<int:id>/', views.addpdf, name='addpdf'),
    path('paddfolder', views.paddfolder, name='paddfolder'),
    path('deletepdf/<int:id>/',views.deletepdf,name="deletepdf"),
    path('pdeletefolder/<int:id>/',views.pdeletefolder,name="pdeletefolder"),
    path('listen/<int:id>/<int:id1>/',views.listen,name="listen"),
    #for files
    path('fpblog', views.fpblog_view, name='fpblog'),
    path('fp/<int:id>/', views.fpdetail_view, name='fpdetail'),
    path('fpaddim/<int:id>/', views.faddpdf, name='faddpdf'),
    path('fpaddfolder', views.fpaddfolder, name='fpaddfolder'),
    path('fdeletepdf/<int:id>/',views.fdeletepdf,name="fdeletepdf"),
    path('fpdeletefolder/<int:id>/',views.fpdeletefolder,name="fpdeletefolder"),
    path("resetutil",views.resetutil,name="resetutil"),
    path("changepassword/<str:a>/<str:b>/<str:c>/",views.forgetutil,name="forgetutil"),
    path("forget",views.forget,name="forget"),
    path("reset/<str:a>/<str:b>/<str:c>/",views.reset,name="reset"),
    
    path('like/<int:id>', views.like, name='like'),
    path('dlike/<int:id>', views.dlike, name='dlike'),
    path('addtolist/<int:id>', views.addtolist, name='addtolist'),
    path('deletefromlist/<int:id>', views.deletefromlist, name='deletefromlist')

]
