import logging
import time
from typing import Any, Awaitable, Callable, Coroutine, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from aiogram_prometheus.collectors import MiddlewareAiogramCollector

logger = logging.getLogger('aiogram_prometheus')


class ReceivedEventsLoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        start_time = time.time()

        try:
            res = await handler(event, data)

        except BaseException as ex:
            elapsed_time = time.time() - start_time
            logger.warning(
                'error event dump',
                extra={
                    'event_type': event.__class__.__name__,
                    'event_bot_id': event.bot.id,
                    'event_bot_username': getattr(event.bot._me, 'username', 'None'),
                    'event_elapsed_time': elapsed_time,
                    'exception': ex,
                },
            )

            raise ex

        elapsed_time = time.time() - start_time
        logger.debug(
            'event dump',
            extra={
                'event_type': event.__class__.__name__,
                'event_bot_id': event.bot.id,
                'event_bot_username': getattr(event.bot._me, 'username', 'None'),
                'event_elapsed_time': elapsed_time,
            },
        )

        return res


class MetricMiddleware(BaseMiddleware):
    collector: MiddlewareAiogramCollector

    def __init__(self, collector: MiddlewareAiogramCollector) -> None:
        self.collector = collector

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Coroutine[Any, Any, Any]:
        start_time = time.time()

        try:
            res = await handler(event, data)

        except BaseException as ex:
            delta_time = time.time() - start_time
            self.collector.add_event(event, False, delta_time)
            raise ex

        delta_time = time.time() - start_time
        self.collector.add_event(event, True, delta_time)
        return res
