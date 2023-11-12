import codecs
import json
from .get_data import FortuneApiData


def text_format(
        data: FortuneApiData,
        header: bool = False,
        show_directory: bool = True,
        decode_off_fortunes: bool = False,
        out_json: bool = False,
):

    if data.content_type() == FortuneApiData.DICT:
        print_fortune(
            data.content['fortune'],
            data.content['file'],
            data.content['index'],
            decode_off_fortunes,
            'json' if out_json is True else 'text'
        )
        if header:
            print("{} ({})".format(data.content['file'], data.content['index']))
        return

    if show_directory is False and data.isDirectory is True:
        return

    if header:
        print(f"path: {data.path}, isDirectory: {data.isDirectory}")

    if data.isDirectory is True:
        for item in data.content:
            print(item)
    else:
        index: int = 0
        for item in data.content:
            if header:
                print(f"%fortune (index: {index}):")
            print_fortune(
                item,
                data.path,
                index,
                decode_off_fortunes,
                'json' if out_json is True else 'text'
            )
            index += 1


def print_fortune(
        fortune: str,
        path: str,
        index: int,
        decode: bool,
        out_format: str = 'text'
) -> None:
    if decode is True and path.find('off/') >= 0:
        fortune = codecs.encode(fortune, 'rot_13')
    if out_format == 'json':
        try:
            print(
                json.dumps({
                    'file': path,
                    'index': index,
                    'fortune': fortune,
                    },
                    ensure_ascii=False
                )
                .encode('utf8')
                .decode()
            )
        except:
            print("ERROR: {} {} {}".format(path, index, fortune))
            exit(1)
    else:
        print(fortune)
