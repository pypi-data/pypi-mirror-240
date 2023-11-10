# coding: UTF-8
import sys
bstack11111_opy_ = sys.version_info [0] == 2
bstack1lllll1l_opy_ = 2048
bstack1ll_opy_ = 7
def bstack111ll_opy_ (bstack111ll1l_opy_):
    global bstack1l1l11l_opy_
    bstack11ll1l_opy_ = ord (bstack111ll1l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack111ll1l_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack1ll11l1_opy_)
    bstack1l1l1ll_opy_ = bstack1ll11l1_opy_ [:bstack1lllll1_opy_] + bstack1ll11l1_opy_ [bstack1lllll1_opy_:]
    if bstack11111_opy_:
        bstack11llll_opy_ = unicode () .join ([unichr (ord (char) - bstack1lllll1l_opy_ - (bstack111llll_opy_ + bstack11ll1l_opy_) % bstack1ll_opy_) for bstack111llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack11llll_opy_ = str () .join ([chr (ord (char) - bstack1lllll1l_opy_ - (bstack111llll_opy_ + bstack11ll1l_opy_) % bstack1ll_opy_) for bstack111llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack11llll_opy_)
import os
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from urllib.parse import urlparse
from datetime import datetime
from bstack_utils.constants import bstack1l1ll11lll_opy_ as bstack1l1lllllll_opy_
from bstack_utils.helper import bstack1lll1111l1_opy_, bstack1l1l11l1l_opy_, bstack1l1ll1ll11_opy_, bstack1l1ll1l111_opy_, bstack1ll1ll1l1_opy_, get_host_info, bstack1l1lll1lll_opy_, bstack1ll1l111_opy_, bstack1l1lll11ll_opy_
from browserstack_sdk._version import __version__
logger = logging.getLogger(__name__)
@bstack1l1lll11ll_opy_(class_method=False)
def _1l1lll1l1l_opy_(driver):
  response = {}
  try:
    caps = driver.capabilities
    response = {
        bstack111ll_opy_ (u"ࠫࡴࡹ࡟࡯ࡣࡰࡩࠬ಴"): caps.get(bstack111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫವ"), None),
        bstack111ll_opy_ (u"࠭࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠪಶ"): caps.get(bstack111ll_opy_ (u"ࠧࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠩಷ"), None),
        bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡡࡱࡥࡲ࡫ࠧಸ"): caps.get(bstack111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧಹ"), None),
        bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠬ಺"): caps.get(bstack111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠬ಻"), None)
    }
  except Exception as error:
    logger.debug(bstack111ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺಼ࠡࠩ") + str(error))
  return response
def bstack111ll1ll1_opy_(config):
  return config.get(bstack111ll_opy_ (u"࠭ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾ࠭ಽ"), False) or any([p.get(bstack111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧಾ"), False) == True for p in config[bstack111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫಿ")]])
