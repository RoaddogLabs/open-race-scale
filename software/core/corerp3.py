import sys
import time
from core.loadcell import LoadCell
from core.scaledata import ScaleData


class ScaleControl:
    def __init__(self, interface=None, simulate=False):
        self.interface = interface
        self.load_cells = {'FL': LoadCell(4, 5, simulate=simulate),
                           'FR': LoadCell(4, 5, simulate=simulate),
                           'RL': LoadCell(4, 5, simulate=simulate),
                           'RR': LoadCell(4, 5, simulate=simulate)}

        self.scale_data = {'FL': ScaleData('FL'),
                           'FR': ScaleData('FR'),
                           'RL': ScaleData('RL'),
                           'RR': ScaleData('RR'),
                           'TOTAL': ScaleData('TOTAL', calculated=True)}

    def update(self):
        # get weights from the load cell interface
        self._get_weights()

        # calculate the total weight of all load cells
        self._calculate_total()

        # update the corner weights; always calculate total before updating corner weights
        for k in self.load_cells:
            self._calculate_corner(k)

        # TODO do all weight and percentage calculations here

        print('FL: ' + str(self.load_cells['FL']),
              'FR: ' + str(self.load_cells['FR']),
              'RL: ' + str(self.load_cells['RL']),
              'RR: ' + str(self.load_cells['RR']))

    def _get_weights(self):
        for k, v in self.load_cells.items():
            v.get_measure()

    def _calculate_total(self):
        total_weight = 0
        self.scale_data['TOTAL'].percent = 100
        for k, v in self.load_cells.items():
            total_weight += v.weight
        self.scale_data['TOTAL'].weight = total_weight
        return total_weight

    def _calculate_corner(self, identifier):
        self.scale_data[identifier].weight = self.load_cells[identifier].weight
        corner_weight = self.scale_data[identifier].weight
        corner_percent = (corner_weight / self.scale_data['TOTAL'].weight) * 100
        return corner_weight, corner_percent

    def _send_data(self):
        # TODO finish bluetooth implementation so that scale data can be sent to clients
        if self.interface is not None:
            self.interface.send(str(self.scale_data))


if __name__ == '__main__':
    """
    If the core is run by itself then it is headless and needs to set up a BT server for clients to read, conversely if
    the core is run by the local GUI, then the GUI will access the scale controller directly and BT is not started
    """
    # TODO in future the bluetooth server should always be started, then data can be accessed by a client even if local
    # TODO GUI is running. Another option is to always have a local GUI

    import RPi.GPIO as GPIO
    from core.btserver import BluetoothServer
    sc = ScaleControl(BluetoothServer())

    while True:

        try:
            sc.update()
            time.sleep(1)

        except (KeyboardInterrupt, SystemExit):
            GPIO.cleanup()
            sys.exit()
