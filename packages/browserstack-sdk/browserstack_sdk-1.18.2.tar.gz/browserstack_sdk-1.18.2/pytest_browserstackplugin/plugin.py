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
import atexit
import datetime
import inspect
import logging
import os
import sys
import threading
from uuid import uuid4
import pytest
from packaging import version
from browserstack_sdk.__init__ import (bstack1111l1ll1_opy_, bstack1l11l111_opy_, update, bstack11lll11ll_opy_,
                                       bstack11llll1l_opy_, bstack1l1ll1ll_opy_, bstack111l1lll1_opy_, bstack11ll1l1ll_opy_,
                                       bstack1lllll11_opy_, bstack1lll1ll11_opy_, bstack11111ll1l_opy_, bstack1llll1ll_opy_,
                                       bstack1l11lll1l_opy_, getAccessibilityResults, getAccessibilityResultsSummary)
from browserstack_sdk._version import __version__
from bstack_utils.capture import bstack1l1ll11ll1_opy_
from bstack_utils.constants import bstack1ll1ll1l1l_opy_, bstack1ll1l1l111_opy_, bstack111lll1l_opy_, bstack111l1111l_opy_, \
    bstack11lll1l11_opy_
from bstack_utils.helper import bstack1l11l111l_opy_, bstack111l1ll1l_opy_, bstack1l1l1l1l1l_opy_, bstack1lll1111l1_opy_, bstack1l1l1l1lll_opy_, \
    bstack1l11lll111_opy_, bstack1llllll11_opy_, bstack1lll1l1l_opy_, bstack1l1l111111_opy_, bstack1lll1l1ll1_opy_, Notset, \
    bstack1l11l11l_opy_, bstack1l11llllll_opy_, bstack1l11ll11ll_opy_, Result, bstack1l11ll1lll_opy_, bstack1l11ll1111_opy_, bstack1l1lll11ll_opy_
from bstack_utils.bstack1l11l11l1l_opy_ import bstack1l11l1ll11_opy_
from bstack_utils.messages import bstack1111l11l_opy_, bstack1ll11l1lll_opy_, bstack1111llll_opy_, bstack1lllll1l1_opy_, bstack1ll11l1ll1_opy_, \
    bstack11l111l1l_opy_, bstack11111111_opy_, bstack11lll1l1_opy_, bstack1l1lll11l_opy_, bstack1111lll1_opy_, \
    bstack1111llll1_opy_, bstack11l11l111_opy_
from bstack_utils.proxy import bstack1ll1llll11_opy_, bstack111111l1l_opy_
from bstack_utils.bstack1lll11ll1l_opy_ import bstack11ll1llll1_opy_, bstack11ll1ll1ll_opy_, bstack11ll1l111l_opy_, bstack11ll1ll1l1_opy_, \
    bstack11ll1l11l1_opy_, bstack11ll1ll11l_opy_, bstack11ll1lll11_opy_, bstack111l11ll1_opy_, bstack11ll1ll111_opy_
from bstack_utils.bstack11ll111111_opy_ import bstack11ll11111l_opy_
from bstack_utils.bstack11ll1l11ll_opy_ import bstack1l1lllll1_opy_, bstack1llll111l_opy_, bstack1l1ll11l_opy_
from bstack_utils.bstack11l1l1llll_opy_ import bstack11l1l11l1l_opy_
from bstack_utils.bstack1ll11111_opy_ import bstack1llll111ll_opy_
import bstack_utils.bstack1llll1l111_opy_ as bstack1ll1llll1_opy_
bstack1lll111ll1_opy_ = None
bstack1l1lll1ll_opy_ = None
bstack1lll1lll_opy_ = None
bstack11llllll_opy_ = None
bstack1l1l111ll_opy_ = None
bstack1l1l1lll_opy_ = None
bstack1lllll1l11_opy_ = None
bstack1111l11ll_opy_ = None
bstack11ll111l1_opy_ = None
bstack1llll1l1ll_opy_ = None
bstack11lll1ll_opy_ = None
bstack1ll11ll11l_opy_ = None
bstack11l1l1lll_opy_ = None
bstack1ll1lll1ll_opy_ = bstack111ll_opy_ (u"ࠪࠫፑ")
CONFIG = {}
bstack11l1ll1l_opy_ = False
bstack1llll1l11_opy_ = bstack111ll_opy_ (u"ࠫࠬፒ")
bstack1ll1111ll_opy_ = bstack111ll_opy_ (u"ࠬ࠭ፓ")
bstack1l1l111l1_opy_ = False
bstack1ll1ll11ll_opy_ = []
bstack1l1l1l1ll_opy_ = bstack1ll1l1l111_opy_
bstack111ll111ll_opy_ = bstack111ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ፔ")
bstack111lllll11_opy_ = False
logger = logging.getLogger(__name__)
logging.basicConfig(level=bstack1l1l1l1ll_opy_,
                    format=bstack111ll_opy_ (u"ࠧ࡝ࡰࠨࠬࡦࡹࡣࡵ࡫ࡰࡩ࠮ࡹࠠ࡜ࠧࠫࡲࡦࡳࡥࠪࡵࡠ࡟ࠪ࠮࡬ࡦࡸࡨࡰࡳࡧ࡭ࡦࠫࡶࡡࠥ࠳ࠠࠦࠪࡰࡩࡸࡹࡡࡨࡧࠬࡷࠬፕ"),
                    datefmt=bstack111ll_opy_ (u"ࠨࠧࡋ࠾ࠪࡓ࠺ࠦࡕࠪፖ"),
                    stream=sys.stdout)
store = {
    bstack111ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭ፗ"): []
}
def bstack11l11ll1_opy_():
    global CONFIG
    global bstack1l1l1l1ll_opy_
    if bstack111ll_opy_ (u"ࠪࡰࡴ࡭ࡌࡦࡸࡨࡰࠬፘ") in CONFIG:
        bstack1l1l1l1ll_opy_ = bstack1ll1ll1l1l_opy_[CONFIG[bstack111ll_opy_ (u"ࠫࡱࡵࡧࡍࡧࡹࡩࡱ࠭ፙ")]]
        logging.getLogger().setLevel(bstack1l1l1l1ll_opy_)
try:
    from playwright.sync_api import (
        BrowserContext,
        Page
    )
except:
    pass
import json
_111lllllll_opy_ = {}
current_test_uuid = None
def bstack1111l1ll_opy_(page, bstack1llll11l1_opy_):
    try:
        page.evaluate(bstack111ll_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨፚ"),
                      bstack111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࠥࡥࡨࡺࡩࡰࡰࠥ࠾ࠥࠨࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ࠭ࠢࠥࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸࠨ࠺ࠡࡽࠥࡲࡦࡳࡥࠣ࠼ࠪ፛") + json.dumps(
                          bstack1llll11l1_opy_) + bstack111ll_opy_ (u"ࠢࡾࡿࠥ፜"))
    except Exception as e:
        print(bstack111ll_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡴࡡ࡮ࡧࠣࡿࢂࠨ፝"), e)
def bstack1ll1l1llll_opy_(page, message, level):
    try:
        page.evaluate(bstack111ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ፞"), bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡥࡳࡴ࡯ࡵࡣࡷࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡦࡤࡸࡦࠨ࠺ࠨ፟") + json.dumps(
            message) + bstack111ll_opy_ (u"ࠫ࠱ࠨ࡬ࡦࡸࡨࡰࠧࡀࠧ፠") + json.dumps(level) + bstack111ll_opy_ (u"ࠬࢃࡽࠨ፡"))
    except Exception as e:
        print(bstack111ll_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦࡻࡾࠤ።"), e)
def bstack1lll1l1lll_opy_(page, status, message=bstack111ll_opy_ (u"ࠢࠣ፣")):
    try:
        if (status == bstack111ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣ፤")):
            page.evaluate(bstack111ll_opy_ (u"ࠤࡢࠤࡂࡄࠠࡼࡿࠥ፥"),
                          bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁࠢࡢࡥࡷ࡭ࡴࡴࠢ࠻ࠢࠥࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡵࡩࡦࡹ࡯࡯ࠤ࠽ࠫ፦") + json.dumps(
                              bstack111ll_opy_ (u"ࠦࡘࡩࡥ࡯ࡣࡵ࡭ࡴࠦࡦࡢ࡫࡯ࡩࡩࠦࡷࡪࡶ࡫࠾ࠥࠨ፧") + str(message)) + bstack111ll_opy_ (u"ࠬ࠲ࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ፨") + json.dumps(status) + bstack111ll_opy_ (u"ࠨࡽࡾࠤ፩"))
        else:
            page.evaluate(bstack111ll_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ፪"),
                          bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࡟ࡦࡺࡨࡧࡺࡺ࡯ࡳ࠼ࠣࡿࠧࡧࡣࡵ࡫ࡲࡲࠧࡀࠠࠣࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦ࠱ࠦࠢࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠥ࠾ࠥࢁࠢࡴࡶࡤࡸࡺࡹࠢ࠻ࠩ፫") + json.dumps(
                              status) + bstack111ll_opy_ (u"ࠤࢀࢁࠧ፬"))
    except Exception as e:
        print(bstack111ll_opy_ (u"ࠥࡩࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠦࡳࡦࡶࠣࡷࡪࡹࡳࡪࡱࡱࠤࡸࡺࡡࡵࡷࡶࠤࢀࢃࠢ፭"), e)
def pytest_configure(config):
    config.args = bstack1llll111ll_opy_.bstack11l11ll1ll_opy_(config.args)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    bstack111lll1111_opy_ = item.config.getoption(bstack111ll_opy_ (u"ࠫࡸࡱࡩࡱࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪ࠭፮"))
    plugins = item.config.getoption(bstack111ll_opy_ (u"ࠧࡶ࡬ࡶࡩ࡬ࡲࡸࠨ፯"))
    report = outcome.get_result()
    bstack111ll1l11l_opy_(item, call, report)
    if bstack111ll_opy_ (u"ࠨࡰࡺࡶࡨࡷࡹࡥࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡵࡲࡵࡨ࡫ࡱࠦ፰") not in plugins or bstack1lll1l1ll1_opy_():
        return
    summary = []
    driver = getattr(item, bstack111ll_opy_ (u"ࠢࡠࡦࡵ࡭ࡻ࡫ࡲࠣ፱"), None)
    page = getattr(item, bstack111ll_opy_ (u"ࠣࡡࡳࡥ࡬࡫ࠢ፲"), None)
    try:
        if (driver == None):
            driver = threading.current_thread().bstackSessionDriver
    except:
        pass
    item._driver = driver
    if (driver is not None):
        bstack111l1lll1l_opy_(item, report, summary, bstack111lll1111_opy_)
    if (page is not None):
        bstack111ll1ll11_opy_(item, report, summary, bstack111lll1111_opy_)
