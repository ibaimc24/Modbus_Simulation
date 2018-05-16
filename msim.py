from configparser import ConfigParser


def load_configuration():

    config = ConfigParser()
    config.read('Modbus-simulator.conf')


load_configuration()