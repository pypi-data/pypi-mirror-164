import os
import tempfile
import unittest
from unittest.mock import MagicMock

import huggingface_hub

import gradio as gr
from gradio import flagging


class TestDefaultFlagging(unittest.TestCase):
    def test_default_flagging_callback(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            io = gr.Interface(lambda x: x, "text", "text", flagging_dir=tmpdirname)
            io.launch(prevent_thread_lock=True)
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 1)  # 2 rows written including header
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 2)  # 3 rows written including header
        io.close()


class TestSimpleFlagging(unittest.TestCase):
    def test_simple_csv_flagging_callback(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            io = gr.Interface(
                lambda x: x,
                "text",
                "text",
                flagging_dir=tmpdirname,
                flagging_callback=flagging.SimpleCSVLogger(),
            )
            io.launch(prevent_thread_lock=True)
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 0)  # no header in SimpleCSVLogger
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 1)  # no header in SimpleCSVLogger
        io.close()


class TestHuggingFaceDatasetSaver(unittest.TestCase):
    def test_saver_setup(self):
        huggingface_hub.create_repo = MagicMock()
        huggingface_hub.Repository = MagicMock()
        flagger = flagging.HuggingFaceDatasetSaver("test", "test")
        with tempfile.TemporaryDirectory() as tmpdirname:
            flagger.setup(tmpdirname)
        huggingface_hub.create_repo.assert_called_once()

    def test_saver_flag(self):
        huggingface_hub.create_repo = MagicMock()
        huggingface_hub.Repository = MagicMock()
        with tempfile.TemporaryDirectory() as tmpdirname:
            io = gr.Interface(
                lambda x: x,
                "text",
                "text",
                flagging_dir=tmpdirname,
                flagging_callback=flagging.HuggingFaceDatasetSaver("test", "test"),
            )
            os.mkdir(os.path.join(tmpdirname, "test"))
            io.launch(prevent_thread_lock=True)
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 1)  # 2 rows written including header
            row_count = io.flagging_callback.flag(io, ["test"], ["test"])
            self.assertEqual(row_count, 2)  # 3 rows written including header


class TestDisableFlagging(unittest.TestCase):
    def test_flagging_no_permission_error_with_flagging_disabled(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            os.chmod(tmpdirname, 0o444)  # Make directory read-only
            nonwritable_path = os.path.join(tmpdirname, "flagging_dir")

            io = gr.Interface(
                lambda x: x,
                "text",
                "text",
                allow_flagging="never",
                flagging_dir=nonwritable_path,
            )
            try:
                io.launch(prevent_thread_lock=True)
            except PermissionError:
                self.fail("launch() raised a PermissionError unexpectedly")

        io.close()


if __name__ == "__main__":
    unittest.main()
