#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetPrivacy(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``165``
        - ID: ``DADBC950``

    Parameters:
        key (:obj:`InputPrivacyKey <pyrogram.raw.base.InputPrivacyKey>`):
            N/A

    Returns:
        :obj:`account.PrivacyRules <pyrogram.raw.base.account.PrivacyRules>`
    """

    __slots__: List[str] = ["key"]

    ID = 0xdadbc950
    QUALNAME = "functions.account.GetPrivacy"

    def __init__(self, *, key: "raw.base.InputPrivacyKey") -> None:
        self.key = key  # InputPrivacyKey

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetPrivacy":
        # No flags
        
        key = TLObject.read(b)
        
        return GetPrivacy(key=key)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.key.write())
        
        return b.getvalue()
