"""
    (c)2020,2022 K. Goger - https://github.com/kr-g
    legal: https://github.com/kr-g/mpymodcore/blob/master/LICENSE
"""

from modcore.log import LogSupport, logger

try:
    # from modext.fiber import FiberLoop, Fiber
    from modext.fiber.fiber_worker import FiberWorkerLoop, FiberWorker
except:
    logger.warn("fiber module not loaded")

from modext.http.http_func import NotAllowedException
from modext.http.webserv import WebServer, COOKIE_HEADER, SET_COOKIE_HEADER

from .filter import *
from .content import StaticFiles
from .router import Router
from .session import store

from .proc import Processor


class WindUp(LogSupport):
    def __init__(self, wrap_socket=None, suppress_id=False):
        LogSupport.__init__(self)
        self.suppress_id = suppress_id
        self.ws = WebServer(wrap_socket=wrap_socket, suppress_id=suppress_id)
        self._set_default()
        self._exec_iter = self._g_run_exec()

    def _set_default(self):
        self.headerfilter = self.headerfilter_default()
        self.bodyfilter = self.bodyfilter_default()
        self.generators = self.generators_default()
        self.post_proc = self.post_proc_default()

        self.allowed = ["GET", "POST", "PUT", "DELETE"]

        self.html404 = None

        self.exec_class = Processor
        self.exec_close_delay = None

        self.accept_timeout = 153
        self.request_max_size = 4096

        self.calls = 0
        self.exec = []

        # self.send_buffer_size = 512

        # outbound processing fiber loop
        self._outbound = FiberWorkerLoop()
        # windup serves the outbound loop within his own loop
        self.run_outbound_loop = True
        ## todo
        # self.run_outbound_loop_ha = False

    def start(self, generators=None):
        self.ws.start()
        self.info("listening on", self.ws.addr)
        if generators:
            self.generators.extend(generators)

    def stop(self):
        self.ws.stop()
        for e in self.exec:
            e.kill("stop")
            e.close()
        self.exec = []

    def headerfilter_default(self):
        # depending on app needs filter are added, or left out
        headerfilter = [
            # keep them at the top
            CookieFilter(),
            store.pre_filter(),
            # keep them together
            PathSplitFilter(),
            XPathDecodeFilter(),
            XPathSlashDenseFilter(),
            ParameterSplitFilter(),
            ParameterValueFilter(),
            ParameterPackFilter(),
            ParameterDenseFilter(),
            #
        ]
        return headerfilter

    def bodyfilter_default(self):
        bodyfilter = [
            BodyTextDecodeFilter(),
            JsonParserFilter(),
            FormDataFilter(),
            FormDataDecodeFilter(),
        ]
        return bodyfilter

    def generators_default(self):
        generators = [
            StaticFiles(["/www"]),
        ]
        return generators

    def post_proc_default(self):
        post_proc = [
            store.post_filter(),
        ]
        return post_proc

    def supported_methods(self):
        allowed = set()
        for g in self.generators:
            if isinstance(g, Router):
                mlist = g.supported_methods()
                allowed.update(mlist)
        return list(allowed)

    def loop(self):

        req = None
        exec = None
        try:
            if self.ws.can_accept():

                self.info("new-request")
                req = self.ws.accept(timeout=self.accept_timeout)
                self.calls += 1

                req.windup = self

                # create processor
                exec = self.exec_class(self, req, callid=self.calls)
                self.exec.append(exec)

        except Exception as ex:
            self.excep(ex, "accept-processor")

            if req:
                req.close()
            return

        if self.run_outbound_loop:
            # exec fiber loop
            try:
                self.run_outbound()
            except Exception as ex:
                self.excep(ex, "fiber outbound")

        self._run_exec()

    def _run_exec(self):
        next(self._exec_iter)

    def _g_run_exec(self):

        yield

        while True:

            if len(self.exec) == 0:
                yield

            for e in self.exec:
                # todo move to own fiber worker ?
                try:

                    self.info("pending exec", e.callid, "total", len(self.exec))
                    e.loop()

                    yield

                    if e.done() == True:
                        self.exec.remove(e)
                        self.prepare_close(e)

                except Exception as ex:
                    self.excep(ex, "callid", e.callid)

                    e.kill("proc-fail")
                    self.exec.remove(e)
                    req = e.req

                    if isinstance(ex, NotAllowedException):
                        req.send_response(status=405)  # not allowed http status

                    if isinstance(ex, FilterException):
                        # failed in early stage
                        # for later stage (generator) content and header
                        # are already send, just close the socket then
                        req.send_response(status=400)

                    e.close()

    def run_outbound(self):
        self._outbound.release()
        if len(self._outbound) > 0:
            self._outbound()

    def prepare_close(self, exec):
        delay = self.exec_close_delay

        def close_func(self):
            # delay closing the socket
            if delay != None and delay > 0:
                yield from self.sleep_ms(delay)
            yield
            exec.close()
            self.info("exec processor closed")
            yield

        fbr = FiberWorker(func=close_func)
        self._outbound.append(fbr)

        self.info("exec scheduled for done", exec.callid, type(exec))

    def call404(self, req):
        self.warn("not found 404", req.request.xpath)
        if self.html404 == None:
            req.send_response(
                status=404,
            )
        else:
            # custom 404 page
            # req gets destructed by next round
            self.html404(req)
