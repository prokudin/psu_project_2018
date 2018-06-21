# -*- coding: utf-8 -*-
from argparse import Namespace
import fitpack  # This import is needed even though not explicitly referenced.
from fitlab.resman import RESMAN
from fitlab.mcsamp import MCSAMP
from fitlab.maxlike import ML
from fitlab.speedtest import SPEEDTEST
from tools.config import conf, load_config


def conf_run(task=None, noexit=True):
    if task is None:
        task = conf["args"].task

    if noexit:
        conf["screen mode"] = "please don't sys.exit"

    conf["resman"] = RESMAN(conf)

    if task == 0:
        SPEEDTEST().run()
    elif task == 1:
        ML().run_minimize()
    elif task == 2:
        ML().run_leastsq()
    elif task == 3:
        MCSAMP().run_nest()
    elif task == 4:
        MCSAMP().run_imc()
    elif task == 5:
        MCSAMP().analysis()
    elif task == 6:
        MCSAMP().simulation()
    elif task == 7:
        MCSAMP().simulation2()
    else:
        raise ValueError("task must be in range(8)")


def gen_config(file="", task=0, runid=0, reaction="sidis"):
    args = Namespace(
        config=file,
        task=task,
        runid=runid,
        file=file,
        reaction=reaction
    )

    load_config(file)
    conf["args"] = args


if __name__ == "__main__":
    # conf = gen_config("../inputs/upol_hermes_noevolution.py", task=2)
    gen_config("../inputs/upol_hermes_alexei.py", task=2)
    conf_run(noexit=False)
