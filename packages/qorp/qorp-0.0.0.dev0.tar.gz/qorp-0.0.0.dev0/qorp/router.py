from asyncio import Future
import asyncio
from contextlib import contextmanager
from typing import Dict, Set

from .encryption import X25519PrivateKey, X25519PublicKey
from .frontend import Frontend
from .messages import RouteRequest
from .nodes import Node, Neighbour
from .transports import Listener


RREQ_TIMEOUT = 10


class Router(Node):

    private_key: X25519PrivateKey
    public_key: X25519PublicKey
    broadcast_listeners: Set[Listener]
    frontend: Frontend
    neighbours: Set[Neighbour]
    directions: Dict[Node, Neighbour]
    pending_requests: Dict[Node, Set["Future[Neighbour]"]]

    async def find_direction(self, target: Node, timeout: int = RREQ_TIMEOUT):
        request = RouteRequest(self, target)
        with self._track_request(target) as future:
            for neighbour in self.neighbours:
                neighbour.send(request)
            response = await asyncio.wait_for(future, timeout)
        return response

    @contextmanager
    def _track_request(self, target: Node):
        future: Future[Neighbour] = Future()
        requests = self.pending_requests.setdefault(target, set())
        requests.add(future)
        try:
            yield future
        finally:
            requests.remove(future)
