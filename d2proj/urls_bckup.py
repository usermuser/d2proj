from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sven/', 'd2app.views.svenfunc'),
    url(r'^earthshaker/', 'd2app.views.eartfunc'),
    url(r'^night stalker/', 'd2app.views.stalfunc'),
    url(r'^tiny/', 'd2app.views.tinyfunc'),
    url(r'^kunkka/', 'd2app.views.kunkfunc'),
    url(r'^beastmaster/', 'd2app.views.beastfunc'),
    url(r'^dragon knight/', 'd2app.views.dragfunc'),
    url(r'^clockwerk/', 'd2app.views.clockfunc'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