def bstack111l1lll1l_opy_(item, report, summary, bstack111lll1111_opy_):
    if report.when in [bstack111ll_opy_ (u"ࠤࡶࡩࡹࡻࡰࠣ፳"), bstack111ll_opy_ (u"ࠥࡸࡪࡧࡲࡥࡱࡺࡲࠧ፴")]:
        return
    if not bstack1l1l1l1l1l_opy_():
        return
    try:
        if (str(bstack111lll1111_opy_).lower() != bstack111ll_opy_ (u"ࠫࡹࡸࡵࡦࠩ፵")):
            item._driver.execute_script(
                bstack111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡐࡤࡱࡪࠨࠬࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼࠤࡱࡥࡲ࡫ࠢ࠻ࠢࠪ፶") + json.dumps(
                    report.nodeid) + bstack111ll_opy_ (u"࠭ࡽࡾࠩ፷"))
    except Exception as e:
        summary.append(
            bstack111ll_opy_ (u"ࠢࡘࡃࡕࡒࡎࡔࡇ࠻ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡳࡡࡳ࡭ࠣࡷࡪࡹࡳࡪࡱࡱࠤࡳࡧ࡭ࡦ࠼ࠣࡿ࠵ࢃࠢ፸").format(e)
        )
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ፹")))
    bstack1l1llllll_opy_ = bstack111ll_opy_ (u"ࠤࠥ፺")
    bstack11ll1ll111_opy_(report)
    if not passed:
        try:
            bstack1l1llllll_opy_ = report.longrepr.reprcrash
        except Exception as e:
            summary.append(
                bstack111ll_opy_ (u"࡛ࠥࡆࡘࡎࡊࡐࡊ࠾ࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡦࡨࡸࡪࡸ࡭ࡪࡰࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡸࡥࡢࡵࡲࡲ࠿ࠦࡻ࠱ࡿࠥ፻").format(e)
            )
        try:
            if (threading.current_thread().bstackTestErrorMessages == None):
                threading.current_thread().bstackTestErrorMessages = []
        except Exception as e:
            threading.current_thread().bstackTestErrorMessages = []
        threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1llllll_opy_))
    if not report.skipped:
        passed = report.passed or (report.failed and hasattr(report, bstack111ll_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ፼")))
        bstack1l1llllll_opy_ = bstack111ll_opy_ (u"ࠧࠨ፽")
        if not passed:
            try:
                bstack1l1llllll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll_opy_ (u"ࠨࡗࡂࡔࡑࡍࡓࡍ࠺ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡩ࡫ࡴࡦࡴࡰ࡭ࡳ࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡴࡨࡥࡸࡵ࡮࠻ࠢࡾ࠴ࢂࠨ፾").format(e)
                )
            try:
                if (threading.current_thread().bstackTestErrorMessages == None):
                    threading.current_thread().bstackTestErrorMessages = []
            except Exception as e:
                threading.current_thread().bstackTestErrorMessages = []
            threading.current_thread().bstackTestErrorMessages.append(str(bstack1l1llllll_opy_))
        try:
            if passed:
                item._driver.execute_script(
                    bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡥࡥࡹࡧࡦࡹࡹࡵࡲ࠻ࠢࡾࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡤࡲࡳࡵࡴࡢࡶࡨࠦ࠱ࠦ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧࡀࠠࡼ࡞ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣ࡮ࡨࡺࡪࡲࠢ࠻ࠢࠥ࡭ࡳ࡬࡯ࠣ࠮ࠣࡠࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡨࡦࡺࡡࠣ࠼ࠣࠫ፿")
                    + json.dumps(bstack111ll_opy_ (u"ࠣࡲࡤࡷࡸ࡫ࡤࠢࠤᎀ"))
                    + bstack111ll_opy_ (u"ࠤ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࢂࡢࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࠧᎁ")
                )
            else:
                item._driver.execute_script(
                    bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡨࡼࡪࡩࡵࡵࡱࡵ࠾ࠥࢁ࡜ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡤࡧࡹ࡯࡯࡯ࠤ࠽ࠤࠧࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠢ࠭ࠢ࡟ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣ࠼ࠣࡿࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡱ࡫ࡶࡦ࡮ࠥ࠾ࠥࠨࡥࡳࡴࡲࡶࠧ࠲ࠠ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡥࡣࡷࡥࠧࡀࠠࠨᎂ")
                    + json.dumps(str(bstack1l1llllll_opy_))
                    + bstack111ll_opy_ (u"ࠦࡡࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽ࡝ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢃࠢᎃ")
                )
        except Exception as e:
            summary.append(bstack111ll_opy_ (u"ࠧ࡝ࡁࡓࡐࡌࡒࡌࡀࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡥࡳࡴ࡯ࡵࡣࡷࡩ࠿ࠦࡻ࠱ࡿࠥᎄ").format(e))
def bstack111ll1ll11_opy_(item, report, summary, bstack111lll1111_opy_):
    if report.when in [bstack111ll_opy_ (u"ࠨࡳࡦࡶࡸࡴࠧᎅ"), bstack111ll_opy_ (u"ࠢࡵࡧࡤࡶࡩࡵࡷ࡯ࠤᎆ")]:
        return
    if (str(bstack111lll1111_opy_).lower() != bstack111ll_opy_ (u"ࠨࡶࡵࡹࡪ࠭ᎇ")):
        bstack1111l1ll_opy_(item._page, report.nodeid)
    passed = report.passed or report.skipped or (report.failed and hasattr(report, bstack111ll_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦᎈ")))
    bstack1l1llllll_opy_ = bstack111ll_opy_ (u"ࠥࠦᎉ")
    bstack11ll1ll111_opy_(report)
    if not report.skipped:
        if not passed:
            try:
                bstack1l1llllll_opy_ = report.longrepr.reprcrash
            except Exception as e:
                summary.append(
                    bstack111ll_opy_ (u"ࠦ࡜ࡇࡒࡏࡋࡑࡋ࠿ࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡧࡩࡹ࡫ࡲ࡮࡫ࡱࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡲࡦࡣࡶࡳࡳࡀࠠࡼ࠲ࢀࠦᎊ").format(e)
                )
        try:
            if passed:
                bstack1lll1l1lll_opy_(item._page, bstack111ll_opy_ (u"ࠧࡶࡡࡴࡵࡨࡨࠧᎋ"))
            else:
                if bstack1l1llllll_opy_:
                    bstack1ll1l1llll_opy_(item._page, str(bstack1l1llllll_opy_), bstack111ll_opy_ (u"ࠨࡥࡳࡴࡲࡶࠧᎌ"))
                    bstack1lll1l1lll_opy_(item._page, bstack111ll_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪࠢᎍ"), str(bstack1l1llllll_opy_))
                else:
                    bstack1lll1l1lll_opy_(item._page, bstack111ll_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࠣᎎ"))
        except Exception as e:
            summary.append(bstack111ll_opy_ (u"ࠤ࡚ࡅࡗࡔࡉࡏࡉ࠽ࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡶࡲࡧࡥࡹ࡫ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳ࠻ࠢࡾ࠴ࢂࠨᎏ").format(e))
try:
    from typing import Generator
    import pytest_playwright.pytest_playwright as p
    @pytest.fixture
    def page(context: BrowserContext, request: pytest.FixtureRequest) -> Generator[Page, None, None]:
        page = context.new_page()
        request.node._page = page
        yield page
except:
    pass
def pytest_addoption(parser):
    parser.addoption(bstack111ll_opy_ (u"ࠥ࠱࠲ࡹ࡫ࡪࡲࡖࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠢ᎐"), default=bstack111ll_opy_ (u"ࠦࡋࡧ࡬ࡴࡧࠥ᎑"), help=bstack111ll_opy_ (u"ࠧࡇࡵࡵࡱࡰࡥࡹ࡯ࡣࠡࡵࡨࡸࠥࡹࡥࡴࡵ࡬ࡳࡳࠦ࡮ࡢ࡯ࡨࠦ᎒"))
    try:
        import pytest_selenium.pytest_selenium
    except:
        parser.addoption(bstack111ll_opy_ (u"ࠨ࠭࠮ࡦࡵ࡭ࡻ࡫ࡲࠣ᎓"), action=bstack111ll_opy_ (u"ࠢࡴࡶࡲࡶࡪࠨ᎔"), default=bstack111ll_opy_ (u"ࠣࡥ࡫ࡶࡴࡳࡥࠣ᎕"),
                         help=bstack111ll_opy_ (u"ࠤࡇࡶ࡮ࡼࡥࡳࠢࡷࡳࠥࡸࡵ࡯ࠢࡷࡩࡸࡺࡳࠣ᎖"))
def bstack111ll11ll1_opy_(log):
    if not (log[bstack111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᎗")] and log[bstack111ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬ᎘")].strip()):
        return
    active = bstack111ll11l11_opy_()
    log = {
        bstack111ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᎙"): log[bstack111ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᎚")],
        bstack111ll_opy_ (u"ࠧࡵ࡫ࡰࡩࡸࡺࡡ࡮ࡲࠪ᎛"): datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠨ࡜ࠪ᎜"),
        bstack111ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪ᎝"): log[bstack111ll_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫ᎞")],
    }
    if active:
        if active[bstack111ll_opy_ (u"ࠫࡹࡿࡰࡦࠩ᎟")] == bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪᎠ"):
            log[bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭Ꭱ")] = active[bstack111ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᎢ")]
        elif active[bstack111ll_opy_ (u"ࠨࡶࡼࡴࡪ࠭Ꭳ")] == bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺࠧᎤ"):
            log[bstack111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤࡻࡵࡪࡦࠪᎥ")] = active[bstack111ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳࡥࡵࡶ࡫ࡧࠫᎦ")]
    bstack1llll111ll_opy_.bstack11l11ll11l_opy_([log])
