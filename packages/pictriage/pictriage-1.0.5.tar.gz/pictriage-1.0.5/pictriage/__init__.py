import argparse
import atexit
import logging
import os
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import shlex

import ibis
import natsort
import uvicorn
from ibis.nodes import register, Node, Expression
from starlette.applications import Starlette
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import HTMLResponse, Response
from starlette.routing import Mount
from starlette.routing import Route
from starlette.staticfiles import StaticFiles

IMAGE_FILE_EXTENSIONS = [
    '.apng',
    '.avif',
    '.bmp',
    '.gif',
    '.jpeg',
    '.jpg',
    '.png',
    '.svg',
    '.webp',
]
MOVE_DIR_FLAG = '--move-dir'

parser = argparse.ArgumentParser(description="manually organize & clean-up a folder of images")
parser.add_argument(
    'dir', nargs='?', default='.', help="Root folder containing images (can contain subfolders)"
)

parser.add_argument(MOVE_DIR_FLAG, help="Directory to move images to (if the 'move' action is selected)")
parser.add_argument(
    '--thumbnail-width',
    type=int,
    default=128,
    help="Width of thumbnails, in pixels (when in thumbnail mode)",
)
parser.add_argument(
    '--zoom-pane-width', type=int, default=512, help="Width of the zoom pane, in pixels"
)
parser.add_argument(
    '--zoom-image-width',
    type=int,
    default=1024,
    help="Width of the zoomed image, in pixels",
)
parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', default=random.randint(52000, 53000))
args = parser.parse_args()
files_root = Path(args.dir).resolve()
if not files_root.is_dir():
    sys.exit(f"dir does not exist: {args.move_dir}")


thumbnail_width = args.thumbnail_width
zoom_pane_width = args.zoom_pane_width
zoom_image_width = max(args.zoom_image_width, zoom_pane_width)

if args.move_dir:
    move_dir = Path(args.move_dir)
    if not move_dir.is_dir():
        sys.exit(f"{MOVE_DIR_FLAG} does not exist: {args.move_dir}")
    if files_root in move_dir.parents:
        sys.exit(f"{MOVE_DIR_FLAG} cannot be a subdirectory of the main directory")
else:
    move_dir = None


loader = ibis.loaders.FileReloader(Path(__file__).parent.joinpath('templates'))

if sys.platform == 'win32':
    file_browser_name = "Windows Explorer"
elif sys.platform == 'darwin':
    file_browser_name = "Finder"
else:
    file_browser_name = "File browser"

@register('static')
class StaticNode(Node):
    def process_token(self, token):
        _, path = token.text.split()
        self.path_expr = Expression(path, token)

    def wrender(self, context):
        return app.router.url_path_for('static', path=self.path_expr.eval(context))


@register('rand')
class StaticNode(Node):
    def wrender(self, context):
        return str(random.randint(0, 10000000))




class Index(HTTPEndpoint):
    template_name = 'ManageTree.html'

    def get(self, request: Request):
        folders = []
        num_images = 0
        folder_mtimes = {}

        for root, dirs, files in os.walk(files_root):
            root_path = Path(root)
            folder = root_path.relative_to(files_root)
            latest_mtime = 0
            img_files = []
            for file in files:
                fp = root_path.joinpath(file)
                if fp.suffix.lower() in IMAGE_FILE_EXTENSIONS:
                    stat = fp.stat()
                    mtime = stat.st_mtime
                    if mtime > latest_mtime:
                        latest_mtime = mtime
                    img_files.append(file)
                    num_images += 1
            fps = [
                folder.joinpath(file).as_posix()
                for file in natsort.os_sorted(img_files)
            ]
            if fps:
                folder_mtimes[folder] = latest_mtime
                folders.append((folder, fps))
        folders.sort(key=lambda e: folder_mtimes[e[0]], reverse=True)
        gallery_img_width = thumbnail_width if GlobalState.lens_visibility else 512
        ctx = dict(
            AVAILABLE_ACTIONS=[member.value for member in ClickAction],
            NONE_ACTION=ClickAction.NONE.value,
            current_action=GlobalState.click_action.value,
            img_width=GlobalState.img_width,
            folders=folders,
            num_images=num_images,
            lens_visibility=GlobalState.lens_visibility,
            gallery_img_width=gallery_img_width,
            zoom_pane_width=zoom_pane_width,
            MOVE_DIR=move_dir,
            ZOOM_IMAGE_WIDTH=zoom_image_width,
            MOVE_DIR_FLAG=MOVE_DIR_FLAG,
            root_folder_name=files_root.parts[-1],
            file_browser_name=file_browser_name,
        )
        print('current_action', GlobalState.click_action)
        template = loader('ManageTree.html')
        # if someone doesn't like 512, they can just use their browser zoom

        return HTMLResponse(template.render(ctx, strict_mode=True))


class SettingsChanged(HTTPEndpoint):
    async def post(self, request: Request):
        form = await request.form()

        action = form.get('action')
        print('action', repr(action))
        if action:
            GlobalState.click_action = ClickAction(action)

        new_size = form.get('img_width')
        if new_size:
            GlobalState.img_width = int(new_size)

        

        return Response('')

class LaunchFileBrowser(HTTPEndpoint):
    async def post(self, request: Request):
        form = await request.form()

        folder = form['folder']
        os.startfile(files_root.joinpath(folder))
        
        return Response("Launched file browser")


