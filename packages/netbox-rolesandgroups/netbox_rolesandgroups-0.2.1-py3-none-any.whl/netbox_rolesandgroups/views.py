from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from . import forms, models, tables, filtersets
from netbox_subsystems.tables import SubsystemTable


### SystemRole
class SystemRoleView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()

    def get_extra_context(self, request, instance):
        techrole_table = tables.TechRoleTable(models.TechRole.objects.filter(roles=instance))
        techrole_table.configure(request)
        subsystem_table = SubsystemTable(instance.subsystems.all())
        subsystem_table.configure(request)
        return {
            'techrole_table': techrole_table,
            'subsystem_table': subsystem_table,
        }


class SystemRoleListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()
    table = tables.SystemRoleTable
    filterset = filtersets.SystemRoleFilterSet
    filterset_form = forms.SystemRoleFilterForm


class SystemRoleEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.prefetch_related('subsystems', 'tags')
    form = forms.SystemRoleForm
    template_name = 'netbox_rolesandgroups/systemrole_edit.html'


class SystemRoleDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()


### TechRole
class TechRoleView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('tenancy.view_system',)
    queryset = models.TechRole.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.SystemRoleTable(instance.roles.all())
        table.configure(request)
        return {
            'systemrole_table': table,
        }


class TechRoleListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('tenancy.view_system',)
    queryset = models.TechRole.objects.all()
    table = tables.TechRoleTable
    filterset = filtersets.TechRoleFilterSet
    filterset_form = forms.TechRoleFilterForm


class TechRoleEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('tenancy.view_system',)
    queryset = models.TechRole.objects.all()
    form = forms.TechRoleForm

    template_name = 'netbox_rolesandgroups/techrole_edit.html'


class TechRoleDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('tenancy.view_system',)
    queryset = models.TechRole.objects.all()
