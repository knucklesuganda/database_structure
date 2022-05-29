import typing

import fastapi
import uvicorn
from starlette.responses import JSONResponse

from containers import Container
from users.api import router as users_router


class CustomResponse(JSONResponse):
    def render(self, content: typing.Any) -> bytes:
        return super(CustomResponse, self).render({
            "data": content,
            "version": "1.0.0",
        })


app = fastapi.FastAPI(default_response_class=CustomResponse)
app.include_router(users_router, prefix='/users')

container = Container()


if __name__ == '__main__':
    uvicorn.run(app)
