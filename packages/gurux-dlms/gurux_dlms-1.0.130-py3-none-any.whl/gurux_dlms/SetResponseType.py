#
#  --------------------------------------------------------------------------
#   Gurux Ltd
#
#
#
#  Filename: $HeadURL$
#
#  Version: $Revision$,
#                   $Date$
#                   $Author$
#
#  Copyright (c) Gurux Ltd
#
# ---------------------------------------------------------------------------
#
#   DESCRIPTION
#
#  This file is a part of Gurux Device Framework.
#
#  Gurux Device Framework is Open Source software; you can redistribute it
#  and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; version 2 of the License.
#  Gurux Device Framework is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  More information of Gurux products: http://www.gurux.org
#
#  This code is licensed under the GNU General Public License v2.
#  Full text may be retrieved at http://www.gnu.org/licenses/gpl-2.0.txt
# ---------------------------------------------------------------------------
from gurux_dlms.GXIntEnum import GXIntEnum

class SetResponseType(GXIntEnum):
    """Enumerates Set response types."""
    #
    # Normal set response.
    #
    NORMAL = 1

    #
    # Set response in data blocks.
    #
    DATA_BLOCK = 2

    #
    # Set response in last data block.
    #
    LAST_DATA_BLOCK = 3

    #
    # Set response in last data block with list.
    #
    LAST_DATA_BLOCK_WITH_LIST = 4

    #
    # Set with list response.
    #
    WITH_LIST = 5
