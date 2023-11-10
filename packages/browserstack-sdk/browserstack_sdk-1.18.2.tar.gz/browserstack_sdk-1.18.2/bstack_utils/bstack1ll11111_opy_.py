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
import datetime
import json
import logging
import os
import threading
from bstack_utils.helper import bstack1l1lll1lll_opy_, bstack1ll1ll1l1_opy_, get_host_info, bstack1l1ll1ll11_opy_, bstack1l1ll1l111_opy_, bstack1l11ll11l1_opy_, \
    bstack1l1l11l11l_opy_, bstack1l11ll111l_opy_, bstack1ll1l111_opy_, bstack1l1l1l1ll1_opy_, bstack1l11lllll1_opy_, bstack1l1lll11ll_opy_
from bstack_utils.bstack11ll111lll_opy_ import bstack11ll111ll1_opy_
from bstack_utils.bstack11l1l1llll_opy_ import bstack11l1l11l11_opy_
bstack11l111l111_opy_ = [
    bstack111ll_opy_ (u"ࠬࡒ࡯ࡨࡅࡵࡩࡦࡺࡥࡥࠩኈ"), bstack111ll_opy_ (u"࠭ࡃࡃࡖࡖࡩࡸࡹࡩࡰࡰࡆࡶࡪࡧࡴࡦࡦࠪ኉"), bstack111ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩኊ"), bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕ࡮࡭ࡵࡶࡥࡥࠩኋ"),
    bstack111ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫኌ"), bstack111ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫኍ"), bstack111ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡔࡸࡲࡘࡺࡡࡳࡶࡨࡨࠬ኎")
]
bstack11l11l1lll_opy_ = bstack111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶ࠾࠴࠵ࡣࡰ࡮࡯ࡩࡨࡺ࡯ࡳ࠯ࡲࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺ࠰ࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯ࡥࡲࡱࠬ኏")
logger = logging.getLogger(__name__)
class bstack1llll111ll_opy_:
    bstack11ll111lll_opy_ = None
    bs_config = None
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def launch(cls, bs_config, bstack11l11l1l11_opy_):
        cls.bs_config = bs_config
        if not cls.bstack11l1111l1l_opy_():
            return
        cls.bstack11l111l1l1_opy_()
        bstack1ll111111l_opy_ = bstack1l1ll1ll11_opy_(bs_config)
        bstack1l1lllll11_opy_ = bstack1l1ll1l111_opy_(bs_config)
        data = {
            bstack111ll_opy_ (u"࠭ࡦࡰࡴࡰࡥࡹ࠭ነ"): bstack111ll_opy_ (u"ࠧ࡫ࡵࡲࡲࠬኑ"),
            bstack111ll_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡡࡱࡥࡲ࡫ࠧኒ"): bs_config.get(bstack111ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧና"), bstack111ll_opy_ (u"ࠪࠫኔ")),
            bstack111ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩን"): bs_config.get(bstack111ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨኖ"), os.path.basename(os.path.abspath(os.getcwd()))),
            bstack111ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡤ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩኗ"): bs_config.get(bstack111ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩኘ")),
            bstack111ll_opy_ (u"ࠨࡦࡨࡷࡨࡸࡩࡱࡶ࡬ࡳࡳ࠭ኙ"): bs_config.get(bstack111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡅࡧࡶࡧࡷ࡯ࡰࡵ࡫ࡲࡲࠬኚ"), bstack111ll_opy_ (u"ࠪࠫኛ")),
            bstack111ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡢࡸ࡮ࡳࡥࠨኜ"): datetime.datetime.now().isoformat(),
            bstack111ll_opy_ (u"ࠬࡺࡡࡨࡵࠪኝ"): bstack1l11ll11l1_opy_(bs_config),
            bstack111ll_opy_ (u"࠭ࡨࡰࡵࡷࡣ࡮ࡴࡦࡰࠩኞ"): get_host_info(),
            bstack111ll_opy_ (u"ࠧࡤ࡫ࡢ࡭ࡳ࡬࡯ࠨኟ"): bstack1ll1ll1l1_opy_(),
            bstack111ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪ࡟ࡳࡷࡱࡣ࡮ࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨአ"): os.environ.get(bstack111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠨኡ")),
            bstack111ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࡢࡸࡪࡹࡴࡴࡡࡵࡩࡷࡻ࡮ࠨኢ"): os.environ.get(bstack111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡖࡊࡘࡕࡏࠩኣ"), False),
            bstack111ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳࡥࡣࡰࡰࡷࡶࡴࡲࠧኤ"): bstack1l1lll1lll_opy_(),
            bstack111ll_opy_ (u"࠭࡯ࡣࡵࡨࡶࡻࡧࡢࡪ࡮࡬ࡸࡾࡥࡶࡦࡴࡶ࡭ࡴࡴࠧእ"): {
                bstack111ll_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࡑࡥࡲ࡫ࠧኦ"): bstack11l11l1l11_opy_.get(bstack111ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࡣࡳࡧ࡭ࡦࠩኧ"), bstack111ll_opy_ (u"ࠩࡓࡽࡹ࡫ࡳࡵࠩከ")),
                bstack111ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࡜ࡥࡳࡵ࡬ࡳࡳ࠭ኩ"): bstack11l11l1l11_opy_.get(bstack111ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠨኪ")),
                bstack111ll_opy_ (u"ࠬࡹࡤ࡬ࡘࡨࡶࡸ࡯࡯࡯ࠩካ"): bstack11l11l1l11_opy_.get(bstack111ll_opy_ (u"࠭ࡳࡥ࡭ࡢࡺࡪࡸࡳࡪࡱࡱࠫኬ"))
            }
        }
        config = {
            bstack111ll_opy_ (u"ࠧࡢࡷࡷ࡬ࠬክ"): (bstack1ll111111l_opy_, bstack1l1lllll11_opy_),
            bstack111ll_opy_ (u"ࠨࡪࡨࡥࡩ࡫ࡲࡴࠩኮ"): cls.default_headers()
        }
        response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"ࠩࡓࡓࡘ࡚ࠧኯ"), cls.request_url(bstack111ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵࠪኰ")), data, config)
        if response.status_code != 200:
            os.environ[bstack111ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡄࡑࡐࡔࡑࡋࡔࡆࡆࠪ኱")] = bstack111ll_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫኲ")
            os.environ[bstack111ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧኳ")] = bstack111ll_opy_ (u"ࠧ࡯ࡷ࡯ࡰࠬኴ")
            os.environ[bstack111ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡍࡇࡓࡉࡇࡇࡣࡎࡊࠧኵ")] = bstack111ll_opy_ (u"ࠤࡱࡹࡱࡲࠢ኶")
            os.environ[bstack111ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡂࡎࡏࡓ࡜ࡥࡓࡄࡔࡈࡉࡓ࡙ࡈࡐࡖࡖࠫ኷")] = bstack111ll_opy_ (u"ࠦࡳࡻ࡬࡭ࠤኸ")
            bstack11l11llll1_opy_ = response.json()
            if bstack11l11llll1_opy_ and bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ኹ")]:
                error_message = bstack11l11llll1_opy_[bstack111ll_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧኺ")]
                if bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠧࡦࡴࡵࡳࡷ࡚ࡹࡱࡧࠪኻ")] == bstack111ll_opy_ (u"ࠨࡇࡕࡖࡔࡘ࡟ࡊࡐ࡙ࡅࡑࡏࡄࡠࡅࡕࡉࡉࡋࡎࡕࡋࡄࡐࡘ࠭ኼ"):
                    logger.error(error_message)
                elif bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࡕࡻࡳࡩࠬኽ")] == bstack111ll_opy_ (u"ࠪࡉࡗࡘࡏࡓࡡࡄࡇࡈࡋࡓࡔࡡࡇࡉࡓࡏࡅࡅࠩኾ"):
                    logger.info(error_message)
                elif bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࡗࡽࡵ࡫ࠧ኿")] == bstack111ll_opy_ (u"ࠬࡋࡒࡓࡑࡕࡣࡘࡊࡋࡠࡆࡈࡔࡗࡋࡃࡂࡖࡈࡈࠬዀ"):
                    logger.error(error_message)
                else:
                    logger.error(error_message)
            else:
                logger.error(bstack111ll_opy_ (u"ࠨࡄࡢࡶࡤࠤࡺࡶ࡬ࡰࡣࡧࠤࡹࡵࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡔࡦࡵࡷࠤࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࠤ࡫ࡧࡩ࡭ࡧࡧࠤࡩࡻࡥࠡࡶࡲࠤࡸࡵ࡭ࡦࠢࡨࡶࡷࡵࡲࠣ዁"))
            return [None, None, None]
        logger.debug(bstack111ll_opy_ (u"ࠧࡕࡧࡶࡸࠥࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠥࡈࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦࡓࡶࡥࡦࡩࡸࡹࡦࡶ࡮ࠤࠫዂ"))
        os.environ[bstack111ll_opy_ (u"ࠨࡄࡖࡣ࡙ࡋࡓࡕࡑࡓࡗࡤࡈࡕࡊࡎࡇࡣࡈࡕࡍࡑࡎࡈࡘࡊࡊࠧዃ")] = bstack111ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧዄ")
        bstack11l11llll1_opy_ = response.json()
        if bstack11l11llll1_opy_.get(bstack111ll_opy_ (u"ࠪ࡮ࡼࡺࠧዅ")):
            os.environ[bstack111ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬ዆")] = bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠬࡰࡷࡵࠩ዇")]
            os.environ[bstack111ll_opy_ (u"࠭ࡃࡓࡇࡇࡉࡓ࡚ࡉࡂࡎࡖࡣࡋࡕࡒࡠࡅࡕࡅࡘࡎ࡟ࡓࡇࡓࡓࡗ࡚ࡉࡏࡉࠪወ")] = json.dumps({
                bstack111ll_opy_ (u"ࠧࡶࡵࡨࡶࡳࡧ࡭ࡦࠩዉ"): bstack1ll111111l_opy_,
                bstack111ll_opy_ (u"ࠨࡲࡤࡷࡸࡽ࡯ࡳࡦࠪዊ"): bstack1l1lllll11_opy_
            })
        if bstack11l11llll1_opy_.get(bstack111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫዋ")):
            os.environ[bstack111ll_opy_ (u"ࠪࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡃࡗࡌࡐࡉࡥࡈࡂࡕࡋࡉࡉࡥࡉࡅࠩዌ")] = bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡢ࡬ࡦࡹࡨࡦࡦࡢ࡭ࡩ࠭ው")]
        if bstack11l11llll1_opy_.get(bstack111ll_opy_ (u"ࠬࡧ࡬࡭ࡱࡺࡣࡸࡩࡲࡦࡧࡱࡷ࡭ࡵࡴࡴࠩዎ")):
            os.environ[bstack111ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡅࡑࡒࡏࡘࡡࡖࡇࡗࡋࡅࡏࡕࡋࡓ࡙࡙ࠧዏ")] = str(bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠧࡢ࡮࡯ࡳࡼࡥࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫዐ")])
        return [bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠨ࡬ࡺࡸࠬዑ")], bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡠࡪࡤࡷ࡭࡫ࡤࡠ࡫ࡧࠫዒ")], bstack11l11llll1_opy_[bstack111ll_opy_ (u"ࠪࡥࡱࡲ࡯ࡸࡡࡶࡧࡷ࡫ࡥ࡯ࡵ࡫ࡳࡹࡹࠧዓ")]]
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def stop(cls):
        if not cls.on():
            return
        if os.environ[bstack111ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡌ࡚ࡘࠬዔ")] == bstack111ll_opy_ (u"ࠧࡴࡵ࡭࡮ࠥዕ") or os.environ[bstack111ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠬዖ")] == bstack111ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧ዗"):
            print(bstack111ll_opy_ (u"ࠨࡇ࡛ࡇࡊࡖࡔࡊࡑࡑࠤࡎࡔࠠࡴࡶࡲࡴࡇࡻࡩ࡭ࡦࡘࡴࡸࡺࡲࡦࡣࡰࠤࡗࡋࡑࡖࡇࡖࡘ࡚ࠥࡏࠡࡖࡈࡗ࡙ࠦࡏࡃࡕࡈࡖ࡛ࡇࡂࡊࡎࡌࡘ࡞ࠦ࠺ࠡࡏ࡬ࡷࡸ࡯࡮ࡨࠢࡤࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩࡰࡰࠣࡸࡴࡱࡥ࡯ࠩዘ"))
            return {
                bstack111ll_opy_ (u"ࠩࡶࡸࡦࡺࡵࡴࠩዙ"): bstack111ll_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩዚ"),
                bstack111ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬዛ"): bstack111ll_opy_ (u"࡚ࠬ࡯࡬ࡧࡱ࠳ࡧࡻࡩ࡭ࡦࡌࡈࠥ࡯ࡳࠡࡷࡱࡨࡪ࡬ࡩ࡯ࡧࡧ࠰ࠥࡨࡵࡪ࡮ࡧࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡪࡩ࡫ࡸࠥ࡮ࡡࡷࡧࠣࡪࡦ࡯࡬ࡦࡦࠪዜ")
            }
        else:
            cls.bstack11ll111lll_opy_.shutdown()
            data = {
                bstack111ll_opy_ (u"࠭ࡳࡵࡱࡳࡣࡹ࡯࡭ࡦࠩዝ"): datetime.datetime.now().isoformat()
            }
            config = {
                bstack111ll_opy_ (u"ࠧࡩࡧࡤࡨࡪࡸࡳࠨዞ"): cls.default_headers()
            }
            bstack1l1l1l11ll_opy_ = bstack111ll_opy_ (u"ࠨࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡸࡺ࡯ࡱࠩዟ").format(os.environ[bstack111ll_opy_ (u"ࠤࡅࡗࡤ࡚ࡅࡔࡖࡒࡔࡘࡥࡂࡖࡋࡏࡈࡤࡎࡁࡔࡊࡈࡈࡤࡏࡄࠣዠ")])
            bstack11l11l111l_opy_ = cls.request_url(bstack1l1l1l11ll_opy_)
            response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"ࠪࡔ࡚࡚ࠧዡ"), bstack11l11l111l_opy_, data, config)
            if not response.ok:
                raise Exception(bstack111ll_opy_ (u"ࠦࡘࡺ࡯ࡱࠢࡵࡩࡶࡻࡥࡴࡶࠣࡲࡴࡺࠠࡰ࡭ࠥዢ"))
    @classmethod
    def bstack11l11lll1l_opy_(cls):
        if cls.bstack11ll111lll_opy_ is None:
            return
        cls.bstack11ll111lll_opy_.shutdown()
    @classmethod
    def bstack1ll1l1l1_opy_(cls):
        if cls.on():
            print(
                bstack111ll_opy_ (u"ࠬ࡜ࡩࡴ࡫ࡷࠤ࡭ࡺࡴࡱࡵ࠽࠳࠴ࡵࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽ࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡨࡵ࡭࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀࠤࡹࡵࠠࡷ࡫ࡨࡻࠥࡨࡵࡪ࡮ࡧࠤࡷ࡫ࡰࡰࡴࡷ࠰ࠥ࡯࡮ࡴ࡫ࡪ࡬ࡹࡹࠬࠡࡣࡱࡨࠥࡳࡡ࡯ࡻࠣࡱࡴࡸࡥࠡࡦࡨࡦࡺ࡭ࡧࡪࡰࡪࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡰࡱࠦࡡࡵࠢࡲࡲࡪࠦࡰ࡭ࡣࡦࡩࠦࡢ࡮ࠨዣ").format(os.environ[bstack111ll_opy_ (u"ࠨࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡆ࡚ࡏࡌࡅࡡࡋࡅࡘࡎࡅࡅࡡࡌࡈࠧዤ")]))
    @classmethod
    def bstack11l111l1l1_opy_(cls):
        if cls.bstack11ll111lll_opy_ is not None:
            return
        cls.bstack11ll111lll_opy_ = bstack11ll111ll1_opy_(cls.bstack11l11ll111_opy_)
        cls.bstack11ll111lll_opy_.start()
    @classmethod
    def bstack11l1111l11_opy_(cls, bstack11l11lll11_opy_, bstack11l11l11l1_opy_=bstack111ll_opy_ (u"ࠧࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡣࡷࡧ࡭࠭ዥ")):
        if not cls.on():
            return
        bstack1lll111ll_opy_ = bstack11l11lll11_opy_[bstack111ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬዦ")]
        bstack11l11111ll_opy_ = {
            bstack111ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪዧ"): bstack111ll_opy_ (u"ࠪࡘࡪࡹࡴࡠࡕࡷࡥࡷࡺ࡟ࡖࡲ࡯ࡳࡦࡪࠧየ"),
            bstack111ll_opy_ (u"࡙ࠫ࡫ࡳࡵࡔࡸࡲࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭ዩ"): bstack111ll_opy_ (u"࡚ࠬࡥࡴࡶࡢࡉࡳࡪ࡟ࡖࡲ࡯ࡳࡦࡪࠧዪ"),
            bstack111ll_opy_ (u"࠭ࡔࡦࡵࡷࡖࡺࡴࡓ࡬࡫ࡳࡴࡪࡪࠧያ"): bstack111ll_opy_ (u"ࠧࡕࡧࡶࡸࡤ࡙࡫ࡪࡲࡳࡩࡩࡥࡕࡱ࡮ࡲࡥࡩ࠭ዬ"),
            bstack111ll_opy_ (u"ࠨࡎࡲ࡫ࡈࡸࡥࡢࡶࡨࡨࠬይ"): bstack111ll_opy_ (u"ࠩࡏࡳ࡬ࡥࡕࡱ࡮ࡲࡥࡩ࠭ዮ"),
            bstack111ll_opy_ (u"ࠪࡌࡴࡵ࡫ࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫዯ"): bstack111ll_opy_ (u"ࠫࡍࡵ࡯࡬ࡡࡖࡸࡦࡸࡴࡠࡗࡳࡰࡴࡧࡤࠨደ"),
            bstack111ll_opy_ (u"ࠬࡎ࡯ࡰ࡭ࡕࡹࡳࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧዱ"): bstack111ll_opy_ (u"࠭ࡈࡰࡱ࡮ࡣࡊࡴࡤࡠࡗࡳࡰࡴࡧࡤࠨዲ"),
            bstack111ll_opy_ (u"ࠧࡄࡄࡗࡗࡪࡹࡳࡪࡱࡱࡇࡷ࡫ࡡࡵࡧࡧࠫዳ"): bstack111ll_opy_ (u"ࠨࡅࡅࡘࡤ࡛ࡰ࡭ࡱࡤࡨࠬዴ")
        }.get(bstack1lll111ll_opy_)
        if bstack11l11l11l1_opy_ == bstack111ll_opy_ (u"ࠩࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡥࡹࡩࡨࠨድ"):
            cls.bstack11l111l1l1_opy_()
            cls.bstack11ll111lll_opy_.add(bstack11l11lll11_opy_)
        elif bstack11l11l11l1_opy_ == bstack111ll_opy_ (u"ࠪࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࡳࠨዶ"):
            cls.bstack11l11ll111_opy_([bstack11l11lll11_opy_], bstack11l11l11l1_opy_)
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def bstack11l11ll111_opy_(cls, bstack11l11lll11_opy_, bstack11l11l11l1_opy_=bstack111ll_opy_ (u"ࠫࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡧࡴࡤࡪࠪዷ")):
        config = {
            bstack111ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭ዸ"): cls.default_headers()
        }
        response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"࠭ࡐࡐࡕࡗࠫዹ"), cls.request_url(bstack11l11l11l1_opy_), bstack11l11lll11_opy_, config)
        bstack1l1llll11l_opy_ = response.json()
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def bstack11l11ll11l_opy_(cls, bstack11l111ll11_opy_):
        bstack11l111llll_opy_ = []
        for log in bstack11l111ll11_opy_:
            bstack11l11l1111_opy_ = {
                bstack111ll_opy_ (u"ࠧ࡬࡫ࡱࡨࠬዺ"): bstack111ll_opy_ (u"ࠨࡖࡈࡗ࡙ࡥࡌࡐࡉࠪዻ"),
                bstack111ll_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨዼ"): log[bstack111ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩዽ")],
                bstack111ll_opy_ (u"ࠫࡹ࡯࡭ࡦࡵࡷࡥࡲࡶࠧዾ"): log[bstack111ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨዿ")],
                bstack111ll_opy_ (u"࠭ࡨࡵࡶࡳࡣࡷ࡫ࡳࡱࡱࡱࡷࡪ࠭ጀ"): {},
                bstack111ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨጁ"): log[bstack111ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩጂ")],
            }
            if bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩጃ") in log:
                bstack11l11l1111_opy_[bstack111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪጄ")] = log[bstack111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጅ")]
            elif bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጆ") in log:
                bstack11l11l1111_opy_[bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ጇ")] = log[bstack111ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧገ")]
            bstack11l111llll_opy_.append(bstack11l11l1111_opy_)
        cls.bstack11l1111l11_opy_({
            bstack111ll_opy_ (u"ࠨࡧࡹࡩࡳࡺ࡟ࡵࡻࡳࡩࠬጉ"): bstack111ll_opy_ (u"ࠩࡏࡳ࡬ࡉࡲࡦࡣࡷࡩࡩ࠭ጊ"),
            bstack111ll_opy_ (u"ࠪࡰࡴ࡭ࡳࠨጋ"): bstack11l111llll_opy_
        })
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def bstack11l1l11111_opy_(cls, steps):
        bstack11l111l11l_opy_ = []
        for step in steps:
            bstack11l11l11ll_opy_ = {
                bstack111ll_opy_ (u"ࠫࡰ࡯࡮ࡥࠩጌ"): bstack111ll_opy_ (u"࡚ࠬࡅࡔࡖࡢࡗ࡙ࡋࡐࠨግ"),
                bstack111ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬጎ"): step[bstack111ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ጏ")],
                bstack111ll_opy_ (u"ࠨࡶ࡬ࡱࡪࡹࡴࡢ࡯ࡳࠫጐ"): step[bstack111ll_opy_ (u"ࠩࡷ࡭ࡲ࡫ࡳࡵࡣࡰࡴࠬ጑")],
                bstack111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫጒ"): step[bstack111ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬጓ")],
                bstack111ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧጔ"): step[bstack111ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨጕ")]
            }
            if bstack111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧ጖") in step:
                bstack11l11l11ll_opy_[bstack111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨ጗")] = step[bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩጘ")]
            elif bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪጙ") in step:
                bstack11l11l11ll_opy_[bstack111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጚ")] = step[bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጛ")]
            bstack11l111l11l_opy_.append(bstack11l11l11ll_opy_)
        cls.bstack11l1111l11_opy_({
            bstack111ll_opy_ (u"࠭ࡥࡷࡧࡱࡸࡤࡺࡹࡱࡧࠪጜ"): bstack111ll_opy_ (u"ࠧࡍࡱࡪࡇࡷ࡫ࡡࡵࡧࡧࠫጝ"),
            bstack111ll_opy_ (u"ࠨ࡮ࡲ࡫ࡸ࠭ጞ"): bstack11l111l11l_opy_
        })
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def bstack11l111lll1_opy_(cls, screenshot):
        cls.bstack11l1111l11_opy_({
            bstack111ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ጟ"): bstack111ll_opy_ (u"ࠪࡐࡴ࡭ࡃࡳࡧࡤࡸࡪࡪࠧጠ"),
            bstack111ll_opy_ (u"ࠫࡱࡵࡧࡴࠩጡ"): [{
                bstack111ll_opy_ (u"ࠬࡱࡩ࡯ࡦࠪጢ"): bstack111ll_opy_ (u"࠭ࡔࡆࡕࡗࡣࡘࡉࡒࡆࡇࡑࡗࡍࡕࡔࠨጣ"),
                bstack111ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪጤ"): datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠨ࡜ࠪጥ"),
                bstack111ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪጦ"): screenshot[bstack111ll_opy_ (u"ࠪ࡭ࡲࡧࡧࡦࠩጧ")],
                bstack111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫጨ"): screenshot[bstack111ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡶࡷ࡬ࡨࠬጩ")]
            }]
        }, bstack11l11l11l1_opy_=bstack111ll_opy_ (u"࠭ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡤࡴࡨࡩࡳࡹࡨࡰࡶࡶࠫጪ"))
    @classmethod
    @bstack1l1lll11ll_opy_(class_method=True)
    def bstack1llll1111l_opy_(cls, driver):
        current_test_uuid = cls.current_test_uuid()
        if not current_test_uuid:
            return
        cls.bstack11l1111l11_opy_({
            bstack111ll_opy_ (u"ࠧࡦࡸࡨࡲࡹࡥࡴࡺࡲࡨࠫጫ"): bstack111ll_opy_ (u"ࠨࡅࡅࡘࡘ࡫ࡳࡴ࡫ࡲࡲࡈࡸࡥࡢࡶࡨࡨࠬጬ"),
            bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫጭ"): {
                bstack111ll_opy_ (u"ࠥࡹࡺ࡯ࡤࠣጮ"): cls.current_test_uuid(),
                bstack111ll_opy_ (u"ࠦ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠥጯ"): cls.bstack11l111ll1l_opy_(driver)
            }
        })
    @classmethod
    def on(cls):
        if os.environ.get(bstack111ll_opy_ (u"ࠬࡈࡓࡠࡖࡈࡗ࡙ࡕࡐࡔࡡࡍ࡛࡙࠭ጰ"), None) is None or os.environ[bstack111ll_opy_ (u"࠭ࡂࡔࡡࡗࡉࡘ࡚ࡏࡑࡕࡢࡎ࡜࡚ࠧጱ")] == bstack111ll_opy_ (u"ࠢ࡯ࡷ࡯ࡰࠧጲ"):
            return False
        return True
    @classmethod
    def bstack11l1111l1l_opy_(cls):
        return bstack1l11lllll1_opy_(cls.bs_config.get(bstack111ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡢࡴࡧࡵࡺࡦࡨࡩ࡭࡫ࡷࡽࠬጳ"), False))
    @staticmethod
    def request_url(url):
        return bstack111ll_opy_ (u"ࠩࡾࢁ࠴ࢁࡽࠨጴ").format(bstack11l11l1lll_opy_, url)
    @staticmethod
    def default_headers():
        headers = {
            bstack111ll_opy_ (u"ࠪࡇࡴࡴࡴࡦࡰࡷ࠱࡙ࡿࡰࡦࠩጵ"): bstack111ll_opy_ (u"ࠫࡦࡶࡰ࡭࡫ࡦࡥࡹ࡯࡯࡯࠱࡭ࡷࡴࡴࠧጶ"),
            bstack111ll_opy_ (u"ࠬ࡞࠭ࡃࡕࡗࡅࡈࡑ࠭ࡕࡇࡖࡘࡔࡖࡓࠨጷ"): bstack111ll_opy_ (u"࠭ࡴࡳࡷࡨࠫጸ")
        }
        if os.environ.get(bstack111ll_opy_ (u"ࠧࡃࡕࡢࡘࡊ࡙ࡔࡐࡒࡖࡣࡏ࡝ࡔࠨጹ"), None):
            headers[bstack111ll_opy_ (u"ࠨࡃࡸࡸ࡭ࡵࡲࡪࡼࡤࡸ࡮ࡵ࡮ࠨጺ")] = bstack111ll_opy_ (u"ࠩࡅࡩࡦࡸࡥࡳࠢࡾࢁࠬጻ").format(os.environ[bstack111ll_opy_ (u"ࠥࡆࡘࡥࡔࡆࡕࡗࡓࡕ࡙࡟ࡋ࡙ࡗࠦጼ")])
        return headers
    @staticmethod
    def current_test_uuid():
        return getattr(threading.current_thread(), bstack111ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨጽ"), None)
    @staticmethod
    def bstack11l111ll1l_opy_(driver):
        return {
            bstack1l11ll111l_opy_(): bstack1l1l11l11l_opy_(driver)
        }
    @staticmethod
    def bstack11l1111lll_opy_(exception_info, report):
        return [{bstack111ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨጾ"): [exception_info.exconly(), report.longreprtext]}]
    @staticmethod
    def bstack1l1l11l111_opy_(typename):
        if bstack111ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࠤጿ") in typename:
            return bstack111ll_opy_ (u"ࠢࡂࡵࡶࡩࡷࡺࡩࡰࡰࡈࡶࡷࡵࡲࠣፀ")
        return bstack111ll_opy_ (u"ࠣࡗࡱ࡬ࡦࡴࡤ࡭ࡧࡧࡉࡷࡸ࡯ࡳࠤፁ")
    @staticmethod
    def bstack11l11l1ll1_opy_(func):
        def wrap(*args, **kwargs):
            if bstack1llll111ll_opy_.on():
                return func(*args, **kwargs)
            return
        return wrap
    @staticmethod
    def bstack11l1111ll1_opy_(test, hook_name=None):
        bstack11l11lllll_opy_ = test.parent
        if hook_name in [bstack111ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧፂ"), bstack111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫፃ"), bstack111ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪፄ"), bstack111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧፅ")]:
            bstack11l11lllll_opy_ = test
        scope = []
        while bstack11l11lllll_opy_ is not None:
            scope.append(bstack11l11lllll_opy_.name)
            bstack11l11lllll_opy_ = bstack11l11lllll_opy_.parent
        scope.reverse()
        return scope[2:]
    @staticmethod
    def bstack11l11ll1l1_opy_(hook_type):
        if hook_type == bstack111ll_opy_ (u"ࠨࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠦፆ"):
            return bstack111ll_opy_ (u"ࠢࡔࡧࡷࡹࡵࠦࡨࡰࡱ࡮ࠦፇ")
        elif hook_type == bstack111ll_opy_ (u"ࠣࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠧፈ"):
            return bstack111ll_opy_ (u"ࠤࡗࡩࡦࡸࡤࡰࡹࡱࠤ࡭ࡵ࡯࡬ࠤፉ")
    @staticmethod
    def bstack11l11ll1ll_opy_(bstack1llll111l1_opy_):
        try:
            if not bstack1llll111ll_opy_.on():
                return bstack1llll111l1_opy_
            if os.environ.get(bstack111ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡕࡉࡗ࡛ࡎࠣፊ"), None) == bstack111ll_opy_ (u"ࠦࡹࡸࡵࡦࠤፋ"):
                tests = os.environ.get(bstack111ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡗࡋࡒࡖࡐࡢࡘࡊ࡙ࡔࡔࠤፌ"), None)
                if tests is None or tests == bstack111ll_opy_ (u"ࠨ࡮ࡶ࡮࡯ࠦፍ"):
                    return bstack1llll111l1_opy_
                bstack1llll111l1_opy_ = tests.split(bstack111ll_opy_ (u"ࠧ࠭ࠩፎ"))
                return bstack1llll111l1_opy_
        except Exception as exc:
            print(bstack111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡳࡧࡵࡹࡳࠦࡨࡢࡰࡧࡰࡪࡸ࠺ࠡࠤፏ"), str(exc))
        return bstack1llll111l1_opy_
    @classmethod
    def bstack11l11l1l1l_opy_(cls, event: str, bstack11l11lll11_opy_: bstack11l1l11l11_opy_):
        bstack11l111l1ll_opy_ = {
            bstack111ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ፐ"): event,
            bstack11l11lll11_opy_.bstack11l1ll1111_opy_(): bstack11l11lll11_opy_.bstack11l1l1111l_opy_(event)
        }
        bstack1llll111ll_opy_.bstack11l1111l11_opy_(bstack11l111l1ll_opy_)