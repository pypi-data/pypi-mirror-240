from django.contrib import admin
from django import forms
from django.contrib.admin import register

# NEMO Imports
from NEMO_mqtt.models import MqttInterlockServer, MqttInterlock


class MqttInterlockServerAdminForm(forms.ModelForm):
    class Meta:
        model = MqttInterlockServer
        widgets = {"password": forms.PasswordInput(render_value=True)}
        fields = "__all__"

    # def clean(self):
    #     TODO
    #     if any(self.errors):
    #         return
    #     cleaned_data = super().clean()
    #     category = cleaned_data["category"]
    #     from NEMO import interlocks
    #     interlocks.get(category, False).clean_interlock_card(self)
    #     return cleaned_data


@register(MqttInterlockServer)
class MqttInterlockServerAdmin(admin.ModelAdmin):
    form = MqttInterlockServerAdminForm
    list_display = (
        "get_server_enabled",
        "card",
        "server",
        "port",
        "user",
        "client_id",
        "auth_mode",
        "tls_verify",
    )

    @admin.display(boolean=True, ordering="interlock__card__enabled", description="Server Enabled")
    def get_server_enabled(self, obj):
        return obj.card.enabled


class MqttInterlockAdminForm(forms.ModelForm):
    class Meta:
        model = MqttInterlockServer
        widgets = {"password": forms.PasswordInput(render_value=True)}
        fields = "__all__"

    pass


@register(MqttInterlock)
class MqttInterlockAdmin(admin.ModelAdmin):
    form = MqttInterlockAdminForm
    list_display = (
        "interlock",
        "get_interlock_enabled",
        "command_topic",
        "state_topic",
        "on_payload",
        "off_payload",
        "qos",
    )

    @admin.display(boolean=True, ordering="interlock__card__enabled", description="Server Enabled")
    def get_interlock_enabled(self, obj):
        return obj.interlock.card.enabled
