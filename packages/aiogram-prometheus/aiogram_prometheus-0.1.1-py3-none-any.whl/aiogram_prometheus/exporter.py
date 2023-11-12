import asyncio
import logging
from threading import Lock
from typing import List

from aiogram import Bot, Dispatcher
from prometheus_client import REGISTRY, CollectorRegistry
from prometheus_client_utils.collectors.asyncio_loop import AsyncioCollector
from prometheus_client_utils.push_clients.base import BasePushClient

from aiogram_prometheus.collectors import BotAiogramCollector, DispatcherAiogramCollector, MiddlewareAiogramCollector
from aiogram_prometheus.middlewares import MetricMiddleware

logger = logging.getLogger('faust_prometheus')


class AiogramPrometheusExporter(object):
    dp: Dispatcher
    bots: List[Bot]
    push_client: BasePushClient

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

        self.registry.register(DispatcherAiogramCollector(self.dp))

        self.dp.startup.register(self.startup_observer)
        self.dp.shutdown.register(self.shutdown_observer)

    @property
    def middleware(self):
        collector = MiddlewareAiogramCollector()
        self.registry.register(collector)
        return MetricMiddleware(collector)

    async def start(self):
        """Запуск отправки метрик в сборщик"""

        with self._lock:
            if self._started:
                return

            self._started = True

            loop = asyncio.get_running_loop()

            self.registry.register(AsyncioCollector(loop))

            self.push_client.schedule_push(15)

    async def stop(self):
        """Запуск отслеживания и отправки метрик"""

        with self._lock:
            if not self._started:
                return

            self._started = False

            self.push_client._schedule_task.cancel()

    async def startup_observer(self, bot: Bot):
        await bot.me()

        self.registry.register(BotAiogramCollector(bot))

        await self.start()

    async def shutdown_observer(self, bot: Bot):
        await self.stop()
