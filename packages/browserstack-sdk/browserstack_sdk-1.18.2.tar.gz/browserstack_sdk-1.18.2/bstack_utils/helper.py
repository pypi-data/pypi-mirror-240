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
import os
import re
import subprocess
import traceback
from urllib.parse import urlparse
import git
import requests
from packaging import version
from bstack_utils.config import Config
from bstack_utils.constants import bstack1l1l1ll1ll_opy_, bstack1ll1l1111_opy_, bstack1ll11l1l11_opy_, bstack11111l11_opy_
from bstack_utils.messages import bstack1ll1lll11l_opy_, bstack11l111l1l_opy_
from bstack_utils.proxy import bstack11111lll1_opy_, bstack1ll1llll11_opy_
bstack111l11ll_opy_ = Config.get_instance()
def bstack1l1ll1ll11_opy_(config):
    return config[bstack111ll_opy_ (u"࠭ࡵࡴࡧࡵࡒࡦࡳࡥࠨྕ")]
def bstack1l1ll1l111_opy_(config):
    return config[bstack111ll_opy_ (u"ࠧࡢࡥࡦࡩࡸࡹࡋࡦࡻࠪྖ")]
def bstack1ll11ll1ll_opy_():
    try:
        import playwright
        return True
    except ImportError:
        return False
def bstack1l1l1ll111_opy_(obj):
    values = []
    bstack1l1l1111l1_opy_ = re.compile(bstack111ll_opy_ (u"ࡳࠤࡡࡇ࡚࡙ࡔࡐࡏࡢࡘࡆࡍ࡟࡝ࡦ࠮ࠨࠧྗ"), re.I)
    for key in obj.keys():
        if bstack1l1l1111l1_opy_.match(key):
            values.append(obj[key])
    return values
def bstack1l11ll11l1_opy_(config):
    tags = []
    tags.extend(bstack1l1l1ll111_opy_(os.environ))
    tags.extend(bstack1l1l1ll111_opy_(config))
    return tags
def bstack1l11lll111_opy_(markers):
    tags = []
    for marker in markers:
        tags.append(marker.name)
    return tags
def bstack1l11lll11l_opy_(bstack1l1l111l1l_opy_):
    if not bstack1l1l111l1l_opy_:
        return bstack111ll_opy_ (u"ࠩࠪ྘")
    return bstack111ll_opy_ (u"ࠥࡿࢂࠦࠨࡼࡿࠬࠦྙ").format(bstack1l1l111l1l_opy_.name, bstack1l1l111l1l_opy_.email)
