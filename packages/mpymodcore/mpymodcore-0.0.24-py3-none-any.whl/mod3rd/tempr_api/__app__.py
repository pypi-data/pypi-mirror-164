import os
import json

from modext.auto_config.ext_spec import Plugin

from modcore.log import logger

from modext.windup import WindUp, Router

from mod3rd.tempr.temprec import temp_rec

router = Router("/tempr")


PAGE_SIZE = 5


@router.get("/all")
def get_all(req, args):
    data = list(temp_rec.iter_rec())
    total = len(data)
    page = 0
    try:
        page = int(args.param.page)
        pos = PAGE_SIZE * page
        data = data[pos : pos + PAGE_SIZE + 1]
    except Exception as ex:
        pass

    if len(data) > PAGE_SIZE:
        data = data[0:PAGE_SIZE]

    data = {
        "files": data,
        "total": total,
        "page": page,
        "pages": int(total / PAGE_SIZE) + int(total % PAGE_SIZE > 0),
    }
    logger.info(data)
    req.send_json(data)


@router.get("/measure")
def measure(req, args):
    now, tempr, press = temp_rec.measure()
    data = temp_rec.pack(now, tempr, press)
    logger.info(data)
    req.send_json(data)


@router.get("/measure_save")
def measure_save(req, args):
    now, tempr, press = temp_rec.measure_save()
    data = temp_rec.pack(now, tempr, press)
    logger.info(data)
    req.send_json(data)


@router.get("/pop")
def tempr_pop(req, args):
    data = temp_rec.pop_rec()
    req.send_json(data)


class TemprApi(Plugin):
    def __init__(self):
        super().__init__()
        self.caption = "Temperature and Pressure Api"
        self.path_spec = "mod3rd.tempr_api"
        self.generators = [
            router,
        ]
        self.url_caption_tuple_list = [
            (router.root + "/measure", None),
            (router.root + "/measure_save", None),
            (router.root + "/all", None),
            (router.root + "/pop", None),
        ]


app_ext = TemprApi()
