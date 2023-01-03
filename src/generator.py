import abc
import csv
import pathlib
from pathlib import Path


def prepare_files():
    canvas_generator = CanvasGenerator()
    config = {'imgs_data_csv_path': pathlib.Path(__file__).parent / "./config/brewery_imgs_data.csv",
              'imgs_coords_csv_path': pathlib.Path(__file__).parent / "./config/brewery_imgs_coords.csv",
              }
    return canvas_generator.process(config)


class Generator(abc.ABC):
    @abc.abstractmethod
    def process(self, config):
        pass


class CanvasGenerator(Generator):
    def process(self, config):
        self._set_imgs_data_csv_path(config)
        self._set_imgs_coords_csv_path(config)
        self._create_imgs_and_canvas_items()
        return self.output

    def _set_imgs_data_csv_path(self, config):
        self._imgs_data_csv_path = config.get('imgs_data_csv_path')

    def _set_imgs_coords_csv_path(self, config):
        self._imgs_coords_csv_path = config.get('imgs_coords_csv_path')

    def _create_imgs_and_canvas_items(self):
        if self._imgs_data_csv_path and self._imgs_coords_csv_path:
            self._imgs_data = self._read_csv_file(self._imgs_data_csv_path)
            self._create_images()
            self._calculate_abs_dimensions()
            self._imgs_coords = self._read_csv_file(self._imgs_coords_csv_path)

            canvas_items = self._create_canvas_items()
            canvas = "\n".join(canvas_items)
            with open(pathlib.Path(__file__).parent / "./templates/template.html") as html_file:
                template_html = html_file.read()

            bg = ".brewery_bg {\nposition: relative;\nbackground-size: 100% auto;\nwidth:100%;\ntop: 0;\nleft: 0;\n}"
            img = ".{} {{\nposition: absolute;\nwidth: {}%;\nheight: auto;\ntop: {}%;\nleft: {}%;\ntransform: translate(-50%, -50%);\n}}"
            ca = []
            for el in self._imgs_coords:
                if el['id'] == "brewery_bg":
                    ca.append(bg)
                else:
                    width = 1.5
                    top = 100 * float(el['y'])
                    left = 100 * float(el['x'])
                    ca.append(img.format(el['id'], width, top, left))
            css = "\n".join(ca)
            with open(pathlib.Path(__file__).parent / "./templates/template.css") as css_file:
                template_css = css_file.read()

            img = '{} = "./img/{}.png"'
            doc = 'document.querySelector("img.{}").setAttribute("src", {})'
            capy = []
            for el in self._imgs_data:
                capy.append(img.format(el['name'], el['name']))
            for el in self._imgs_coords:
                capy.append(doc.format(el['id'], el['name']))
            py = "\n".join(capy)

            with open(pathlib.Path(__file__).parent / "./templates/template.py") as py_file:
                template_py = py_file.read()

            self.output = {'html': template_html.format(canvas),
                           'css': template_css.format(css),
                           'py': template_py.format(py),
                           }

    def _read_csv_file(self, path):
        with open(path, encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            return list(reader)

    def _create_images(self):
        self._imgs = {}
        for img in self._imgs_data:
            self._imgs.update({img['name']: {Path(__file__).parent / f"./img/{img['name']}.png",
                                             img['width'],
                                             img['height'],
                                             }})

    def _calculate_abs_dimensions(self):
        self._abs_width, self._abs_height = max(int(img['width']) for img in self._imgs_data), \
                                            max(int(img['height']) for img in self._imgs_data)

    def _create_canvas_items(self):
        canvas_items = []
        canvas_items.append('<div class="canvas">')
        for img in self._imgs_coords:
            canvas_items.append(f'<img class="{img["id"]}" src="src">')
        canvas_items.append('</div>')
        return canvas_items
        # self._canvas_items.append(self.create_image(float(img['x']) * self._abs_width,
        #                                             float(img['y']) * self._abs_height,
        #                                             anchor=tkinter.CENTER,
        #                                             image=self._imgs[img['name']].image_tk))

    # def _resize(self, event):
    #     abs_scale_w, abs_scale_h = self._calculate_abs_scales(event)
    #     self._resize_images(abs_scale_w, abs_scale_h)
    #     self._resize_canvas_items(abs_scale_w, abs_scale_h)
    #
    # def _calculate_abs_scales(self, event):
    #     return event.width / self._abs_width, event.height / self._abs_height
    #
    # def _resize_images(self, abs_scale_w, abs_scale_h):
    #     for img in self._imgs.values():
    #         img.resize(abs_scale_w, abs_scale_h)
    #
    # def _resize_canvas_items(self, abs_scale_w, abs_scale_h):
    #     for canvas_item, img in zip(self._canvas_items, self._imgs_coords):
    #         self.itemconfig(canvas_item, image=self._imgs[img['name']].image_tk)
    #         self.coords(canvas_item,
    #                     round(abs_scale_w * float(img['x']) * self._abs_width),
    #                     round(abs_scale_h * float(img['y']) * self._abs_height),
    #                     )


if __name__ == "__main__":
    output = prepare_files()
    with open(pathlib.Path(__file__).parent / "./index.html", "w", encoding="utf-8") as html:
        html.write(output['html'])
    with open(pathlib.Path(__file__).parent / "./styles.css", "w", encoding="utf-8") as css:
        css.write(output['css'])
    with open(pathlib.Path(__file__).parent / "./main.py", "w", encoding="utf-8") as py:
        py.write(output['py'])
