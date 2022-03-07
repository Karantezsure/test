from typing import Optional
from decimal import Decimal

from dipdup.models import Transaction
from dipdup.context import HandlerContext

import demo_tzbtc.models as models

from demo_tzbtc.types.tzbtc.parameter.transfer import TransferParameter
from demo_tzbtc.types.tzbtc.storage import TzbtcStorage
from demo_tzbtc.handlers.on_balance_update import on_balance_update


async def on_transfer(
    ctx: HandlerContext,
    transfer: Transaction[TransferParameter, TzbtcStorage],
) -> None:
    if transfer.parameter.from_ == transfer.parameter.to:
        # NOTE: Internal tzBTC transaction
        return

    amount = Decimal(transfer.parameter.value) / (10 ** 8)
    await on_balance_update(
        address=transfer.parameter.from_,
        balance_update=-amount,
        timestamp=transfer.data.timestamp,
    )
    await on_balance_update(address=transfer.parameter.to,
                            balance_update=amount,
                            timestamp=transfer.data.timestamp)