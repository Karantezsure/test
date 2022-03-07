from typing import Optional
from decimal import Decimal

from dipdup.models import Transaction
from dipdup.context import HandlerContext

import demo_tzbtc.models as models

from demo_tzbtc.types.tzbtc.parameter.mint import MintParameter
from demo_tzbtc.types.tzbtc.storage import TzbtcStorage
from demo_tzbtc.handlers.on_balance_update import on_balance_update


async def on_mint(
    ctx: HandlerContext,
    mint: Transaction[MintParameter, TzbtcStorage],
) -> None:
    ctx.logger("hey");
    amount = Decimal(mint.parameter.value) / (10 ** 8)
    await on_balance_update(
        address=mint.parameter.to,
        balance_update=amount,
        timestamp=mint.data.timestamp
    )