def bstack1l1lll1lll_opy_():
    try:
        repo = git.Repo(search_parent_directories=True)
        bstack1l1l1l1l11_opy_ = repo.common_dir
        info = {
            bstack111ll_opy_ (u"ࠦࡸ࡮ࡡࠣྚ"): repo.head.commit.hexsha,
            bstack111ll_opy_ (u"ࠧࡹࡨࡰࡴࡷࡣࡸ࡮ࡡࠣྛ"): repo.git.rev_parse(repo.head.commit, short=True),
            bstack111ll_opy_ (u"ࠨࡢࡳࡣࡱࡧ࡭ࠨྜ"): repo.active_branch.name,
            bstack111ll_opy_ (u"ࠢࡵࡣࡪࠦྜྷ"): repo.git.describe(all=True, tags=True, exact_match=True),
            bstack111ll_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡵࡧࡵࠦྞ"): bstack1l11lll11l_opy_(repo.head.commit.committer),
            bstack111ll_opy_ (u"ࠤࡦࡳࡲࡳࡩࡵࡶࡨࡶࡤࡪࡡࡵࡧࠥྟ"): repo.head.commit.committed_datetime.isoformat(),
            bstack111ll_opy_ (u"ࠥࡥࡺࡺࡨࡰࡴࠥྠ"): bstack1l11lll11l_opy_(repo.head.commit.author),
            bstack111ll_opy_ (u"ࠦࡦࡻࡴࡩࡱࡵࡣࡩࡧࡴࡦࠤྡ"): repo.head.commit.authored_datetime.isoformat(),
            bstack111ll_opy_ (u"ࠧࡩ࡯࡮࡯࡬ࡸࡤࡳࡥࡴࡵࡤ࡫ࡪࠨྡྷ"): repo.head.commit.message,
            bstack111ll_opy_ (u"ࠨࡲࡰࡱࡷࠦྣ"): repo.git.rev_parse(bstack111ll_opy_ (u"ࠢ࠮࠯ࡶ࡬ࡴࡽ࠭ࡵࡱࡳࡰࡪࡼࡥ࡭ࠤྤ")),
            bstack111ll_opy_ (u"ࠣࡥࡲࡱࡲࡵ࡮ࡠࡩ࡬ࡸࡤࡪࡩࡳࠤྥ"): bstack1l1l1l1l11_opy_,
            bstack111ll_opy_ (u"ࠤࡺࡳࡷࡱࡴࡳࡧࡨࡣ࡬࡯ࡴࡠࡦ࡬ࡶࠧྦ"): subprocess.check_output([bstack111ll_opy_ (u"ࠥ࡫࡮ࡺࠢྦྷ"), bstack111ll_opy_ (u"ࠦࡷ࡫ࡶ࠮ࡲࡤࡶࡸ࡫ࠢྨ"), bstack111ll_opy_ (u"ࠧ࠳࠭ࡨ࡫ࡷ࠱ࡨࡵ࡭࡮ࡱࡱ࠱ࡩ࡯ࡲࠣྩ")]).strip().decode(
                bstack111ll_opy_ (u"࠭ࡵࡵࡨ࠰࠼ࠬྪ")),
            bstack111ll_opy_ (u"ࠢ࡭ࡣࡶࡸࡤࡺࡡࡨࠤྫ"): repo.git.describe(tags=True, abbrev=0, always=True),
            bstack111ll_opy_ (u"ࠣࡥࡲࡱࡲ࡯ࡴࡴࡡࡶ࡭ࡳࡩࡥࡠ࡮ࡤࡷࡹࡥࡴࡢࡩࠥྫྷ"): repo.git.rev_list(
                bstack111ll_opy_ (u"ࠤࡾࢁ࠳࠴ࡻࡾࠤྭ").format(repo.head.commit, repo.git.describe(tags=True, abbrev=0, always=True)), count=True)
        }
        remotes = repo.remotes
        bstack1l1l111ll1_opy_ = []
        for remote in remotes:
            bstack1l11ll1l1l_opy_ = {
                bstack111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣྮ"): remote.name,
                bstack111ll_opy_ (u"ࠦࡺࡸ࡬ࠣྯ"): remote.url,
            }
            bstack1l1l111ll1_opy_.append(bstack1l11ll1l1l_opy_)
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥྰ"): bstack111ll_opy_ (u"ࠨࡧࡪࡶࠥྱ"),
            **info,
            bstack111ll_opy_ (u"ࠢࡳࡧࡰࡳࡹ࡫ࡳࠣྲ"): bstack1l1l111ll1_opy_
        }
    except Exception as err:
        print(bstack111ll_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱࡱࡳࡹࡱࡧࡴࡪࡰࡪࠤࡌ࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡻ࡮ࡺࡨࠡࡧࡵࡶࡴࡸ࠺ࠡࡽࢀࠦླ").format(err))
        return {}
def bstack1ll1ll1l1_opy_():
    env = os.environ
    if (bstack111ll_opy_ (u"ࠤࡍࡉࡓࡑࡉࡏࡕࡢ࡙ࡗࡒࠢྴ") in env and len(env[bstack111ll_opy_ (u"ࠥࡎࡊࡔࡋࡊࡐࡖࡣ࡚ࡘࡌࠣྵ")]) > 0) or (
            bstack111ll_opy_ (u"ࠦࡏࡋࡎࡌࡋࡑࡗࡤࡎࡏࡎࡇࠥྶ") in env and len(env[bstack111ll_opy_ (u"ࠧࡐࡅࡏࡍࡌࡒࡘࡥࡈࡐࡏࡈࠦྷ")]) > 0):
        return {
            bstack111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦྸ"): bstack111ll_opy_ (u"ࠢࡋࡧࡱ࡯࡮ࡴࡳࠣྐྵ"),
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦྺ"): env.get(bstack111ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡗࡕࡐࠧྻ")),
            bstack111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧྼ"): env.get(bstack111ll_opy_ (u"ࠦࡏࡕࡂࡠࡐࡄࡑࡊࠨ྽")),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ྾"): env.get(bstack111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ྿"))
        }
    if env.get(bstack111ll_opy_ (u"ࠢࡄࡋࠥ࿀")) == bstack111ll_opy_ (u"ࠣࡶࡵࡹࡪࠨ࿁") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠤࡆࡍࡗࡉࡌࡆࡅࡌࠦ࿂"))):
        return {
            bstack111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ࿃"): bstack111ll_opy_ (u"ࠦࡈ࡯ࡲࡤ࡮ࡨࡇࡎࠨ࿄"),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ࿅"): env.get(bstack111ll_opy_ (u"ࠨࡃࡊࡔࡆࡐࡊࡥࡂࡖࡋࡏࡈࡤ࡛ࡒࡍࠤ࿆")),
            bstack111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤ࿇"): env.get(bstack111ll_opy_ (u"ࠣࡅࡌࡖࡈࡒࡅࡠࡌࡒࡆࠧ࿈")),
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ࿉"): env.get(bstack111ll_opy_ (u"ࠥࡇࡎࡘࡃࡍࡇࡢࡆ࡚ࡏࡌࡅࡡࡑ࡙ࡒࠨ࿊"))
        }
    if env.get(bstack111ll_opy_ (u"ࠦࡈࡏࠢ࿋")) == bstack111ll_opy_ (u"ࠧࡺࡲࡶࡧࠥ࿌") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠨࡔࡓࡃ࡙ࡍࡘࠨ࿍"))):
        return {
            bstack111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ࿎"): bstack111ll_opy_ (u"ࠣࡖࡵࡥࡻ࡯ࡳࠡࡅࡌࠦ࿏"),
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ࿐"): env.get(bstack111ll_opy_ (u"ࠥࡘࡗࡇࡖࡊࡕࡢࡆ࡚ࡏࡌࡅࡡ࡚ࡉࡇࡥࡕࡓࡎࠥ࿑")),
            bstack111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ࿒"): env.get(bstack111ll_opy_ (u"࡚ࠧࡒࡂࡘࡌࡗࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ࿓")),
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿔"): env.get(bstack111ll_opy_ (u"ࠢࡕࡔࡄ࡚ࡎ࡙࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ࿕"))
        }
    if env.get(bstack111ll_opy_ (u"ࠣࡅࡌࠦ࿖")) == bstack111ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࿗") and env.get(bstack111ll_opy_ (u"ࠥࡇࡎࡥࡎࡂࡏࡈࠦ࿘")) == bstack111ll_opy_ (u"ࠦࡨࡵࡤࡦࡵ࡫࡭ࡵࠨ࿙"):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ࿚"): bstack111ll_opy_ (u"ࠨࡃࡰࡦࡨࡷ࡭࡯ࡰࠣ࿛"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ࿜"): None,
            bstack111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿝"): None,
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣ࿞"): None
        }
    if env.get(bstack111ll_opy_ (u"ࠥࡆࡎ࡚ࡂࡖࡅࡎࡉ࡙ࡥࡂࡓࡃࡑࡇࡍࠨ࿟")) and env.get(bstack111ll_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡄࡑࡐࡑࡎ࡚ࠢ࿠")):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥ࿡"): bstack111ll_opy_ (u"ࠨࡂࡪࡶࡥࡹࡨࡱࡥࡵࠤ࿢"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥ࿣"): env.get(bstack111ll_opy_ (u"ࠣࡄࡌࡘࡇ࡛ࡃࡌࡇࡗࡣࡌࡏࡔࡠࡊࡗࡘࡕࡥࡏࡓࡋࡊࡍࡓࠨ࿤")),
            bstack111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ࿥"): None,
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿦"): env.get(bstack111ll_opy_ (u"ࠦࡇࡏࡔࡃࡗࡆࡏࡊ࡚࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨ࿧"))
        }
    if env.get(bstack111ll_opy_ (u"ࠧࡉࡉࠣ࿨")) == bstack111ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ࿩") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠢࡅࡔࡒࡒࡊࠨ࿪"))):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨ࿫"): bstack111ll_opy_ (u"ࠤࡇࡶࡴࡴࡥࠣ࿬"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨ࿭"): env.get(bstack111ll_opy_ (u"ࠦࡉࡘࡏࡏࡇࡢࡆ࡚ࡏࡌࡅࡡࡏࡍࡓࡑࠢ࿮")),
            bstack111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢ࿯"): None,
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ࿰"): env.get(bstack111ll_opy_ (u"ࠢࡅࡔࡒࡒࡊࡥࡂࡖࡋࡏࡈࡤࡔࡕࡎࡄࡈࡖࠧ࿱"))
        }
    if env.get(bstack111ll_opy_ (u"ࠣࡅࡌࠦ࿲")) == bstack111ll_opy_ (u"ࠤࡷࡶࡺ࡫ࠢ࿳") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠥࡗࡊࡓࡁࡑࡊࡒࡖࡊࠨ࿴"))):
        return {
            bstack111ll_opy_ (u"ࠦࡳࡧ࡭ࡦࠤ࿵"): bstack111ll_opy_ (u"࡙ࠧࡥ࡮ࡣࡳ࡬ࡴࡸࡥࠣ࿶"),
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡻࡲ࡭ࠤ࿷"): env.get(bstack111ll_opy_ (u"ࠢࡔࡇࡐࡅࡕࡎࡏࡓࡇࡢࡓࡗࡍࡁࡏࡋ࡝ࡅ࡙ࡏࡏࡏࡡࡘࡖࡑࠨ࿸")),
            bstack111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥ࿹"): env.get(bstack111ll_opy_ (u"ࠤࡖࡉࡒࡇࡐࡉࡑࡕࡉࡤࡐࡏࡃࡡࡑࡅࡒࡋࠢ࿺")),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤ࿻"): env.get(bstack111ll_opy_ (u"ࠦࡘࡋࡍࡂࡒࡋࡓࡗࡋ࡟ࡋࡑࡅࡣࡎࡊࠢ࿼"))
        }
    if env.get(bstack111ll_opy_ (u"ࠧࡉࡉࠣ࿽")) == bstack111ll_opy_ (u"ࠨࡴࡳࡷࡨࠦ࿾") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠢࡈࡋࡗࡐࡆࡈ࡟ࡄࡋࠥ࿿"))):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨက"): bstack111ll_opy_ (u"ࠤࡊ࡭ࡹࡒࡡࡣࠤခ"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨဂ"): env.get(bstack111ll_opy_ (u"ࠦࡈࡏ࡟ࡋࡑࡅࡣ࡚ࡘࡌࠣဃ")),
            bstack111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢင"): env.get(bstack111ll_opy_ (u"ࠨࡃࡊࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦစ")),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨဆ"): env.get(bstack111ll_opy_ (u"ࠣࡅࡌࡣࡏࡕࡂࡠࡋࡇࠦဇ"))
        }
    if env.get(bstack111ll_opy_ (u"ࠤࡆࡍࠧဈ")) == bstack111ll_opy_ (u"ࠥࡸࡷࡻࡥࠣဉ") and bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋࠢည"))):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥဋ"): bstack111ll_opy_ (u"ࠨࡂࡶ࡫࡯ࡨࡰ࡯ࡴࡦࠤဌ"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥဍ"): env.get(bstack111ll_opy_ (u"ࠣࡄࡘࡍࡑࡊࡋࡊࡖࡈࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢဎ")),
            bstack111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦဏ"): env.get(bstack111ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡍࡌࡘࡊࡥࡌࡂࡄࡈࡐࠧတ")) or env.get(bstack111ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡎࡍ࡙ࡋ࡟ࡑࡋࡓࡉࡑࡏࡎࡆࡡࡑࡅࡒࡋࠢထ")),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦဒ"): env.get(bstack111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡐࡏࡔࡆࡡࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣဓ"))
        }
    if bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠢࡕࡈࡢࡆ࡚ࡏࡌࡅࠤန"))):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨပ"): bstack111ll_opy_ (u"ࠤ࡙࡭ࡸࡻࡡ࡭ࠢࡖࡸࡺࡪࡩࡰࠢࡗࡩࡦࡳࠠࡔࡧࡵࡺ࡮ࡩࡥࡴࠤဖ"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨဗ"): bstack111ll_opy_ (u"ࠦࢀࢃࡻࡾࠤဘ").format(env.get(bstack111ll_opy_ (u"࡙࡙ࠬࡔࡖࡈࡑࡤ࡚ࡅࡂࡏࡉࡓ࡚ࡔࡄࡂࡖࡌࡓࡓ࡙ࡅࡓࡘࡈࡖ࡚ࡘࡉࠨမ")), env.get(bstack111ll_opy_ (u"࠭ࡓ࡚ࡕࡗࡉࡒࡥࡔࡆࡃࡐࡔࡗࡕࡊࡆࡅࡗࡍࡉ࠭ယ"))),
            bstack111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤရ"): env.get(bstack111ll_opy_ (u"ࠣࡕ࡜ࡗ࡙ࡋࡍࡠࡆࡈࡊࡎࡔࡉࡕࡋࡒࡒࡎࡊࠢလ")),
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡰࡸࡱࡧ࡫ࡲࠣဝ"): env.get(bstack111ll_opy_ (u"ࠥࡆ࡚ࡏࡌࡅࡡࡅ࡙ࡎࡒࡄࡊࡆࠥသ"))
        }
    if bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠦࡆࡖࡐࡗࡇ࡜ࡓࡗࠨဟ"))):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥဠ"): bstack111ll_opy_ (u"ࠨࡁࡱࡲࡹࡩࡾࡵࡲࠣအ"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥဢ"): bstack111ll_opy_ (u"ࠣࡽࢀ࠳ࡵࡸ࡯࡫ࡧࡦࡸ࠴ࢁࡽ࠰ࡽࢀ࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃࠢဣ").format(env.get(bstack111ll_opy_ (u"ࠩࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣ࡚ࡘࡌࠨဤ")), env.get(bstack111ll_opy_ (u"ࠪࡅࡕࡖࡖࡆ࡛ࡒࡖࡤࡇࡃࡄࡑࡘࡒ࡙ࡥࡎࡂࡏࡈࠫဥ")), env.get(bstack111ll_opy_ (u"ࠫࡆࡖࡐࡗࡇ࡜ࡓࡗࡥࡐࡓࡑࡍࡉࡈ࡚࡟ࡔࡎࡘࡋࠬဦ")), env.get(bstack111ll_opy_ (u"ࠬࡇࡐࡑࡘࡈ࡝ࡔࡘ࡟ࡃࡗࡌࡐࡉࡥࡉࡅࠩဧ"))),
            bstack111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣဨ"): env.get(bstack111ll_opy_ (u"ࠢࡂࡒࡓ࡚ࡊ࡟ࡏࡓࡡࡍࡓࡇࡥࡎࡂࡏࡈࠦဩ")),
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢဪ"): env.get(bstack111ll_opy_ (u"ࠤࡄࡔࡕ࡜ࡅ࡚ࡑࡕࡣࡇ࡛ࡉࡍࡆࡢࡒ࡚ࡓࡂࡆࡔࠥါ"))
        }
    if env.get(bstack111ll_opy_ (u"ࠥࡅ࡟࡛ࡒࡆࡡࡋࡘ࡙ࡖ࡟ࡖࡕࡈࡖࡤࡇࡇࡆࡐࡗࠦာ")) and env.get(bstack111ll_opy_ (u"࡙ࠦࡌ࡟ࡃࡗࡌࡐࡉࠨိ")):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥီ"): bstack111ll_opy_ (u"ࠨࡁࡻࡷࡵࡩࠥࡉࡉࠣု"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥူ"): bstack111ll_opy_ (u"ࠣࡽࢀࡿࢂ࠵࡟ࡣࡷ࡬ࡰࡩ࠵ࡲࡦࡵࡸࡰࡹࡹ࠿ࡣࡷ࡬ࡰࡩࡏࡤ࠾ࡽࢀࠦေ").format(env.get(bstack111ll_opy_ (u"ࠩࡖ࡝ࡘ࡚ࡅࡎࡡࡗࡉࡆࡓࡆࡐࡗࡑࡈࡆ࡚ࡉࡐࡐࡖࡉࡗ࡜ࡅࡓࡗࡕࡍࠬဲ")), env.get(bstack111ll_opy_ (u"ࠪࡗ࡞࡙ࡔࡆࡏࡢࡘࡊࡇࡍࡑࡔࡒࡎࡊࡉࡔࠨဳ")), env.get(bstack111ll_opy_ (u"ࠫࡇ࡛ࡉࡍࡆࡢࡆ࡚ࡏࡌࡅࡋࡇࠫဴ"))),
            bstack111ll_opy_ (u"ࠧࡰ࡯ࡣࡡࡱࡥࡲ࡫ࠢဵ"): env.get(bstack111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡍࡉࠨံ")),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥ࡮ࡶ࡯ࡥࡩࡷࠨ့"): env.get(bstack111ll_opy_ (u"ࠣࡄࡘࡍࡑࡊ࡟ࡃࡗࡌࡐࡉࡏࡄࠣး"))
        }
    if any([env.get(bstack111ll_opy_ (u"ࠤࡆࡓࡉࡋࡂࡖࡋࡏࡈࡤࡈࡕࡊࡎࡇࡣࡎࡊ္ࠢ")), env.get(bstack111ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡒࡆࡕࡒࡐ࡛ࡋࡄࡠࡕࡒ࡙ࡗࡉࡅࡠࡘࡈࡖࡘࡏࡏࡏࠤ်")), env.get(bstack111ll_opy_ (u"ࠦࡈࡕࡄࡆࡄࡘࡍࡑࡊ࡟ࡔࡑࡘࡖࡈࡋ࡟ࡗࡇࡕࡗࡎࡕࡎࠣျ"))]):
        return {
            bstack111ll_opy_ (u"ࠧࡴࡡ࡮ࡧࠥြ"): bstack111ll_opy_ (u"ࠨࡁࡘࡕࠣࡇࡴࡪࡥࡃࡷ࡬ࡰࡩࠨွ"),
            bstack111ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡥࡵࡳ࡮ࠥှ"): env.get(bstack111ll_opy_ (u"ࠣࡅࡒࡈࡊࡈࡕࡊࡎࡇࡣࡕ࡛ࡂࡍࡋࡆࡣࡇ࡛ࡉࡍࡆࡢ࡙ࡗࡒࠢဿ")),
            bstack111ll_opy_ (u"ࠤ࡭ࡳࡧࡥ࡮ࡢ࡯ࡨࠦ၀"): env.get(bstack111ll_opy_ (u"ࠥࡇࡔࡊࡅࡃࡗࡌࡐࡉࡥࡂࡖࡋࡏࡈࡤࡏࡄࠣ၁")),
            bstack111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡲࡺࡳࡢࡦࡴࠥ၂"): env.get(bstack111ll_opy_ (u"ࠧࡉࡏࡅࡇࡅ࡙ࡎࡒࡄࡠࡄࡘࡍࡑࡊ࡟ࡊࡆࠥ၃"))
        }
    if env.get(bstack111ll_opy_ (u"ࠨࡢࡢ࡯ࡥࡳࡴࡥࡢࡶ࡫࡯ࡨࡓࡻ࡭ࡣࡧࡵࠦ၄")):
        return {
            bstack111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ၅"): bstack111ll_opy_ (u"ࠣࡄࡤࡱࡧࡵ࡯ࠣ၆"),
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧ၇"): env.get(bstack111ll_opy_ (u"ࠥࡦࡦࡳࡢࡰࡱࡢࡦࡺ࡯࡬ࡥࡔࡨࡷࡺࡲࡴࡴࡗࡵࡰࠧ၈")),
            bstack111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨ၉"): env.get(bstack111ll_opy_ (u"ࠧࡨࡡ࡮ࡤࡲࡳࡤࡹࡨࡰࡴࡷࡎࡴࡨࡎࡢ࡯ࡨࠦ၊")),
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧ။"): env.get(bstack111ll_opy_ (u"ࠢࡣࡣࡰࡦࡴࡵ࡟ࡣࡷ࡬ࡰࡩࡔࡵ࡮ࡤࡨࡶࠧ၌"))
        }
    if env.get(bstack111ll_opy_ (u"࡙ࠣࡈࡖࡈࡑࡅࡓࠤ၍")) or env.get(bstack111ll_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦ၎")):
        return {
            bstack111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣ၏"): bstack111ll_opy_ (u"ࠦ࡜࡫ࡲࡤ࡭ࡨࡶࠧၐ"),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣၑ"): env.get(bstack111ll_opy_ (u"ࠨࡗࡆࡔࡆࡏࡊࡘ࡟ࡃࡗࡌࡐࡉࡥࡕࡓࡎࠥၒ")),
            bstack111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤၓ"): bstack111ll_opy_ (u"ࠣࡏࡤ࡭ࡳࠦࡐࡪࡲࡨࡰ࡮ࡴࡥࠣၔ") if env.get(bstack111ll_opy_ (u"ࠤ࡚ࡉࡗࡉࡋࡆࡔࡢࡑࡆࡏࡎࡠࡒࡌࡔࡊࡒࡉࡏࡇࡢࡗ࡙ࡇࡒࡕࡇࡇࠦၕ")) else None,
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤၖ"): env.get(bstack111ll_opy_ (u"ࠦ࡜ࡋࡒࡄࡍࡈࡖࡤࡍࡉࡕࡡࡆࡓࡒࡓࡉࡕࠤၗ"))
        }
    if any([env.get(bstack111ll_opy_ (u"ࠧࡍࡃࡑࡡࡓࡖࡔࡐࡅࡄࡖࠥၘ")), env.get(bstack111ll_opy_ (u"ࠨࡇࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢၙ")), env.get(bstack111ll_opy_ (u"ࠢࡈࡑࡒࡋࡑࡋ࡟ࡄࡎࡒ࡙ࡉࡥࡐࡓࡑࡍࡉࡈ࡚ࠢၚ"))]):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨၛ"): bstack111ll_opy_ (u"ࠤࡊࡳࡴ࡭࡬ࡦࠢࡆࡰࡴࡻࡤࠣၜ"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨၝ"): None,
            bstack111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨၞ"): env.get(bstack111ll_opy_ (u"ࠧࡖࡒࡐࡌࡈࡇ࡙ࡥࡉࡅࠤၟ")),
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧၠ"): env.get(bstack111ll_opy_ (u"ࠢࡃࡗࡌࡐࡉࡥࡉࡅࠤၡ"))
        }
    if env.get(bstack111ll_opy_ (u"ࠣࡕࡋࡍࡕࡖࡁࡃࡎࡈࠦၢ")):
        return {
            bstack111ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢၣ"): bstack111ll_opy_ (u"ࠥࡗ࡭࡯ࡰࡱࡣࡥࡰࡪࠨၤ"),
            bstack111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢၥ"): env.get(bstack111ll_opy_ (u"࡙ࠧࡈࡊࡒࡓࡅࡇࡒࡅࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦၦ")),
            bstack111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣၧ"): bstack111ll_opy_ (u"ࠢࡋࡱࡥࠤࠨࢁࡽࠣၨ").format(env.get(bstack111ll_opy_ (u"ࠨࡕࡋࡍࡕࡖࡁࡃࡎࡈࡣࡏࡕࡂࡠࡋࡇࠫၩ"))) if env.get(bstack111ll_opy_ (u"ࠤࡖࡌࡎࡖࡐࡂࡄࡏࡉࡤࡐࡏࡃࡡࡌࡈࠧၪ")) else None,
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤၫ"): env.get(bstack111ll_opy_ (u"ࠦࡘࡎࡉࡑࡒࡄࡆࡑࡋ࡟ࡃࡗࡌࡐࡉࡥࡎࡖࡏࡅࡉࡗࠨၬ"))
        }
    if bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠧࡔࡅࡕࡎࡌࡊ࡞ࠨၭ"))):
        return {
            bstack111ll_opy_ (u"ࠨ࡮ࡢ࡯ࡨࠦၮ"): bstack111ll_opy_ (u"ࠢࡏࡧࡷࡰ࡮࡬ࡹࠣၯ"),
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟ࡶࡴ࡯ࠦၰ"): env.get(bstack111ll_opy_ (u"ࠤࡇࡉࡕࡒࡏ࡚ࡡࡘࡖࡑࠨၱ")),
            bstack111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧၲ"): env.get(bstack111ll_opy_ (u"ࠦࡘࡏࡔࡆࡡࡑࡅࡒࡋࠢၳ")),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦၴ"): env.get(bstack111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣၵ"))
        }
    if bstack1l11lllll1_opy_(env.get(bstack111ll_opy_ (u"ࠢࡈࡋࡗࡌ࡚ࡈ࡟ࡂࡅࡗࡍࡔࡔࡓࠣၶ"))):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨၷ"): bstack111ll_opy_ (u"ࠤࡊ࡭ࡹࡎࡵࡣࠢࡄࡧࡹ࡯࡯࡯ࡵࠥၸ"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨၹ"): bstack111ll_opy_ (u"ࠦࢀࢃ࠯ࡼࡿ࠲ࡥࡨࡺࡩࡰࡰࡶ࠳ࡷࡻ࡮ࡴ࠱ࡾࢁࠧၺ").format(env.get(bstack111ll_opy_ (u"ࠬࡍࡉࡕࡊࡘࡆࡤ࡙ࡅࡓࡘࡈࡖࡤ࡛ࡒࡍࠩၻ")), env.get(bstack111ll_opy_ (u"࠭ࡇࡊࡖࡋ࡙ࡇࡥࡒࡆࡒࡒࡗࡎ࡚ࡏࡓ࡛ࠪၼ")), env.get(bstack111ll_opy_ (u"ࠧࡈࡋࡗࡌ࡚ࡈ࡟ࡓࡗࡑࡣࡎࡊࠧၽ"))),
            bstack111ll_opy_ (u"ࠣ࡬ࡲࡦࡤࡴࡡ࡮ࡧࠥၾ"): env.get(bstack111ll_opy_ (u"ࠤࡊࡍ࡙ࡎࡕࡃࡡ࡚ࡓࡗࡑࡆࡍࡑ࡚ࠦၿ")),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤႀ"): env.get(bstack111ll_opy_ (u"ࠦࡌࡏࡔࡉࡗࡅࡣࡗ࡛ࡎࡠࡋࡇࠦႁ"))
        }
    if env.get(bstack111ll_opy_ (u"ࠧࡉࡉࠣႂ")) == bstack111ll_opy_ (u"ࠨࡴࡳࡷࡨࠦႃ") and env.get(bstack111ll_opy_ (u"ࠢࡗࡇࡕࡇࡊࡒࠢႄ")) == bstack111ll_opy_ (u"ࠣ࠳ࠥႅ"):
        return {
            bstack111ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢႆ"): bstack111ll_opy_ (u"࡚ࠥࡪࡸࡣࡦ࡮ࠥႇ"),
            bstack111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢႈ"): bstack111ll_opy_ (u"ࠧ࡮ࡴࡵࡲ࠽࠳࠴ࢁࡽࠣႉ").format(env.get(bstack111ll_opy_ (u"࠭ࡖࡆࡔࡆࡉࡑࡥࡕࡓࡎࠪႊ"))),
            bstack111ll_opy_ (u"ࠢ࡫ࡱࡥࡣࡳࡧ࡭ࡦࠤႋ"): None,
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢႌ"): None,
        }
    if env.get(bstack111ll_opy_ (u"ࠤࡗࡉࡆࡓࡃࡊࡖ࡜ࡣ࡛ࡋࡒࡔࡋࡒࡒႍࠧ")):
        return {
            bstack111ll_opy_ (u"ࠥࡲࡦࡳࡥࠣႎ"): bstack111ll_opy_ (u"࡙ࠦ࡫ࡡ࡮ࡥ࡬ࡸࡾࠨႏ"),
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡺࡸ࡬ࠣ႐"): None,
            bstack111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣ႑"): env.get(bstack111ll_opy_ (u"ࠢࡕࡇࡄࡑࡈࡏࡔ࡚ࡡࡓࡖࡔࡐࡅࡄࡖࡢࡒࡆࡓࡅࠣ႒")),
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢ႓"): env.get(bstack111ll_opy_ (u"ࠤࡅ࡙ࡎࡒࡄࡠࡐࡘࡑࡇࡋࡒࠣ႔"))
        }
    if any([env.get(bstack111ll_opy_ (u"ࠥࡇࡔࡔࡃࡐࡗࡕࡗࡊࠨ႕")), env.get(bstack111ll_opy_ (u"ࠦࡈࡕࡎࡄࡑࡘࡖࡘࡋ࡟ࡖࡔࡏࠦ႖")), env.get(bstack111ll_opy_ (u"ࠧࡉࡏࡏࡅࡒ࡙ࡗ࡙ࡅࡠࡗࡖࡉࡗࡔࡁࡎࡇࠥ႗")), env.get(bstack111ll_opy_ (u"ࠨࡃࡐࡐࡆࡓ࡚ࡘࡓࡆࡡࡗࡉࡆࡓࠢ႘"))]):
        return {
            bstack111ll_opy_ (u"ࠢ࡯ࡣࡰࡩࠧ႙"): bstack111ll_opy_ (u"ࠣࡅࡲࡲࡨࡵࡵࡳࡵࡨࠦႚ"),
            bstack111ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡠࡷࡵࡰࠧႛ"): None,
            bstack111ll_opy_ (u"ࠥ࡮ࡴࡨ࡟࡯ࡣࡰࡩࠧႜ"): env.get(bstack111ll_opy_ (u"ࠦࡇ࡛ࡉࡍࡆࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧႝ")) or None,
            bstack111ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡣࡳࡻ࡭ࡣࡧࡵࠦ႞"): env.get(bstack111ll_opy_ (u"ࠨࡂࡖࡋࡏࡈࡤࡏࡄࠣ႟"), 0)
        }
    if env.get(bstack111ll_opy_ (u"ࠢࡈࡑࡢࡎࡔࡈ࡟ࡏࡃࡐࡉࠧႠ")):
        return {
            bstack111ll_opy_ (u"ࠣࡰࡤࡱࡪࠨႡ"): bstack111ll_opy_ (u"ࠤࡊࡳࡈࡊࠢႢ"),
            bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡸࡶࡱࠨႣ"): None,
            bstack111ll_opy_ (u"ࠦ࡯ࡵࡢࡠࡰࡤࡱࡪࠨႤ"): env.get(bstack111ll_opy_ (u"ࠧࡍࡏࡠࡌࡒࡆࡤࡔࡁࡎࡇࠥႥ")),
            bstack111ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡤࡴࡵ࡮ࡤࡨࡶࠧႦ"): env.get(bstack111ll_opy_ (u"ࠢࡈࡑࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡉࡏࡖࡐࡗࡉࡗࠨႧ"))
        }
    if env.get(bstack111ll_opy_ (u"ࠣࡅࡉࡣࡇ࡛ࡉࡍࡆࡢࡍࡉࠨႨ")):
        return {
            bstack111ll_opy_ (u"ࠤࡱࡥࡲ࡫ࠢႩ"): bstack111ll_opy_ (u"ࠥࡇࡴࡪࡥࡇࡴࡨࡷ࡭ࠨႪ"),
            bstack111ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡢࡹࡷࡲࠢႫ"): env.get(bstack111ll_opy_ (u"ࠧࡉࡆࡠࡄࡘࡍࡑࡊ࡟ࡖࡔࡏࠦႬ")),
            bstack111ll_opy_ (u"ࠨࡪࡰࡤࡢࡲࡦࡳࡥࠣႭ"): env.get(bstack111ll_opy_ (u"ࠢࡄࡈࡢࡔࡎࡖࡅࡍࡋࡑࡉࡤࡔࡁࡎࡇࠥႮ")),
            bstack111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪ࡟࡯ࡷࡰࡦࡪࡸࠢႯ"): env.get(bstack111ll_opy_ (u"ࠤࡆࡊࡤࡈࡕࡊࡎࡇࡣࡎࡊࠢႰ"))
        }
    return {bstack111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡡࡱࡹࡲࡨࡥࡳࠤႱ"): None}
def get_host_info():
    uname = os.uname()
    return {
        bstack111ll_opy_ (u"ࠦ࡭ࡵࡳࡵࡰࡤࡱࡪࠨႲ"): uname.nodename,
        bstack111ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢႳ"): uname.sysname,
        bstack111ll_opy_ (u"ࠨࡴࡺࡲࡨࠦႴ"): uname.machine,
        bstack111ll_opy_ (u"ࠢࡷࡧࡵࡷ࡮ࡵ࡮ࠣႵ"): uname.version,
        bstack111ll_opy_ (u"ࠣࡣࡵࡧ࡭ࠨႶ"): uname.machine
    }
def bstack111l1ll1l_opy_():
    try:
        import selenium
        return True
    except ImportError:
        return False
def bstack1l11ll111l_opy_():
    if bstack111l11ll_opy_.get_property(bstack111ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡡࡶࡩࡸࡹࡩࡰࡰࠪႷ")):
        return bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩႸ")
    return bstack111ll_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࡤ࡭ࡲࡪࡦࠪႹ")
def bstack1l1l11l11l_opy_(driver):
    info = {
        bstack111ll_opy_ (u"ࠬࡩࡡࡱࡣࡥ࡭ࡱ࡯ࡴࡪࡧࡶࠫႺ"): driver.capabilities,
        bstack111ll_opy_ (u"࠭ࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠪႻ"): driver.session_id,
        bstack111ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࠨႼ"): driver.capabilities.get(bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭Ⴝ"), None),
        bstack111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠫႾ"): driver.capabilities.get(bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠫႿ"), None),
        bstack111ll_opy_ (u"ࠫࡵࡲࡡࡵࡨࡲࡶࡲ࠭Ⴠ"): driver.capabilities.get(bstack111ll_opy_ (u"ࠬࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠫჁ"), None),
    }
    if bstack1l11ll111l_opy_() == bstack111ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬჂ"):
        info[bstack111ll_opy_ (u"ࠧࡱࡴࡲࡨࡺࡩࡴࠨჃ")] = bstack111ll_opy_ (u"ࠨࡣࡳࡴ࠲ࡧࡵࡵࡱࡰࡥࡹ࡫ࠧჄ") if bstack1l111l111_opy_() else bstack111ll_opy_ (u"ࠩࡤࡹࡹࡵ࡭ࡢࡶࡨࠫჅ")
    return info
