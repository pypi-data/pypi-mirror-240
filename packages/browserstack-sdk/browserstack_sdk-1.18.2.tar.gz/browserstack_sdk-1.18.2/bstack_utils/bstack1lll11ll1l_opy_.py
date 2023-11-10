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
import re
from bstack_utils.bstack11ll1l11ll_opy_ import bstack11ll1l1111_opy_
def bstack11ll1l1ll1_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᇷ")):
        return bstack111ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᇸ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᇹ")):
        return bstack111ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᇺ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᇻ")):
        return bstack111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᇼ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᇽ")):
        return bstack111ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᇾ")
def bstack11ll1l1l11_opy_(fixture_name):
    return bool(re.match(bstack111ll_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᇿ"), fixture_name))
def bstack11ll1ll1l1_opy_(fixture_name):
    return bool(re.match(bstack111ll_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪሀ"), fixture_name))
def bstack11ll1l11l1_opy_(fixture_name):
    return bool(re.match(bstack111ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪሁ"), fixture_name))
def bstack11ll1lll1l_opy_(fixture_name):
    if fixture_name.startswith(bstack111ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ሂ")):
        return bstack111ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ሃ"), bstack111ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫሄ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧህ")):
        return bstack111ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧሆ"), bstack111ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ሇ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨለ")):
        return bstack111ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨሉ"), bstack111ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩሊ")
    elif fixture_name.startswith(bstack111ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩላ")):
        return bstack111ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩሌ"), bstack111ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫል")
    return None, None
def bstack11ll1ll1ll_opy_(hook_name):
    if hook_name in [bstack111ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨሎ"), bstack111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬሏ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11ll1l111l_opy_(hook_name):
    if hook_name in [bstack111ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬሐ"), bstack111ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫሑ")]:
        return bstack111ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫሒ")
    elif hook_name in [bstack111ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ሓ"), bstack111ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ሔ")]:
        return bstack111ll_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ሕ")
    elif hook_name in [bstack111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧሖ"), bstack111ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ሗ")]:
        return bstack111ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩመ")
    elif hook_name in [bstack111ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨሙ"), bstack111ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨሚ")]:
        return bstack111ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫማ")
    return hook_name
def bstack11ll1ll11l_opy_(node, scenario):
    if hasattr(node, bstack111ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫሜ")):
        parts = node.nodeid.rsplit(bstack111ll_opy_ (u"ࠥ࡟ࠧም"))
        params = parts[-1]
        return bstack111ll_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦሞ").format(scenario.name, params)
    return scenario.name
def bstack11ll1l1l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111ll_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧሟ")):
            examples = list(node.callspec.params[bstack111ll_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬሠ")].values())
        return examples
    except:
        return []
def bstack11ll1lll11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11ll1ll111_opy_(report):
    try:
        status = bstack111ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧሡ")
        if report.passed or (report.failed and hasattr(report, bstack111ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥሢ"))):
            status = bstack111ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩሣ")
        elif report.skipped:
            status = bstack111ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫሤ")
        bstack11ll1l1111_opy_(status)
    except:
        pass
def bstack111l11ll1_opy_(status):
    try:
        bstack11ll1l1lll_opy_ = bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫሥ")
        if status == bstack111ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬሦ"):
            bstack11ll1l1lll_opy_ = bstack111ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ሧ")
        elif status == bstack111ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨረ"):
            bstack11ll1l1lll_opy_ = bstack111ll_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩሩ")
        bstack11ll1l1111_opy_(bstack11ll1l1lll_opy_)
    except:
        pass
def bstack11ll1llll1_opy_(item=None, report=None, summary=None, extra=None):
    return