def bstack111ll11l11_opy_():
    if len(store[bstack111ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡨࡰࡱ࡮ࡣࡺࡻࡩࡥࠩᎧ")]) > 0 and store[bstack111ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟ࡩࡱࡲ࡯ࡤࡻࡵࡪࡦࠪᎨ")][-1]:
        return {
            bstack111ll_opy_ (u"ࠧࡵࡻࡳࡩࠬᎩ"): bstack111ll_opy_ (u"ࠨࡪࡲࡳࡰ࠭Ꭺ"),
            bstack111ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࡣࡺࡻࡩࡥࠩᎫ"): store[bstack111ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᎬ")][-1]
        }
    if store.get(bstack111ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᎭ"), None):
        return {
            bstack111ll_opy_ (u"ࠬࡺࡹࡱࡧࠪᎮ"): bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࠫᎯ"),
            bstack111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡࡸࡹ࡮ࡪࠧᎰ"): store[bstack111ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᎱ")]
        }
    return None
bstack111llllll1_opy_ = bstack1l1ll11ll1_opy_(bstack111ll11ll1_opy_)
def pytest_runtest_call(item):
    try:
        global CONFIG
        global bstack111lllll11_opy_
        if bstack111lllll11_opy_:
            driver = getattr(item, bstack111ll_opy_ (u"ࠩࡢࡨࡷ࡯ࡶࡦࡴࠪᎲ"), None)
            bstack111l1lllll_opy_ = bstack1ll1llll1_opy_.bstack1l1lll1ll1_opy_(CONFIG, bstack1l11lll111_opy_(item.own_markers))
            item._a11y_started = bstack1ll1llll1_opy_.bstack1l1ll1ll1l_opy_(driver, bstack111l1lllll_opy_)
        if not bstack1llll111ll_opy_.on() or bstack111ll111ll_opy_ != bstack111ll_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᎳ"):
            return
        global current_test_uuid, bstack111llllll1_opy_
        bstack111llllll1_opy_.start()
        bstack111ll1llll_opy_ = {
            bstack111ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᎴ"): uuid4().__str__(),
            bstack111ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᎵ"): datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"࡚࠭ࠨᎶ")
        }
        current_test_uuid = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᎷ")]
        store[bstack111ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡶࡷ࡬ࡨࠬᎸ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᎹ")]
        threading.current_thread().current_test_uuid = current_test_uuid
        _111lllllll_opy_[item.nodeid] = {**_111lllllll_opy_[item.nodeid], **bstack111ll1llll_opy_}
        bstack11l111111l_opy_(item, _111lllllll_opy_[item.nodeid], bstack111ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡗࡹࡧࡲࡵࡧࡧࠫᎺ"))
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡶࡺࡴࡴࡦࡵࡷࡣࡨࡧ࡬࡭࠼ࠣࡿࢂ࠭Ꮋ"), str(err))
def pytest_runtest_setup(item):
    if bstack1l1l111111_opy_():
        atexit.register(bstack11ll1ll1l_opy_)
        try:
            item.config.hook.pytest_selenium_runtest_makereport = bstack11ll1llll1_opy_
        except Exception as err:
            threading.current_thread().testStatus = bstack111ll_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᎼ")
    try:
        if not bstack1llll111ll_opy_.on():
            return
        bstack111llllll1_opy_.start()
        uuid = uuid4().__str__()
        bstack111ll1llll_opy_ = {
            bstack111ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᎽ"): uuid,
            bstack111ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᎾ"): datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠨ࡜ࠪᎿ"),
            bstack111ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᏀ"): bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᏁ"),
            bstack111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᏂ"): bstack111ll_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᏃ"),
            bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᏄ"): bstack111ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭Ꮕ")
        }
        threading.current_thread().bstack111ll1l1l1_opy_ = uuid
        store[bstack111ll_opy_ (u"ࠨࡥࡸࡶࡷ࡫࡮ࡵࡡࡷࡩࡸࡺ࡟ࡪࡶࡨࡱࠬᏆ")] = item
        store[bstack111ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢ࡬ࡴࡵ࡫ࡠࡷࡸ࡭ࡩ࠭Ꮗ")] = [uuid]
        if not _111lllllll_opy_.get(item.nodeid, None):
            _111lllllll_opy_[item.nodeid] = {bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᏈ"): [], bstack111ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭Ꮙ"): []}
        _111lllllll_opy_[item.nodeid][bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᏊ")].append(bstack111ll1llll_opy_[bstack111ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᏋ")])
        _111lllllll_opy_[item.nodeid + bstack111ll_opy_ (u"ࠧ࠮ࡵࡨࡸࡺࡶࠧᏌ")] = bstack111ll1llll_opy_
        bstack11l11111l1_opy_(item, bstack111ll1llll_opy_, bstack111ll_opy_ (u"ࠨࡊࡲࡳࡰࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᏍ"))
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡴࡸࡲࡹ࡫ࡳࡵࡡࡶࡩࡹࡻࡰ࠻ࠢࡾࢁࠬᏎ"), str(err))
def pytest_runtest_teardown(item):
    try:
        if getattr(item, bstack111ll_opy_ (u"ࠪࡣࡦ࠷࠱ࡺࡡࡶࡸࡦࡸࡴࡦࡦࠪᏏ"), False):
            logger.info(bstack111ll_opy_ (u"ࠦࡆࡻࡴࡰ࡯ࡤࡸࡪࠦࡴࡦࡵࡷࠤࡨࡧࡳࡦࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠥ࡮ࡡࡴࠢࡨࡲࡩ࡫ࡤ࠯ࠢࡓࡶࡴࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡦ࡮ࡲࡩࡵࡻࠣࡸࡪࡹࡴࡪࡰࡪࠤ࡮ࡹࠠࡶࡰࡧࡩࡷࡽࡡࡺ࠰ࠣࠦᏐ"))
            driver = getattr(item, bstack111ll_opy_ (u"ࠬࡥࡤࡳ࡫ࡹࡩࡷ࠭Ꮡ"), None)
            bstack1ll1llll1_opy_.bstack1l1ll1l1ll_opy_(driver, item)
        if not bstack1llll111ll_opy_.on():
            return
        bstack111ll1llll_opy_ = {
            bstack111ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᏒ"): uuid4().__str__(),
            bstack111ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᏓ"): datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠨ࡜ࠪᏔ"),
            bstack111ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᏕ"): bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᏖ"),
            bstack111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧᏗ"): bstack111ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᏘ"),
            bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᏙ"): bstack111ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᏚ")
        }
        _111lllllll_opy_[item.nodeid + bstack111ll_opy_ (u"ࠨ࠯ࡷࡩࡦࡸࡤࡰࡹࡱࠫᏛ")] = bstack111ll1llll_opy_
        bstack11l11111l1_opy_(item, bstack111ll1llll_opy_, bstack111ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᏜ"))
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡳࡽࡹ࡫ࡳࡵࡡࡵࡹࡳࡺࡥࡴࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲ࠿ࠦࡻࡾࠩᏝ"), str(err))
@pytest.hookimpl(hookwrapper=True)
def pytest_fixture_setup(fixturedef, request):
    if not bstack1llll111ll_opy_.on():
        yield
        return
    start_time = datetime.datetime.now()
    if bstack11ll1ll1l1_opy_(fixturedef.argname):
        store[bstack111ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡯ࡴࡦ࡯ࠪᏞ")] = request.node
    elif bstack11ll1l11l1_opy_(fixturedef.argname):
        store[bstack111ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡣ࡭ࡣࡶࡷࡤ࡯ࡴࡦ࡯ࠪᏟ")] = request.node
    outcome = yield
    try:
        fixture = {
            bstack111ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᏠ"): fixturedef.argname,
            bstack111ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᏡ"): bstack1l1l1l1lll_opy_(outcome),
            bstack111ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪᏢ"): (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
        bstack111ll11lll_opy_ = store[bstack111ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡸࡪࡹࡴࡠ࡫ࡷࡩࡲ࠭Ꮳ")]
        if not _111lllllll_opy_.get(bstack111ll11lll_opy_.nodeid, None):
            _111lllllll_opy_[bstack111ll11lll_opy_.nodeid] = {bstack111ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᏤ"): []}
        _111lllllll_opy_[bstack111ll11lll_opy_.nodeid][bstack111ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭Ꮵ")].append(fixture)
    except Exception as err:
        logger.debug(bstack111ll_opy_ (u"ࠬࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡵࡿࡴࡦࡵࡷࡣ࡫࡯ࡸࡵࡷࡵࡩࡤࡹࡥࡵࡷࡳ࠾ࠥࢁࡽࠨᏦ"), str(err))
if bstack1lll1l1ll1_opy_() and bstack1llll111ll_opy_.on():
    def pytest_bdd_before_step(request, step):
        try:
            _111lllllll_opy_[request.node.nodeid][bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᏧ")].bstack11l1ll11l1_opy_(id(step))
        except Exception as err:
            print(bstack111ll_opy_ (u"ࠧࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡦࡪ࡬࡯ࡳࡧࡢࡷࡹ࡫ࡰ࠻ࠢࡾࢁࠬᏨ"), str(err))
    def pytest_bdd_step_error(request, step, exception):
        try:
            _111lllllll_opy_[request.node.nodeid][bstack111ll_opy_ (u"ࠨࡶࡨࡷࡹࡥࡤࡢࡶࡤࠫᏩ")].bstack11l1l111ll_opy_(id(step), Result.failed(exception=exception))
        except Exception as err:
            print(bstack111ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡹࡴࡦࡲࡢࡩࡷࡸ࡯ࡳ࠼ࠣࡿࢂ࠭Ꮺ"), str(err))
    def pytest_bdd_after_step(request, step):
        try:
            bstack11l1l1llll_opy_: bstack11l1l11l1l_opy_ = _111lllllll_opy_[request.node.nodeid][bstack111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡦࡤࡸࡦ࠭Ꮻ")]
            bstack11l1l1llll_opy_.bstack11l1l111ll_opy_(id(step), Result.passed())
        except Exception as err:
            print(bstack111ll_opy_ (u"ࠫࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡴࡶࡨࡴࡤ࡫ࡲࡳࡱࡵ࠾ࠥࢁࡽࠨᏬ"), str(err))
    def pytest_bdd_before_scenario(request, feature, scenario):
        global bstack111ll111ll_opy_
        try:
            if not bstack1llll111ll_opy_.on() or bstack111ll111ll_opy_ != bstack111ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠩᏭ"):
                return
            global bstack111llllll1_opy_
            bstack111llllll1_opy_.start()
            if not _111lllllll_opy_.get(request.node.nodeid, None):
                _111lllllll_opy_[request.node.nodeid] = {}
            bstack11l1l1llll_opy_ = bstack11l1l11l1l_opy_.bstack11l1l1lll1_opy_(
                scenario, feature, request.node,
                name=bstack11ll1ll11l_opy_(request.node, scenario),
                bstack11l1l1l1l1_opy_=bstack1lll1111l1_opy_(),
                file_path=feature.filename,
                scope=[feature.name],
                framework=bstack111ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨᏮ"),
                tags=bstack11ll1lll11_opy_(feature, scenario)
            )
            _111lllllll_opy_[request.node.nodeid][bstack111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᏯ")] = bstack11l1l1llll_opy_
            bstack111lllll1l_opy_(bstack11l1l1llll_opy_.uuid)
            bstack1llll111ll_opy_.bstack11l11l1l1l_opy_(bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᏰ"), bstack11l1l1llll_opy_)
        except Exception as err:
            print(bstack111ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤࡨࡥࡧࡱࡵࡩࡤࡹࡣࡦࡰࡤࡶ࡮ࡵ࠺ࠡࡽࢀࠫᏱ"), str(err))
def bstack111ll1l111_opy_(bstack111l1llll1_opy_):
    if bstack111l1llll1_opy_ in store[bstack111ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᏲ")]:
        store[bstack111ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤ࡮࡯ࡰ࡭ࡢࡹࡺ࡯ࡤࠨᏳ")].remove(bstack111l1llll1_opy_)
def bstack111lllll1l_opy_(bstack111llll11l_opy_):
    store[bstack111ll_opy_ (u"ࠬࡩࡵࡳࡴࡨࡲࡹࡥࡴࡦࡵࡷࡣࡺࡻࡩࡥࠩᏴ")] = bstack111llll11l_opy_
    threading.current_thread().current_test_uuid = bstack111llll11l_opy_
@bstack1llll111ll_opy_.bstack11l11l1ll1_opy_
def bstack111ll1l11l_opy_(item, call, report):
    global bstack111ll111ll_opy_
    try:
        if report.when == bstack111ll_opy_ (u"࠭ࡣࡢ࡮࡯ࠫᏵ"):
            bstack111llllll1_opy_.reset()
        if report.when == bstack111ll_opy_ (u"ࠧࡤࡣ࡯ࡰࠬ᏶"):
            if bstack111ll111ll_opy_ == bstack111ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ᏷"):
                _111lllllll_opy_[item.nodeid][bstack111ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᏸ")] = bstack1l11ll1lll_opy_(report.stop)
                bstack11l111111l_opy_(item, _111lllllll_opy_[item.nodeid], bstack111ll_opy_ (u"ࠪࡘࡪࡹࡴࡓࡷࡱࡊ࡮ࡴࡩࡴࡪࡨࡨࠬᏹ"), report, call)
                store[bstack111ll_opy_ (u"ࠫࡨࡻࡲࡳࡧࡱࡸࡤࡺࡥࡴࡶࡢࡹࡺ࡯ࡤࠨᏺ")] = None
            elif bstack111ll111ll_opy_ == bstack111ll_opy_ (u"ࠧࡶࡹࡵࡧࡶࡸ࠲ࡨࡤࡥࠤᏻ"):
                bstack11l1l1llll_opy_ = _111lllllll_opy_[item.nodeid][bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᏼ")]
                bstack11l1l1llll_opy_.set(hooks=_111lllllll_opy_[item.nodeid].get(bstack111ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ᏽ"), []))
                exception, bstack1l1l1l1111_opy_ = None, None
                if call.excinfo:
                    exception = call.excinfo.value
                    bstack1l1l1l1111_opy_ = [call.excinfo.exconly(), report.longreprtext]
                bstack11l1l1llll_opy_.stop(time=bstack1l11ll1lll_opy_(report.stop), result=Result(result=report.outcome, exception=exception, bstack1l1l1l1111_opy_=bstack1l1l1l1111_opy_))
                bstack1llll111ll_opy_.bstack11l11l1l1l_opy_(bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪ᏾"), _111lllllll_opy_[item.nodeid][bstack111ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡥࡣࡷࡥࠬ᏿")])
        elif report.when in [bstack111ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ᐀"), bstack111ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭ᐁ")]:
            bstack111lll111l_opy_ = item.nodeid + bstack111ll_opy_ (u"ࠬ࠳ࠧᐂ") + report.when
            if report.skipped:
                hook_type = bstack111ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᐃ") if report.when == bstack111ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᐄ") else bstack111ll_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᐅ")
                _111lllllll_opy_[bstack111lll111l_opy_] = {
                    bstack111ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᐆ"): uuid4().__str__(),
                    bstack111ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᐇ"): datetime.datetime.utcfromtimestamp(report.start).isoformat() + bstack111ll_opy_ (u"ࠫ࡟࠭ᐈ"),
                    bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᐉ"): hook_type
                }
            _111lllllll_opy_[bstack111lll111l_opy_][bstack111ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᐊ")] = datetime.datetime.utcfromtimestamp(report.stop).isoformat() + bstack111ll_opy_ (u"࡛ࠧࠩᐋ")
            bstack111ll1l111_opy_(_111lllllll_opy_[bstack111lll111l_opy_][bstack111ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᐌ")])
            bstack11l11111l1_opy_(item, _111lllllll_opy_[bstack111lll111l_opy_], bstack111ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᐍ"), report, call)
            if report.when == bstack111ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᐎ"):
                if report.outcome == bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᐏ"):
                    bstack111ll1llll_opy_ = {
                        bstack111ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᐐ"): uuid4().__str__(),
                        bstack111ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪᐑ"): bstack1lll1111l1_opy_(),
                        bstack111ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᐒ"): bstack1lll1111l1_opy_()
                    }
                    _111lllllll_opy_[item.nodeid] = {**_111lllllll_opy_[item.nodeid], **bstack111ll1llll_opy_}
                    bstack11l111111l_opy_(item, _111lllllll_opy_[item.nodeid], bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡕࡷࡥࡷࡺࡥࡥࠩᐓ"))
                    bstack11l111111l_opy_(item, _111lllllll_opy_[item.nodeid], bstack111ll_opy_ (u"ࠩࡗࡩࡸࡺࡒࡶࡰࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫᐔ"), report, call)
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠪࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢ࡫ࡥࡳࡪ࡬ࡦࡡࡲ࠵࠶ࡿ࡟ࡵࡧࡶࡸࡤ࡫ࡶࡦࡰࡷ࠾ࠥࢁࡽࠨᐕ"), str(err))
def bstack111lll11l1_opy_(test, bstack111ll1llll_opy_, result=None, call=None, bstack1lll111ll_opy_=None, outcome=None):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    bstack11l1l1llll_opy_ = {
        bstack111ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᐖ"): bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠬࡻࡵࡪࡦࠪᐗ")],
        bstack111ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᐘ"): bstack111ll_opy_ (u"ࠧࡵࡧࡶࡸࠬᐙ"),
        bstack111ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᐚ"): test.name,
        bstack111ll_opy_ (u"ࠩࡥࡳࡩࡿࠧᐛ"): {
            bstack111ll_opy_ (u"ࠪࡰࡦࡴࡧࠨᐜ"): bstack111ll_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫᐝ"),
            bstack111ll_opy_ (u"ࠬࡩ࡯ࡥࡧࠪᐞ"): inspect.getsource(test.obj)
        },
        bstack111ll_opy_ (u"࠭ࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᐟ"): test.name,
        bstack111ll_opy_ (u"ࠧࡴࡥࡲࡴࡪ࠭ᐠ"): test.name,
        bstack111ll_opy_ (u"ࠨࡵࡦࡳࡵ࡫ࡳࠨᐡ"): bstack1llll111ll_opy_.bstack11l1111ll1_opy_(test),
        bstack111ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬᐢ"): file_path,
        bstack111ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬᐣ"): file_path,
        bstack111ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᐤ"): bstack111ll_opy_ (u"ࠬࡶࡥ࡯ࡦ࡬ࡲ࡬࠭ᐥ"),
        bstack111ll_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫᐦ"): file_path,
        bstack111ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫᐧ"): bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬᐨ")],
        bstack111ll_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᐩ"): bstack111ll_opy_ (u"ࠪࡔࡾࡺࡥࡴࡶࠪᐪ"),
        bstack111ll_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧᐫ"): {
            bstack111ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩᐬ"): test.nodeid
        },
        bstack111ll_opy_ (u"࠭ࡴࡢࡩࡶࠫᐭ"): bstack1l11lll111_opy_(test.own_markers)
    }
    if bstack1lll111ll_opy_ in [bstack111ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᐮ"), bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᐯ")]:
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠩࡰࡩࡹࡧࠧᐰ")] = {
            bstack111ll_opy_ (u"ࠪࡪ࡮ࡾࡴࡶࡴࡨࡷࠬᐱ"): bstack111ll1llll_opy_.get(bstack111ll_opy_ (u"ࠫ࡫࡯ࡸࡵࡷࡵࡩࡸ࠭ᐲ"), [])
        }
    if bstack1lll111ll_opy_ == bstack111ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙࡫ࡪࡲࡳࡩࡩ࠭ᐳ"):
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᐴ")] = bstack111ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᐵ")
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧᐶ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨᐷ")]
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᐸ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᐹ")]
    if result:
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬᐺ")] = result.outcome
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧᐻ")] = result.duration * 1000
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᐼ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᐽ")]
        if result.failed:
            bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᐾ")] = bstack1llll111ll_opy_.bstack1l1l11l111_opy_(call.excinfo.typename)
            bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫᐿ")] = bstack1llll111ll_opy_.bstack11l1111lll_opy_(call.excinfo, result)
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᑀ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᑁ")]
    if outcome:
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᑂ")] = bstack1l1l1l1lll_opy_(outcome)
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨᑃ")] = 0
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ᑄ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧᑅ")]
        if bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᑆ")] == bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᑇ"):
            bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫᑈ")] = bstack111ll_opy_ (u"࠭ࡕ࡯ࡪࡤࡲࡩࡲࡥࡥࡇࡵࡶࡴࡸࠧᑉ")  # bstack111lll11ll_opy_
            bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨᑊ")] = [{bstack111ll_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫᑋ"): [bstack111ll_opy_ (u"ࠩࡶࡳࡲ࡫ࠠࡦࡴࡵࡳࡷ࠭ᑌ")]}]
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩᑍ")] = bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪᑎ")]
    return bstack11l1l1llll_opy_
def bstack111llll111_opy_(test, bstack11l1111111_opy_, bstack1lll111ll_opy_, result, call, outcome, bstack111ll111l1_opy_):
    file_path = os.path.relpath(test.fspath.strpath, start=os.getcwd())
    hook_type = bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨᑏ")]
    hook_name = bstack11l1111111_opy_[bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡳࡧ࡭ࡦࠩᑐ")]
    hook_data = {
        bstack111ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᑑ"): bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᑒ")],
        bstack111ll_opy_ (u"ࠩࡷࡽࡵ࡫ࠧᑓ"): bstack111ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨᑔ"),
        bstack111ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᑕ"): bstack111ll_opy_ (u"ࠬࢁࡽࠨᑖ").format(bstack11ll1ll1ll_opy_(hook_name)),
        bstack111ll_opy_ (u"࠭ࡢࡰࡦࡼࠫᑗ"): {
            bstack111ll_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬᑘ"): bstack111ll_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨᑙ"),
            bstack111ll_opy_ (u"ࠩࡦࡳࡩ࡫ࠧᑚ"): None
        },
        bstack111ll_opy_ (u"ࠪࡷࡨࡵࡰࡦࠩᑛ"): test.name,
        bstack111ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫᑜ"): bstack1llll111ll_opy_.bstack11l1111ll1_opy_(test, hook_name),
        bstack111ll_opy_ (u"ࠬ࡬ࡩ࡭ࡧࡢࡲࡦࡳࡥࠨᑝ"): file_path,
        bstack111ll_opy_ (u"࠭࡬ࡰࡥࡤࡸ࡮ࡵ࡮ࠨᑞ"): file_path,
        bstack111ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑟ"): bstack111ll_opy_ (u"ࠨࡲࡨࡲࡩ࡯࡮ࡨࠩᑠ"),
        bstack111ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧᑡ"): file_path,
        bstack111ll_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧᑢ"): bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠫࡸࡺࡡࡳࡶࡨࡨࡤࡧࡴࠨᑣ")],
        bstack111ll_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᑤ"): bstack111ll_opy_ (u"࠭ࡐࡺࡶࡨࡷࡹ࠳ࡣࡶࡥࡸࡱࡧ࡫ࡲࠨᑥ") if bstack111ll111ll_opy_ == bstack111ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠫᑦ") else bstack111ll_opy_ (u"ࠨࡒࡼࡸࡪࡹࡴࠨᑧ"),
        bstack111ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡵࡻࡳࡩࠬᑨ"): hook_type
    }
    bstack111ll11111_opy_ = bstack111ll11l1l_opy_(_111lllllll_opy_.get(test.nodeid, None))
    if bstack111ll11111_opy_:
        hook_data[bstack111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࡤ࡯ࡤࠨᑩ")] = bstack111ll11111_opy_
    if result:
        hook_data[bstack111ll_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫᑪ")] = result.outcome
        hook_data[bstack111ll_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴ࡟ࡪࡰࡢࡱࡸ࠭ᑫ")] = result.duration * 1000
        hook_data[bstack111ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᑬ")] = bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬᑭ")]
        if result.failed:
            hook_data[bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᑮ")] = bstack1llll111ll_opy_.bstack1l1l11l111_opy_(call.excinfo.typename)
            hook_data[bstack111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᑯ")] = bstack1llll111ll_opy_.bstack11l1111lll_opy_(call.excinfo, result)
    if outcome:
        hook_data[bstack111ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪᑰ")] = bstack1l1l1l1lll_opy_(outcome)
        hook_data[bstack111ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳࡥࡩ࡯ࡡࡰࡷࠬᑱ")] = 100
        hook_data[bstack111ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᑲ")] = bstack11l1111111_opy_[bstack111ll_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫᑳ")]
        if hook_data[bstack111ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑴ")] == bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᑵ"):
            hook_data[bstack111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࡢࡸࡾࡶࡥࠨᑶ")] = bstack111ll_opy_ (u"࡙ࠪࡳ࡮ࡡ࡯ࡦ࡯ࡩࡩࡋࡲࡳࡱࡵࠫᑷ")  # bstack111lll11ll_opy_
            hook_data[bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬᑸ")] = [{bstack111ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᑹ"): [bstack111ll_opy_ (u"࠭ࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠪᑺ")]}]
    if bstack111ll111l1_opy_:
        hook_data[bstack111ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧᑻ")] = bstack111ll111l1_opy_.result
        hook_data[bstack111ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩᑼ")] = bstack1l11llllll_opy_(bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ᑽ")], bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨᑾ")])
        hook_data[bstack111ll_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩᑿ")] = bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᒀ")]
        if hook_data[bstack111ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ᒁ")] == bstack111ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᒂ"):
            hook_data[bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࡡࡷࡽࡵ࡫ࠧᒃ")] = bstack1llll111ll_opy_.bstack1l1l11l111_opy_(bstack111ll111l1_opy_.exception_type)
            hook_data[bstack111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪᒄ")] = [{bstack111ll_opy_ (u"ࠪࡦࡦࡩ࡫ࡵࡴࡤࡧࡪ࠭ᒅ"): bstack1l11ll11ll_opy_(bstack111ll111l1_opy_.exception)}]
    return hook_data
def bstack11l111111l_opy_(test, bstack111ll1llll_opy_, bstack1lll111ll_opy_, result=None, call=None, outcome=None):
    bstack11l1l1llll_opy_ = bstack111lll11l1_opy_(test, bstack111ll1llll_opy_, result, call, bstack1lll111ll_opy_, outcome)
    driver = getattr(test, bstack111ll_opy_ (u"ࠫࡤࡪࡲࡪࡸࡨࡶࠬᒆ"), None)
    if bstack1lll111ll_opy_ == bstack111ll_opy_ (u"࡚ࠬࡥࡴࡶࡕࡹࡳ࡙ࡴࡢࡴࡷࡩࡩ࠭ᒇ") and driver:
        bstack11l1l1llll_opy_[bstack111ll_opy_ (u"࠭ࡩ࡯ࡶࡨ࡫ࡷࡧࡴࡪࡱࡱࡷࠬᒈ")] = bstack1llll111ll_opy_.bstack11l111ll1l_opy_(driver)
    if bstack1lll111ll_opy_ == bstack111ll_opy_ (u"ࠧࡕࡧࡶࡸࡗࡻ࡮ࡔ࡭࡬ࡴࡵ࡫ࡤࠨᒉ"):
        bstack1lll111ll_opy_ = bstack111ll_opy_ (u"ࠨࡖࡨࡷࡹࡘࡵ࡯ࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪᒊ")
    bstack11l111l1ll_opy_ = {
        bstack111ll_opy_ (u"ࠩࡨࡺࡪࡴࡴࡠࡶࡼࡴࡪ࠭ᒋ"): bstack1lll111ll_opy_,
        bstack111ll_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬᒌ"): bstack11l1l1llll_opy_
    }
    bstack1llll111ll_opy_.bstack11l1111l11_opy_(bstack11l111l1ll_opy_)
def bstack11l11111l1_opy_(test, bstack111ll1llll_opy_, bstack1lll111ll_opy_, result=None, call=None, outcome=None, bstack111ll111l1_opy_=None):
    hook_data = bstack111llll111_opy_(test, bstack111ll1llll_opy_, bstack1lll111ll_opy_, result, call, outcome, bstack111ll111l1_opy_)
    bstack11l111l1ll_opy_ = {
        bstack111ll_opy_ (u"ࠫࡪࡼࡥ࡯ࡶࡢࡸࡾࡶࡥࠨᒍ"): bstack1lll111ll_opy_,
        bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡶࡺࡴࠧᒎ"): hook_data
    }
    bstack1llll111ll_opy_.bstack11l1111l11_opy_(bstack11l111l1ll_opy_)
def bstack111ll11l1l_opy_(bstack111ll1llll_opy_):
    if not bstack111ll1llll_opy_:
        return None
    if bstack111ll1llll_opy_.get(bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡩࡧࡴࡢࠩᒏ"), None):
        return getattr(bstack111ll1llll_opy_[bstack111ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡪࡡࡵࡣࠪᒐ")], bstack111ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ᒑ"), None)
    return bstack111ll1llll_opy_.get(bstack111ll_opy_ (u"ࠩࡸࡹ࡮ࡪࠧᒒ"), None)
@pytest.fixture(autouse=True)
def second_fixture(caplog, request):
    yield
    try:
        if not bstack1llll111ll_opy_.on():
            return
        places = [bstack111ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩᒓ"), bstack111ll_opy_ (u"ࠫࡨࡧ࡬࡭ࠩᒔ"), bstack111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᒕ")]
        bstack11l111ll11_opy_ = []
        for bstack111lll1lll_opy_ in places:
            records = caplog.get_records(bstack111lll1lll_opy_)
            bstack111ll1lll1_opy_ = bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᒖ") if bstack111lll1lll_opy_ == bstack111ll_opy_ (u"ࠧࡤࡣ࡯ࡰࠬᒗ") else bstack111ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࡢࡹࡺ࡯ࡤࠨᒘ")
            bstack111ll1l1ll_opy_ = request.node.nodeid + (bstack111ll_opy_ (u"ࠩࠪᒙ") if bstack111lll1lll_opy_ == bstack111ll_opy_ (u"ࠪࡧࡦࡲ࡬ࠨᒚ") else bstack111ll_opy_ (u"ࠫ࠲࠭ᒛ") + bstack111lll1lll_opy_)
            bstack111llll11l_opy_ = bstack111ll11l1l_opy_(_111lllllll_opy_.get(bstack111ll1l1ll_opy_, None))
            if not bstack111llll11l_opy_:
                continue
            for record in records:
                if bstack1l11ll1111_opy_(record.message):
                    continue
                bstack11l111ll11_opy_.append({
                    bstack111ll_opy_ (u"ࠬࡺࡩ࡮ࡧࡶࡸࡦࡳࡰࠨᒜ"): datetime.datetime.utcfromtimestamp(record.created).isoformat() + bstack111ll_opy_ (u"࡚࠭ࠨᒝ"),
                    bstack111ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᒞ"): record.levelname,
                    bstack111ll_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩᒟ"): record.message,
                    bstack111ll1lll1_opy_: bstack111llll11l_opy_
                })
        if len(bstack11l111ll11_opy_) > 0:
            bstack1llll111ll_opy_.bstack11l11ll11l_opy_(bstack11l111ll11_opy_)
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠩࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡧࡴࡴࡤࡠࡨ࡬ࡼࡹࡻࡲࡦ࠼ࠣࡿࢂ࠭ᒠ"), str(err))
def bstack111lll1l11_opy_(driver_command, response):
    if driver_command == bstack111ll_opy_ (u"ࠪࡷࡨࡸࡥࡦࡰࡶ࡬ࡴࡺࠧᒡ"):
        bstack1llll111ll_opy_.bstack11l111lll1_opy_({
            bstack111ll_opy_ (u"ࠫ࡮ࡳࡡࡨࡧࠪᒢ"): response[bstack111ll_opy_ (u"ࠬࡼࡡ࡭ࡷࡨࠫᒣ")],
            bstack111ll_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠࡷࡸ࡭ࡩ࠭ᒤ"): store[bstack111ll_opy_ (u"ࠧࡤࡷࡵࡶࡪࡴࡴࡠࡶࡨࡷࡹࡥࡵࡶ࡫ࡧࠫᒥ")]
        })
def bstack11ll1ll1l_opy_():
    global bstack1ll1ll11ll_opy_
    bstack1llll111ll_opy_.bstack11l11lll1l_opy_()
    for driver in bstack1ll1ll11ll_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
def bstack1ll1lllll1_opy_(self, *args, **kwargs):
    bstack1lll1lll1l_opy_ = bstack1lll111ll1_opy_(self, *args, **kwargs)
    bstack1llll111ll_opy_.bstack1llll1111l_opy_(self)
    return bstack1lll1lll1l_opy_
def bstack1ll1ll1l_opy_(framework_name):
    global bstack1ll1lll1ll_opy_
    global bstack1l1ll1ll1_opy_
    bstack1ll1lll1ll_opy_ = framework_name
    logger.info(bstack11l11l111_opy_.format(bstack1ll1lll1ll_opy_.split(bstack111ll_opy_ (u"ࠨ࠯ࠪᒦ"))[0]))
    try:
        from selenium import webdriver
        from selenium.webdriver.common.service import Service
        from selenium.webdriver.remote.webdriver import WebDriver
        if bstack1l1l1l1l1l_opy_():
            Service.start = bstack111l1lll1_opy_
            Service.stop = bstack11ll1l1ll_opy_
            webdriver.Remote.__init__ = bstack11ll1111_opy_
            webdriver.Remote.get = bstack11l1ll111_opy_
            if not isinstance(os.getenv(bstack111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡒ࡜ࡘࡊ࡙ࡔࡠࡒࡄࡖࡆࡒࡌࡆࡎࠪᒧ")), str):
                return
            WebDriver.close = bstack1lllll11_opy_
            WebDriver.quit = bstack1111lllll_opy_
            WebDriver.getAccessibilityResults = getAccessibilityResults
            WebDriver.getAccessibilityResultsSummary = getAccessibilityResultsSummary
        if not bstack1l1l1l1l1l_opy_() and bstack1llll111ll_opy_.on():
            webdriver.Remote.__init__ = bstack1ll1lllll1_opy_
        bstack1l1ll1ll1_opy_ = True
    except Exception as e:
        pass
    bstack111ll11l_opy_()
    if os.environ.get(bstack111ll_opy_ (u"ࠪࡗࡊࡒࡅࡏࡋࡘࡑࡤࡕࡒࡠࡒࡏࡅ࡞࡝ࡒࡊࡉࡋࡘࡤࡏࡎࡔࡖࡄࡐࡑࡋࡄࠨᒨ")):
        bstack1l1ll1ll1_opy_ = eval(os.environ.get(bstack111ll_opy_ (u"ࠫࡘࡋࡌࡆࡐࡌ࡙ࡒࡥࡏࡓࡡࡓࡐࡆ࡟ࡗࡓࡋࡊࡌ࡙ࡥࡉࡏࡕࡗࡅࡑࡒࡅࡅࠩᒩ")))
    if not bstack1l1ll1ll1_opy_:
        bstack11111ll1l_opy_(bstack111ll_opy_ (u"ࠧࡖࡡࡤ࡭ࡤ࡫ࡪࡹࠠ࡯ࡱࡷࠤ࡮ࡴࡳࡵࡣ࡯ࡰࡪࡪࠢᒪ"), bstack1111llll1_opy_)
    if bstack1lll1l1l1l_opy_():
        try:
            from selenium.webdriver.remote.remote_connection import RemoteConnection
            RemoteConnection._get_proxy_url = bstack1l11l1l11_opy_
        except Exception as e:
            logger.error(bstack11l111l1l_opy_.format(str(e)))
    if bstack111ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᒫ") in str(framework_name).lower():
        if not bstack1l1l1l1l1l_opy_():
            return
        try:
            from pytest_selenium import pytest_selenium
            from _pytest.config import Config
            pytest_selenium.pytest_report_header = bstack11llll1l_opy_
            from pytest_selenium.drivers import browserstack
            browserstack.pytest_selenium_runtest_makereport = bstack1l1ll1ll_opy_
            Config.getoption = bstack1lllllll1l_opy_
        except Exception as e:
            pass
        try:
            from pytest_bdd import reporting
            reporting.runtest_makereport = bstack1lll1lll11_opy_
        except Exception as e:
            pass
def bstack1111lllll_opy_(self):
    global bstack1ll1lll1ll_opy_
    global bstack11ll11lll_opy_
    global bstack1l1lll1ll_opy_
    try:
        if bstack111ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᒬ") in bstack1ll1lll1ll_opy_ and self.session_id != None and bstack1l11l111l_opy_(threading.current_thread(), bstack111ll_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬᒭ"), bstack111ll_opy_ (u"ࠩࠪᒮ")) != bstack111ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᒯ"):
            bstack1lll111l1l_opy_ = bstack111ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᒰ") if len(threading.current_thread().bstackTestErrorMessages) == 0 else bstack111ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᒱ")
            bstack111ll111l_opy_ = bstack1l1lllll1_opy_(bstack111ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᒲ"), bstack111ll_opy_ (u"ࠧࠨᒳ"), bstack1lll111l1l_opy_, bstack111ll_opy_ (u"ࠨ࠮ࠣࠫᒴ").join(
                threading.current_thread().bstackTestErrorMessages), bstack111ll_opy_ (u"ࠩࠪᒵ"), bstack111ll_opy_ (u"ࠪࠫᒶ"))
            if self != None:
                self.execute_script(bstack111ll111l_opy_)
    except Exception as e:
        logger.debug(bstack111ll_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡻ࡭࡯࡬ࡦࠢࡰࡥࡷࡱࡩ࡯ࡩࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࠧᒷ") + str(e))
    bstack1l1lll1ll_opy_(self)
    self.session_id = None
def bstack11ll1111_opy_(self, command_executor,
             desired_capabilities=None, browser_profile=None, proxy=None,
             keep_alive=True, file_detector=None, options=None):
    global CONFIG
    global bstack11ll11lll_opy_
    global bstack1l111l1l_opy_
    global bstack1l1l111l1_opy_
    global bstack1ll1lll1ll_opy_
    global bstack1lll111ll1_opy_
    global bstack1ll1ll11ll_opy_
    global bstack1llll1l11_opy_
    global bstack1ll1111ll_opy_
    global bstack111lllll11_opy_
    CONFIG[bstack111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᒸ")] = str(bstack1ll1lll1ll_opy_) + str(__version__)
    command_executor = bstack1lll1l1l_opy_(bstack1llll1l11_opy_)
    logger.debug(bstack1lllll1l1_opy_.format(command_executor))
    proxy = bstack1l11lll1l_opy_(CONFIG, proxy)
    bstack111llll1l_opy_ = 0
    try:
        if bstack1l1l111l1_opy_ is True:
            bstack111llll1l_opy_ = int(os.environ.get(bstack111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᒹ")))
    except:
        bstack111llll1l_opy_ = 0
    bstack1ll11lll1l_opy_ = bstack1111l1ll1_opy_(CONFIG, bstack111llll1l_opy_)
    logger.debug(bstack11lll1l1_opy_.format(str(bstack1ll11lll1l_opy_)))
    if bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࠫᒺ") in CONFIG and CONFIG[bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᒻ")]:
        bstack1l1ll11l_opy_(bstack1ll11lll1l_opy_, bstack1ll1111ll_opy_)
    if desired_capabilities:
        bstack1lllll1lll_opy_ = bstack1l11l111_opy_(desired_capabilities)
        bstack1lllll1lll_opy_[bstack111ll_opy_ (u"ࠩࡸࡷࡪ࡝࠳ࡄࠩᒼ")] = bstack1l11l11l_opy_(CONFIG)
        bstack1ll11lll11_opy_ = bstack1111l1ll1_opy_(bstack1lllll1lll_opy_)
        if bstack1ll11lll11_opy_:
            bstack1ll11lll1l_opy_ = update(bstack1ll11lll11_opy_, bstack1ll11lll1l_opy_)
        desired_capabilities = None
    if options:
        bstack1lll1ll11_opy_(options, bstack1ll11lll1l_opy_)
    if not options:
        options = bstack11lll11ll_opy_(bstack1ll11lll1l_opy_)
    if bstack1ll1llll1_opy_.bstack111llllll_opy_(CONFIG, bstack111llll1l_opy_) and bstack1ll1llll1_opy_.bstack11ll11l1_opy_(bstack1ll11lll1l_opy_, options):
        bstack111lllll11_opy_ = True
        bstack1ll1llll1_opy_.set_capabilities(bstack1ll11lll1l_opy_, CONFIG)
    if proxy and bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"ࠪ࠸࠳࠷࠰࠯࠲ࠪᒽ")):
        options.proxy(proxy)
    if options and bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"ࠫ࠸࠴࠸࠯࠲ࠪᒾ")):
        desired_capabilities = None
    if (
            not options and not desired_capabilities
    ) or (
            bstack1llllll11_opy_() < version.parse(bstack111ll_opy_ (u"ࠬ࠹࠮࠹࠰࠳ࠫᒿ")) and not desired_capabilities
    ):
        desired_capabilities = {}
        desired_capabilities.update(bstack1ll11lll1l_opy_)
    logger.info(bstack1111llll_opy_)
    if bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"࠭࠴࠯࠳࠳࠲࠵࠭ᓀ")):
        bstack1lll111ll1_opy_(self, command_executor=command_executor,
                  options=options, keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"ࠧ࠴࠰࠻࠲࠵࠭ᓁ")):
        bstack1lll111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities, options=options,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    elif bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"ࠨ࠴࠱࠹࠸࠴࠰ࠨᓂ")):
        bstack1lll111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive, file_detector=file_detector)
    else:
        bstack1lll111ll1_opy_(self, command_executor=command_executor,
                  desired_capabilities=desired_capabilities,
                  browser_profile=browser_profile, proxy=proxy,
                  keep_alive=keep_alive)
    try:
        bstack11lll111_opy_ = bstack111ll_opy_ (u"ࠩࠪᓃ")
        if bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"ࠪ࠸࠳࠶࠮࠱ࡤ࠴ࠫᓄ")):
            bstack11lll111_opy_ = self.caps.get(bstack111ll_opy_ (u"ࠦࡴࡶࡴࡪ࡯ࡤࡰࡍࡻࡢࡖࡴ࡯ࠦᓅ"))
        else:
            bstack11lll111_opy_ = self.capabilities.get(bstack111ll_opy_ (u"ࠧࡵࡰࡵ࡫ࡰࡥࡱࡎࡵࡣࡗࡵࡰࠧᓆ"))
        if bstack11lll111_opy_:
            if bstack1llllll11_opy_() <= version.parse(bstack111ll_opy_ (u"࠭࠳࠯࠳࠶࠲࠵࠭ᓇ")):
                self.command_executor._url = bstack111ll_opy_ (u"ࠢࡩࡶࡷࡴ࠿࠵࠯ࠣᓈ") + bstack1llll1l11_opy_ + bstack111ll_opy_ (u"ࠣ࠼࠻࠴࠴ࡽࡤ࠰ࡪࡸࡦࠧᓉ")
            else:
                self.command_executor._url = bstack111ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦᓊ") + bstack11lll111_opy_ + bstack111ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦᓋ")
            logger.debug(bstack1ll11l1lll_opy_.format(bstack11lll111_opy_))
        else:
            logger.debug(bstack1111l11l_opy_.format(bstack111ll_opy_ (u"ࠦࡔࡶࡴࡪ࡯ࡤࡰࠥࡎࡵࡣࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨࠧᓌ")))
    except Exception as e:
        logger.debug(bstack1111l11l_opy_.format(e))
    bstack11ll11lll_opy_ = self.session_id
    if bstack111ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᓍ") in bstack1ll1lll1ll_opy_:
        threading.current_thread().bstack1llll1l11l_opy_ = self.session_id
        threading.current_thread().bstackSessionDriver = self
        threading.current_thread().bstackTestErrorMessages = []
        bstack1llll111ll_opy_.bstack1llll1111l_opy_(self)
    bstack1ll1ll11ll_opy_.append(self)
    if bstack111ll_opy_ (u"࠭ࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡴࠩᓎ") in CONFIG and bstack111ll_opy_ (u"ࠧࡴࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠬᓏ") in CONFIG[bstack111ll_opy_ (u"ࠨࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡶࠫᓐ")][bstack111llll1l_opy_]:
        bstack1l111l1l_opy_ = CONFIG[bstack111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᓑ")][bstack111llll1l_opy_][bstack111ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᓒ")]
    logger.debug(bstack1111lll1_opy_.format(bstack11ll11lll_opy_))
