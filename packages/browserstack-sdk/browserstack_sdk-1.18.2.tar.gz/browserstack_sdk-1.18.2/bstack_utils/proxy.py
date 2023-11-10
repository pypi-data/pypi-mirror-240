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
from urllib.parse import urlparse
from bstack_utils.messages import bstack1l111ll1ll_opy_
def bstack11ll1lllll_opy_(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False
def bstack11lll11l11_opy_(bstack11lll111ll_opy_, bstack11lll11111_opy_):
    from pypac import get_pac
    from pypac import PACSession
    from pypac.parser import PACFile
    import socket
    if os.path.isfile(bstack11lll111ll_opy_):
        with open(bstack11lll111ll_opy_) as f:
            pac = PACFile(f.read())
    elif bstack11ll1lllll_opy_(bstack11lll111ll_opy_):
        pac = get_pac(url=bstack11lll111ll_opy_)
    else:
        raise Exception(bstack111ll_opy_ (u"ࠬࡖࡡࡤࠢࡩ࡭ࡱ࡫ࠠࡥࡱࡨࡷࠥࡴ࡯ࡵࠢࡨࡼ࡮ࡹࡴ࠻ࠢࡾࢁࠬᇒ").format(bstack11lll111ll_opy_))
    session = PACSession(pac)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((bstack111ll_opy_ (u"ࠨ࠸࠯࠺࠱࠼࠳࠾ࠢᇓ"), 80))
        bstack11lll111l1_opy_ = s.getsockname()[0]
        s.close()
    except:
        bstack11lll111l1_opy_ = bstack111ll_opy_ (u"ࠧ࠱࠰࠳࠲࠵࠴࠰ࠨᇔ")
    proxy_url = session.get_pac().find_proxy_for_url(bstack11lll11111_opy_, bstack11lll111l1_opy_)
    return proxy_url
def bstack1ll11l11ll_opy_(config):
    return bstack111ll_opy_ (u"ࠨࡪࡷࡸࡵࡖࡲࡰࡺࡼࠫᇕ") in config or bstack111ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࡑࡴࡲࡼࡾ࠭ᇖ") in config
def bstack1ll1llll11_opy_(config):
    if not bstack1ll11l11ll_opy_(config):
        return
    if config.get(bstack111ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡑࡴࡲࡼࡾ࠭ᇗ")):
        return config.get(bstack111ll_opy_ (u"ࠫ࡭ࡺࡴࡱࡒࡵࡳࡽࡿࠧᇘ"))
    if config.get(bstack111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࡔࡷࡵࡸࡺࠩᇙ")):
        return config.get(bstack111ll_opy_ (u"࠭ࡨࡵࡶࡳࡷࡕࡸ࡯ࡹࡻࠪᇚ"))
def bstack11111lll1_opy_(config, bstack11lll11111_opy_):
    proxy = bstack1ll1llll11_opy_(config)
    proxies = {}
    if config.get(bstack111ll_opy_ (u"ࠧࡩࡶࡷࡴࡕࡸ࡯ࡹࡻࠪᇛ")) or config.get(bstack111ll_opy_ (u"ࠨࡪࡷࡸࡵࡹࡐࡳࡱࡻࡽࠬᇜ")):
        if proxy.endswith(bstack111ll_opy_ (u"ࠩ࠱ࡴࡦࡩࠧᇝ")):
            proxies = bstack111111l1l_opy_(proxy, bstack11lll11111_opy_)
        else:
            proxies = {
                bstack111ll_opy_ (u"ࠪ࡬ࡹࡺࡰࡴࠩᇞ"): proxy
            }
    return proxies
def bstack111111l1l_opy_(bstack11lll111ll_opy_, bstack11lll11111_opy_):
    proxies = {}
    global bstack11lll11l1l_opy_
    if bstack111ll_opy_ (u"ࠫࡕࡇࡃࡠࡒࡕࡓ࡝࡟ࠧᇟ") in globals():
        return bstack11lll11l1l_opy_
    try:
        proxy = bstack11lll11l11_opy_(bstack11lll111ll_opy_, bstack11lll11111_opy_)
        if bstack111ll_opy_ (u"ࠧࡊࡉࡓࡇࡆࡘࠧᇠ") in proxy:
            proxies = {}
        elif bstack111ll_opy_ (u"ࠨࡈࡕࡖࡓࠦᇡ") in proxy or bstack111ll_opy_ (u"ࠢࡉࡖࡗࡔࡘࠨᇢ") in proxy or bstack111ll_opy_ (u"ࠣࡕࡒࡇࡐ࡙ࠢᇣ") in proxy:
            bstack11lll1111l_opy_ = proxy.split(bstack111ll_opy_ (u"ࠤࠣࠦᇤ"))
            if bstack111ll_opy_ (u"ࠥ࠾࠴࠵ࠢᇥ") in bstack111ll_opy_ (u"ࠦࠧᇦ").join(bstack11lll1111l_opy_[1:]):
                proxies = {
                    bstack111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᇧ"): bstack111ll_opy_ (u"ࠨࠢᇨ").join(bstack11lll1111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᇩ"): str(bstack11lll1111l_opy_[0]).lower() + bstack111ll_opy_ (u"ࠣ࠼࠲࠳ࠧᇪ") + bstack111ll_opy_ (u"ࠤࠥᇫ").join(bstack11lll1111l_opy_[1:])
                }
        elif bstack111ll_opy_ (u"ࠥࡔࡗࡕࡘ࡚ࠤᇬ") in proxy:
            bstack11lll1111l_opy_ = proxy.split(bstack111ll_opy_ (u"ࠦࠥࠨᇭ"))
            if bstack111ll_opy_ (u"ࠧࡀ࠯࠰ࠤᇮ") in bstack111ll_opy_ (u"ࠨࠢᇯ").join(bstack11lll1111l_opy_[1:]):
                proxies = {
                    bstack111ll_opy_ (u"ࠧࡩࡶࡷࡴࡸ࠭ᇰ"): bstack111ll_opy_ (u"ࠣࠤᇱ").join(bstack11lll1111l_opy_[1:])
                }
            else:
                proxies = {
                    bstack111ll_opy_ (u"ࠩ࡫ࡸࡹࡶࡳࠨᇲ"): bstack111ll_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᇳ") + bstack111ll_opy_ (u"ࠦࠧᇴ").join(bstack11lll1111l_opy_[1:])
                }
        else:
            proxies = {
                bstack111ll_opy_ (u"ࠬ࡮ࡴࡵࡲࡶࠫᇵ"): proxy
            }
    except Exception as e:
        print(bstack111ll_opy_ (u"ࠨࡳࡰ࡯ࡨࠤࡪࡸࡲࡰࡴࠥᇶ"), bstack1l111ll1ll_opy_.format(bstack11lll111ll_opy_, str(e)))
    bstack11lll11l1l_opy_ = proxies
    return proxies