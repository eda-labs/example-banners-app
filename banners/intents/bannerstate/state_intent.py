#!/usr/bin/env python3
from banners.api.v1alpha1.pysrc.bannerstate import BannerState
from banners.intents.bannerstate.init import init_globals_defaults, validate
from banners.intents.bannerstate.state_handlers import get_state_handler
from common.constants import PLATFORM_EDA
from utils.log import log_msg

EDA_DEBUG = False


def process_state_cr(cr):
    log_msg("BannerState CR:", debug=EDA_DEBUG, dict=cr)
    cr_obj = BannerState.from_input(cr)
    validate(cr_obj)
    init_globals_defaults(cr_obj)
    handler = get_state_handler(PLATFORM_EDA)
    handler.handle_cr(cr_obj)