def bstack111llllll_opy_(config, bstack111llll1l_opy_):
  try:
    if not bstack1l1l11l1l_opy_(config):
      return False
    bstack1l1llllll1_opy_ = config.get(bstack111ll_opy_ (u"ࠩࡤࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠩೀ"), False)
    bstack1l1lll11l1_opy_ = config[bstack111ll_opy_ (u"ࠪࡴࡱࡧࡴࡧࡱࡵࡱࡸ࠭ು")][bstack111llll1l_opy_].get(bstack111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠫೂ"), None)
    if bstack1l1lll11l1_opy_ != None:
      bstack1l1llllll1_opy_ = bstack1l1lll11l1_opy_
    bstack1l1llll1l1_opy_ = os.getenv(bstack111ll_opy_ (u"ࠬࡈࡓࡠࡃ࠴࠵࡞ࡥࡊࡘࡖࠪೃ")) is not None and len(os.getenv(bstack111ll_opy_ (u"࠭ࡂࡔࡡࡄ࠵࠶࡟࡟ࡋ࡙ࡗࠫೄ"))) > 0 and os.getenv(bstack111ll_opy_ (u"ࠧࡃࡕࡢࡅ࠶࠷࡙ࡠࡌ࡚ࡘࠬ೅")) != bstack111ll_opy_ (u"ࠨࡰࡸࡰࡱ࠭ೆ")
    return bstack1l1llllll1_opy_ and bstack1l1llll1l1_opy_
  except Exception as error:
    logger.debug(bstack111ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡸࡨࡶ࡮࡬ࡹࡪࡰࡪࠤࡹ࡮ࡥࠡࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡦࡴࡵࡳࡷࠦ࠺ࠡࠩೇ") + str(error))
  return False
def bstack1l1lll1ll1_opy_(bstack1l1ll1l1l1_opy_, test_tags):
  bstack1l1ll1l1l1_opy_ = os.getenv(bstack111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫೈ"))
  if bstack1l1ll1l1l1_opy_ is None:
    return True
  bstack1l1ll1l1l1_opy_ = json.loads(bstack1l1ll1l1l1_opy_)
  try:
    include_tags = bstack1l1ll1l1l1_opy_[bstack111ll_opy_ (u"ࠫ࡮ࡴࡣ࡭ࡷࡧࡩ࡙ࡧࡧࡴࡋࡱࡘࡪࡹࡴࡪࡰࡪࡗࡨࡵࡰࡦࠩ೉")] if bstack111ll_opy_ (u"ࠬ࡯࡮ࡤ࡮ࡸࡨࡪ࡚ࡡࡨࡵࡌࡲ࡙࡫ࡳࡵ࡫ࡱ࡫ࡘࡩ࡯ࡱࡧࠪೊ") in bstack1l1ll1l1l1_opy_ and isinstance(bstack1l1ll1l1l1_opy_[bstack111ll_opy_ (u"࠭ࡩ࡯ࡥ࡯ࡹࡩ࡫ࡔࡢࡩࡶࡍࡳ࡚ࡥࡴࡶ࡬ࡲ࡬࡙ࡣࡰࡲࡨࠫೋ")], list) else []
    exclude_tags = bstack1l1ll1l1l1_opy_[bstack111ll_opy_ (u"ࠧࡦࡺࡦࡰࡺࡪࡥࡕࡣࡪࡷࡎࡴࡔࡦࡵࡷ࡭ࡳ࡭ࡓࡤࡱࡳࡩࠬೌ")] if bstack111ll_opy_ (u"ࠨࡧࡻࡧࡱࡻࡤࡦࡖࡤ࡫ࡸࡏ࡮ࡕࡧࡶࡸ࡮ࡴࡧࡔࡥࡲࡴࡪ್࠭") in bstack1l1ll1l1l1_opy_ and isinstance(bstack1l1ll1l1l1_opy_[bstack111ll_opy_ (u"ࠩࡨࡼࡨࡲࡵࡥࡧࡗࡥ࡬ࡹࡉ࡯ࡖࡨࡷࡹ࡯࡮ࡨࡕࡦࡳࡵ࡫ࠧ೎")], list) else []
    excluded = any(tag in exclude_tags for tag in test_tags)
    included = len(include_tags) == 0 or any(tag in include_tags for tag in test_tags)
    return not excluded and included
  except Exception as error:
    logger.debug(bstack111ll_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡺ࡬࡮ࡲࡥࠡࡸࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡧࡦࡹࡥࠡࡨࡲࡶࠥࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡨࡥࡧࡱࡵࡩࠥࡹࡣࡢࡰࡱ࡭ࡳ࡭࠮ࠡࡇࡵࡶࡴࡸࠠ࠻ࠢࠥ೏") + str(error))
  return False
def bstack1llll1lll1_opy_(config, bstack1ll11111l1_opy_, bstack1l1ll1llll_opy_):
  bstack1ll111111l_opy_ = bstack1l1ll1ll11_opy_(config)
  bstack1l1lllll11_opy_ = bstack1l1ll1l111_opy_(config)
  if bstack1ll111111l_opy_ is None or bstack1l1lllll11_opy_ is None:
    logger.error(bstack111ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡣࡳࡧࡤࡸ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡲࡶࡰࠣࡪࡴࡸࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰ࠽ࠤࡒ࡯ࡳࡴ࡫ࡱ࡫ࠥࡧࡵࡵࡪࡨࡲࡹ࡯ࡣࡢࡶ࡬ࡳࡳࠦࡴࡰ࡭ࡨࡲࠬ೐"))
    return [None, None]
  try:
    settings = json.loads(os.getenv(bstack111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭೑"), bstack111ll_opy_ (u"࠭ࡻࡾࠩ೒")))
    data = {
        bstack111ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ೓"): config[bstack111ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭೔")],
        bstack111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬೕ"): config.get(bstack111ll_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ೖ"), os.path.basename(os.getcwd())),
        bstack111ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡗ࡭ࡲ࡫ࠧ೗"): bstack1lll1111l1_opy_(),
        bstack111ll_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪ೘"): config.get(bstack111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡉ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩ೙"), bstack111ll_opy_ (u"ࠧࠨ೚")),
        bstack111ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ೛"): {
            bstack111ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࡓࡧ࡭ࡦࠩ೜"): bstack1ll11111l1_opy_,
            bstack111ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ೝ"): bstack1l1ll1llll_opy_,
            bstack111ll_opy_ (u"ࠫࡸࡪ࡫ࡗࡧࡵࡷ࡮ࡵ࡮ࠨೞ"): __version__
        },
        bstack111ll_opy_ (u"ࠬࡹࡥࡵࡶ࡬ࡲ࡬ࡹࠧ೟"): settings,
        bstack111ll_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࡃࡰࡰࡷࡶࡴࡲࠧೠ"): bstack1l1lll1lll_opy_(),
        bstack111ll_opy_ (u"ࠧࡤ࡫ࡌࡲ࡫ࡵࠧೡ"): bstack1ll1ll1l1_opy_(),
        bstack111ll_opy_ (u"ࠨࡪࡲࡷࡹࡏ࡮ࡧࡱࠪೢ"): get_host_info(),
        bstack111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫೣ"): bstack1l1l11l1l_opy_(config)
    }
    headers = {
        bstack111ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩ೤"): bstack111ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧ೥"),
    }
    config = {
        bstack111ll_opy_ (u"ࠬࡧࡵࡵࡪࠪ೦"): (bstack1ll111111l_opy_, bstack1l1lllll11_opy_),
        bstack111ll_opy_ (u"࠭ࡨࡦࡣࡧࡩࡷࡹࠧ೧"): headers
    }
    response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"ࠧࡑࡑࡖࡘࠬ೨"), bstack1l1lllllll_opy_ + bstack111ll_opy_ (u"ࠨ࠱ࡷࡩࡸࡺ࡟ࡳࡷࡱࡷࠬ೩"), data, config)
    bstack1l1llll11l_opy_ = response.json()
    if bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠩࡶࡹࡨࡩࡥࡴࡵࠪ೪")]:
      logger.info(bstack111ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥࠡࠩ೫") + str(response.status_code) + bstack111ll_opy_ (u"ࠫࡡࡴࠧ೬") + str(bstack1l1llll11l_opy_))
      parsed = json.loads(os.getenv(bstack111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡡࡄࡇࡈࡋࡓࡔࡋࡅࡍࡑࡏࡔ࡚ࡡࡆࡓࡓࡌࡉࡈࡗࡕࡅ࡙ࡏࡏࡏࡡ࡜ࡑࡑ࠭೭"), bstack111ll_opy_ (u"࠭ࡻࡾࠩ೮")))
      parsed[bstack111ll_opy_ (u"ࠧࡴࡥࡤࡲࡳ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠨ೯")] = bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭೰")][bstack111ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪೱ")]
      os.environ[bstack111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚࡟ࡂࡅࡆࡉࡘ࡙ࡉࡃࡋࡏࡍ࡙࡟࡟ࡄࡑࡑࡊࡎࡍࡕࡓࡃࡗࡍࡔࡔ࡟࡚ࡏࡏࠫೲ")] = json.dumps(parsed)
      return bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠫࡩࡧࡴࡢࠩೳ")][bstack111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽ࡙ࡵ࡫ࡦࡰࠪ೴")], bstack1l1llll11l_opy_[bstack111ll_opy_ (u"࠭ࡤࡢࡶࡤࠫ೵")][bstack111ll_opy_ (u"ࠧࡪࡦࠪ೶")]
    else:
      logger.error(bstack111ll_opy_ (u"ࠨࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡺࡴ࡮ࡪࡰࡪࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡅࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡅࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࠺ࠡࠩ೷") + bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ೸")])
      if bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ೹")] == bstack111ll_opy_ (u"ࠫࡎࡴࡶࡢ࡮࡬ࡨࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡶࡡࡴࡵࡨࡨ࠳࠭೺"):
        for bstack1ll11111ll_opy_ in bstack1l1llll11l_opy_[bstack111ll_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࡷࠬ೻")]:
          logger.error(bstack1ll11111ll_opy_[bstack111ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ೼")])
      return None, None
  except Exception as error:
    logger.error(bstack111ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡦࡶࡪࡧࡴࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡵࡹࡳࠦࡦࡰࡴࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡀࠠࠣ೽") +  str(error))
    return None, None
def bstack11ll11ll1_opy_():
  if os.getenv(bstack111ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡍ࡛࡙࠭೾")) is None:
    return {
        bstack111ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩ೿"): bstack111ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩഀ"),
        bstack111ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬഁ"): bstack111ll_opy_ (u"ࠬࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡨࡢࡦࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠫം")
    }
  data = {bstack111ll_opy_ (u"࠭ࡥ࡯ࡦࡗ࡭ࡲ࡫ࠧഃ"): bstack1lll1111l1_opy_()}
  headers = {
      bstack111ll_opy_ (u"ࠧࡂࡷࡷ࡬ࡴࡸࡩࡻࡣࡷ࡭ࡴࡴࠧഄ"): bstack111ll_opy_ (u"ࠨࡄࡨࡥࡷ࡫ࡲࠡࠩഅ") + os.getenv(bstack111ll_opy_ (u"ࠤࡅࡗࡤࡇ࠱࠲࡛ࡢࡎ࡜࡚ࠢആ")),
      bstack111ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩഇ"): bstack111ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧഈ")
  }
  response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"ࠬࡖࡕࡕࠩഉ"), bstack1l1lllllll_opy_ + bstack111ll_opy_ (u"࠭࠯ࡵࡧࡶࡸࡤࡸࡵ࡯ࡵ࠲ࡷࡹࡵࡰࠨഊ"), data, { bstack111ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨഋ"): headers })
  try:
    if response.status_code == 200:
      logger.info(bstack111ll_opy_ (u"ࠣࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠤ࡙࡫ࡳࡵࠢࡕࡹࡳࠦ࡭ࡢࡴ࡮ࡩࡩࠦࡡࡴࠢࡦࡳࡲࡶ࡬ࡦࡶࡨࡨࠥࡧࡴࠡࠤഌ") + datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠩ࡝ࠫ഍"))
      return {bstack111ll_opy_ (u"ࠪࡷࡹࡧࡴࡶࡵࠪഎ"): bstack111ll_opy_ (u"ࠫࡸࡻࡣࡤࡧࡶࡷࠬഏ"), bstack111ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ഐ"): bstack111ll_opy_ (u"࠭ࠧ഑")}
    else:
      response.raise_for_status()
  except requests.RequestException as error:
    logger.error(bstack111ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡧࡴࡳࡰ࡭ࡧࡷ࡭ࡴࡴࠠࡰࡨࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡔࡦࡵࡷࠤࡗࡻ࡮࠻ࠢࠥഒ") + str(error))
    return {
        bstack111ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨഓ"): bstack111ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨഔ"),
        bstack111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫക"): str(error)
    }
def bstack11ll11l1_opy_(caps, options):
  try:
    bstack1ll1111111_opy_ = caps.get(bstack111ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬഖ"), {}).get(bstack111ll_opy_ (u"ࠬࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠩഗ"), caps.get(bstack111ll_opy_ (u"࠭ࡤࡦࡸ࡬ࡧࡪ࠭ഘ"), bstack111ll_opy_ (u"ࠧࠨങ")))
    if bstack1ll1111111_opy_:
      logger.warn(bstack111ll_opy_ (u"ࠣࡃࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࠡࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠥࡽࡩ࡭࡮ࠣࡶࡺࡴࠠࡰࡰ࡯ࡽࠥࡵ࡮ࠡࡆࡨࡷࡰࡺ࡯ࡱࠢࡥࡶࡴࡽࡳࡦࡴࡶ࠲ࠧച"))
      return False
    browser = caps.get(bstack111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠧഛ"), bstack111ll_opy_ (u"ࠪࠫജ")).lower()
    if browser != bstack111ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫഝ"):
      logger.warn(bstack111ll_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࠥࡇࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡱࡲࠠࡳࡷࡱࠤࡴࡴ࡬ࡺࠢࡲࡲࠥࡉࡨࡳࡱࡰࡩࠥࡨࡲࡰࡹࡶࡩࡷࡹ࠮ࠣഞ"))
      return False
    browser_version = caps.get(bstack111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧട"), caps.get(bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠩഠ")))
    if browser_version and browser_version != bstack111ll_opy_ (u"ࠨ࡮ࡤࡸࡪࡹࡴࠨഡ") and int(browser_version) <= 94:
      logger.warn(bstack111ll_opy_ (u"ࠤࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡄࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࠦࡷࡪ࡮࡯ࠤࡷࡻ࡮ࠡࡱࡱࡰࡾࠦ࡯࡯ࠢࡆ࡬ࡷࡵ࡭ࡦࠢࡥࡶࡴࡽࡳࡦࡴࠣࡺࡪࡸࡳࡪࡱࡱࠤ࡬ࡸࡥࡢࡶࡨࡶࠥࡺࡨࡢࡰࠣ࠽࠹࠴ࠢഢ"))
      return False
    if not options is None:
      bstack1l1ll1l11l_opy_ = options.to_capabilities().get(bstack111ll_opy_ (u"ࠪ࡫ࡴࡵࡧ࠻ࡥ࡫ࡶࡴࡳࡥࡐࡲࡷ࡭ࡴࡴࡳࠨണ"), {})
      if bstack111ll_opy_ (u"ࠫ࠲࠳ࡨࡦࡣࡧࡰࡪࡹࡳࠨത") in bstack1l1ll1l11l_opy_.get(bstack111ll_opy_ (u"ࠬࡧࡲࡨࡵࠪഥ"), []):
        logger.warn(bstack111ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥࡸࡵ࡯ࠢࡲࡲࠥࡲࡥࡨࡣࡦࡽࠥ࡮ࡥࡢࡦ࡯ࡩࡸࡹࠠ࡮ࡱࡧࡩ࠳ࠦࡓࡸ࡫ࡷࡧ࡭ࠦࡴࡰࠢࡱࡩࡼࠦࡨࡦࡣࡧࡰࡪࡹࡳࠡ࡯ࡲࡨࡪࠦ࡯ࡳࠢࡤࡺࡴ࡯ࡤࠡࡷࡶ࡭ࡳ࡭ࠠࡩࡧࡤࡨࡱ࡫ࡳࡴࠢࡰࡳࡩ࡫࠮ࠣദ"))
        return False
    return True
  except Exception as error:
    logger.debug(bstack111ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡶࡢ࡮࡬ࡨࡦࡺࡥࠡࡣ࠴࠵ࡾࠦࡳࡶࡲࡳࡳࡷࡺࠠ࠻ࠤധ") + str(error))
    return False
def set_capabilities(caps, config):
  try:
    bstack1l1llll1ll_opy_ = config.get(bstack111ll_opy_ (u"ࠨࡣࡦࡧࡪࡹࡳࡪࡤ࡬ࡰ࡮ࡺࡹࡐࡲࡷ࡭ࡴࡴࡳࠨന"), {})
    bstack1l1llll1ll_opy_[bstack111ll_opy_ (u"ࠩࡤࡹࡹ࡮ࡔࡰ࡭ࡨࡲࠬഩ")] = os.getenv(bstack111ll_opy_ (u"ࠪࡆࡘࡥࡁ࠲࠳࡜ࡣࡏ࡝ࡔࠨപ"))
    bstack1l1llll111_opy_ = json.loads(os.getenv(bstack111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡠࡃࡆࡇࡊ࡙ࡓࡊࡄࡌࡐࡎ࡚࡙ࡠࡅࡒࡒࡋࡏࡇࡖࡔࡄࡘࡎࡕࡎࡠ࡛ࡐࡐࠬഫ"), bstack111ll_opy_ (u"ࠬࢁࡽࠨബ"))).get(bstack111ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧഭ"))
    caps[bstack111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠧമ")] = True
    if bstack111ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩയ") in caps:
      caps[bstack111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪര")][bstack111ll_opy_ (u"ࠪࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࡒࡴࡹ࡯࡯࡯ࡵࠪറ")] = bstack1l1llll1ll_opy_
      caps[bstack111ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬല")][bstack111ll_opy_ (u"ࠬࡧࡣࡤࡧࡶࡷ࡮ࡨࡩ࡭࡫ࡷࡽࡔࡶࡴࡪࡱࡱࡷࠬള")][bstack111ll_opy_ (u"࠭ࡳࡤࡣࡱࡲࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠧഴ")] = bstack1l1llll111_opy_
    else:
      caps[bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴ࡡࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭വ")] = bstack1l1llll1ll_opy_
      caps[bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮ࡢࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࡏࡱࡶ࡬ࡳࡳࡹࠧശ")][bstack111ll_opy_ (u"ࠩࡶࡧࡦࡴ࡮ࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠪഷ")] = bstack1l1llll111_opy_
  except Exception as error:
    logger.debug(bstack111ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥࡹࡥࡵࡶ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡁࡶࡶࡲࡱࡦࡺࡩࡰࡰࠣࡧࡦࡶࡡࡣ࡫࡯࡭ࡹ࡯ࡥࡴ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࠦസ") +  str(error))
def bstack1l1ll1ll1l_opy_(driver, bstack1l1lll111l_opy_):
  try:
    session = driver.session_id
    if session:
      bstack1l1lll1111_opy_ = True
      current_url = driver.current_url
      try:
        url = urlparse(current_url)
      except Exception as e:
        bstack1l1lll1111_opy_ = False
      bstack1l1lll1111_opy_ = url.scheme in [bstack111ll_opy_ (u"ࠦ࡭ࡺࡴࡱࠤഹ"), bstack111ll_opy_ (u"ࠧ࡮ࡴࡵࡲࡶࠦഺ")]
      if bstack1l1lll1111_opy_:
        if bstack1l1lll111l_opy_:
          logger.info(bstack111ll_opy_ (u"ࠨࡓࡦࡶࡸࡴࠥ࡬࡯ࡳࠢࡄࡧࡨ࡫ࡳࡴ࡫ࡥ࡭ࡱ࡯ࡴࡺࠢࡷࡩࡸࡺࡩ࡯ࡩࠣ࡬ࡦࡹࠠࡴࡶࡤࡶࡹ࡫ࡤ࠯ࠢࡄࡹࡹࡵ࡭ࡢࡶࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫ࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠣࡻ࡮ࡲ࡬ࠡࡤࡨ࡫࡮ࡴࠠ࡮ࡱࡰࡩࡳࡺࡡࡳ࡫࡯ࡽ࠳ࠨ഻"))
          driver.execute_async_script(bstack111ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡴࡴࡳࡵࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠤࡂࠦࡡࡳࡩࡸࡱࡪࡴࡴࡴ࡝ࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷ࠳ࡲࡥ࡯ࡩࡷ࡬ࠥ࠳ࠠ࠲࡟࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡪࡳࠦ࠽ࠡࠪࠬࠤࡂࡄࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡡࡥࡦࡈࡺࡪࡴࡴࡍ࡫ࡶࡸࡪࡴࡥࡳࠪࠪࡅ࠶࠷࡙ࡠࡖࡄࡔࡤ࡙ࡔࡂࡔࡗࡉࡉ࠭ࠬࠡࡨࡱ࠶࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡴࡶࠣࡩࠥࡃࠠ࡯ࡧࡺࠤࡈࡻࡳࡵࡱࡰࡉࡻ࡫࡮ࡵࠪࠪࡅ࠶࠷࡙ࡠࡈࡒࡖࡈࡋ࡟ࡔࡖࡄࡖ࡙࠭ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡷࡪࡰࡧࡳࡼ࠴ࡤࡪࡵࡳࡥࡹࡩࡨࡆࡸࡨࡲࡹ࠮ࡥࠪ࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡶࡸࠥ࡬࡮࠳ࠢࡀࠤ࠭࠯ࠠ࠾ࡀࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡵࡩࡲࡵࡶࡦࡇࡹࡩࡳࡺࡌࡪࡵࡷࡩࡳ࡫ࡲࠩࠩࡄ࠵࠶࡟࡟ࡕࡃࡓࡣࡘ࡚ࡁࡓࡖࡈࡈࠬ࠲ࠠࡧࡰࠬ࠿ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡥࡱࡲࡢࡢࡥ࡮ࠬ࠮ࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡩࡲ࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨ഼ࠢ"))
          logger.info(bstack111ll_opy_ (u"ࠣࡃࡸࡸࡴࡳࡡࡵࡧࠣࡸࡪࡹࡴࠡࡥࡤࡷࡪࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠢ࡫ࡥࡸࠦࡳࡵࡣࡵࡸࡪࡪ࠮ࠣഽ"))
        else:
          driver.execute_script(bstack111ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡵࡷࠤࡪࠦ࠽ࠡࡰࡨࡻࠥࡉࡵࡴࡶࡲࡱࡊࡼࡥ࡯ࡶࠫࠫࡆ࠷࠱࡚ࡡࡉࡓࡗࡉࡅࡠࡕࡗࡓࡕ࠭ࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡧ࡭ࡸࡶࡡࡵࡥ࡫ࡉࡻ࡫࡮ࡵࠪࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧാ"))
      return bstack1l1lll111l_opy_
  except Exception as e:
    logger.error(bstack111ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡸࡦࡸࡴࡪࡰࡪࠤࡦࡩࡣࡦࡵࡶ࡭ࡧ࡯࡬ࡪࡶࡼࠤࡦࡻࡴࡰ࡯ࡤࡸ࡮ࡵ࡮ࠡࡵࡦࡥࡳࠦࡦࡰࡴࠣࡸ࡭࡯ࡳࠡࡶࡨࡷࡹࠦࡣࡢࡵࡨ࠾ࠥࠨി") + str(e))
    return False
def bstack1l1ll1l1ll_opy_(driver, item):
  try:
    bstack1l1ll1lll1_opy_ = [item.cls.__name__] if not item.cls is None else []
    bstack1l1lll1l11_opy_ = {
        bstack111ll_opy_ (u"ࠦࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠤീ"): True,
        bstack111ll_opy_ (u"ࠧࡺࡥࡴࡶࡇࡩࡹࡧࡩ࡭ࡵࠥു"): {
            bstack111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦൂ"): item.name,
            bstack111ll_opy_ (u"ࠢࡵࡧࡶࡸࡗࡻ࡮ࡊࡦࠥൃ"): os.environ.get(bstack111ll_opy_ (u"ࠨࡄࡖࡣࡆ࠷࠱࡚ࡡࡗࡉࡘ࡚࡟ࡓࡗࡑࡣࡎࡊࠧൄ")),
            bstack111ll_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦ൅"): str(item.path),
            bstack111ll_opy_ (u"ࠥࡷࡨࡵࡰࡦࡎ࡬ࡷࡹࠨെ"): [item.module.__name__, *bstack1l1ll1lll1_opy_, item.name],
        },
        bstack111ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨേ"): _1l1lll1l1l_opy_(driver)
    }
    driver.execute_async_script(bstack111ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳࡹࡴࠡࡥࡤࡰࡱࡨࡡࡤ࡭ࠣࡁࠥࡧࡲࡨࡷࡰࡩࡳࡺࡳ࡜ࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶ࠲ࡱ࡫࡮ࡨࡶ࡫ࠤ࠲ࠦ࠱࡞࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡮ࡩࡴ࠰ࡵࡩࡸࠦ࠽ࠡࡰࡸࡰࡱࡁࠊࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡩࠤ࠭ࡧࡲࡨࡷࡰࡩࡳࡺࡳ࡜࠲ࡠ࠲ࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠫࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡥࡩࡪࡅࡷࡧࡱࡸࡑ࡯ࡳࡵࡧࡱࡩࡷ࠮ࠧࡂ࠳࠴࡝ࡤ࡚ࡁࡑࡡࡗࡖࡆࡔࡓࡑࡑࡕࡘࡊࡘࠧ࠭ࠢࠫࡩࡻ࡫࡮ࡵࠫࠣࡁࡃࠦࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡻ࡮ࡴࡤࡰࡹ࠱ࡸࡦࡶࡔࡳࡣࡱࡷࡵࡵࡲࡵࡧࡵࡈࡦࡺࡡࠡ࠿ࠣࡩࡻ࡫࡮ࡵ࠰ࡧࡩࡹࡧࡩ࡭࠽ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡪࡵ࠱ࡶࡪࡹࠠ࠾ࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡷࡥࡵ࡚ࡲࡢࡰࡶࡴࡴࡸࡴࡦࡴࡇࡥࡹࡧ࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠭ࡺࡨࡪࡵ࠱ࡶࡪࡹࠩ࠼ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡾࠫ࠾ࠎࠥࠦࠠࠡࠢࠣࠤࠥࢃࠊࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲࡸࡺࠠࡦࠢࡀࠤࡳ࡫ࡷࠡࡅࡸࡷࡹࡵ࡭ࡆࡸࡨࡲࡹ࠮ࠧࡂ࠳࠴࡝ࡤ࡚ࡅࡔࡖࡢࡉࡓࡊࠧ࠭ࠢࡾࠤࡩ࡫ࡴࡢ࡫࡯࠾ࠥࡧࡲࡨࡷࡰࡩࡳࡺࡳ࡜࠲ࡠࠤࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡺ࡭ࡳࡪ࡯ࡸ࠰ࡧ࡭ࡸࡶࡡࡵࡥ࡫ࡉࡻ࡫࡮ࡵࠪࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࡪࡨࠣࠬࠦࡧࡲࡨࡷࡰࡩࡳࡺࡳ࡜࠲ࡠ࠲ࡸࡧࡶࡦࡔࡨࡷࡺࡲࡴࡴࠫࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡧࡦࡲ࡬ࡣࡣࡦ࡯࠭࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࢀࠎࠥࠦࠠࠡࠤࠥࠦൈ"), bstack1l1lll1l11_opy_)
    logger.info(bstack111ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࡯ࡢࡪ࡮࡬ࡸࡾࠦࡴࡦࡵࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡹ࡮ࡩࡴࠢࡷࡩࡸࡺࠠࡤࡣࡶࡩࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠤ൉"))
  except Exception as bstack1l1lllll1l_opy_:
    logger.error(bstack111ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࡩࡣ࡫࡯࡭ࡹࡿࠠࡳࡧࡶࡹࡱࡺࡳࠡࡥࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡱࡴࡲࡧࡪࡹࡳࡦࡦࠣࡪࡴࡸࠠࡵࡪࡨࠤࡹ࡫ࡳࡵࠢࡦࡥࡸ࡫࠺ࠡࠤൊ") + item.path + bstack111ll_opy_ (u"ࠣࠢࡈࡶࡷࡵࡲࠡ࠼ࠥോ") + str(bstack1l1lllll1l_opy_))