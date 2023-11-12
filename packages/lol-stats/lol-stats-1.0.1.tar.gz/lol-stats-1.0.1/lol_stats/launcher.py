import os
import runpy
import sys

def launch(port=8126):
    os.environ['LOL_STATS_PORT'] = str(port)

    runpy.run_module("lol_stats.program", run_name="__main__", alter_sys=True)



