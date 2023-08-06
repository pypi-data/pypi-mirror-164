"""Cron jobs."""

from aiocronjob import Manager
from dataclasses import dataclass
from logging import getLogger
from typing import Coroutine, Callable


log = getLogger(__name__)


@dataclass(frozen=True)
class CronJob:
    """Cron job."""

    name: str
    crontab: str
    job: Callable[[], Coroutine]


class CronManager(Manager):
    """Cron manager."""

    async def on_job_started(self, job_name: str):
        """On cron job start."""
        log.debug(f'Job {job_name} started')

    async def on_job_exception(self, job_name: str, exception: BaseException):
        """On cron job on job exception."""
        log.error(f'Job {job_name} exc: {exception}', exc_info=True)

    async def on_job_cancelled(self, job_name: str):
        """On cron job cancelled."""
        log.error(f'Job {job_name} cancelled')

    async def on_job_finished(self, job_name: str):
        """On cron job execution."""
        log.error(f'Job {job_name} finished')

    async def on_startup(self):
        """Cron manager prepare."""
        log.error('Cron manager started')

    async def on_shutdown(self):
        """Cron manager release."""
        log.error('Cron manager finished')
