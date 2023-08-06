"""Configure."""

from typing import Dict, List, Type
from logging import getLogger

from spec import types

log = getLogger(__name__)

# Use for service maintenance
# TODO: add modules status later
service_router = types.Router(prefix='/service', tags=['service'])


@service_router.get('/health')
async def health() -> types.JSONResponse:
    """Default health."""
    return types.JSONResponse({'status': 'ok'})


def prepare_routers(
    app: types.App,
    routers: List[types.Router] = None,
    service_routes: bool = True,
):
    """Prepare routers."""

    if service_routes:
        app.router.include_router(service_router)

    if routers:
        for router in routers:
            app.router.include_router(router)


def prepare_openapi(app: types.App, spec: types.Spec):
    """Prepare openapi."""

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = types.get_openapi(
        title=spec.service.name or spec.service.tech_name,
        version=spec.service.tech_version,
        description=spec.service.tech_description,
        routes=app.routes,
    )

    app.openapi_schema = openapi_schema

    return app.openapi_schema


def create(
    routers: List[types.Router] = None,
    modules: List[types.Module] = None,
    settings: Type[types.UserSettings] = None,
    kw: Dict = None,
    service_routes: bool = True,
) -> types.App:
    """Create service app."""

    spec = types.load_spec()
    user_settings = settings() if settings else None

    app = types.App(**kw) if kw else types.App()
    app.settings = user_settings
    app.spec = spec

    prepare_routers(app, routers=routers, service_routes=service_routes)
    prepare_openapi(app=app, spec=spec)

    if modules:
        for module in modules:
            try:
                module.inject(app)
            except Exception as _inject_ext:
                log_extra = {'alias': module.name}
                if app.spec.environment.dont_care_secrets():
                    log_extra.update({
                        'spec': spec,
                        'settings': settings,
                        'kw': kw,
                    })
                log.error(
                    f'Inject module {module.name} error: {_inject_ext}',
                    extra=log_extra,
                )
                raise types.exc_type.ModuleException(_inject_ext)

    return app
