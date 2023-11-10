from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import SystemRole, TechRole
from netbox_subsystems.api.nested_serializers import NestedSystemSerializer, NestedSubsystemSerializer

# system Role Serializer
class NestedSystemRoleSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_rolesandgroups-api:system-role-detail'
    )

    class Meta:
        model = SystemRole
        fields = (
            'id', 'url', 'display', 'name', 'slug',
        )


class SystemRoleSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_rolesandgroups-api:system-role-detail'
    )

    system = NestedSystemSerializer(required=False, allow_null=True)
    subsystem = NestedSubsystemSerializer(required=False, allow_null=True)
    parent = NestedSystemRoleSerializer(required=False, allow_null=True)

    class Meta:
        model = SystemRole
        fields = (
            'id', 'url', 'display', 'name', 'slug', 'system', 'subsystem', 'parent', 'upload_interface',
            'upload_format', 'mapping_security_group', 'sed', 'link', 'description', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated',
        )


# system Role Group  Serializer
class TechRoleSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_rolesandgroups-api:tech-role-detail'
    )

    role = NestedSystemRoleSerializer(many=True, required=False)

    class Meta:
        model = TechRole
        fields = (
            'id', 'url', 'display', 'name', 'slug', 'role', 'comments', 'tags',
            'custom_fields', 'created', 'last_updated',
        )


class NestedTechRoleSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_rolesandgroups-api:tech-role-detail'
    )

    class Meta:
        model = TechRole
        fields = (
            'id', 'url', 'display', 'name', 'slug',
        )

