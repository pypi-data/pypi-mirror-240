from typing import Iterable

import aiogram
from aiogram import Bot, Dispatcher
from aiogram.types import Message, TelegramObject
from prometheus_client import Counter, Histogram
from prometheus_client.metrics_core import GaugeMetricFamily, InfoMetricFamily, Metric
from prometheus_client.registry import Collector


class DispatcherAiogramCollector(Collector):
    dp: Dispatcher

    def __init__(self, dp: Dispatcher, prefix: str = 'aiogram_') -> None:
        self.dp = dp
        self.prefix = prefix

        self.aiogram_info_metric = InfoMetricFamily(
            'aiogram',
            'Info about aiogram',
            value={
                'version': aiogram.__version__,
                'api_version': aiogram.__api_version__,
            },
        )

        self.dispatcher_info_metric = InfoMetricFamily(
            f'{self.prefix}_dispatcher',
            'Info about aiogram dispatcher',
            value={
                # 'version': self.dp.errors,
                # 'api_version': aiogram.__api_version__,
            },
        )

    def collect(self) -> Iterable[Metric]:
        yield self.aiogram_info_metric

        c = GaugeMetricFamily(
            f'{self.prefix}_observers',
            'Count of dispatcher`s observers',
            labels=['name'],
        )

        c.add_metric(['shutdown'], len(self.dp.shutdown.handlers))
        c.add_metric(['startup'], len(self.dp.startup.handlers))

        for observer_name, observer in self.dp.observers.items():
            c.add_metric([observer_name], len(observer.handlers))

        yield c

        yield InfoMetricFamily(
            f'{self.prefix}_fsm',
            'Info about dispatcher`s fsm',
            {
                'storage': self.dp.fsm.storage.__class__.__name__,
                'strategy': self.dp.fsm.strategy.__class__.__name__,
                'events_isolation': str(self.dp.fsm.events_isolation),
            },
        )


class BotAiogramCollector(Collector):
    bot: Bot

    def __init__(self, bot: Bot, prefix: str = 'aiogram_') -> None:
        self.bot = bot
        self.prefix = prefix

    def collect(self) -> Iterable[Metric]:
        bot_user = self.bot._me
        assert bot_user is not None

        yield InfoMetricFamily(
            f'{self.prefix}_bot',
            'Info about bot',
            {
                'id': str(self.bot.id),
                'username': str(bot_user.username),
                'is_bot': str(bot_user.is_bot),
                'first_name': str(bot_user.first_name),
                'last_name': str(bot_user.last_name),
                'language_code': str(bot_user.language_code),
                'is_premium': str(bot_user.is_premium),
                'added_to_attachment_menu': str(bot_user.added_to_attachment_menu),
                'can_join_groups': str(bot_user.can_join_groups),
                'can_read_all_group_messages': str(bot_user.can_read_all_group_messages),
                'supports_inline_queries': str(bot_user.supports_inline_queries),
                'parse_mode': str(self.bot.parse_mode),
                'disable_web_page_preview': str(self.bot.disable_web_page_preview),
                'protect_content': str(self.bot.protect_content),
            },
        )


class MiddlewareAiogramCollector(Collector):
    prefix: str
    events_counter: Counter
    events_histogram: Histogram

    def __init__(self, prefix: str = 'aiogram_') -> None:
        self.prefix = prefix

        labels = ['event_type', 'bot_username', 'chat_id', 'sender_id', 'status']

        self.events_counter = Counter(
            f'{self.prefix}_events',
            'Count of aiogram`s events',
            labels,
            registry=None,
        )
        self.events_histogram = Histogram(
            f'{self.prefix}_events_time',
            'Time of aiogram`s events',
            labels,
            registry=None,
        )

    def add_event(self, event: TelegramObject, success: bool, executing_time: float):
        labels = [
            event.__class__.__name__,
            event.bot._me.username,
            None,
            None,
            'success' if success else 'error',
        ]

        if isinstance(event, Message):
            labels = [
                event.__class__.__name__,
                event.bot._me.username,
                event.chat.id,
                event.from_user.id,
                'success' if success else 'error',
            ]

        self.events_counter.labels(*labels).inc()
        self.events_histogram.labels(*labels).observe(executing_time)

    def collect(self) -> Iterable[Metric]:
        yield from self.events_counter.collect()
        yield from self.events_histogram.collect()
