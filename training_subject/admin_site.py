from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_url = '/administration/'
    enable_nav_sidebar = False
    site_header = 'Training Subject'
    site_title = 'Training Subject'
    index_title = 'Training Subject'


training_subject_admin = AdminSite(name='training_subject_admin')
