import os
from dataclasses import dataclass

def get_board_path(board_name=None):
    return os.path.join(os.path.dirname(__file__), board_name) if board_name else os.path.dirname(__file__)

def get_proto_board_data():
    return str(os.path.join(os.path.dirname(__file__), 'boards.yaml'))

@dataclass(frozen=True)
class TPBoardConfig():
    board_config = {
        'DM320118': {
            'vendor_id': 1003,
            'debugger_pid': 8465,
            'application_pid': 8978,
            'serial_series': 'MCHP3311',
            'kitname': 'CryptoAuth Trust Platform',
            'product_string': 'CryptoAuth Trust Platform',
            'mcu_part_number': 'ATSAMD21E18A',
            'program_tool': 'nEDBG'
            }
    }

@dataclass(frozen=True)
class PIC32CMLSBoardConfig():
    board_config = {
        'EV76R77A': {
            'vendor_id': 1003,
            'debugger_pid': 8465,
            'application_pid': 8978,
            'serial_series': 'MCHP3383',
            'kitname': 'PIC32CMLS60 Curiosity Pro',
            'product_string': 'CryptoAuth LS60',
            'mcu_part_number': '32CM5164LS60100',
            'program_tool': 'EDBG'
            }
    }

__all__ = ['get_board_path', 'get_proto_board_data', 'TPBoardConfig', 'PIC32CMLSBoardConfig']
