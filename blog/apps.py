from django.apps import AppConfig
# from django.contrib.auth.models import Group

class BlogConfig(AppConfig):
    name = 'blog'

    # def ready(self):
    #     # إنشاء المجموعات عند بدء تشغيل التطبيق
    #     writer_group, created = Group.objects.get_or_create(name='Writer')
    #     admin_group, created = Group.objects.get_or_create(name='Admin')
