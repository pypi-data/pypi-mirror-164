#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

"""
FastyBird BUS connector entities module
"""

# Python base dependencies
from typing import Dict, List, Union

# Library dependencies
from fastybird_devices_module.entities.connector import (
    ConnectorEntity,
    ConnectorStaticPropertyEntity,
)
from fastybird_devices_module.entities.device import DeviceEntity
from fastybird_metadata.types import ConnectorSource, ModuleSource, PluginSource

# Library libs
from fastybird_fb_bus_connector.types import (
    CONNECTOR_NAME,
    DEFAULT_BAUD_RATE,
    DEFAULT_SERIAL_INTERFACE,
    DEVICE_NAME,
    MASTER_ADDRESS,
    ConnectorAttribute,
    ProtocolVersion,
)


class FbBusConnectorEntity(ConnectorEntity):  # pylint: disable=too-few-public-methods
    """
    FB BUS connector entity

    @package        FastyBird:FbBusConnector!
    @module         entities

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __mapper_args__ = {"polymorphic_identity": CONNECTOR_NAME}

    # -----------------------------------------------------------------------------

    @property
    def type(self) -> str:
        """Connector type"""
        return CONNECTOR_NAME

    # -----------------------------------------------------------------------------

    @property
    def source(self) -> Union[ModuleSource, ConnectorSource, PluginSource]:
        """Entity source type"""
        return ConnectorSource.FB_BUS_CONNECTOR

    # -----------------------------------------------------------------------------

    @property
    def address(self) -> int:
        """Connector communication master address"""
        address_property = next(
            iter([record for record in self.properties if record.identifier == ConnectorAttribute.ADDRESS.value]),
            None,
        )

        if (
            address_property is None
            or not isinstance(address_property, ConnectorStaticPropertyEntity)
            or not isinstance(address_property.value, int)
        ):
            return MASTER_ADDRESS

        return address_property.value

    # -----------------------------------------------------------------------------

    @property
    def interface(self) -> str:
        """Connector serial interface"""
        interface_property = next(
            iter([record for record in self.properties if record.identifier == ConnectorAttribute.INTERFACE.value]),
            None,
        )

        if (
            interface_property is None
            or not isinstance(interface_property, ConnectorStaticPropertyEntity)
            or not isinstance(interface_property.value, str)
        ):
            return DEFAULT_SERIAL_INTERFACE

        return interface_property.value

    # -----------------------------------------------------------------------------

    @property
    def baud_rate(self) -> int:
        """Connector communication baud rate"""
        baud_rate_property = next(
            iter([record for record in self.properties if record.identifier == ConnectorAttribute.BAUD_RATE.value]),
            None,
        )

        if (
            baud_rate_property is None
            or not isinstance(baud_rate_property, ConnectorStaticPropertyEntity)
            or not isinstance(baud_rate_property.value, int)
        ):
            return DEFAULT_BAUD_RATE

        return baud_rate_property.value

    # -----------------------------------------------------------------------------

    @property
    def protocol(self) -> ProtocolVersion:
        """Connector communication protocol version"""
        protocol_property = next(
            iter([record for record in self.properties if record.identifier == ConnectorAttribute.PROTOCOL.value]),
            None,
        )

        if (
            protocol_property is None
            or not isinstance(protocol_property, ConnectorStaticPropertyEntity)
            or not ProtocolVersion.has_value(int(str(protocol_property.value)))
        ):
            return ProtocolVersion.V1

        return ProtocolVersion(protocol_property.value)

    # -----------------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Union[str, int, bool, List[str], None]]:
        """Transform entity to dictionary"""
        return {
            **super().to_dict(),
            **{
                "address": self.address,
                "interface": self.interface,
                "baud_rate": self.baud_rate,
                "protocol": self.protocol.value,
            },
        }


class FbBusDeviceEntity(DeviceEntity):  # pylint: disable=too-few-public-methods
    """
    FB BUS device entity

    @package        FastyBird:FbBusConnector!
    @module         entities

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """

    __mapper_args__ = {"polymorphic_identity": DEVICE_NAME}

    # -----------------------------------------------------------------------------

    @property
    def type(self) -> str:
        """Device type"""
        return DEVICE_NAME

    # -----------------------------------------------------------------------------

    @property
    def source(self) -> Union[ModuleSource, ConnectorSource, PluginSource]:
        """Entity source type"""
        return ConnectorSource.FB_BUS_CONNECTOR
