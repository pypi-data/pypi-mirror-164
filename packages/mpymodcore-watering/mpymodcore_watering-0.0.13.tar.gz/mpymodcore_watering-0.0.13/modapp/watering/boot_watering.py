# This file is executed on every boot (including wake-boot from deepsleep)


from modext.misc.boot import *


# basic configuration

cfg = {
    "TZ": 60 * 60 * 2,  # ntp, better use ntp_tz_serv, TZ_cet classes
    "SD_SLOT": 3,  # default for esp32 with psram / TTGO
    "SD_PATH": "/sd",
    # this is a variable what can be referenced!
    # led pin for ttgo board
    "led": 21,
}


from moddev.interval import Interval

cfg.update(
    {
        "int_ntp": 15,
        "int_ntp:timebase": 1000 * 60,  # 1 min timebase
        "int_ntp:event": "ntp-sync",  # event to fire
    }
)

int_ntp = Interval("int_ntp")
modc.add(int_ntp)

cfg.update(
    {
        "session_purge": 30,
        "session_purge:timebase": 1000 * 60,  # 1 min timebase
        "session_purge:event": "session-man",  # event to fire
    }
)

session_purge = Interval("session_purge")
modc.add(session_purge)

cfg.update(
    {
        "run_gc": 15,
        "run_gc:timebase": 1000 * 60,  # 1 min timebase
        "run_gc:event": "gc",  # event to fire
    }
)

run_gc = Interval("run_gc")
modc.add(run_gc)

cfg.update(
    {
        "live_ping": 5,  # timeout in sec, default timebase 1000
        "live_ping:event": ["pin:led:toggle"],  # access led parameter from cfg
    }
)

live_ping = Interval("live_ping")
modc.add(live_ping)


from moddev.button import Button

cfg.update(
    {
        "boot_btn": 0,  # pin no -> gpio 0
        "boot_btn:debounce": 100,  # 100ms - default, can be obmitted
        "boot_btn:neg_logic": True,  # boot button gpio0 becomes signaled with value 0 by pressing
        "boot_btn:fire_on_up": True,  # default, fires when releasing
        "boot_btn:event": [
            "pin:led:off",
            "break",
        ],  # raise 2 events
    }
)

boot_btn = Button("boot_btn")
modc.add(boot_btn)

# use this when using temperature and pressure recording
cfg.update(
    {
        "tempr_timeout": 15,
        "tempr_timeout:timebase": 1000 * 60,  # 1 min timebase
        "tempr:addr": 0x76,
        "tempr:scl": 15,
        "tempr:sda": 13,
        "tempr:freq": 400000,
        "tempr_sd_relative": False,
    }
)


# configure
cfg_loader = start_auto_config()

# add all modules before this call
start_modcore(config=cfg)

logger.info("modcore config done. start windup.")


# this is located in modext.misc.boot
# add additional routers
generators.extend(
    [
        # empty
    ]
)

start_windup()

# give some hints
# print_main_info()
print("")
print("call loop() to start")
print("")


def loop():
    loop_async(cfg)


# uncomment in production
# loop()
