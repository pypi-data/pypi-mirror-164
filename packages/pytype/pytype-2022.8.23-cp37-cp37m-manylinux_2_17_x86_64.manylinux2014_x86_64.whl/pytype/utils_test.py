"""Tests for utils.py."""
import os

from pytype import utils

import unittest


class UtilsTest(unittest.TestCase):
  """Test generic utilities."""

  def test_numeric_sort_key(self):
    k = utils.numeric_sort_key
    self.assertLess(k("1aaa"), k("12aa"))
    self.assertLess(k("12aa"), k("123a"))
    self.assertLess(k("a1aa"), k("a12a"))
    self.assertLess(k("a12a"), k("a123"))

  def test_pretty_dnf(self):
    dnf = [["a", "b"], "c", ["d", "e", "f"]]
    self.assertEqual(utils.pretty_dnf(dnf), "(a & b) | c | (d & e & f)")

  def test_list_strip_prefix(self):
    self.assertEqual([1, 2, 3], utils.list_strip_prefix([1, 2, 3], []))
    self.assertEqual([2, 3], utils.list_strip_prefix([1, 2, 3], [1]))
    self.assertEqual([3], utils.list_strip_prefix([1, 2, 3], [1, 2]))
    self.assertEqual([], utils.list_strip_prefix([1, 2, 3], [1, 2, 3]))
    self.assertEqual([1, 2, 3],
                     utils.list_strip_prefix([1, 2, 3], [0, 1, 2, 3]))
    self.assertEqual([], utils.list_strip_prefix([], [1, 2, 3]))
    self.assertEqual(list("wellington"), utils.list_strip_prefix(
        list("newwellington"), list("new")))
    self.assertEqual(
        "a.somewhat.long.path.src2.d3.shrdlu".split("."),
        utils.list_strip_prefix(
            "top.a.somewhat.long.path.src2.d3.shrdlu".split("."),
            "top".split(".")))

  def test_list_starts_with(self):
    self.assertTrue(utils.list_startswith([1, 2, 3], []))
    self.assertTrue(utils.list_startswith([1, 2, 3], [1]))
    self.assertTrue(utils.list_startswith([1, 2, 3], [1, 2]))
    self.assertTrue(utils.list_startswith([1, 2, 3], [1, 2, 3]))
    self.assertFalse(utils.list_startswith([1, 2, 3], [2]))
    self.assertTrue(utils.list_startswith([], []))
    self.assertFalse(utils.list_startswith([], [1]))

  def test_invert_dict(self):
    a = {"p": ["q", "r"], "x": ["q", "z"]}
    b = utils.invert_dict(a)
    self.assertCountEqual(b["q"], ["p", "x"])
    self.assertEqual(b["r"], ["p"])
    self.assertEqual(b["z"], ["x"])

  def test_dynamic_var(self):
    var = utils.DynamicVar()
    self.assertIsNone(var.get())
    with var.bind(123):
      self.assertEqual(123, var.get())
      with var.bind(456):
        self.assertEqual(456, var.get())
      self.assertEqual(123, var.get())
    self.assertIsNone(var.get())

  def test_version_from_string(self):
    self.assertEqual(utils.version_from_string("3.7"), (3, 7))

  def test_validate_version(self):
    old = utils._VALIDATE_PYTHON_VERSION_UPPER_BOUND
    utils._VALIDATE_PYTHON_VERSION_UPPER_BOUND = True
    self._validate_version_helper((1, 1))
    self._validate_version_helper((2, 1))
    self._validate_version_helper((2, 8))
    self._validate_version_helper((3, 1))
    self._validate_version_helper((3, 42))
    utils._VALIDATE_PYTHON_VERSION_UPPER_BOUND = old

  def _validate_version_helper(self, python_version):
    with self.assertRaises(utils.UsageError):
      utils.validate_version(python_version)

  def test_parse_interpreter_version(self):
    test_cases = (
        ("Python 3.8.3", (3, 8)),
        ("Python 3.8.4 :: Something custom (64-bit)", (3, 8)),
        ("[OS-Y 64-bit] Python 3.9.1", (3, 9)),
    )
    for version_str, expected in test_cases:
      self.assertEqual(expected, utils.parse_exe_version_string(version_str))

  def test_get_python_exe_version(self):
    version = utils.get_python_exe_version(["python"])
    self.assertIsInstance(version, tuple)
    self.assertEqual(len(version), 2)

  def test_custom_python_exe(self):
    temp = utils._CUSTOM_PYTHON_EXES
    # Since the logic for getting a custom exe checks for the file's existence
    # in the pytype/ src directory, we pick an existing file to pretend to be a
    # Python exe.
    utils._CUSTOM_PYTHON_EXES = {(3, 10): "utils.py"}
    (exe,), = utils.get_python_exes((3, 10))
    self.assertEqual(os.path.basename(exe), "utils.py")
    utils._CUSTOM_PYTHON_EXES = temp


def _make_tuple(x):
  return tuple(range(x))


class DecoratorsTest(unittest.TestCase):
  """Test decorators."""

  def test_annotating_decorator(self):
    foo = utils.AnnotatingDecorator()
    @foo(3)
    def f():  # pylint: disable=unused-variable
      pass
    self.assertEqual(foo.lookup["f"], 3)


if __name__ == "__main__":
  unittest.main()
