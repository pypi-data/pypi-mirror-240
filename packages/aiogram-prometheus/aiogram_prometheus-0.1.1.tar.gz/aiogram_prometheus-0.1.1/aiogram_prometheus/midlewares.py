from typing import Any, Awaitable, Callable, Coroutine

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class MetricsBaseMiddleware(BaseMiddleware):
    """Промежуточный слой для сборка метрик"""

    def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        return super().__call__(handler, event, data)
