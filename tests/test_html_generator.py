import unittest

from src.generator import *
import pathlib


class TestHTMLGenerator(unittest.TestCase):
    def test_Should_GetContent_When_GivenNonemptyContent(self):
        generator = CanvasGenerator()
        config = {'imgs_data_csv_path': pathlib.Path(__file__).parent / "./files/imgs_data.csv",
                  'imgs_coords_csv_path': pathlib.Path(__file__).parent / "./files/imgs_coords.csv",
                  }

        with open(pathlib.Path(__file__).parent / "./files/generator.html", encoding="utf-8") as html:
            expected_html = html.read()
        with open(pathlib.Path(__file__).parent / "./files/generator.css", encoding="utf-8") as css:
            expected_css = css.read()
        with open(pathlib.Path(__file__).parent / "./files/generator.py", encoding="utf-8") as py:
            expected_py = py.read()

        self.assertEqual(expected_html, generator.process(config)['html'])
        self.assertEqual(expected_css, generator.process(config)['css'])
        self.assertEqual(expected_py, generator.process(config)['py'])


if __name__ == "__main__":
    unittest.main()
