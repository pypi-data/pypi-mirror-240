import asyncio
import logging
from functools import cached_property
from threading import Lock
from typing import List, Type

from aiogram import Bot, Dispatcher
from aiogram.client.session.middlewares.request_logging import RequestLogging
from prometheus_client import REGISTRY, CollectorRegistry
from prometheus_client_utils.collectors.asyncio_loop import AsyncioCollector
from prometheus_client_utils.push_clients.base import BasePushClient

from aiogram_prometheus.collectors import (
    BotAiogramCollector,
    DispatcherAiogramCollector,
    MessageMiddlewareAiogramCollector,
    ReceivedMessagesAiogramCollector,
    SendedMessagesAiogramCollector,
    SessionMiddlewareAiogramCollector,
)
from aiogram_prometheus.middlewares import MetricMessageMiddleware, MetricRequestMiddleware

logger = logging.getLogger('faust_prometheus')


class AiogramPrometheusExporter(object):
    dp: Dispatcher
    bots: List[Bot]
    push_client: BasePushClient

    DispatcherAiogramCollectorClass: Type[DispatcherAiogramCollector] = DispatcherAiogramCollector
    BotAiogramCollectorClass: Type[BotAiogramCollector] = BotAiogramCollector
    MiddlewareAiogramCollectorClass: Type[MessageMiddlewareAiogramCollector] = MessageMiddlewareAiogramCollector
    SessionMiddlewareAiogramCollectorClass: Type[SessionMiddlewareAiogramCollector] = SessionMiddlewareAiogramCollector
    SendedMessagesAiogramCollectorClass: Type[SendedMessagesAiogramCollector] = SendedMessagesAiogramCollector
    ReceivedMessagesAiogramCollectorClass: Type[ReceivedMessagesAiogramCollector] = ReceivedMessagesAiogramCollector

    def __init__(
        self,
        dp: Dispatcher,
        *bots: Bot,
        registry: CollectorRegistry = REGISTRY,
        push_client: BasePushClient,
    ) -> None:
        self.dp = dp
        self.bots = list(bots)
        self.registry = registry
        self.push_client = push_client

        self._started = False
        self._lock = Lock()

        self.dispatcher_collector(self.dp)

        self.dp.startup.register(self.startup_observer)
        self.dp.shutdown.register(self.shutdown_observer)

        self.dp.message.middleware(self.message_middleware)

    def received_messages_collector(self) -> ReceivedMessagesAiogramCollector:
        collector = self.ReceivedMessagesAiogramCollectorClass()
        self.registry.register(collector)
        return collector

    def sended_messages_collector(self) -> SendedMessagesAiogramCollector:
        collector = self.SendedMessagesAiogramCollectorClass()
        self.registry.register(collector)
        return collector

    def session_middleware_collector(self) -> SessionMiddlewareAiogramCollector:
        collector = self.SessionMiddlewareAiogramCollectorClass()
        self.registry.register(collector)
        return collector

    def message_middleware_collector(self) -> MessageMiddlewareAiogramCollector:
        collector = self.MiddlewareAiogramCollectorClass()
        self.registry.register(collector)
        return collector

    def bot_collector(self, bot: Bot) -> BotAiogramCollector:
        collector = self.BotAiogramCollectorClass(bot)
        self.registry.register(collector)
        return collector

    def dispatcher_collector(self, dp: Dispatcher) -> DispatcherAiogramCollector:
        collector = self.DispatcherAiogramCollectorClass(dp)
        self.registry.register(collector)
        return collector

    @cached_property
    def message_middleware(self) -> MetricMessageMiddleware:
        return MetricMessageMiddleware(self.message_middleware_collector())

    @cached_property
    def session_middleware(self) -> MetricRequestMiddleware:
        return MetricRequestMiddleware(self.session_middleware_collector())

    async def start(self):
        """Запуск отправки метрик в сборщик"""

        with self._lock:
            if self._started:
                return

            self._started = True

            loop = asyncio.get_running_loop()

            self.registry.register(AsyncioCollector(loop))

            self.push_client.schedule_push(5)

    async def stop(self):
        """Запуск отслеживания и отправки метрик"""

        with self._lock:
            if not self._started:
                return

            self._started = False

            self.push_client._schedule_task.cancel()

    async def startup_observer(self, bot: Bot):
        await bot.me()
        bot.session.middleware(RequestLogging())
        bot.session.middleware(self.session_middleware)

        self.bot_collector(bot)

        await self.start()

    async def shutdown_observer(self, bot: Bot):
        await self.stop()
