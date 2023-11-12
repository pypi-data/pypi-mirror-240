# Copyright (C) 2023  Loren Eteval <loren.eteval@proton.me>
#
# This file is part of Furious.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from Furious.Core.Core import XrayCore, Hysteria1
from Furious.Gui.Action import Action, Seperator
from Furious.Widget.Widget import Menu
from Furious.Utility.Constants import APP, DATA_DIR
from Furious.Utility.Utility import Switch, bootstrapIcon
from Furious.Utility.Translator import gettext as _


BUILTIN_ROUTING_TABLE = {
    'Bypass Mainland China': {
        XrayCore.name(): {
            'domainStrategy': 'IPIfNonMatch',
            'domainMatcher': 'hybrid',
            'rules': [
                # ads
                {
                    'type': 'field',
                    'domain': [
                        'geosite:category-ads-all',
                    ],
                    'outboundTag': 'block',
                },
                # geosite
                {
                    'type': 'field',
                    'domain': [
                        'geosite:cn',
                    ],
                    'outboundTag': 'direct',
                },
                # geoip
                {
                    'type': 'field',
                    'ip': [
                        'geoip:private',
                        'geoip:cn',
                    ],
                    'outboundTag': 'direct',
                },
                # Proxy everything
                {
                    'type': 'field',
                    'port': '0-65535',
                    'outboundTag': 'proxy',
                },
            ],
        },
        Hysteria1.name(): {
            'acl': (DATA_DIR / 'hysteria' / 'bypass-mainland-China.acl').as_posix(),
            'mmdb': (DATA_DIR / 'hysteria' / 'country.mmdb').as_posix(),
        },
    },
    'Bypass Iran': {
        XrayCore.name(): {
            'domainStrategy': 'IPIfNonMatch',
            'domainMatcher': 'hybrid',
            'rules': [
                # ads
                {
                    'type': 'field',
                    'domain': [
                        'geosite:category-ads-all',
                        'iran:ads',
                    ],
                    'outboundTag': 'block',
                },
                # Iran sites
                {
                    'type': 'field',
                    'domain': [
                        'iran:ir',
                        'iran:other',
                    ],
                    'outboundTag': 'direct',
                },
                # Iran IP
                {
                    'type': 'field',
                    'ip': [
                        'geoip:private',
                        'geoip:ir',
                    ],
                    'outboundTag': 'direct',
                },
                # Proxy everything
                {
                    'type': 'field',
                    'port': '0-65535',
                    'outboundTag': 'proxy',
                },
            ],
        },
        Hysteria1.name(): {
            'acl': (DATA_DIR / 'hysteria' / 'bypass-Iran.acl').as_posix(),
            'mmdb': (DATA_DIR / 'hysteria' / 'country.mmdb').as_posix(),
        },
    },
    'Route My Traffic Through Tor': {
        XrayCore.name(): {},
        Hysteria1.name(): {},
    },
    'Global': {
        XrayCore.name(): {
            'domainStrategy': 'IPIfNonMatch',
            'domainMatcher': 'hybrid',
            'rules': [
                # Proxy everything
                {
                    'type': 'field',
                    'port': '0-65535',
                    'outboundTag': 'proxy',
                },
            ],
        },
        Hysteria1.name(): {},
    },
    'Custom': {
        XrayCore.name(): {},
        Hysteria1.name(): {},
    },
}

BUILTIN_ROUTING = list(BUILTIN_ROUTING_TABLE.keys())


def routingToIndex():
    currentRouting = APP().Routing

    try:
        index = int(currentRouting)
    except ValueError:
        for i, routing in enumerate(BUILTIN_ROUTING):
            if routing == currentRouting:
                return i

        return -1
    except Exception:
        # Any non-exit exceptions

        return -1
    else:
        return index + len(BUILTIN_ROUTING)


class BuiltinRoutingChildAction(Action):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def triggeredCallback(self, checked):
        textEnglish = self.textEnglish

        if APP().Routing != textEnglish:
            # De-activate
            APP().RoutesWidget.activateItemByIndex(routingToIndex(), activate=False)
            APP().Routing = textEnglish
            # Activate
            APP().RoutesWidget.activateItemByIndex(routingToIndex(), activate=True)

            if APP().isConnected():
                # Connected. Re-configure connection
                APP().tray.ConnectAction.connectingAction(
                    showProgressBar=True,
                    showRoutingChangedMessage=True,
                    currentRouting=textEnglish,
                    isBuiltinRouting=True,
                )


class RoutingChildAction(Action):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.translatable = False

    def triggeredCallback(self, checked):
        routingAction = APP().tray.RoutingAction

        for index, action in enumerate(
            # Skip built-in actions.
            routingAction.menu().actions()[len(BUILTIN_ROUTING) :]
        ):
            if id(self) == id(action):
                # Found action

                if APP().Routing != str(index):
                    route = APP().RoutesWidget.RoutesList[index]

                    # De-activate
                    APP().RoutesWidget.activateItemByIndex(
                        routingToIndex(), activate=False
                    )
                    APP().Routing = str(index)
                    # Activate
                    APP().RoutesWidget.activateItemByIndex(
                        routingToIndex(), activate=True
                    )

                    if APP().isConnected():
                        # Connected. Re-configure connection
                        APP().tray.ConnectAction.connectingAction(
                            showProgressBar=True,
                            showRoutingChangedMessage=True,
                            currentRouting=route['remark'],
                            isBuiltinRouting=False,
                        )

                # Select routing action done
                return

        raise Exception('Fatal error occurred')

    @property
    def textEnglish(self):
        return self.text()


class RoutingAction(Action):
    def __init__(self):
        if APP().Routing == 'Bypass':
            # Update value for backward compatibility
            APP().Routing = 'Bypass Mainland China'

        super().__init__(
            _('Routing'),
            icon=bootstrapIcon('shuffle.svg'),
            menu=Menu(
                *list(
                    BuiltinRoutingChildAction(
                        _(routing),
                        checkable=True,
                        checked=APP().Routing == routing,
                    )
                    for routing in BUILTIN_ROUTING
                ),
                *list(
                    RoutingChildAction(
                        route['remark'],
                        checkable=True,
                        checked=APP().Routing == str(index),
                    )
                    for index, route in enumerate(APP().RoutesWidget.RoutesList)
                ),
            ),
        )
