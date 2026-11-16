"""Verify the workaround for the published driver's edge-setting behavior."""

import megabas
import pytest

from custom_components.smmegabas.driver_adapter import set_contact_count_edge


@pytest.mark.parametrize("old,new", [(3, 1), (3, 2), (1, 2), (2, 0), (0, 3)])
def test_edge_selection_clears_previous_bits(monkeypatch, old, new):
    registers = {
        megabas.I2C_MEM_DRY_CONTACT_RISING_ENABLE: old & 1,
        megabas.I2C_MEM_DRY_CONTACT_FALLING_ENABLE: (old >> 1) & 1,
    }

    class Bus:
        def read_byte_data(self, _address, register):
            return registers[register]

        def write_byte_data(self, _address, register, value):
            registers[register] = value

        def close(self):
            pass

    monkeypatch.setattr(megabas.smbus2, "SMBus", lambda _: Bus())
    set_contact_count_edge(0, 1, new)
    assert megabas.getContactCountEdge(0, 1) == new


def test_invalid_edge_does_not_change_settings(monkeypatch):
    writes = []
    monkeypatch.setattr(megabas, "setContactCountEdge", lambda *args: writes.append(args))
    with pytest.raises(ValueError, match="Invalid"):
        set_contact_count_edge(0, 1, 4)
    assert not writes
