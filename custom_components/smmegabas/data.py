FULL_NAME="Building Automation"
LINK="https://sequentmicrosystems.com/products/building-automation-8-layer-stackable-hat-v4-for-raspberry-pi"

from . import driver_adapter
API = driver_adapter
DOMAIN = "smmegabas"
NAME_PREFIX = "smmb"
SM_MAP = {
    "button": {
        "watchdog_reload": {
            "chan_no": 1,
            "optional": True,
            "com": {"set": "wdtReload"},
        },
        "owb_scan": {
            "chan_no": 1,
            "optional": True,
            "com": {"set": "owbScan"},
        },
    },
    "select": {
        "contact_edge": {
            "chan_no": 4,
            "optional": True,
            "com": {"get": "getContactCountEdge", "set": "set_contact_count_edge"},
            "option_map": {"None": 0, "Rising": 1, "Falling": 2, "Both": 3},
        },
    },
    "datetime": {
        "rtc": {
            "chan_no": 1,
            "optional": True,
            "com": {"get": "rtcGet", "set": "rtcSet"},
        },
    },
    #"button": {
    #    "contact_cnt_rst": {
    #        "chan_no": 4,
    #        "com": {
    #            "set": "rstContactCounter",
    #        },
    #    }
    #},
    "binary_sensor": {
        "contact": {
            "chan_no": 4,
            "uom": "",
            "com": {
                "get": "getContactCh",
            },
        },
    },
    "sensor":  {
        "owb_count": {
                "chan_no": 1,
                "optional": True,
                "com": {"get": "owbGetSensorNo"},
        },
        "u_in": {
                "chan_no": 8,
                "uom": "V",
                "com": {
                    "get": "getUIn",
                },
        },
        "r1k": {
                "chan_no": 8,
                "uom": "kOwm",
                "com": {
                    "get": "getRIn1K",
                },
        },
        "r10k": {
                "chan_no": 8,
                "uom": "kOwm",
                "com": {
                    "get": "getRIn10K",
                },
        },
        "contact_cnt": {
                "chan_no": 4,
                "uom": "",
                "com": {
                    "get": "getContactCounter",
                },
        },
        "card_volt": {
                "chan_no": 1,
                "uom": "V",
                "com": {
                    "get": "getInVolt",
                },
        },
        "rasp_volt": {
                "chan_no": 1,
                "uom": "V",
                "com": {
                    "get": "getRaspVolt",
                },
        },
        "cpu_temp": {
                "chan_no": 1,
                "uom": "°C",
                "com": {
                    "get": "getCpuTemp",
                },
        }
    },
    "switch": {
        "triac": {
                "chan_no": 4,
                "com": {
                    "get": "getTriac",
                    "set": "setTriac",
                },
        }
    },
    "number": {
        "watchdog_period": {
                "chan_no": 1,
                "optional": True,
                "uom": "s",
                "min_value": 10,
                "max_value": 65000,
                "step": 1,
                "com": {"get": "wdtGetPeriod", "set": "wdtSetPeriod"},
        },
        "u_out": {
                "chan_no": 4,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "getUOut",
                    "set": "setUOut",
                },
        },
    },
}
