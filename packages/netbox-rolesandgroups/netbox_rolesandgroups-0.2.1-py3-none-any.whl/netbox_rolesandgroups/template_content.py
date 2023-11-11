from extras.plugins import PluginTemplateExtension
from django.conf import settings
from .models import SystemRole, TechRole

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_rolesandgroups', {})


class SystemRoleList(PluginTemplateExtension):
    model = 'netbox_subsystems.system'

    def left_page(self):
        if plugin_settings.get('enable_system_roles') and plugin_settings.get('system_roles_location') == 'left':
            systemroles = SystemRole.objects.filter(system=self.context['object'])
            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': systemroles,
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_system_roles') and plugin_settings.get('system_roles_location') == 'right':
            systemroles = SystemRole.objects.filter(system=self.context['object'])
            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': systemroles,
            })
        else:
            return ""


class TechRoleList(PluginTemplateExtension):
    model = 'netbox_subsystems.subsystem'

    def left_page(self):
        if plugin_settings.get('enable_system_techrole') and plugin_settings.get('system_techrole_location') == 'left':
            systemroles = SystemRole.objects.filter(subsystems__in=[self.context['object']])
            techroles = TechRole.objects.filter(roles__in=[systemrole.id for systemrole in systemroles])
            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': systemroles,
                'techroles': techroles,
            })
        else:
            return ""

    def right_page(self):
        if plugin_settings.get('enable_system_techrole') and plugin_settings.get('system_techrole_location') == 'right':
            systemroles = SystemRole.objects.filter(subsystems__in=[self.context['object']])
            techroles = TechRole.objects.filter(roles__in=[systemrole.id for systemrole in systemroles])
            return self.render('netbox_rolesandgroups/systemrole_include.html', extra_context={
                'system_roles': systemroles,
                'techroles': techroles,
            })
        else:
            return ""


template_extensions = [SystemRoleList, TechRoleList]