def bstack11l1ll111_opy_(self, url):
    global bstack11ll111l1_opy_
    global CONFIG
    try:
        bstack1llll111l_opy_(url, CONFIG, logger)
    except Exception as err:
        logger.debug(bstack1l1lll11l_opy_.format(str(err)))
    try:
        bstack11ll111l1_opy_(self, url)
    except Exception as e:
        try:
            bstack11ll1111l_opy_ = str(e)
            if any(err_msg in bstack11ll1111l_opy_ for err_msg in bstack111l1111l_opy_):
                bstack1llll111l_opy_(url, CONFIG, logger, True)
        except Exception as err:
            logger.debug(bstack1l1lll11l_opy_.format(str(err)))
        raise e
def bstack1ll111ll1_opy_(item, when):
    global bstack1ll11ll11l_opy_
    try:
        bstack1ll11ll11l_opy_(item, when)
    except Exception as e:
        pass
def bstack1lll1lll11_opy_(item, call, rep):
    global bstack11l1l1lll_opy_
    global bstack1ll1ll11ll_opy_
    name = bstack111ll_opy_ (u"ࠫࠬᓓ")
    try:
        if rep.when == bstack111ll_opy_ (u"ࠬࡩࡡ࡭࡮ࠪᓔ"):
            bstack11ll11lll_opy_ = threading.current_thread().bstack1llll1l11l_opy_
            bstack111lll1111_opy_ = item.config.getoption(bstack111ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡗࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᓕ"))
            try:
                if (str(bstack111lll1111_opy_).lower() != bstack111ll_opy_ (u"ࠧࡵࡴࡸࡩࠬᓖ")):
                    name = str(rep.nodeid)
                    bstack111ll111l_opy_ = bstack1l1lllll1_opy_(bstack111ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩᓗ"), name, bstack111ll_opy_ (u"ࠩࠪᓘ"), bstack111ll_opy_ (u"ࠪࠫᓙ"), bstack111ll_opy_ (u"ࠫࠬᓚ"), bstack111ll_opy_ (u"ࠬ࠭ᓛ"))
                    for driver in bstack1ll1ll11ll_opy_:
                        if bstack11ll11lll_opy_ == driver.session_id:
                            driver.execute_script(bstack111ll111l_opy_)
            except Exception as e:
                logger.debug(bstack111ll_opy_ (u"࠭ࡅࡳࡴࡲࡶࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࡑࡥࡲ࡫ࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭ᓜ").format(str(e)))
            try:
                bstack111l11ll1_opy_(rep.outcome.lower())
                if rep.outcome.lower() != bstack111ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᓝ"):
                    status = bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᓞ") if rep.outcome.lower() == bstack111ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᓟ") else bstack111ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᓠ")
                    reason = bstack111ll_opy_ (u"ࠫࠬᓡ")
                    if status == bstack111ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᓢ"):
                        reason = rep.longrepr.reprcrash.message
                        if (not threading.current_thread().bstackTestErrorMessages):
                            threading.current_thread().bstackTestErrorMessages = []
                        threading.current_thread().bstackTestErrorMessages.append(reason)
                    level = bstack111ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᓣ") if status == bstack111ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᓤ") else bstack111ll_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᓥ")
                    data = name + bstack111ll_opy_ (u"ࠩࠣࡴࡦࡹࡳࡦࡦࠤࠫᓦ") if status == bstack111ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᓧ") else name + bstack111ll_opy_ (u"ࠫࠥ࡬ࡡࡪ࡮ࡨࡨࠦࠦࠧᓨ") + reason
                    bstack1l1ll111_opy_ = bstack1l1lllll1_opy_(bstack111ll_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᓩ"), bstack111ll_opy_ (u"࠭ࠧᓪ"), bstack111ll_opy_ (u"ࠧࠨᓫ"), bstack111ll_opy_ (u"ࠨࠩᓬ"), level, data)
                    for driver in bstack1ll1ll11ll_opy_:
                        if bstack11ll11lll_opy_ == driver.session_id:
                            driver.execute_script(bstack1l1ll111_opy_)
            except Exception as e:
                logger.debug(bstack111ll_opy_ (u"ࠩࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡣࡰࡰࡷࡩࡽࡺࠠࡧࡱࡵࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡵࡨࡷࡸ࡯࡯࡯࠼ࠣࡿࢂ࠭ᓭ").format(str(e)))
    except Exception as e:
        logger.debug(bstack111ll_opy_ (u"ࠪࡉࡷࡸ࡯ࡳࠢ࡬ࡲࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡣࡷࡩࠥ࡯࡮ࠡࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠥࡺࡥࡴࡶࠣࡷࡹࡧࡴࡶࡵ࠽ࠤࢀࢃࠧᓮ").format(str(e)))
    bstack11l1l1lll_opy_(item, call, rep)
notset = Notset()
def bstack1lllllll1l_opy_(self, name: str, default=notset, skip: bool = False):
    global bstack11lll1ll_opy_
    if str(name).lower() == bstack111ll_opy_ (u"ࠫࡩࡸࡩࡷࡧࡵࠫᓯ"):
        return bstack111ll_opy_ (u"ࠧࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠦᓰ")
    else:
        return bstack11lll1ll_opy_(self, name, default, skip)
def bstack1l11l1l11_opy_(self):
    global CONFIG
    global bstack1lllll1l11_opy_
    try:
        proxy = bstack1ll1llll11_opy_(CONFIG)
        if proxy:
            if proxy.endswith(bstack111ll_opy_ (u"࠭࠮ࡱࡣࡦࠫᓱ")):
                proxies = bstack111111l1l_opy_(proxy, bstack1lll1l1l_opy_())
                if len(proxies) > 0:
                    protocol, bstack1ll11l111l_opy_ = proxies.popitem()
                    if bstack111ll_opy_ (u"ࠢ࠻࠱࠲ࠦᓲ") in bstack1ll11l111l_opy_:
                        return bstack1ll11l111l_opy_
                    else:
                        return bstack111ll_opy_ (u"ࠣࡪࡷࡸࡵࡀ࠯࠰ࠤᓳ") + bstack1ll11l111l_opy_
            else:
                return proxy
    except Exception as e:
        logger.error(bstack111ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡫ࡱࠤࡸ࡫ࡴࡵ࡫ࡱ࡫ࠥࡶࡲࡰࡺࡼࠤࡺࡸ࡬ࠡ࠼ࠣࡿࢂࠨᓴ").format(str(e)))
    return bstack1lllll1l11_opy_(self)
def bstack1lll1l1l1l_opy_():
    return (bstack111ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᓵ") in CONFIG or bstack111ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡵࡓࡶࡴࡾࡹࠨᓶ") in CONFIG) and bstack111l1ll1l_opy_() and bstack1llllll11_opy_() >= version.parse(
        bstack111lll1l_opy_)
def bstack1lll1llll_opy_(self,
               executablePath=None,
               channel=None,
               args=None,
               ignoreDefaultArgs=None,
               handleSIGINT=None,
               handleSIGTERM=None,
               handleSIGHUP=None,
               timeout=None,
               env=None,
               headless=None,
               devtools=None,
               proxy=None,
               downloadsPath=None,
               slowMo=None,
               tracesDir=None,
               chromiumSandbox=None,
               firefoxUserPrefs=None
               ):
    global CONFIG
    global bstack1l111l1l_opy_
    global bstack1l1l111l1_opy_
    global bstack1ll1lll1ll_opy_
    CONFIG[bstack111ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡗࡉࡑࠧᓷ")] = str(bstack1ll1lll1ll_opy_) + str(__version__)
    bstack111llll1l_opy_ = 0
    try:
        if bstack1l1l111l1_opy_ is True:
            bstack111llll1l_opy_ = int(os.environ.get(bstack111ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᓸ")))
    except:
        bstack111llll1l_opy_ = 0
    CONFIG[bstack111ll_opy_ (u"ࠢࡪࡵࡓࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨᓹ")] = True
    bstack1ll11lll1l_opy_ = bstack1111l1ll1_opy_(CONFIG, bstack111llll1l_opy_)
    logger.debug(bstack11lll1l1_opy_.format(str(bstack1ll11lll1l_opy_)))
    if CONFIG.get(bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࡌࡰࡥࡤࡰࠬᓺ")):
        bstack1l1ll11l_opy_(bstack1ll11lll1l_opy_, bstack1ll1111ll_opy_)
    if bstack111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᓻ") in CONFIG and bstack111ll_opy_ (u"ࠪࡷࡪࡹࡳࡪࡱࡱࡒࡦࡳࡥࠨᓼ") in CONFIG[bstack111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲࡹࠧᓽ")][bstack111llll1l_opy_]:
        bstack1l111l1l_opy_ = CONFIG[bstack111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡳࠨᓾ")][bstack111llll1l_opy_][bstack111ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᓿ")]
    import urllib
    import json
    bstack1l1111l1_opy_ = bstack111ll_opy_ (u"ࠧࡸࡵࡶ࠾࠴࠵ࡣࡥࡲ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠰ࡦࡳࡲ࠵ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࡂࡧࡦࡶࡳ࠾ࠩᔀ") + urllib.parse.quote(json.dumps(bstack1ll11lll1l_opy_))
    browser = self.connect(bstack1l1111l1_opy_)
    return browser
def bstack111ll11l_opy_():
    global bstack1l1ll1ll1_opy_
    try:
        from playwright._impl._browser_type import BrowserType
        BrowserType.launch = bstack1lll1llll_opy_
        bstack1l1ll1ll1_opy_ = True
    except Exception as e:
        pass
def bstack111lll1ll1_opy_():
    global CONFIG
    global bstack11l1ll1l_opy_
    global bstack1llll1l11_opy_
    global bstack1ll1111ll_opy_
    global bstack1l1l111l1_opy_
    CONFIG = json.loads(os.environ.get(bstack111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡄࡑࡑࡊࡎࡍࠧᔁ")))
    bstack11l1ll1l_opy_ = eval(os.environ.get(bstack111ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡋࡖࡣࡆࡖࡐࡠࡃࡘࡘࡔࡓࡁࡕࡇࠪᔂ")))
    bstack1llll1l11_opy_ = os.environ.get(bstack111ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡋ࡙ࡇࡥࡕࡓࡎࠪᔃ"))
    bstack1llll1ll_opy_(CONFIG, bstack11l1ll1l_opy_)
    bstack11l11ll1_opy_()
    global bstack1lll111ll1_opy_
    global bstack1l1lll1ll_opy_
    global bstack1lll1lll_opy_
    global bstack11llllll_opy_
    global bstack1l1l111ll_opy_
    global bstack1l1l1lll_opy_
    global bstack1111l11ll_opy_
    global bstack11ll111l1_opy_
    global bstack1lllll1l11_opy_
    global bstack11lll1ll_opy_
    global bstack1ll11ll11l_opy_
    global bstack11l1l1lll_opy_
    try:
        from selenium import webdriver
        from selenium.webdriver.remote.webdriver import WebDriver
        bstack1lll111ll1_opy_ = webdriver.Remote.__init__
        bstack1l1lll1ll_opy_ = WebDriver.quit
        bstack1111l11ll_opy_ = WebDriver.close
        bstack11ll111l1_opy_ = WebDriver.get
    except Exception as e:
        pass
    if (bstack111ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᔄ") in CONFIG or bstack111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᔅ") in CONFIG) and bstack111l1ll1l_opy_():
        if bstack1llllll11_opy_() < version.parse(bstack111lll1l_opy_):
            logger.error(bstack11111111_opy_.format(bstack1llllll11_opy_()))
        else:
            try:
                from selenium.webdriver.remote.remote_connection import RemoteConnection
                bstack1lllll1l11_opy_ = RemoteConnection._get_proxy_url
            except Exception as e:
                logger.error(bstack11l111l1l_opy_.format(str(e)))
    try:
        from _pytest.config import Config
        bstack11lll1ll_opy_ = Config.getoption
        from _pytest import runner
        bstack1ll11ll11l_opy_ = runner._update_current_test_var
    except Exception as e:
        logger.warn(e, bstack1ll11l1ll1_opy_)
    try:
        from pytest_bdd import reporting
        bstack11l1l1lll_opy_ = reporting.runtest_makereport
    except Exception as e:
        logger.debug(bstack111ll_opy_ (u"࠭ࡐ࡭ࡧࡤࡷࡪࠦࡩ࡯ࡵࡷࡥࡱࡲࠠࡱࡻࡷࡩࡸࡺ࠭ࡣࡦࡧࠤࡹࡵࠠࡳࡷࡱࠤࡵࡿࡴࡦࡵࡷ࠱ࡧࡪࡤࠡࡶࡨࡷࡹࡹࠧᔆ"))
    bstack1ll1111ll_opy_ = CONFIG.get(bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࡒ࡯ࡤࡣ࡯ࡓࡵࡺࡩࡰࡰࡶࠫᔇ"), {}).get(bstack111ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᔈ"))
    bstack1l1l111l1_opy_ = True
    bstack1ll1ll1l_opy_(bstack11lll1l11_opy_)
if (bstack1l1l111111_opy_()):
    bstack111lll1ll1_opy_()
@bstack1l1lll11ll_opy_(class_method=False)
def bstack111lll1l1l_opy_(hook_name, event, bstack111ll1111l_opy_=None):
    if hook_name not in [bstack111ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᔉ"), bstack111ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᔊ"), bstack111ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᔋ"), bstack111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᔌ"), bstack111ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᔍ"), bstack111ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᔎ"), bstack111ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᔏ"), bstack111ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᔐ")]:
        return
    node = store[bstack111ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣࡹ࡫ࡳࡵࡡ࡬ࡸࡪࡳࠧᔑ")]
    if hook_name in [bstack111ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᔒ"), bstack111ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᔓ")]:
        node = store[bstack111ll_opy_ (u"࠭ࡣࡶࡴࡵࡩࡳࡺ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡪࡶࡨࡱࠬᔔ")]
    elif hook_name in [bstack111ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᔕ"), bstack111ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩᔖ")]:
        node = store[bstack111ll_opy_ (u"ࠩࡦࡹࡷࡸࡥ࡯ࡶࡢࡧࡱࡧࡳࡴࡡ࡬ࡸࡪࡳࠧᔗ")]
    if event == bstack111ll_opy_ (u"ࠪࡦࡪ࡬࡯ࡳࡧࠪᔘ"):
        hook_type = bstack11ll1l111l_opy_(hook_name)
        uuid = uuid4().__str__()
        bstack11l1111111_opy_ = {
            bstack111ll_opy_ (u"ࠫࡺࡻࡩࡥࠩᔙ"): uuid,
            bstack111ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩᔚ"): bstack1lll1111l1_opy_(),
            bstack111ll_opy_ (u"࠭ࡴࡺࡲࡨࠫᔛ"): bstack111ll_opy_ (u"ࠧࡩࡱࡲ࡯ࠬᔜ"),
            bstack111ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫᔝ"): hook_type,
            bstack111ll_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟࡯ࡣࡰࡩࠬᔞ"): hook_name
        }
        store[bstack111ll_opy_ (u"ࠪࡧࡺࡸࡲࡦࡰࡷࡣ࡭ࡵ࡯࡬ࡡࡸࡹ࡮ࡪࠧᔟ")].append(uuid)
        bstack111ll1ll1l_opy_ = node.nodeid
        if hook_type == bstack111ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᔠ"):
            if not _111lllllll_opy_.get(bstack111ll1ll1l_opy_, None):
                _111lllllll_opy_[bstack111ll1ll1l_opy_] = {bstack111ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡶࠫᔡ"): []}
            _111lllllll_opy_[bstack111ll1ll1l_opy_][bstack111ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡷࠬᔢ")].append(bstack11l1111111_opy_[bstack111ll_opy_ (u"ࠧࡶࡷ࡬ࡨࠬᔣ")])
        _111lllllll_opy_[bstack111ll1ll1l_opy_ + bstack111ll_opy_ (u"ࠨ࠯ࠪᔤ") + hook_name] = bstack11l1111111_opy_
        bstack11l11111l1_opy_(node, bstack11l1111111_opy_, bstack111ll_opy_ (u"ࠩࡋࡳࡴࡱࡒࡶࡰࡖࡸࡦࡸࡴࡦࡦࠪᔥ"))
    elif event == bstack111ll_opy_ (u"ࠪࡥ࡫ࡺࡥࡳࠩᔦ"):
        bstack111lll111l_opy_ = node.nodeid + bstack111ll_opy_ (u"ࠫ࠲࠭ᔧ") + hook_name
        _111lllllll_opy_[bstack111lll111l_opy_][bstack111ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪᔨ")] = bstack1lll1111l1_opy_()
        bstack111ll1l111_opy_(_111lllllll_opy_[bstack111lll111l_opy_][bstack111ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫᔩ")])
        bstack11l11111l1_opy_(node, _111lllllll_opy_[bstack111lll111l_opy_], bstack111ll_opy_ (u"ࠧࡉࡱࡲ࡯ࡗࡻ࡮ࡇ࡫ࡱ࡭ࡸ࡮ࡥࡥࠩᔪ"), bstack111ll111l1_opy_=bstack111ll1111l_opy_)
def bstack111llll1l1_opy_():
    global bstack111ll111ll_opy_
    if bstack1lll1l1ll1_opy_():
        bstack111ll111ll_opy_ = bstack111ll_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴ࠮ࡤࡧࡨࠬᔫ")
    else:
        bstack111ll111ll_opy_ = bstack111ll_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᔬ")
@bstack1llll111ll_opy_.bstack11l11l1ll1_opy_
def bstack111llll1ll_opy_():
    bstack111llll1l1_opy_()
    if bstack111l1ll1l_opy_():
        bstack11ll11111l_opy_(bstack111lll1l11_opy_)
    bstack1l11l11l1l_opy_ = bstack1l11l1ll11_opy_(bstack111lll1l1l_opy_)
bstack111llll1ll_opy_()