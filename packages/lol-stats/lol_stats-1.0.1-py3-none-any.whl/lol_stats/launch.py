import runpy
import sys


def launch(port=8126):

    sys.argv.append(str(port))

    runpy.run_module("program", run_name="__main__", alter_sys=True)



