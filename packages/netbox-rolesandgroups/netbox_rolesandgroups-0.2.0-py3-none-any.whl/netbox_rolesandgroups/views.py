from django.contrib.auth.mixins import PermissionRequiredMixin
from netbox.views import generic
from . import forms, models, tables, filtersets


### SystemRole
class SystemRoleView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()

    def get_extra_context(self, request, instance):
        table = tables.TechRoleTable(instance.techrole.all())
        table.configure(request)
        return {
            'techrole_table': table,
        }


class SystemRoleListView(PermissionRequiredMixin, generic.ObjectListView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()
    table = tables.SystemRoleTable
    filterset = filtersets.SystemRoleFilterSet
    filterset_form = forms.SystemRoleFilterForm


class SystemRoleEditView(PermissionRequiredMixin, generic.ObjectEditView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()
    form = forms.SystemRoleForm
    template_name = 'netbox_rolesandgroups/systemrole_edit.html'


class SystemRoleDeleteView(PermissionRequiredMixin, generic.ObjectDeleteView):
    permission_required = ('tenancy.view_system',)
    queryset = models.SystemRole.objects.all()


### TechRole
class TechRoleView(PermissionRequiredMixin, generic.ObjectView):
    permission_required = ('tenancy.view_system',)
    queryset = models.TechRole.objects.all()


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
