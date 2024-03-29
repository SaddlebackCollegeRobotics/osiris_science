from science_clients.water_pump_client import WaterPumpClient
from science_clients.vacuum_client import VacuumClient
from science_clients.funnel_cake_client import FunnelCakeClient


class FunnelCake(object):
    def __init__(self):
        self.funnel_index = 1
        self.funnel_list_prev_index = 0
        self.funnel_list = {1: False,
                            2: False,
                            3: False,
                            4: False,
                            5: False}

        self.water_pump_on = False
        self.vacuum_on = False

        self.funnel_cake_client = FunnelCakeClient()
        self.water_pump_client = WaterPumpClient()
        self.vacuum_client = VacuumClient()

    def rotate_funnel_index(self, index):
        self.funnel_list_prev_index = self.funnel_index
        self.funnel_index = index
        if self.funnel_index == 6:
            self.funnel_index = 1

    def get_funnel_list(self) -> dict:
        return self.funnel_list

    def turn_funnel_pump_on(self):
        self.funnel_list[self.funnel_index] = True
        self.funnel_list[self.funnel_list_prev_index] = False

    def turn_water_pump_on(self):
        self.water_pump_on = True
        self.water_pump_client.send_request(self.water_pump_on)
        self.water_pump_client.run_node()

    def turn_water_pump_off(self):
        self.water_pump_on = False
        self.water_pump_client.send_request(self.water_pump_on)
        self.water_pump_client.run_node()

    def turn_vacuum_on(self):
        self.vacuum_on = True
        self.vacuum_client.send_request(self.vacuum_on)
        self.vacuum_client.run_node()

    def turn_vacuum_off(self):
        self.vacuum_on = False
        self.vacuum_client.send_request(self.vacuum_on)
        self.vacuum_client.run_node()

    def close(self):
        self.funnel_cake_client.destroy_node()
        self.water_pump_client.destroy_node()
        self.vacuum_client.destroy_node()
