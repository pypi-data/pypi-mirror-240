import asyncio

from dbus_next import BusType, Variant
from dbus_next.aio import MessageBus
from dbus_next.service import ServiceInterface, method

from qtoggleserver import startup


BUS_NAME = 'org.bluez'
PROPERTIES_IFACE = 'org.freedesktop.DBus.Properties'
DEVICE_IFACE = 'org.bluez.Device1'
AGENT_PATH = '/io/qtoggle/agent'
AGENT_IFACE = 'org.bluez.Agent1'
AGENT_MANAGER_IFACE = 'org.bluez.AgentManager1'
AGENT_MANAGER_PATH = '/org/bluez'
CAPABILITY = 'KeyboardDisplay'
ADAPTER_PATH = '/org/bluez/hci0'
ADAPTER_IFACE = 'org.bluez.Adapter1'


class Agent(ServiceInterface):
    def __init__(self, bus: MessageBus) -> None:
        super().__init__(AGENT_IFACE)

        self.bus: MessageBus = bus

    async def set_trusted(self, path: str) -> None:
        introspection = await self.bus.introspect(BUS_NAME, path)
        obj = self.bus.get_proxy_object(BUS_NAME, path, introspection)
        props = obj.get_interface(PROPERTIES_IFACE)
        await props.call_set(DEVICE_IFACE, 'Trusted', Variant('b', True))

    @method()
    def Release(self) -> None:
        print('Release')

    @method()
    def Cancel(self) -> None:
        print('Cancel')

    @method()
    def AuthorizeService(self, device: 'o', uuid: 's') -> None:
        print('AuthorizeService %s %s', device, uuid)

    @method()
    def RequestPinCode(self, device: 'o') -> None:
        print('RequestPinCode %s', device)
        return '1234'

    @method()
    def RequestConfirmation(self, device: 'o', passkey: 'u') -> None:
        print('DisplayConfirmation %s %s', device, passkey)

    @method()
    def RequestAuthorization(self, device: 'o') -> None:
        print('RequestAuthorization %s', device)

    @method()
    async def RequestPasskey(self, device: 'o') -> 'u':
        print('RequestPasskey %s', device)
        await self.set_trusted(device)
        return 1234

    @method()
    def DisplayPasskey(self, device: 'o', passkey: 'u', entered: 'q') -> None:
        print('DisplayPasskey %s %s %s', device, passkey, entered)

    @method()
    def DisplayPinCode(self, device: 'o', pincode: 's') -> None:
        print('DisplayPinCode %s %s', device, pincode)


async def setup_adapter(bus: MessageBus) -> None:
    introspection = await bus.introspect(BUS_NAME, ADAPTER_PATH)
    obj = bus.get_proxy_object(BUS_NAME, ADAPTER_PATH, introspection)
    props = obj.get_interface(PROPERTIES_IFACE)
    await props.call_set(ADAPTER_IFACE, 'DiscoverableTimeout', Variant('u', 0))
    await props.call_set(ADAPTER_IFACE, 'Discoverable', Variant('b', True))
    await props.call_set(ADAPTER_IFACE, 'PairableTimeout', Variant('u', 0))
    await props.call_set(ADAPTER_IFACE, 'Pairable', Variant('b', True))


async def setup_agent(bus: MessageBus) -> None:
    agent = Agent(bus)
    bus.export(AGENT_PATH, agent)

    introspection = await bus.introspect(BUS_NAME, AGENT_MANAGER_PATH)
    obj = bus.get_proxy_object(BUS_NAME, AGENT_MANAGER_PATH, introspection)
    agent_manager_obj = obj.get_interface(AGENT_MANAGER_IFACE)

    await agent_manager_obj.call_register_agent(AGENT_PATH, CAPABILITY)
    await agent_manager_obj.call_request_default_agent(AGENT_PATH)


async def main():
    startup.parse_args()
    startup.init_settings()
    startup.init_logging()
    startup.init_signals()
    startup.init_tornado()

    bus = await MessageBus(bus_type=BusType.SYSTEM).connect()
    await setup_adapter(bus)
    await setup_agent(bus)

    await asyncio.sleep(10000)


asyncio.get_event_loop().run_until_complete(main())
