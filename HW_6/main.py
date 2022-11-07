"""
Відсортувати файли в папці.
"""

import argparse
import asyncio
import logging

from aiopath import AsyncPath
from aioshutil import copyfile, move
from pathlib import Path

"""
--source [-s] picture
--output [-o]
"""

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")
output_folder = AsyncPath(output)


async def grabs_folder(path: AsyncPath) -> None:
    async for el in path.iterdir():
        if await el.is_dir():
            await grabs_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath) -> None:
    ext = file.suffix
    new_path = output_folder / ext
    try:
        await new_path.mkdir(exist_ok=True, parents=True)
        await move(file, new_path / file.name)
    except OSError as err:
        logging.error(err)


def remove_empty_folders(path: Path):
    for child in path.iterdir():
        remove_empty_folders(child)
    path.rmdir()


if __name__ == '__main__':
    base_folder = AsyncPath(source)
    asyncio.run(grabs_folder(base_folder))
    base_folder2 = Path(source)
    remove_empty_folders(base_folder2)
    print(f"Посортовані файли тут: {output_folder}")