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


class UpdateChannelAvailableMessages(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``165``
        - ID: ``B23FC698``

    Parameters:
        channel_id (``int`` ``64-bit``):
            N/A

        available_min_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["channel_id", "available_min_id"]

    ID = 0xb23fc698
    QUALNAME = "types.UpdateChannelAvailableMessages"

    def __init__(self, *, channel_id: int, available_min_id: int) -> None:
        self.channel_id = channel_id  # long
        self.available_min_id = available_min_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelAvailableMessages":
        # No flags
        
        channel_id = Long.read(b)
        
        available_min_id = Int.read(b)
        
        return UpdateChannelAvailableMessages(channel_id=channel_id, available_min_id=available_min_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.available_min_id))
        
        return b.getvalue()
