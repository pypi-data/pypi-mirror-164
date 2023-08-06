from PIL import Image as image_pil_main
from PIL import ExifTags
from PIL.Image import Image, Exif
import cv2
import numpy
import requests
import tempfile
import io
import base64
from numpy import ndarray
from injectable import injectable, autowired, Autowired
from tekleo_common_utils.utils_random import UtilsRandom
from pillow_heif import register_heif_opener
import cairosvg
import xml.etree.ElementTree as ET


@injectable
class UtilsImage:
    @autowired
    def __init__(self, utils_random: Autowired(UtilsRandom)):
        self.utils_random = utils_random
        register_heif_opener()

    def convert_image_pil_to_image_cv(self, image_pil: Image) -> ndarray:
        return cv2.cvtColor(numpy.array(image_pil), cv2.COLOR_RGB2BGR)

    def convert_image_cv_to_image_pil(self, image_cv: ndarray) -> Image:
        return image_pil_main.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))

    def _open_image_pil_svg(self, image_path: str) -> Image:
        # Make sure this is SVG
        if not image_path.lower().endswith("svg"):
            raise RuntimeError("Can't open a non-svg fil! image_path=" + str(image_path))

        # Initial width/height
        svg_width = 1000
        svg_height = 1000

        # Open SVG as XML
        with open(image_path) as f:
            # Parse XML
            xml_tree = ET.parse(f)
            xml_root = xml_tree.getroot()
            xml_root_items = xml_root.items()
            width_segment = [i for i in xml_root_items if i[0] == 'width'][0]
            height_segment = [i for i in xml_root_items if i[0] == 'height'][0]
            width_str = width_segment[1].replace('px', '')
            height_str = height_segment[1].replace('px', '')

            # Parse width
            if width_str.endswith("pt"):
                svg_width = int(float(width_str.replace('pt', '')) * 1.25)
            else:
                svg_width = int(width_str)

            # Parse height
            if height_str.endswith("pt"):
                svg_height = int(float(height_str.replace('pt', '')) * 1.25)
            else:
                svg_height = int(height_str)

        # Convert SVG to PNG
        output_stream = io.BytesIO()
        cairosvg.svg2png(url=image_path, write_to=output_stream, background_color="white", unsafe=False, output_width=svg_width, output_height=svg_height)
        image_pil = image_pil_main.open(output_stream)
        return image_pil

    def open_image_pil(self, image_path: str, rotate_to_exif_orientation: bool = True) -> Image:
        image_pil = None

        # If this is an SVG
        if image_path.lower().endswith('.svg'):
            # Open as SVG
            image_pil = self._open_image_pil_svg(image_path)
        # If this is a normal image
        else:
            # Open the image if it's a normal image
            image_pil = image_pil_main.open(image_path)

        # If we need to rotate in align with exif data - rotate first and clear exif after
        if rotate_to_exif_orientation:
            image_pil = self.rotate_image_according_to_exif_orientation(image_pil)
            image_pil = self.clear_exif_data(image_pil)
        return image_pil

    def open_image_cv(self, image_path: str, rotate_to_exif_orientation: bool = True) -> ndarray:
        return self.convert_image_pil_to_image_cv(self.open_image_pil(image_path, rotate_to_exif_orientation=rotate_to_exif_orientation))

    def save_image_pil(self, image_pil: Image, image_path: str, quality: int = 100, subsampling: int = 0) -> str:
        # Make sure the image is in RGB mode
        image_extension = image_path.split('.')[-1].lower()
        if image_extension in ['jpg', 'jpeg'] and image_pil.mode.lower() != 'rgb':
            image_pil = image_pil.convert('RGB')
        image_pil.save(image_path, quality=quality, subsampling=subsampling)
        return image_path

    def save_image_cv(self, image_cv: ndarray, image_path: str) -> str:
        return self.save_image_pil(self.convert_image_cv_to_image_pil(image_cv), image_path)

    def debug_image_pil(self, image_pil: Image, window_name: str = 'Debug Image'):
        image_cv = self.convert_image_pil_to_image_cv(image_pil)
        self.debug_image_cv(image_cv, window_name)

    def debug_image_cv(self, image_cv: ndarray, window_name: str = 'Debug Image'):
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, image_cv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def download_image_pil(self, image_url: str, timeout_in_seconds: int = 90) -> Image:
        # Make request
        headers = {'User-Agent': self.utils_random.get_random_user_agent()}
        response = requests.get(image_url, headers=headers, timeout=timeout_in_seconds, stream=True)
        response.raise_for_status()

        # Download the image into buffer
        buffer = tempfile.SpooledTemporaryFile(max_size=1e9)
        downloaded = 0
        for chunk in response.iter_content(chunk_size=1024):
            downloaded += len(chunk)
            buffer.write(chunk)
        buffer.seek(0)

        # Convert buffer to image
        image = image_pil_main.open(io.BytesIO(buffer.read()))
        return image

    def encode_image_pil_as_base64(self, image_pil: Image) -> str:
        bytes_io = io.BytesIO()
        image_pil.save(bytes_io, format="PNG")
        return str(base64.b64encode(bytes_io.getvalue()), 'utf-8')

    def decode_image_pil_from_base64(self, image_base64: str) -> Image:
        image_bytes = base64.b64decode(bytes(image_base64, 'utf-8'))
        image = image_pil_main.open(io.BytesIO(image_bytes))
        return image

    def clear_exif_data(self, image_pil: Image) -> Image:
        if 'exif' in image_pil.info:
            del image_pil.info['exif']
        return image_pil

    def rotate_image_according_to_exif_orientation(self, image_pil: Image) -> Image:
        # Check that we have valid exif data
        exif_data = image_pil.getexif()
        if len(exif_data) == 0:
            return image_pil

        # Make sure we have orientation key
        orientation_key = [k for k in ExifTags.TAGS.keys() if ExifTags.TAGS[k] == 'Orientation'][0]
        if orientation_key not in exif_data:
            return image_pil

        # Get value and rotate accordingly
        orientation_value = exif_data.get(orientation_key)
        if orientation_value == 3:
            image_pil = image_pil.rotate(180, expand=True)
        elif orientation_value == 6:
            image_pil = image_pil.rotate(270, expand=True)
        elif orientation_value == 8:
            image_pil = image_pil.rotate(90, expand=True)

        return image_pil

    def convert_to_jpg(self, image_path: str) -> str:
        extension = image_path.split('.')[-1]
        new_image_path = image_path.replace('.' + extension, '.jpg')
        image_pil = self.open_image_pil(image_path)
        self.save_image_pil(image_pil, new_image_path)
        return new_image_path