class renderLensVisibility(HTTPEndpoint):
    async def post(self, request: Request):
        form = await request.form()
        GlobalState.lens_visibility = bool(form.get('lens_visibility'))
        return HTMLResponse('')


import enum


class ClickAction(enum.Enum):
    # important to have 'none' option so that you can switch into readonly mode
    NONE = 'None'
    DELETE = 'Delete'
    MOVE = 'Move' if move_dir else 'Move (not enabled)'
    ROTATE_LEFT = 'Rotate left'
    ROTATE_RIGHT = 'Rotate right'


# put CCW first because it's conceptually left


def process_image(path: Path):
    rel_to_files_root = path.relative_to(files_root)
    if GlobalState.click_action == ClickAction.DELETE:
        target = Path(recycle_bin).joinpath(rel_to_files_root)
        target.parent.mkdir(exist_ok=True, parents=True)
        path.rename(target)
        print(f"Moved image to {recycle_bin}, will delete when the server is stopped.")
        return
    if GlobalState.click_action == ClickAction.MOVE:
        target = move_dir.joinpath(rel_to_files_root)
        if target.exists():
            path.unlink()
            return
        target.parent.mkdir(parents=True, exist_ok=True)
        path.rename(target)
    if GlobalState.click_action in [ClickAction.ROTATE_LEFT, ClickAction.ROTATE_RIGHT]:

        path_for_ffmpeg = files_root.joinpath(path)
        # need to start with ./ because some filenames
        # have to quote it because e.g. some file names can start with hyphen
        # (e.g. youtube videos)
        # which is interpreted as an option flag
        # path_for_ffmpeg = './' + path_for_ffmpeg.relative_to(Path('.')).as_posix()

        transpose = {ClickAction.ROTATE_LEFT: 2, ClickAction.ROTATE_RIGHT: 1}[
            GlobalState.click_action
        ]

        # ffmpeg can't edit files in place 
        # (actually it seems it can sometimes, but not always)
        temp_file_path = Path(recycle_bin, path.name)

        # TODO: would be better to rotate losslessly through EXIF
        # which would be faster also

        call(
            "ffmpeg -i",
            shlex.quote(str(path_for_ffmpeg)),
            '-vf',
            f"transpose={transpose}",
            '-frames:v 1 -update 1',
            shlex.quote(str(temp_file_path)),
            '-y',
        )
        path_for_ffmpeg.unlink()
        temp_file_path.rename(path_for_ffmpeg)

        


def call(*segments, capture_output=False):
    cmd_str = ' '.join(str(arg) for arg in segments)
    print(cmd_str)
    cmd = shlex.split(cmd_str)
    print(cmd)
    try:
        return subprocess.run(cmd, capture_output=capture_output, check=True)
    except subprocess.CalledProcessError as exc:
        print(exc.stderr)
        raise


class ImageClicked(HTTPEndpoint):
    async def post(self, request):
        rel_to_files_dir = Path((await request.body()).decode())
        abspath = files_root.joinpath(rel_to_files_dir)
        if abspath.is_dir():
            for img in abspath.iterdir():
                if img.is_file() and img.suffix in IMAGE_FILE_EXTENSIONS:
                    process_image(img)
            if GlobalState.click_action == ClickAction.DELETE and not list(abspath.iterdir()):
                abspath.rmdir()
        else:
            process_image(abspath)
        return Response('ok')


class GlobalState:
    click_action = ClickAction.NONE
    img_width = 300
    lens_visibility = False


class MyStatics(StaticFiles):

    pass

    # don't cache files, we always want the most recent version.
    # but it seems that Firefox is reloading the old version of the file from memory
    # even if we serve a new one.
    # so actually we shouldn't do this.

    # network tab doesn't show the files being loaded, even though server logs do.
    # def is_not_modified(self, response_headers, request_headers) -> bool:
    #     return False


app = Starlette(
    debug=True,
    routes=[
        Route('/', Index),
        Route('/clicked', ImageClicked),
        Route('/settings', SettingsChanged),
        Route('/file-browser', LaunchFileBrowser),
        Route('/lens_visibility', renderLensVisibility),
        Mount(
            '/static',
            app=MyStatics(directory=files_root, packages=[__name__]),
            name="static",
        ),
    ],
)

recycle_bin = tempfile.mkdtemp()


def exit_handler():
    shutil.rmtree(recycle_bin)


atexit.register(exit_handler)


def main():
    uvicorn_logger = logging.getLogger("uvicorn")
    uvicorn_logger.setLevel('WARNING')

    import webbrowser

    # it's ok if the server takes a few seconds, the browser will
    # keep trying to load.
    webbrowser.open(f'http://{args.host}:{args.port}')

    # "You can use such a file object as a context manager
    # to have it closed automatically when the code block exits,
    # or you leave it to be closed when the interpreter exits."

    uvicorn.run(
        f'{__name__}:app',
        host=args.host,
        port=args.port,
        reload=bool(os.getenv('PICTRIAGE_DEV')),
        reload_dirs=[Path(__file__).parent],
        # Don't write access log because we get tons of output when
        # loading a large folder
        access_log=False,
    )


if __name__ == '__main__':
    main()
