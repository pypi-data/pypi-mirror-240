import django_tables2 as tables

from netbox.tables import NetBoxTable, columns
from .models import SystemRole, TechRole


system_ROLE_LINK = """
{% if record %}
    <a href="{% url 'plugins:netbox_rolesandgroups:systemrole' pk=record.pk %}">{% firstof record.name record.name %}</a>
{% endif %}
"""

system_ROLE_GROUP_LINK = """
{% if record %}
    <a href="{% url 'plugins:netbox_rolesandgroups:techrole' pk=record.pk %}">{% firstof record.name record.name %}</a>
{% endif %}
"""


class SystemRoleTable(NetBoxTable):
    name = tables.TemplateColumn(template_code=system_ROLE_LINK)
    system = tables.Column(
        linkify=True
    )
    subsystem = tables.Column(
        linkify=True
    )
    parent = tables.Column(
        linkify=True
    )

    tags = columns.TagColumn(
        url_name='plugins:netbox_rolesandgroups:systemrole_list'
    )

    class Meta(NetBoxTable.Meta):
        model = SystemRole
        fields = ('pk', 'id', 'name', 'system', 'subsystem', 'parent', 'upload_interface', 'upload_format',
                  'mapping_security_group', 'sed', 'link', 'description', 'slug', 'comments', 'actions',
                  'created', 'last_updated', 'tags')
        default_columns = ('name', 'slug', 'system', 'tags')


class TechRoleTable(NetBoxTable):
    name = tables.TemplateColumn(template_code=system_ROLE_LINK)
    role = tables.Column(
        linkify=True
    )
    tags = columns.TagColumn(
        url_name='plugins:netbox_rolesandgroups:techrole_list'
    )

    class Meta(NetBoxTable.Meta):
        model = TechRole
        fields = ('pk', 'id', 'name', 'role', 'slug', 'comments', 'actions',
                  'created', 'last_updated', 'tags')
        default_columns = ('name', 'slug', 'role', 'tags')
