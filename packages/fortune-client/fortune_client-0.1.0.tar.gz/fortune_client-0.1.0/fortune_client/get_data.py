
from .fortune_client import FortuneClient
from .parameters import Parameters
from .fortune_api_data import FortuneApiData, SLASH


def get_data(params: Parameters):
    fortune_client = FortuneClient(params.url)

    path: str = params.path[0] if len(params.path) > 0 else ''
    data: list | dict = fortune_client.request(
        path,
        params.explore,
        params.index,
    )

    if data is None:
        print("ERROR - data is None: {}".format(path))
        exit(1)
        # data = []

    yield FortuneApiData.create(path, data)

    if params.recursive:
        for item in data:
            if path is not None and len(path) > 0 and path[-1] == SLASH:
                new_path = path + item
            elif path is not None and len(path) > 0:
                new_path = path + SLASH + item
            else:
                new_path = item
            
            next_request_params = Parameters(
                url=params.url,
                explore=True,
                recursive=True if item[-1] == SLASH else False,
                path=(new_path,),
                index=None,
            )
            for sub_item in get_data(next_request_params):
                yield sub_item

