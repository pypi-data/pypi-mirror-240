from typing import List, Dict
from aiohttp import web

from boids_api.boids.boid_telemetry_event import BoidTelemetryEvent
from boids_api.boids.session_configuration_status import SessionConfigurationStatus
from boids_api.boids.session_timestamp import SessionTimestamp
from boids_api.boids.system_event import SystemEvent
from boids_api import util


async def pubsub_boids_boids_get(request: web.Request, ) -> web.Response:
    """pubsub_boids_boids_get

    


    """
    return web.Response(status=200)


async def pubsub_boids_system_events_get(request: web.Request, ) -> web.Response:
    """pubsub_boids_system_events_get

    


    """
    return web.Response(status=200)


async def pubsub_boids_system_time_get(request: web.Request, ) -> web.Response:
    """pubsub_boids_system_time_get

    


    """
    return web.Response(status=200)


async def pubsub_sessions_get(request: web.Request, ) -> web.Response:
    """pubsub_sessions_get

    


    """
    return web.Response(status=200)
