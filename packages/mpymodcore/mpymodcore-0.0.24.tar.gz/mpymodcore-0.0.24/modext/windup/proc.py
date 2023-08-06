"""
    (c)2020,2022 K. Goger - https://github.com/kr-g
    legal: https://github.com/kr-g/mpymodcore/blob/master/LICENSE
"""

from modcore.log import LogSupport

from modext.config import Namespace


class Processor(LogSupport):
    def __init__(self, windup, req, callid=None):
        LogSupport.__init__(self)

        self.windup = windup
        self.request_max_size = windup.request_max_size

        self.req_done = False
        self.callid = callid

        self.req = req
        self.run_iter = self.g_run()

    def g_run(self):
        # todo switch to fiber worker

        req = self.req

        yield

        req.load_request(self.windup.allowed)

        yield

        # when logging use argument list rather then
        # concatenate strings together -> performace
        self.info("request", req.request)
        self.info("request content len", len(req))

        request = req.request
        request.xargs = Namespace()

        for f in self.windup.headerfilter:
            rc = f.filterRequest(request)

            yield

        req.load_content(max_size=self.request_max_size)

        yield

        if req.overflow == True:
            # if bodydata is too big then no data is loaded automatically
            # dont run body filters automatically if max size exceeds
            # if a request contains more data the generator
            # needs to decide what to do in detail
            #
            # some req.x-fields are then not available !!!
            # because each filter sets them on its own !!!
            #
            self.warn("no auto content loading. size=", len(req))
            self.warn("not all req.x-fields area available")
        else:
            for f in self.windup.bodyfilter:
                f.filterRequest(request)

                yield

        self.info("xargs", request.xargs)

        # after auto cleanup with filter this can be None
        body = req.request.body
        if body != None:
            self.info("request content", body)

        for gen in self.windup.generators:
            req_done = gen.handle(req)

            yield

            if req_done:
                break

        #

        if req_done:
            self._after_run_done(req)
        else:
            self._after_run_undone(req)
            return

        yield

        while True:
            try:
                next(req.outbound)
                self.info("exec generator loop")
                yield
            except StopIteration:
                break
            except Exception as ex:
                self.excep(ex, "exec generator loop")
                break

        yield

        self.info("run post proc", self.callid)

        try:
            for f in self.windup.post_proc:
                f.filterRequest(request)

                yield

        except Exception as ex:
            self.excep(ex, "filter post-proc")

        self.req_done = True

        #

    def _after_run_done(self, req):
        pass

    def _after_run_undone(self, req):
        self.windup.call404(req)
        self.req_done = True

    def loop(self):
        if self.run_iter:
            try:
                next(self.run_iter)
            except StopIteration:
                self.run_iter = None

    def done(self):
        return self.req_done

    def stop(self):
        pass

    def kill(self, reason=None):
        pass

    def close(self):
        if self.req != None:
            self.req.close()
            self.req = None
