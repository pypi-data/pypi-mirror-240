from extras.plugins import PluginTemplateExtension
from django.conf import settings
from .models import SystemRole, TechRole

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_rolesandgroups', {})


class SystemRoleList(PluginTemplateExtension):
    model = 'netbox_subsystems.system'

    def left_page(self):
        if plugin_settings.get('enable_system_roles') and plugin_settings.get('system_roles_location') == 'left':

            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': SystemRole.objects.filter(system=self.context['object']),
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_system_roles') and plugin_settings.get('system_roles_location') == 'right':

            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': SystemRole.objects.filter(system=self.context['object']),
            })
        else:
            return ""


class TechRoleList(PluginTemplateExtension):
    model = 'netbox_subsystems.subsystem'

    def left_page(self):
        if plugin_settings.get('enable_system_techrole') and plugin_settings.get('system_techrole_location') == 'left':

            return self.render('netbox_rolesandgroups/techrole_include.html', extra_context={
                'techroles': SystemRole.objects.filter(techrole=self.context['object']),
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_system_techrole') and plugin_settings.get('system_techrole_location') == 'right':

            return self.render('netbox_rolesandgroups/techrole_include.html', extra_context={
                'techroles': SystemRole.objects.filter(techrole=self.context['object']),
            })
        else:
            return ""


template_extensions = [SystemRoleList, TechRoleList]
