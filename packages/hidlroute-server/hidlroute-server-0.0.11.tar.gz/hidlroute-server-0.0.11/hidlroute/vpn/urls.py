#    Hidl Route - opensource vpn management system
#    Copyright (C) 2023 Dmitry Berezovsky, Alexander Cherednichenko
#
#    Hidl Route is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Hidl Route is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.urls import path

from hidlroute.vpn import views

app_name = "hidl_core"
urlpatterns = [
    path("devices/", views.DeviceVPNListView.as_view(), name="devices_list"),
    path("server/<int:server_id>/add_device/", views.device_add, name="device_add"),
    path("edit_device/<int:device_id>/", views.device_edit, name="device_edit"),
    path("device/<int:device_id>/reveal_config/", views.device_reveal_config, name="reveal_config"),
]
