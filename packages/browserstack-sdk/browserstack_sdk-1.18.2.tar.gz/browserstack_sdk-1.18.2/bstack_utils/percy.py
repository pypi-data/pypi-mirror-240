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
import re
import sys
import json
import time
import shutil
import tempfile
import requests
import subprocess
from threading import Thread
from os.path import expanduser
from bstack_utils.constants import *
from requests.auth import HTTPBasicAuth
from bstack_utils.helper import bstack11l1l111_opy_, bstack1ll1l111_opy_
class bstack1lll1111_opy_:
  working_dir = os.getcwd()
  bstack1l111l111_opy_ = False
  config = {}
  binary_path = bstack111ll_opy_ (u"ࠨࠩᅳ")
  bstack11lllll11l_opy_ = bstack111ll_opy_ (u"ࠩࠪᅴ")
  bstack1l1111l111_opy_ = False
  bstack11llll1l11_opy_ = None
  bstack1l1111l11l_opy_ = {}
  bstack1l11111lll_opy_ = 300
  bstack11lllll111_opy_ = False
  logger = None
  bstack11llllll1l_opy_ = False
  bstack11llll1lll_opy_ = bstack111ll_opy_ (u"ࠪࠫᅵ")
  bstack11lll1ll1l_opy_ = {
    bstack111ll_opy_ (u"ࠫࡨ࡮ࡲࡰ࡯ࡨࠫᅶ") : 1,
    bstack111ll_opy_ (u"ࠬ࡬ࡩࡳࡧࡩࡳࡽ࠭ᅷ") : 2,
    bstack111ll_opy_ (u"࠭ࡥࡥࡩࡨࠫᅸ") : 3,
    bstack111ll_opy_ (u"ࠧࡴࡣࡩࡥࡷ࡯ࠧᅹ") : 4
  }
  def __init__(self) -> None: pass
  def bstack1l1111111l_opy_(self):
    bstack11lll1l1ll_opy_ = bstack111ll_opy_ (u"ࠨࠩᅺ")
    bstack11lll1lll1_opy_ = sys.platform
    bstack1l111l11l1_opy_ = bstack111ll_opy_ (u"ࠩࡳࡩࡷࡩࡹࠨᅻ")
    if re.match(bstack111ll_opy_ (u"ࠥࡨࡦࡸࡷࡪࡰࡿࡱࡦࡩࠠࡰࡵࠥᅼ"), bstack11lll1lll1_opy_) != None:
      bstack11lll1l1ll_opy_ = bstack1l1l1ll1l1_opy_ + bstack111ll_opy_ (u"ࠦ࠴ࡶࡥࡳࡥࡼ࠱ࡴࡹࡸ࠯ࡼ࡬ࡴࠧᅽ")
      self.bstack11llll1lll_opy_ = bstack111ll_opy_ (u"ࠬࡳࡡࡤࠩᅾ")
    elif re.match(bstack111ll_opy_ (u"ࠨ࡭ࡴࡹ࡬ࡲࢁࡳࡳࡺࡵࡿࡱ࡮ࡴࡧࡸࡾࡦࡽ࡬ࡽࡩ࡯ࡾࡥࡧࡨࡽࡩ࡯ࡾࡺ࡭ࡳࡩࡥࡽࡧࡰࡧࢁࡽࡩ࡯࠵࠵ࠦᅿ"), bstack11lll1lll1_opy_) != None:
      bstack11lll1l1ll_opy_ = bstack1l1l1ll1l1_opy_ + bstack111ll_opy_ (u"ࠢ࠰ࡲࡨࡶࡨࡿ࠭ࡸ࡫ࡱ࠲ࡿ࡯ࡰࠣᆀ")
      bstack1l111l11l1_opy_ = bstack111ll_opy_ (u"ࠣࡲࡨࡶࡨࡿ࠮ࡦࡺࡨࠦᆁ")
      self.bstack11llll1lll_opy_ = bstack111ll_opy_ (u"ࠩࡺ࡭ࡳ࠭ᆂ")
    else:
      bstack11lll1l1ll_opy_ = bstack1l1l1ll1l1_opy_ + bstack111ll_opy_ (u"ࠥ࠳ࡵ࡫ࡲࡤࡻ࠰ࡰ࡮ࡴࡵࡹ࠰ࡽ࡭ࡵࠨᆃ")
      self.bstack11llll1lll_opy_ = bstack111ll_opy_ (u"ࠫࡱ࡯࡮ࡶࡺࠪᆄ")
    return bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_
  def bstack11lll11ll1_opy_(self):
    try:
      bstack11llllllll_opy_ = [os.path.join(expanduser(bstack111ll_opy_ (u"ࠧࢄࠢᆅ")), bstack111ll_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᆆ")), self.working_dir, tempfile.gettempdir()]
      for path in bstack11llllllll_opy_:
        if(self.bstack11lll1ll11_opy_(path)):
          return path
      raise bstack111ll_opy_ (u"ࠢࡖࡰࡤࡰࡧ࡫ࠠࡵࡱࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠦᆇ")
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡯࡮ࡥࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡶࡡࡵࡪࠣࡪࡴࡸࠠࡱࡧࡵࡧࡾࠦࡤࡰࡹࡱࡰࡴࡧࡤ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࠳ࠠࡼࡿࠥᆈ").format(e))
  def bstack11lll1ll11_opy_(self, path):
    try:
      if not os.path.exists(path):
        os.makedirs(path)
      return True
    except:
      return False
  def bstack1l11111l11_opy_(self, bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_):
    try:
      bstack11lll1llll_opy_ = self.bstack11lll11ll1_opy_()
      bstack1l111l1lll_opy_ = os.path.join(bstack11lll1llll_opy_, bstack111ll_opy_ (u"ࠩࡳࡩࡷࡩࡹ࠯ࡼ࡬ࡴࠬᆉ"))
      bstack1l1111ll1l_opy_ = os.path.join(bstack11lll1llll_opy_, bstack1l111l11l1_opy_)
      if os.path.exists(bstack1l1111ll1l_opy_):
        self.logger.info(bstack111ll_opy_ (u"ࠥࡔࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡳࡺࡴࡤࠡ࡫ࡱࠤࢀࢃࠬࠡࡵ࡮࡭ࡵࡶࡩ࡯ࡩࠣࡨࡴࡽ࡮࡭ࡱࡤࡨࠧᆊ").format(bstack1l1111ll1l_opy_))
        return bstack1l1111ll1l_opy_
      if os.path.exists(bstack1l111l1lll_opy_):
        self.logger.info(bstack111ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡾ࡮ࡶࠠࡧࡱࡸࡲࡩࠦࡩ࡯ࠢࡾࢁ࠱ࠦࡵ࡯ࡼ࡬ࡴࡵ࡯࡮ࡨࠤᆋ").format(bstack1l111l1lll_opy_))
        return self.bstack1l111l1ll1_opy_(bstack1l111l1lll_opy_, bstack1l111l11l1_opy_)
      self.logger.info(bstack111ll_opy_ (u"ࠧࡊ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡥ࡭ࡳࡧࡲࡺࠢࡩࡶࡴࡳࠠࡼࡿࠥᆌ").format(bstack11lll1l1ll_opy_))
      response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"࠭ࡇࡆࡖࠪᆍ"), bstack11lll1l1ll_opy_, {}, {})
      if response.status_code == 200:
        with open(bstack1l111l1lll_opy_, bstack111ll_opy_ (u"ࠧࡸࡤࠪᆎ")) as file:
          file.write(response.content)
        self.logger.info(bstack1l111l11ll_opy_ (u"ࠣࡆࡲࡻࡳࡲ࡯ࡢࡦࡨࡨࠥࡶࡥࡳࡥࡼࠤࡧ࡯࡮ࡢࡴࡼࠤࡦࡴࡤࠡࡵࡤࡺࡪࡪࠠࡢࡶࠣࡿࡧ࡯࡮ࡢࡴࡼࡣࡿ࡯ࡰࡠࡲࡤࡸ࡭ࢃࠢᆏ"))
        return self.bstack1l111l1ll1_opy_(bstack1l111l1lll_opy_, bstack1l111l11l1_opy_)
      else:
        raise(bstack1l111l11ll_opy_ (u"ࠤࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࠠࡵࡪࡨࠤ࡫࡯࡬ࡦ࠰ࠣࡗࡹࡧࡴࡶࡵࠣࡧࡴࡪࡥ࠻ࠢࡾࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࡹࡴࡢࡶࡸࡷࡤࡩ࡯ࡥࡧࢀࠦᆐ"))
    except:
      self.logger.error(bstack111ll_opy_ (u"࡙ࠥࡳࡧࡢ࡭ࡧࠣࡸࡴࠦࡤࡰࡹࡱࡰࡴࡧࡤࠡࡲࡨࡶࡨࡿࠠࡣ࡫ࡱࡥࡷࡿࠢᆑ"))
  def bstack1l1111l1l1_opy_(self, bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_):
    try:
      bstack1l1111ll1l_opy_ = self.bstack1l11111l11_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_)
      bstack11lllllll1_opy_ = self.bstack11lll1l11l_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_, bstack1l1111ll1l_opy_)
      return bstack1l1111ll1l_opy_, bstack11lllllll1_opy_
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡨࡧࡷࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠣࡴࡦࡺࡨࠣᆒ").format(e))
    return bstack1l1111ll1l_opy_, False
  def bstack11lll1l11l_opy_(self, bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_, bstack1l1111ll1l_opy_, bstack1l11111ll1_opy_ = 0):
    if bstack1l11111ll1_opy_ > 1:
      return False
    if bstack1l1111ll1l_opy_ == None or os.path.exists(bstack1l1111ll1l_opy_) == False:
      self.logger.warn(bstack111ll_opy_ (u"ࠧࡖࡥࡳࡥࡼࠤࡵࡧࡴࡩࠢࡱࡳࡹࠦࡦࡰࡷࡱࡨ࠱ࠦࡲࡦࡶࡵࡽ࡮ࡴࡧࠡࡦࡲࡻࡳࡲ࡯ࡢࡦࠥᆓ"))
      bstack1l1111ll1l_opy_ = self.bstack1l11111l11_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_)
      self.bstack11lll1l11l_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_, bstack1l1111ll1l_opy_, bstack1l11111ll1_opy_+1)
    bstack1l111l111l_opy_ = bstack111ll_opy_ (u"ࠨ࡞࠯ࠬࡃࡴࡪࡸࡣࡺ࡞࠲ࡧࡱ࡯ࠠ࡝ࡦ࠱ࡠࡩ࠱࠮࡝ࡦ࠮ࠦᆔ")
    command = bstack111ll_opy_ (u"ࠧࡼࡿࠣ࠱࠲ࡼࡥࡳࡵ࡬ࡳࡳ࠭ᆕ").format(bstack1l1111ll1l_opy_)
    bstack1l11111111_opy_ = subprocess.check_output(command, shell=True, text=True)
    if re.match(bstack1l111l111l_opy_, bstack1l11111111_opy_) != None:
      return True
    else:
      self.logger.error(bstack111ll_opy_ (u"ࠣࡒࡨࡶࡨࡿࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡥ࡫ࡩࡨࡱࠠࡧࡣ࡬ࡰࡪࡪࠢᆖ"))
      bstack1l1111ll1l_opy_ = self.bstack1l11111l11_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_)
      self.bstack11lll1l11l_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_, bstack1l1111ll1l_opy_, bstack1l11111ll1_opy_+1)
  def bstack1l111l1ll1_opy_(self, bstack1l111l1lll_opy_, bstack1l111l11l1_opy_):
    try:
      working_dir = os.path.dirname(bstack1l111l1lll_opy_)
      shutil.unpack_archive(bstack1l111l1lll_opy_, working_dir)
      bstack1l1111ll1l_opy_ = os.path.join(working_dir, bstack1l111l11l1_opy_)
      os.chmod(bstack1l1111ll1l_opy_, 0o755)
      return bstack1l1111ll1l_opy_
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡻ࡮ࡻ࡫ࡳࠤࡵ࡫ࡲࡤࡻࠣࡦ࡮ࡴࡡࡳࡻࠥᆗ"))
  def bstack1l1111ll11_opy_(self):
    try:
      percy = str(self.config.get(bstack111ll_opy_ (u"ࠪࡴࡪࡸࡣࡺࠩᆘ"), bstack111ll_opy_ (u"ࠦ࡫ࡧ࡬ࡴࡧࠥᆙ"))).lower()
      if percy != bstack111ll_opy_ (u"ࠧࡺࡲࡶࡧࠥᆚ"):
        return False
      self.bstack1l1111l111_opy_ = True
      return True
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡧࡩࡹ࡫ࡣࡵࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᆛ").format(e))
  def init(self, bstack1l111l111_opy_, config, logger):
    self.bstack1l111l111_opy_ = bstack1l111l111_opy_
    self.config = config
    self.logger = logger
    if not self.bstack1l1111ll11_opy_():
      return
    self.bstack1l1111l11l_opy_ = config.get(bstack111ll_opy_ (u"ࠧࡱࡧࡵࡧࡾࡕࡰࡵ࡫ࡲࡲࡸ࠭ᆜ"), {})
    try:
      bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_ = self.bstack1l1111111l_opy_()
      bstack1l1111ll1l_opy_, bstack11lllllll1_opy_ = self.bstack1l1111l1l1_opy_(bstack11lll1l1ll_opy_, bstack1l111l11l1_opy_)
      if bstack11lllllll1_opy_:
        self.binary_path = bstack1l1111ll1l_opy_
        thread = Thread(target=self.bstack11lll11lll_opy_)
        thread.start()
      else:
        self.bstack11llllll1l_opy_ = True
        self.logger.error(bstack111ll_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡹࠡࡲࡤࡸ࡭ࠦࡦࡰࡷࡱࡨࠥ࠳ࠠࡼࡿ࠯ࠤ࡚ࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡐࡦࡴࡦࡽࠧᆝ").format(bstack1l1111ll1l_opy_))
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠤࡘࡲࡦࡨ࡬ࡦࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻ࠯ࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡼࡿࠥᆞ").format(e))
  def bstack11llll1ll1_opy_(self):
    try:
      logfile = os.path.join(self.working_dir, bstack111ll_opy_ (u"ࠪࡰࡴ࡭ࠧᆟ"), bstack111ll_opy_ (u"ࠫࡵ࡫ࡲࡤࡻ࠱ࡰࡴ࡭ࠧᆠ"))
      os.makedirs(os.path.dirname(logfile)) if not os.path.exists(os.path.dirname(logfile)) else None
      self.logger.debug(bstack111ll_opy_ (u"ࠧࡖࡵࡴࡪ࡬ࡲ࡬ࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࡵࠣࡥࡹࠦࡻࡾࠤᆡ").format(logfile))
      self.bstack11lllll11l_opy_ = logfile
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠨࡕ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡶࡩࡹࠦࡰࡦࡴࡦࡽࠥࡲ࡯ࡨࠢࡳࡥࡹ࡮ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᆢ").format(e))
  def bstack11lll11lll_opy_(self):
    bstack1l1111l1ll_opy_ = self.bstack11lllll1l1_opy_()
    if bstack1l1111l1ll_opy_ == None:
      self.bstack11llllll1l_opy_ = True
      self.logger.error(bstack111ll_opy_ (u"ࠢࡑࡧࡵࡧࡾࠦࡴࡰ࡭ࡨࡲࠥࡴ࡯ࡵࠢࡩࡳࡺࡴࡤ࠭ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡵ࡫ࡲࡤࡻࠥᆣ"))
      return False
    command_args = [bstack111ll_opy_ (u"ࠣࡣࡳࡴ࠿࡫ࡸࡦࡥ࠽ࡷࡹࡧࡲࡵࠤᆤ") if self.bstack1l111l111_opy_ else bstack111ll_opy_ (u"ࠩࡨࡼࡪࡩ࠺ࡴࡶࡤࡶࡹ࠭ᆥ")]
    bstack1l111111ll_opy_ = self.bstack1l111l1111_opy_()
    if bstack1l111111ll_opy_ != None:
      command_args.append(bstack111ll_opy_ (u"ࠥ࠱ࡨࠦࡻࡾࠤᆦ").format(bstack1l111111ll_opy_))
    env = os.environ.copy()
    env[bstack111ll_opy_ (u"ࠦࡕࡋࡒࡄ࡛ࡢࡘࡔࡑࡅࡏࠤᆧ")] = bstack1l1111l1ll_opy_
    bstack11llllll11_opy_ = [self.binary_path]
    self.bstack11llll1ll1_opy_()
    self.bstack11llll1l11_opy_ = self.bstack11llll11ll_opy_(bstack11llllll11_opy_ + command_args, env)
    self.logger.debug(bstack111ll_opy_ (u"࡙ࠧࡴࡢࡴࡷ࡭ࡳ࡭ࠠࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠨᆨ"))
    bstack1l11111ll1_opy_ = 0
    while self.bstack11llll1l11_opy_.poll() == None:
      bstack11lll1l111_opy_ = self.bstack1l1111llll_opy_()
      if bstack11lll1l111_opy_:
        self.logger.debug(bstack111ll_opy_ (u"ࠨࡈࡦࡣ࡯ࡸ࡭ࠦࡃࡩࡧࡦ࡯ࠥࡹࡵࡤࡥࡨࡷࡸ࡬ࡵ࡭ࠤᆩ"))
        self.bstack11lllll111_opy_ = True
        return True
      bstack1l11111ll1_opy_ += 1
      self.logger.debug(bstack111ll_opy_ (u"ࠢࡉࡧࡤࡰࡹ࡮ࠠࡄࡪࡨࡧࡰࠦࡒࡦࡶࡵࡽࠥ࠳ࠠࡼࡿࠥᆪ").format(bstack1l11111ll1_opy_))
      time.sleep(2)
    self.logger.error(bstack111ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡴࡪࡸࡣࡺ࠮ࠣࡌࡪࡧ࡬ࡵࡪࠣࡇ࡭࡫ࡣ࡬ࠢࡉࡥ࡮ࡲࡥࡥࠢࡤࡪࡹ࡫ࡲࠡࡽࢀࠤࡦࡺࡴࡦ࡯ࡳࡸࡸࠨᆫ").format(bstack1l11111ll1_opy_))
    self.bstack11llllll1l_opy_ = True
    return False
  def bstack1l1111llll_opy_(self, bstack1l11111ll1_opy_ = 0):
    try:
      if bstack1l11111ll1_opy_ > 10:
        return False
      bstack11lllll1ll_opy_ = os.environ.get(bstack111ll_opy_ (u"ࠩࡓࡉࡗࡉ࡙ࡠࡕࡈࡖ࡛ࡋࡒࡠࡃࡇࡈࡗࡋࡓࡔࠩᆬ"), bstack111ll_opy_ (u"ࠪ࡬ࡹࡺࡰ࠻࠱࠲ࡰࡴࡩࡡ࡭ࡪࡲࡷࡹࡀ࠵࠴࠵࠻ࠫᆭ"))
      bstack1l1111lll1_opy_ = bstack11lllll1ll_opy_ + bstack1l1l1llll1_opy_
      response = requests.get(bstack1l1111lll1_opy_)
      return True if response.json() else False
    except:
      return False
  def bstack11lllll1l1_opy_(self):
    bstack1l111ll111_opy_ = bstack111ll_opy_ (u"ࠫࡦࡶࡰࠨᆮ") if self.bstack1l111l111_opy_ else bstack111ll_opy_ (u"ࠬࡧࡵࡵࡱࡰࡥࡹ࡫ࠧᆯ")
    bstack1l1l1l11ll_opy_ = bstack111ll_opy_ (u"ࠨࡡࡱ࡫࠲ࡥࡵࡶ࡟ࡱࡧࡵࡧࡾ࠵ࡧࡦࡶࡢࡴࡷࡵࡪࡦࡥࡷࡣࡹࡵ࡫ࡦࡰࡂࡲࡦࡳࡥ࠾ࡽࢀࠪࡹࡿࡰࡦ࠿ࡾࢁࠧᆰ").format(self.config[bstack111ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᆱ")], bstack1l111ll111_opy_)
    uri = bstack11l1l111_opy_(bstack1l1l1l11ll_opy_)
    try:
      response = bstack1ll1l111_opy_(bstack111ll_opy_ (u"ࠨࡉࡈࡘࠬᆲ"), uri, {}, {bstack111ll_opy_ (u"ࠩࡤࡹࡹ࡮ࠧᆳ"): (self.config[bstack111ll_opy_ (u"ࠪࡹࡸ࡫ࡲࡏࡣࡰࡩࠬᆴ")], self.config[bstack111ll_opy_ (u"ࠫࡦࡩࡣࡦࡵࡶࡏࡪࡿࠧᆵ")])})
      if response.status_code == 200:
        bstack1l111111l1_opy_ = response.json()
        if bstack111ll_opy_ (u"ࠧࡺ࡯࡬ࡧࡱࠦᆶ") in bstack1l111111l1_opy_:
          return bstack1l111111l1_opy_[bstack111ll_opy_ (u"ࠨࡴࡰ࡭ࡨࡲࠧᆷ")]
        else:
          raise bstack111ll_opy_ (u"ࠧࡕࡱ࡮ࡩࡳࠦࡎࡰࡶࠣࡊࡴࡻ࡮ࡥࠢ࠰ࠤࢀࢃࠧᆸ").format(bstack1l111111l1_opy_)
      else:
        raise bstack111ll_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡴࡪࡸࡣࡺࠢࡷࡳࡰ࡫࡮࠭ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤࡸࡺࡡࡵࡷࡶࠤ࠲ࠦࡻࡾ࠮ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥࡈ࡯ࡥࡻࠣ࠱ࠥࢁࡽࠣᆹ").format(response.status_code, response.json())
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡵࡩࡦࡺࡩ࡯ࡩࠣࡴࡪࡸࡣࡺࠢࡳࡶࡴࡰࡥࡤࡶࠥᆺ").format(e))
  def bstack1l111l1111_opy_(self):
    bstack1l11111l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack111ll_opy_ (u"ࠥࡴࡪࡸࡣࡺࡅࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳࠨᆻ"))
    try:
      if bstack111ll_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬᆼ") not in self.bstack1l1111l11l_opy_:
        self.bstack1l1111l11l_opy_[bstack111ll_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭ᆽ")] = 2
      with open(bstack1l11111l1l_opy_, bstack111ll_opy_ (u"࠭ࡷࠨᆾ")) as fp:
        json.dump(self.bstack1l1111l11l_opy_, fp)
      return bstack1l11111l1l_opy_
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡧࡷ࡫ࡡࡵࡧࠣࡴࡪࡸࡣࡺࠢࡦࡳࡳ࡬ࠬࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࢀࢃࠢᆿ").format(e))
  def bstack11llll11ll_opy_(self, cmd, env = os.environ.copy()):
    try:
      if self.bstack11llll1lll_opy_ == bstack111ll_opy_ (u"ࠨࡹ࡬ࡲࠬᇀ"):
        bstack1l111ll11l_opy_ = [bstack111ll_opy_ (u"ࠩࡦࡱࡩ࠴ࡥࡹࡧࠪᇁ"), bstack111ll_opy_ (u"ࠪ࠳ࡨ࠭ᇂ")]
        cmd = bstack1l111ll11l_opy_ + cmd
      cmd = bstack111ll_opy_ (u"ࠫࠥ࠭ᇃ").join(cmd)
      self.logger.debug(bstack111ll_opy_ (u"ࠧࡘࡵ࡯ࡰ࡬ࡲ࡬ࠦࡻࡾࠤᇄ").format(cmd))
      with open(self.bstack11lllll11l_opy_, bstack111ll_opy_ (u"ࠨࡡࠣᇅ")) as bstack11llll1l1l_opy_:
        process = subprocess.Popen(cmd, shell=True, stdout=bstack11llll1l1l_opy_, text=True, stderr=bstack11llll1l1l_opy_, env=env, universal_newlines=True)
      return process
    except Exception as e:
      self.bstack11llllll1l_opy_ = True
      self.logger.error(bstack111ll_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡳࡩࡷࡩࡹࠡࡹ࡬ࡸ࡭ࠦࡣ࡮ࡦࠣ࠱ࠥࢁࡽ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲ࠿ࠦࡻࡾࠤᇆ").format(cmd, e))
  def shutdown(self):
    try:
      if self.bstack11lllll111_opy_:
        self.logger.info(bstack111ll_opy_ (u"ࠣࡕࡷࡳࡵࡶࡩ࡯ࡩࠣࡔࡪࡸࡣࡺࠤᇇ"))
        cmd = [self.binary_path, bstack111ll_opy_ (u"ࠤࡨࡼࡪࡩ࠺ࡴࡶࡲࡴࠧᇈ")]
        self.bstack11llll11ll_opy_(cmd)
        self.bstack11lllll111_opy_ = False
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡱࡳࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡧࡴࡳ࡭ࡢࡰࡧࠤ࠲ࠦࡻࡾ࠮ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᇉ").format(cmd, e))
  def bstack1ll11llll_opy_(self):
    if not self.bstack1l1111l111_opy_:
      return
    try:
      bstack11lll1l1l1_opy_ = 0
      while not self.bstack11lllll111_opy_ and bstack11lll1l1l1_opy_ < self.bstack1l11111lll_opy_:
        if self.bstack11llllll1l_opy_:
          self.logger.info(bstack111ll_opy_ (u"ࠦࡕ࡫ࡲࡤࡻࠣࡷࡪࡺࡵࡱࠢࡩࡥ࡮ࡲࡥࡥࠤᇊ"))
          return
        time.sleep(1)
        bstack11lll1l1l1_opy_ += 1
      os.environ[bstack111ll_opy_ (u"ࠬࡖࡅࡓࡅ࡜ࡣࡇࡋࡓࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࠫᇋ")] = str(self.bstack11llll1111_opy_())
      self.logger.info(bstack111ll_opy_ (u"ࠨࡐࡦࡴࡦࡽࠥࡹࡥࡵࡷࡳࠤࡨࡵ࡭ࡱ࡮ࡨࡸࡪࡪࠢᇌ"))
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"ࠢࡖࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡷࡪࡺࡵࡱࠢࡳࡩࡷࡩࡹ࠭ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࢁࡽࠣᇍ").format(e))
  def bstack11llll1111_opy_(self):
    if self.bstack1l111l111_opy_:
      return
    try:
      bstack11llll11l1_opy_ = [platform[bstack111ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪ࠭ᇎ")].lower() for platform in self.config.get(bstack111ll_opy_ (u"ࠩࡳࡰࡦࡺࡦࡰࡴࡰࡷࠬᇏ"), [])]
      bstack1l111l1l1l_opy_ = sys.maxsize
      bstack11llll111l_opy_ = bstack111ll_opy_ (u"ࠪࠫᇐ")
      for browser in bstack11llll11l1_opy_:
        if browser in self.bstack11lll1ll1l_opy_:
          bstack1l111l1l11_opy_ = self.bstack11lll1ll1l_opy_[browser]
        if bstack1l111l1l11_opy_ < bstack1l111l1l1l_opy_:
          bstack1l111l1l1l_opy_ = bstack1l111l1l11_opy_
          bstack11llll111l_opy_ = browser
      return bstack11llll111l_opy_
    except Exception as e:
      self.logger.error(bstack111ll_opy_ (u"࡚ࠦࡴࡡࡣ࡮ࡨࠤࡹࡵࠠࡧ࡫ࡱࡨࠥࡨࡥࡴࡶࠣࡴࡱࡧࡴࡧࡱࡵࡱ࠱ࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢࡾࢁࠧᇑ").format(e))