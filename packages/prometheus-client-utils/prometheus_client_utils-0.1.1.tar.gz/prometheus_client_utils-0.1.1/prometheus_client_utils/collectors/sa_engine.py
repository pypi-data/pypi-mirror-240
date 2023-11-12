import asyncio
import logging
from collections.abc import AsyncGenerator, Generator, Iterable
from typing import Union

from prometheus_client.metrics_core import InfoMetricFamily, Metric
from prometheus_client.registry import Collector
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncEngine

logger = logging.getLogger('prometheus_client_utils')


class SqlalchemyEngineCollector(Collector):
    def __init__(self, engine: Union[Engine, AsyncEngine]) -> None:
        super().__init__()
        self.engine = engine
        assert isinstance(engine, (Engine, AsyncEngine))

    async def async_collect(self) -> AsyncGenerator[Metric, None]:
        yield InfoMetricFamily('lorem', '')

    def sync_collect(self) -> Generator[Metric, None, None]:
        yield InfoMetricFamily('lorem', '')

    def collect(self) -> Iterable[Metric]:
        if isinstance(self.engine, AsyncEngine):
            itl: list[Metric] = []

            async def inner():
                async for m in self.async_collect():
                    itl.append(m)

            asyncio.run(inner())

            for m in itl:
                yield m

        elif isinstance(self.engine, Engine):
            yield from self.inner_async_collect()

        else:
            logger.error(f'Wrong type: {type(self.engine)}')
