import contextlib
import io
import unittest

from algorithm import convert_latex_to_braille


class ConvertLatexToBrailleSmokeTest(unittest.TestCase):
    def test_convert_latex_to_braille_returns_non_empty_string(self):
        stdout = io.StringIO()

        with contextlib.redirect_stdout(stdout):
            result = convert_latex_to_braille(r"\(x+1\)")

        self.assertIsInstance(result, str)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
