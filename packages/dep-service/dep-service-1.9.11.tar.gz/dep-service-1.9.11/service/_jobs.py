"""Cron jobs."""

from aiocronjob import Manager
from aiocronjob.main import add_routes

from dataclasses import dataclass
from logging import getLogger
from typing import Coroutine, Callable

from pathlib import Path
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from spec.types import App

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


def init_cron(app: App, manager: Manager):
    """Init cron."""

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    add_routes(
        app=app,
        path='/service/cron/',
        manager=manager,
    )

    cron_dir = Path(app.spec.path.static / 'cron')

    if not cron_dir.exists():
        log.error('Static directory does not exist')
        return

    app.mount(
        '/',
        StaticFiles(directory=cron_dir.as_posix(), html=True),
        name='static',
    )
