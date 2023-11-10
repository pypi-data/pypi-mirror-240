from typing import List, Dict
from aiohttp import web

from boids_api.boids.boid import Boid
from boids_api.boids.boid_list import BoidList
from boids_api.boids.error_model import ErrorModel
from boids_api import util


async def session_session_uuid_boid_boid_uuid_delete(request: web.Request, session_uuid, boid_uuid) -> web.Response:
    """session_session_uuid_boid_boid_uuid_delete

    

    :param session_uuid: 
    :type session_uuid: str
    :type session_uuid: str
    :param boid_uuid: 
    :type boid_uuid: str
    :type boid_uuid: str

    """
    return web.Response(status=200)


async def session_session_uuid_boid_boid_uuid_get(request: web.Request, session_uuid, boid_uuid) -> web.Response:
    """session_session_uuid_boid_boid_uuid_get

    

    :param session_uuid: 
    :type session_uuid: str
    :type session_uuid: str
    :param boid_uuid: 
    :type boid_uuid: str
    :type boid_uuid: str

    """
    return web.Response(status=200)


async def session_uuid_boid_get(request: web.Request, uuid, order_by=None, offset=None, limit=None) -> web.Response:
    """session_uuid_boid_get

    Return the list of Boids

    :param uuid: 
    :type uuid: str
    :type uuid: str
    :param order_by: Field name to sort by.  Defaults to ascending. For descending, prepend a &#39;-&#39; minus.  Examples: &#39;title&#39; (sorts by title ascending), &#39;-title&#39; sorts by title descending) 
    :type order_by: str
    :param offset: Pagination offset (0-based)
    :type offset: int
    :param limit: Pagination size
    :type limit: int

    """
    return web.Response(status=200)


async def session_uuid_boid_post(request: web.Request, uuid, body=None) -> web.Response:
    """session_uuid_boid_post

    Create a Boid.  The &#39;id&#39; and &#39;timestamp&#39; fields must not be present. The newly created Boid is assigned an ID by the simulation. 

    :param uuid: 
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = Boid.from_dict(body)
    return web.Response(status=200)
