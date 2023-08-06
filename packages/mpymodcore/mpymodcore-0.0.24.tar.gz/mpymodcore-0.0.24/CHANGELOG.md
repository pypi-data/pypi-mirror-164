
# Changelog

for known issues and backlog refer to 
[`BACKLOG`](https://github.com/kr-g/mpymodcore/blob/master/BACKLOG.md)


## version v0.0.24 - 20220824

- refactored WindUp processor to generator functions
  - todo: switch to fiber worker
- smaller fixes
- file-api browser download option
- WindUp support for http PUT and DELETE methods with `Router` and `AuthRouter`
- updated ace editor to version 1.9.6
- 


- tested on micropython v18
  - it was reported that micropython causes crashes during startup from time to time
  - it was reported that micropython garbage collection does no wipe regulary
  - RECOMMANDATION: use micropython v16  


## version v0.0.23 - 20220623

- tested on micropython v18
- smaller fixes
- added simple pin based remote control module (sort of ascii terminal server)
  - [`term.py`](https://github.com/kr-g/mpymodcore/blob/master/mod3rd/terminal/term.py)
  - sample boot code under 
  [`terminal_port23_sample.py`](https://github.com/kr-g/mpymodcore/blob/master/samples/terminal_port23_sample.py)
  - supports authentication by adding a file `terminal.cfg` in the root folder of the device
  containing a single line with the password
    - **IMPORTANT: this supports no password encryption so far !!!**
  - **IMPORTANT: if the underlying Pin supports all i/o modes is NOT checked**
- added bmp280 support
  - modules for recording temperature and pressure
    - `mod3rd.tempr` - a modcore module for recording temerature and pressure data
    - `mod3rd.tempr_api` - a module for REST support, check dashboard regarding url endpoints
  - use project [`tempres`](https://github.com/kr-g/tempres) 
  to collect tempr data into a local folder and a sqlite database
-
    
    
## version v0.0.22 - 20211107 

- fix ntp module. auto reconnect only when wlan is available again
- network manager module for "known network settings" added. 
 to switch **manually** between networks without entering the password again.
 switching the network only works from soft-ap since the assigned (new) ip-address will be different. 
 the default ip and url with soft-ap is `http://192.168.4.1/admin/wlan`.
 the known network login info (ssid,password) is stored in a separate file in folder `/etc/network`.
 the mac of the wlan is used to build the filename since the ssid as such might be available
 also at different locations (but with a different password).
  - the admin wlan module under url `http://your-ip/admin/wlan` has now an additional col "known" 
   to indicate that it is a known network (identified by mac address)
- the file `wlan.cfg` can contain now 3 lines with:

        ssid
        password
        mac
    
  - where the last line with mac address is optional, but of course will be set automatically 
   when using the wlan admin tool.
  - all above will not remove the `wlan.cfg` file or disable a currently set up wlan connection.
- fix in simplicity `simple_esc_html()`
- 


## version v0.0.21 - 20210829

- change user password `http://your-ip/password` for session user
- fix save_user_password in security_store
- windup core fix cleaning up errored processors
- fix url link to editor in dashboard
- fix winter time in ntp_tz_cet handler
- mod3rd.admin_esp.softap loads now existing credits
- tested on micropython esp32spiram-20210623-v1.16.bin
- ace editor save/load indicator spinner (not really good looking, needs rework)
- reworked rest url extract module, now regex is cached
- 


## version v0.0.20

- html encoding in browser file api
- security sub system in AuthRouter can be enabled/disabled for bootstrapping a new device
  - user with role `root|sudo|admin` required to configure under `http://your-ip/admin/secsys`
- softap config `http://your-ip/admin/softap` implemented missing save feature
- 


## version v0.0.19

- global loglevel can preserved on flash
- logging reads log-level from `etc/log.cfg.txt`
- plugin url class for auto-discovery-configuration
- skeleton for `dashboard` module
- dashboard under `http://your-ip/main/#`
- added mime / media content-type header for WindUp
- `StaticFiles.send_file` now sends corresponding `Content-Type` and `Content-Length` in http response header 
- fix `moddev.wlan` activates wlan before scanning networks
- `send_json` response method sends `Content-Length`
- 


## version v0.0.18

- auto-discovery-configuration `__app__.apt_ext` can be a single Plugin, or a list of Plugin
- module `mod3rd.admin_esp.softap` for SoftAP configuration
- `start_auto_config` supports different timezone handler with `modext.misc.boot.set_timezone`
- auto-discovery-configuration (`ADC`) and `auto_config` loader sets the plugin `path_spec`
- modcore [`lifecycle hooks`](https://github.com/kr-g/mpymodcore/blob/master/modcore/lifecycle.py)
 for more flexible enhanced integration (also with asyncio). sample code in `boot.py`
- reworked
 [`modext.misc.main_async`](https://github.com/kr-g/mpymodcore/blob/master/modext/misc/main_async.py)
 regarding dev mode. cntrl+c and continue call to `run_loop(cfg)` now stable
- added [`modext.misc.async_mod.AsyncModule`](https://github.com/kr-g/mpymodcore/blob/master/modext/misc/async_mod.py)
 as glue for modcore modules and asyncio
- added sample module [`mod3rd.skeleton`](https://github.com/kr-g/mpymodcore/tree/master/mod3rd/skeleton)
 with auto-discovery-configuration for asyncio tasks
 (dynamic adding additional asyncio modules during startup)
- added cntrl+c (soft break) and continue looping support to `AsyncModule`
- 


## version v0.0.17

- fix `TZ_cet`, timezone support
- first draft of auto discovery and auto configuration and dynamic module loading
 for modules having an `__app__.py` file. sample code refer to `boot.py`
- limitation of auto discovery and auto configuration. works only for py not mpy files
- fix file api 
- `mod3rd.admin_esp.wlan` sorted list of available networks
- PEP8
- boot, and main loop redesign. `modext.misc.boot` ships generic boot code
 which can be use in own code, or as template base 
- sample code also in [`boot.py`](https://github.com/kr-g/mpymodcore/blob/master/boot.py)
- proper testing pending
- 


## version v0.0.16

- [ace editor](https://ace.c9.io/) under `mod3rd.admin_windup.editor` can handle now
 also large files > 4 kb. limitation: save blocks the global loop until save completed, no status or error information provided
  use browser console to view log info
- fix `get_http_chunk` reading portions of data chunks from current socket stream
- ace editor support for code beautify for html, css, js, json file types
- fiber worker and fiber worker loop are callable, can be written now as next(fbr) or fbr()
- [modext.misc.main_async](https://github.com/kr-g/mpymodcore/blob/master/modext/misc/main_async.py) 
 asyncio integration for (!!!)
  - modcore / modc
  - windup web server
- sample async startup code in
 [`boot.py`](https://github.com/kr-g/mpymodcore/blob/master/boot.py)
- 


## version v0.0.15

- `modcore.mod.Module` id is derived from class name when not set
- new ntp timezone handling and reloading.
 **important:** time aware modules need to register to event `"ntp"` in `Module.watching_events`
 and recalculate their schedule after new time was set
  - added `moddev.ntp.TZ_Support` for timezone handling with `ntp_serv`
  - added `moddev.ntp_tz_cet.TZ_cet` for central european time support
    - use this as a base for implementing other timezones
  - added `moddev.ntp_tz_serv` module for automatic timezone reloading
  - added sample code in `boot.py`
- `mod3rd.admin_esp.wlan` shows now more wifi information
- added module `mod3rd.admin_windup.content` which adds a new route
 `/admin/generators`. returns a json with all WindUp Routers, and url endpoints listed
- added module `mod3rd.admin_windup.file_api`. rest services for remote OS operations 
 regarding files and folders
- integrated [ace editor](https://ace.c9.io/) under `mod3rd.admin_windup.editor`,
 limitation: max edit file size 4096 bytes, no status or error information provided
  use browser console to view log info
  - sample code in `boot.py`, url is e.g.
  http://your-ip/admin/editor/#?file=/mod3rd/README.md
  - ace integration is EXPERIMENTAL and not tested in deep
- windup sends http status 405 when request method is not supported
- simple file and folder browser (in `file_api` module) with http://your-ip/admin/browser?path=...
- 


## version v0.0.14

- reworked WindUp fiber processing in request outboud part
- added `fibered` parameter to `send_json`, and `send_response` methods
- following objects are served fibered by default now, the total response time
 increased - in favor to overall reaction time of the system (default send_buffer size = 512 )
  - static files  
  - json responses 
- disabled fiber version 1 in windup
- changed `can_accept` timeout handling. the loop now executes faster.
- removed `proc_fiber.py` - old fiber windup processor
- fixed browser warning. added support for
 [same site cookie](https://developer.mozilla.org/de/docs/Web/HTTP/Headers/Set-Cookie/SameSite)
 this defaults to `LAX`
- improved fault tolerant connection handling due to fiberworker
 rework in windup outbound part
- 


## version v0.0.13

- fix: alarm clock exeption if not configured
- refactored Namespace from `modext.winup.proc` to `modext.config` module
- added nRF24L01+ HAL with IRQ support and sample master/slave driver under 
 [`modlib/nrf24l01p`](https://github.com/kr-g/mpymodcore/tree/master/modlib/nrf24l01p)
 sample code under samples folder
- added IRQSuspendCxt context manager class under `modext/irq`
- added simple fiber worker support to windup during closing the connection (250ms delay)
- added basic http functions as generator functions
- added `send_buffer` size parameter to `webserver.send_json` method
- 


## version v0.0.12

- variable `$id$` as part of ssid name in `softap.cfg` will be expanded to machine unique id
- intr Counter rework
- 


## version v0.0.11

- added __contains__ to Namespace. -> fix destorying windup session at the
 end of the request
- added `modext.irq` module for Interrupt and Counter handling
- base for [`mpymodcore_watering`](https://github.com/kr-g/mpymodcore_watering)
- 


## version v0.0.10

- added experimental template engine under
 [`mod3rd`](https://github.com/kr-g/mpymodcore/tree/master/mod3rd)
 current working name `Simplicity`. samples under
 [`samples/other3rd`](https://github.com/kr-g/mpymodcore/tree/master/samples/other3rd)
- fixed xpost group checking in `AuthRouter`, added samples
- added `IGNORE` option to [`TestRecorder`](https://github.com/kr-g/mpymodcore/tree/master/modext/testrecorder)
- added `TestRecoder.print()` for selective capturing content
- added code snipplet for websocket's under `samples/untested`
- moved `fiber channel/stream` to `modext.fiber_stream`
- moved `fiber worker` to `modext.fiber`
- fiber version 1 is marked as deprecated, will be slowly replaced by fiber worker
 (rename of fiber worker to fiber, and fiber loop resp.)
- addded `modext.config.Config` for json based configuration values
- added `modext.config.ReprDict` mixin which creates dict from __repr__ method,
 common usage is ReprDict -> dict -> json.dumps()
- added events `break` and `exit` to `moddev.control`
- moved loop from boot to `modext.misc.main` as generic optional module
-


## version v0.0.9

- reworked `Router` api: @get, @xget, @post and @xpost, so that accessing request
 parameter, and data needs less complex code
  - the function `args` parameter has changed __incompatible__ to the former versions!!!
  - the `args` parameter is now implemented as a namespace, meaning parameter can accessed without
    string quotations and using dict. here an example following
    [`REST`](https://en.wikipedia.org/wiki/Representational_state_transfer)
    having a [`Clean URL`](https://en.wikipedia.org/wiki/Clean_URL)
    
        @router.xget("/pin/:pin/:mode")
        def get_pin(req,args):
            
            # namespace access using args...
            # 
            logger.info( "sid cookie", args.cookies.sessionid )
            
            # probably a bit confusing, but looking on the cookie explains
            # why the sid is here at an other variable...
            logger.info("session_id", args.session.xsession_id )
            
            # log the rest args
            logger.info("rest parameter", args.rest )
            
            # keep the variable to avoid dict lookups -> performance
            rest = args.rest
            logger.info("pin", rest.pin )
            logger.info("mode", rest.mode )
            
            # avoid this -> dict lookup
            logger.info("mode", args.rest.mode )
            
            # do something else here...
            
            req.send_response( response="ok" )

  - the same applies to session, form, and json data
    - args.session [.session_variable]*
    - args.form [.form_field_name]
    - args.json [.attr_name]*
    
  - the 'old' method of accessing this data via `req.request.x[form|json|args|session]`
   is still possible, but will be removed in the future
    
- all `windup_*.py` [`samples`](https://github.com/kr-g/mpymodcore/blob/master/samples)
 have been updated 
  
- WindUp security hardening, user module, secure router with redirect/bad request response
  - added `AuthRouter` for checking permissions on role/group based access.
   the authentication data is saved under
   `/etc/shadow`.
   for each user 2 files are required.
   `_username_.pwd.txt`, and `_username_.grp.txt`. first contains the hashed password, and
   second contains the roles/groups the user belongs too. the roles are separeted by `:`.
   some sample code:
  
        from modext.windup_auth import AuthRouter

        secured_router = AuthRouter()

        @secured_router.get("/top-secret",groups=["admin"])
        def tops(req,args):
            req.send_response( response="ok, admin. you have permission" )

        @secured_router.get("/user-site",groups=["normaluser"])
        def tops(req,args):
            req.send_response( response="ok, buddy. you have permission" )
           
  - added one example [windup_security.py](https://github.com/kr-g/mpymodcore/blob/master/samples/windup_security.py). 
   there are 2 predefined users `test` and `admin`.
   by enter an invalid user name it fake's a session with no user / roles /groups, so that
   it possible to see how rejecting a request works.
   try the following URLs to play with it:
    - http://your-ip/login
    - http://your-ip/logout
    - http://your-ip/top-secret # only admin has permission
    - http://your-ip/user-site # only admin and test have permssion
  - important: there are no predefined roles/groups, and no default behaviour comes with it.
   the security sub-system only checks if a secured request is matching the user role/group.
   even the 2 example roles/groups in the sample `admin` and `normaluser` are just strings.
   e.g. the admin user has 2 roles/groups [assigned](https://github.com/kr-g/mpymodcore/tree/master/etc/shadow).
   these are: admin, and normaluser.
- added `mod3rd.admin_user.login` module. handling of URL `/login` and `/logout` with checking password.
 under `/etc/shadow` there are 3 sample user. `admin`,`test`, and `john` all password `test`
- added first draft for `Bluetooth®` [`GATT`](https://www.bluetooth.com/de/specifications/gatt/characteristics/)
 support under [`samples/untested`](https://github.com/kr-g/mpymodcore/tree/master/samples/untested)
   - sample for Broadcaster/Advertiser and GATT Server/ Peripheral, full
    roundtrip samples covering read, write, and notify with connected
    PC (testing done with `bluetoothctl`)
-


## version v0.0.8

- added `ntp-sync` event to ntp module, after sync was done sucessfully `ntp` event is raised
- added custom configurable event to fire to `moddev.interval`
 (see `boot.py` for `ntp-sync` event).
 e.g. with a few lines of code ntp sync can be triggered periodically 
- added module `moddev.control`. listens to events below:
  - `restart` values `[hard|modcore]`. hardreset, or restart all modcore modules (modc)
  - `status` values `[mem_0|mem_1|memfree]`. print the memory info
  - `gc` perform gc, print before, and after memory info
  - `pin`  control output pin, value data format `pinno:[on|off|toggle]`
- added `EventEmitter` as base class for `Interval`
  - evaluates id:event in config, and fires this. whereas event value can be also a list of strings
- added `AlarmClock` for defined alarm handling (once a day), with optional raising an event
- ntp module fires `ntp` now also after timezone change
- added `Button` for button optional with sending event. supports debouncing
- Button can emit event direclty by pressing, or when released (default)
- added `AlarmCounter` check upper and lower bounds, fires optional event
- moved global `SessionStore` to module `session`, added `session_mod` serving event `session-man`
 which purges all the expired sessions. can be triggered together with `Inverval` periodically
 - fix socket close after 404
 - added `switch` to [`FiberWorker`](https://github.com/kr-g/mpymodcore/blob/master/samples/untested/fiber_worker.py)
  as simple approach for scheduling and balancing workload to a given overall system reaction time
- added `sleep_ms` and `waitfor_ms` to `FiberWorker`
- added new samples in [`samples`](https://github.com/kr-g/mpymodcore/blob/master/samples)
 and in [`boot.py`](https://github.com/kr-g/mpymodcore/blob/master/boot.py) see config section
- fiber worker can spawn now into a different workerloop for execution (e.g. loop with higher prio)
- 


## version v0.0.7

- reworked fiber samples
- FibreWatchdog timer exposed
- custom HTML 404 handling
- simple admin html app for wlan (in unsupported mod3rd folder, not on pypi)
- wlan module rework, scan added, reconnect, `wlan-restart` event
- package redesign, allowing to run simple web based app (e.g. single status page) 
 on smaller devices (ESP8266) too
- new package `modext.http` containing basic request handling func
- new package `modext.windup`, move code out of webserv (which is not available any more)
- moved `fiber` from `modcore` to `modext.fiber` package
- removed WindUp request processing from loop to Processor class
- added fiber processor class, to allow WindUp to work in non-fiber-mode
- added [`fiber worker`](https://github.com/kr-g/mpymodcore/blob/master/samples/untested/fiber_worker.py)
 under new concepts/ untested in samples
- added [`fiber channel/stream`](https://github.com/kr-g/mpymodcore/blob/master/samples/untested/fiber_channel.py)
 under new concepts/ untested in samples
- added [`TestRecorder`](https://github.com/kr-g/mpymodcore/blob/master/modext/testrecorder/testrecorder.py) 
 for testing complex scenarios with id() tracking, approach as simple as `doctest`.
 see [`trec.txt`](https://github.com/kr-g/mpymodcore/blob/master/modext/testrecorder/testrecorder.trec.txt) file.
 __limitation__: not running under micropython as of now
- 


## version v0.0.6

- set_cookie path parameter
- url path filter decode %20 as space
- redirect http request
- fix REST xurl
- WindUp as included web server
- moved samples to own folder
- added ssl suppport (ussl.wrap_socket callback after accept in class WebServer and WindUp)
- 


## version v0.0.5

- added Guard, Detachable, and FiberContext in
 [`fiber`](https://github.com/kr-g/mpymodcore/blob/master/modext/fiber/core.py)
 module
- added fiber samples
- added performance counters to fiber loop
- added send_head and send_data to webserver RequestHandler
- added fiber, and fiberloop processing to
 [`serve.py`](https://github.com/kr-g/mpymodcore/blob/master/modext/webserv/serve.py)
 sample webserver 
- added send json response
-


## version v0.0.4 

- support for long running tasks (without asyncio) with
 [`fiber`](https://github.com/kr-g/mpymodcore/blob/master/modext/fiber/core.py)
 (wrapper around performance optimized generator functions)
- FormDataDecodeFilter for decoding "%" chars in form data


## version v0.0.3

- router with url root parameter
- extra slashes dense for path
- send chunks buffer for static file
- content generator supports py-generator functions
- some more code samples
- changed license to dual licensed
- rest style urls with url variables with @xget and @xpost decorators
- simple session manager (in-memory)
- 


## version v0.0.2

- fixed event name to lower case during fire_event
- added timeout class
- changed event model
- added ifconfig() to softap and wlan
- added minimalistic webserver under modext
- added url filtering for path, query, and parameter
- added simple static content generator
- added cookie filter
- changed package structure
- added index file handling
- added set_cookie()
- added simple router
- changed logging, support check of log level
- addded body content filter for decode
- added json parser filter
- added form data filter

