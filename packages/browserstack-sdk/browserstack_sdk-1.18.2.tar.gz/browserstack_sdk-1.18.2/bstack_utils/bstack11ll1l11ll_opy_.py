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
import json
import os
import threading
from bstack_utils.helper import bstack1l1l11ll11_opy_, bstack11lll1ll1_opy_, bstack1l11l111l_opy_, bstack1l1ll1l11_opy_, \
    bstack1l11ll1ll1_opy_
def bstack11ll1ll1l_opy_(bstack11l1llll11_opy_):
    for driver in bstack11l1llll11_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1l1lllll1_opy_(type, name, status, reason, bstack1lll11ll11_opy_, bstack1l1l1l1l_opy_):
    bstack1lllllll11_opy_ = {
        bstack111ll_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩሪ"): type,
        bstack111ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ራ"): {}
    }
    if type == bstack111ll_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ሬ"):
        bstack1lllllll11_opy_[bstack111ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨር")][bstack111ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬሮ")] = bstack1lll11ll11_opy_
        bstack1lllllll11_opy_[bstack111ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪሯ")][bstack111ll_opy_ (u"ࠨࡦࡤࡸࡦ࠭ሰ")] = json.dumps(str(bstack1l1l1l1l_opy_))
    if type == bstack111ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪሱ"):
        bstack1lllllll11_opy_[bstack111ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ሲ")][bstack111ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩሳ")] = name
    if type == bstack111ll_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨሴ"):
        bstack1lllllll11_opy_[bstack111ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩስ")][bstack111ll_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧሶ")] = status
        if status == bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨሷ") and str(reason) != bstack111ll_opy_ (u"ࠤࠥሸ"):
            bstack1lllllll11_opy_[bstack111ll_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ሹ")][bstack111ll_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫሺ")] = json.dumps(str(reason))
    bstack111ll1l1l_opy_ = bstack111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪሻ").format(json.dumps(bstack1lllllll11_opy_))
    return bstack111ll1l1l_opy_
def bstack1llll111l_opy_(url, config, logger, bstack1llllll1l_opy_=False):
    hostname = bstack11lll1ll1_opy_(url)
    is_private = bstack1l1ll1l11_opy_(hostname)
    try:
        if is_private or bstack1llllll1l_opy_:
            file_path = bstack1l1l11ll11_opy_(bstack111ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ሼ"), bstack111ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ሽ"), logger)
            if os.environ.get(bstack111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ሾ")) and eval(
                    os.environ.get(bstack111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧሿ"))):
                return
            if (bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧቀ") in config and not config[bstack111ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨቁ")]):
                os.environ[bstack111ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪቂ")] = str(True)
                bstack11l1llll1l_opy_ = {bstack111ll_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨቃ"): hostname}
                bstack1l11ll1ll1_opy_(bstack111ll_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ቄ"), bstack111ll_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭ቅ"), bstack11l1llll1l_opy_, logger)
    except Exception as e:
        pass
def bstack1l1ll11l_opy_(caps, bstack11l1lll1ll_opy_):
    if bstack111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪቆ") in caps:
        caps[bstack111ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫቇ")][bstack111ll_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪቈ")] = True
        if bstack11l1lll1ll_opy_:
            caps[bstack111ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭቉")][bstack111ll_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨቊ")] = bstack11l1lll1ll_opy_
    else:
        caps[bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬቋ")] = True
        if bstack11l1lll1ll_opy_:
            caps[bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩቌ")] = bstack11l1lll1ll_opy_
def bstack11ll1l1111_opy_(bstack11l1lll11l_opy_):
    bstack11l1lll1l1_opy_ = bstack1l11l111l_opy_(threading.current_thread(), bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ቍ"), bstack111ll_opy_ (u"ࠪࠫ቎"))
    if bstack11l1lll1l1_opy_ == bstack111ll_opy_ (u"ࠫࠬ቏") or bstack11l1lll1l1_opy_ == bstack111ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ቐ"):
        threading.current_thread().testStatus = bstack11l1lll11l_opy_
    else:
        if bstack11l1lll11l_opy_ == bstack111ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ቑ"):
            threading.current_thread().testStatus = bstack11l1lll11l_opy_