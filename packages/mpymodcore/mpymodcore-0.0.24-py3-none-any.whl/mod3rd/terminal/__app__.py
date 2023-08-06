from modcore import modc, LifeCycle

from modext.misc.async_mod import asyncio, AsyncModule, AsyncSkeletonModule
from modext.auto_config.ext_spec import Plugin

from mod3rd.terminal.term import *


mod_async_terminal = AsyncModule(id="terminal")


@mod_async_terminal.hook(LifeCycle.LOOP, before=True)
def before_loop_run(self):
    self.info("before loop hook called")
    # important !!!
    self.create_task(term_task)
    self.info("terminal async task created", self.atask)


@mod_async_terminal.hook(LifeCycle.LOOP, after=True)
def after_loop_run(self):
    self.info("after loop hook called")
    self.cancel_task()
    self.info("terminal async task prepared cancelation")


modc.add(mod_async_terminal)


# this does nothing since the sample do not provide custom generators for WindUp
class TerminalAsync_plugin(Plugin):
    def __init__(self):
        super().__init__()
        self.caption = "Terminal asyncio module"
        ## todo remove
        self.path_spec = "mod3rd.terminal"
        # self.generators = []
        # self.url_caption_tuple_list = []


app_ext = [TerminalAsync_plugin()]