def bstack1l111l111_opy_():
    if bstack111l11ll_opy_.get_property(bstack111ll_opy_ (u"ࠪࡥࡵࡶ࡟ࡢࡷࡷࡳࡲࡧࡴࡦࠩ჆")):
        return True
    if bstack1l11lllll1_opy_(os.environ.get(bstack111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡍࡘࡥࡁࡑࡒࡢࡅ࡚࡚ࡏࡎࡃࡗࡉࠬჇ"), None)):
        return True
    return False
def bstack1ll1l111_opy_(bstack1l1l111l11_opy_, url, data, config):
    headers = config.get(bstack111ll_opy_ (u"ࠬ࡮ࡥࡢࡦࡨࡶࡸ࠭჈"), None)
    proxies = bstack11111lll1_opy_(config, url)
    auth = config.get(bstack111ll_opy_ (u"࠭ࡡࡶࡶ࡫ࠫ჉"), None)
    response = requests.request(
            bstack1l1l111l11_opy_,
            url=url,
            headers=headers,
            auth=auth,
            json=data,
            proxies=proxies
        )
    return response
def bstack1ll1l1l1l_opy_(bstack11lllll11_opy_, size):
    bstack11l1l11l1_opy_ = []
    while len(bstack11lllll11_opy_) > size:
        bstack1ll1l11ll1_opy_ = bstack11lllll11_opy_[:size]
        bstack11l1l11l1_opy_.append(bstack1ll1l11ll1_opy_)
        bstack11lllll11_opy_ = bstack11lllll11_opy_[size:]
    bstack11l1l11l1_opy_.append(bstack11lllll11_opy_)
    return bstack11l1l11l1_opy_
def bstack1l1l1l1ll1_opy_(message, bstack1l1l1l11l1_opy_=False):
    os.write(1, bytes(message, bstack111ll_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭჊")))
    os.write(1, bytes(bstack111ll_opy_ (u"ࠨ࡞ࡱࠫ჋"), bstack111ll_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨ჌")))
    if bstack1l1l1l11l1_opy_:
        with open(bstack111ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠰ࡳ࠶࠷ࡹ࠮ࠩჍ") + os.environ[bstack111ll_opy_ (u"ࠫࡇ࡙࡟ࡕࡇࡖࡘࡔࡖࡓࡠࡄࡘࡍࡑࡊ࡟ࡉࡃࡖࡌࡊࡊ࡟ࡊࡆࠪ჎")] + bstack111ll_opy_ (u"ࠬ࠴࡬ࡰࡩࠪ჏"), bstack111ll_opy_ (u"࠭ࡡࠨა")) as f:
            f.write(message + bstack111ll_opy_ (u"ࠧ࡝ࡰࠪბ"))
def bstack1l1l1l1l1l_opy_():
    return os.environ[bstack111ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡂࡗࡗࡓࡒࡇࡔࡊࡑࡑࠫგ")].lower() == bstack111ll_opy_ (u"ࠩࡷࡶࡺ࡫ࠧდ")
def bstack11l1l111_opy_(bstack1l1l1l11ll_opy_):
    return bstack111ll_opy_ (u"ࠪࡿࢂ࠵ࡻࡾࠩე").format(bstack1l1l1ll1ll_opy_, bstack1l1l1l11ll_opy_)
def bstack1lll1111l1_opy_():
    return datetime.datetime.utcnow().isoformat() + bstack111ll_opy_ (u"ࠫ࡟࠭ვ")
def bstack1l11llllll_opy_(start, finish):
    return (datetime.datetime.fromisoformat(finish.rstrip(bstack111ll_opy_ (u"ࠬࡠࠧზ"))) - datetime.datetime.fromisoformat(start.rstrip(bstack111ll_opy_ (u"࡚࠭ࠨთ")))).total_seconds() * 1000
def bstack1l11ll1lll_opy_(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat() + bstack111ll_opy_ (u"࡛ࠧࠩი")
def bstack1l1l1l1lll_opy_(outcome):
    _, exception, _ = outcome.excinfo or (None, None, None)
    if exception:
        return bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨკ")
    else:
        return bstack111ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩლ")
def bstack1l11lllll1_opy_(val):
    if val is None:
        return False
    return val.__str__().lower() == bstack111ll_opy_ (u"ࠪࡸࡷࡻࡥࠨმ")
def bstack1l1l11l1ll_opy_(val):
    return val.__str__().lower() == bstack111ll_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪნ")
def bstack1l1lll11ll_opy_(bstack1l11llll1l_opy_=Exception, class_method=False, default_value=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except bstack1l11llll1l_opy_ as e:
                print(bstack111ll_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡻࡾࠢ࠰ࡂࠥࢁࡽ࠻ࠢࡾࢁࠧო").format(func.__name__, bstack1l11llll1l_opy_.__name__, str(e)))
                return default_value
        return wrapper
    def bstack1l1l11l1l1_opy_(bstack1l11ll1l11_opy_):
        def wrapped(cls, *args, **kwargs):
            try:
                return bstack1l11ll1l11_opy_(cls, *args, **kwargs)
            except bstack1l11llll1l_opy_ as e:
                print(bstack111ll_opy_ (u"ࠨࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡼࡿࠣ࠱ࡃࠦࡻࡾ࠼ࠣࡿࢂࠨპ").format(bstack1l11ll1l11_opy_.__name__, bstack1l11llll1l_opy_.__name__, str(e)))
                return default_value
        return wrapped
    if class_method:
        return bstack1l1l11l1l1_opy_
    else:
        return decorator
def bstack1l1l11l1l_opy_(bstack1ll1111ll1_opy_):
    if bstack111ll_opy_ (u"ࠧࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫჟ") in bstack1ll1111ll1_opy_ and bstack1l1l11l1ll_opy_(bstack1ll1111ll1_opy_[bstack111ll_opy_ (u"ࠨࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬრ")]):
        return False
    if bstack111ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡂࡷࡷࡳࡲࡧࡴࡪࡱࡱࠫს") in bstack1ll1111ll1_opy_ and bstack1l1l11l1ll_opy_(bstack1ll1111ll1_opy_[bstack111ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡃࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࠬტ")]):
        return False
    return True
def bstack1lll1l1ll1_opy_():
    try:
        from pytest_bdd import reporting
        return True
    except Exception as e:
        return False
def bstack1lll1l1l_opy_(hub_url):
    if bstack1llllll11_opy_() <= version.parse(bstack111ll_opy_ (u"ࠫ࠸࠴࠱࠴࠰࠳ࠫუ")):
        if hub_url != bstack111ll_opy_ (u"ࠬ࠭ფ"):
            return bstack111ll_opy_ (u"ࠨࡨࡵࡶࡳ࠾࠴࠵ࠢქ") + hub_url + bstack111ll_opy_ (u"ࠢ࠻࠺࠳࠳ࡼࡪ࠯ࡩࡷࡥࠦღ")
        return bstack1ll11l1l11_opy_
    if hub_url != bstack111ll_opy_ (u"ࠨࠩყ"):
        return bstack111ll_opy_ (u"ࠤ࡫ࡸࡹࡶࡳ࠻࠱࠲ࠦშ") + hub_url + bstack111ll_opy_ (u"ࠥ࠳ࡼࡪ࠯ࡩࡷࡥࠦჩ")
    return bstack11111l11_opy_
def bstack1l1l111111_opy_():
    return isinstance(os.getenv(bstack111ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡔ࡞࡚ࡅࡔࡖࡢࡔࡑ࡛ࡇࡊࡐࠪც")), str)
def bstack11lll1ll1_opy_(url):
    return urlparse(url).hostname
def bstack1l1ll1l11_opy_(hostname):
    for bstack11l11lll_opy_ in bstack1ll1l1111_opy_:
        regex = re.compile(bstack11l11lll_opy_)
        if regex.match(hostname):
            return True
    return False
def bstack1l1l11ll11_opy_(bstack1l1l11llll_opy_, file_name, logger):
    bstack1ll1l11111_opy_ = os.path.join(os.path.expanduser(bstack111ll_opy_ (u"ࠬࢄࠧძ")), bstack1l1l11llll_opy_)
    try:
        if not os.path.exists(bstack1ll1l11111_opy_):
            os.makedirs(bstack1ll1l11111_opy_)
        file_path = os.path.join(os.path.expanduser(bstack111ll_opy_ (u"࠭ࡾࠨწ")), bstack1l1l11llll_opy_, file_name)
        if not os.path.isfile(file_path):
            with open(file_path, bstack111ll_opy_ (u"ࠧࡸࠩჭ")):
                pass
            with open(file_path, bstack111ll_opy_ (u"ࠣࡹ࠮ࠦხ")) as outfile:
                json.dump({}, outfile)
        return file_path
    except Exception as e:
        logger.debug(bstack1ll1lll11l_opy_.format(str(e)))
def bstack1l11ll1ll1_opy_(file_name, key, value, logger):
    file_path = bstack1l1l11ll11_opy_(bstack111ll_opy_ (u"ࠩ࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠩჯ"), file_name, logger)
    if file_path != None:
        if os.path.exists(file_path):
            bstack1l11l1ll_opy_ = json.load(open(file_path, bstack111ll_opy_ (u"ࠪࡶࡧ࠭ჰ")))
        else:
            bstack1l11l1ll_opy_ = {}
        bstack1l11l1ll_opy_[key] = value
        with open(file_path, bstack111ll_opy_ (u"ࠦࡼ࠱ࠢჱ")) as outfile:
            json.dump(bstack1l11l1ll_opy_, outfile)
def bstack1l1l1ll1_opy_(file_name, logger):
    file_path = bstack1l1l11ll11_opy_(bstack111ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬჲ"), file_name, logger)
    bstack1l11l1ll_opy_ = {}
    if file_path != None and os.path.exists(file_path):
        with open(file_path, bstack111ll_opy_ (u"࠭ࡲࠨჳ")) as bstack1lll1l1l1_opy_:
            bstack1l11l1ll_opy_ = json.load(bstack1lll1l1l1_opy_)
    return bstack1l11l1ll_opy_
def bstack1ll1ll1lll_opy_(file_path, logger):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        logger.debug(bstack111ll_opy_ (u"ࠧࡆࡴࡵࡳࡷࠦࡩ࡯ࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤ࡫࡯࡬ࡦ࠼ࠣࠫჴ") + file_path + bstack111ll_opy_ (u"ࠨࠢࠪჵ") + str(e))
def bstack1llllll11_opy_():
    from selenium import webdriver
    return version.parse(webdriver.__version__)
class Notset:
    def __repr__(self):
        return bstack111ll_opy_ (u"ࠤ࠿ࡒࡔ࡚ࡓࡆࡖࡁࠦჶ")
def bstack1l11l11l_opy_(config):
    if bstack111ll_opy_ (u"ࠪ࡭ࡸࡖ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩჷ") in config:
        del (config[bstack111ll_opy_ (u"ࠫ࡮ࡹࡐ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪჸ")])
        return False
    if bstack1llllll11_opy_() < version.parse(bstack111ll_opy_ (u"ࠬ࠹࠮࠵࠰࠳ࠫჹ")):
        return False
    if bstack1llllll11_opy_() >= version.parse(bstack111ll_opy_ (u"࠭࠴࠯࠳࠱࠹ࠬჺ")):
        return True
    if bstack111ll_opy_ (u"ࠧࡶࡵࡨ࡛࠸ࡉࠧ჻") in config and config[bstack111ll_opy_ (u"ࠨࡷࡶࡩ࡜࠹ࡃࠨჼ")] is False:
        return False
    else:
        return True
def bstack11l111l1_opy_(args_list, bstack1l1l1111ll_opy_):
    index = -1
    for value in bstack1l1l1111ll_opy_:
        try:
            index = args_list.index(value)
            return index
        except Exception as e:
            return index
    return index
class Result:
    def __init__(self, result=None, duration=None, exception=None, bstack1l1l1l1111_opy_=None):
        self.result = result
        self.duration = duration
        self.exception = exception
        self.exception_type = type(self.exception).__name__ if exception else None
        self.bstack1l1l1l1111_opy_ = bstack1l1l1l1111_opy_
    @classmethod
    def passed(cls):
        return Result(result=bstack111ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩჽ"))
    @classmethod
    def failed(cls, exception=None):
        return Result(result=bstack111ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪჾ"), exception=exception)
    def bstack1l1l11l111_opy_(self):
        if self.result != bstack111ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫჿ"):
            return None
        if bstack111ll_opy_ (u"ࠧࡇࡳࡴࡧࡵࡸ࡮ࡵ࡮ࠣᄀ") in self.exception_type:
            return bstack111ll_opy_ (u"ࠨࡁࡴࡵࡨࡶࡹ࡯࡯࡯ࡇࡵࡶࡴࡸࠢᄁ")
        return bstack111ll_opy_ (u"ࠢࡖࡰ࡫ࡥࡳࡪ࡬ࡦࡦࡈࡶࡷࡵࡲࠣᄂ")
    def bstack1l11lll1ll_opy_(self):
        if self.result != bstack111ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᄃ"):
            return None
        if self.bstack1l1l1l1111_opy_:
            return self.bstack1l1l1l1111_opy_
        return bstack1l11ll11ll_opy_(self.exception)
def bstack1l11ll11ll_opy_(exc):
    return traceback.format_exception(exc)
def bstack1l11ll1111_opy_(message):
    if isinstance(message, str):
        return not bool(message and message.strip())
    return True
def bstack1l11l111l_opy_(object, key, default_value):
    if key in object.__dict__.keys():
        return object.__dict__.get(key)
    return default_value
def bstack11l1l11l_opy_(config, logger):
    try:
        import playwright
        bstack1l1l11ll1l_opy_ = playwright.__file__
        bstack1l11l1llll_opy_ = os.path.split(bstack1l1l11ll1l_opy_)
        bstack1l11lll1l1_opy_ = bstack1l11l1llll_opy_[0] + bstack111ll_opy_ (u"ࠩ࠲ࡨࡷ࡯ࡶࡦࡴ࠲ࡴࡦࡩ࡫ࡢࡩࡨ࠳ࡱ࡯ࡢ࠰ࡥ࡯࡭࠴ࡩ࡬ࡪ࠰࡭ࡷࠬᄄ")
        os.environ[bstack111ll_opy_ (u"ࠪࡋࡑࡕࡂࡂࡎࡢࡅࡌࡋࡎࡕࡡࡋࡘ࡙ࡖ࡟ࡑࡔࡒ࡜࡞࠭ᄅ")] = bstack1ll1llll11_opy_(config)
        with open(bstack1l11lll1l1_opy_, bstack111ll_opy_ (u"ࠫࡷ࠭ᄆ")) as f:
            bstack1l111l1l1_opy_ = f.read()
            bstack1l11llll11_opy_ = bstack111ll_opy_ (u"ࠬ࡭࡬ࡰࡤࡤࡰ࠲ࡧࡧࡦࡰࡷࠫᄇ")
            bstack1l1l11111l_opy_ = bstack1l111l1l1_opy_.find(bstack1l11llll11_opy_)
            if bstack1l1l11111l_opy_ is -1:
              process = subprocess.Popen(bstack111ll_opy_ (u"ࠨ࡮ࡱ࡯ࠣ࡭ࡳࡹࡴࡢ࡮࡯ࠤ࡬ࡲ࡯ࡣࡣ࡯࠱ࡦ࡭ࡥ࡯ࡶࠥᄈ"), shell=True, cwd=bstack1l11l1llll_opy_[0])
              process.wait()
              bstack1l1l1l111l_opy_ = bstack111ll_opy_ (u"ࠧࠣࡷࡶࡩࠥࡹࡴࡳ࡫ࡦࡸࠧࡁࠧᄉ")
              bstack1l1l11lll1_opy_ = bstack111ll_opy_ (u"ࠣࠤࠥࠤࡡࠨࡵࡴࡧࠣࡷࡹࡸࡩࡤࡶ࡟ࠦࡀࠦࡣࡰࡰࡶࡸࠥࢁࠠࡣࡱࡲࡸࡸࡺࡲࡢࡲࠣࢁࠥࡃࠠࡳࡧࡴࡹ࡮ࡸࡥࠩࠩࡪࡰࡴࡨࡡ࡭࠯ࡤ࡫ࡪࡴࡴࠨࠫ࠾ࠤ࡮࡬ࠠࠩࡲࡵࡳࡨ࡫ࡳࡴ࠰ࡨࡲࡻ࠴ࡇࡍࡑࡅࡅࡑࡥࡁࡈࡇࡑࡘࡤࡎࡔࡕࡒࡢࡔࡗࡕࡘ࡚ࠫࠣࡦࡴࡵࡴࡴࡶࡵࡥࡵ࠮ࠩ࠼ࠢࠥࠦࠧᄊ")
              bstack1l1l111lll_opy_ = bstack1l111l1l1_opy_.replace(bstack1l1l1l111l_opy_, bstack1l1l11lll1_opy_)
              with open(bstack1l11lll1l1_opy_, bstack111ll_opy_ (u"ࠩࡺࠫᄋ")) as f:
                f.write(bstack1l1l111lll_opy_)
    except Exception as e:
        logger.error(bstack11l111l1l_opy_.format(str(e)))