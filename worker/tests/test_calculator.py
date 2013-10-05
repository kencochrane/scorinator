from calculator import load_modules, run_module
from mock import patch, Mock, MagicMock


class TestLoadModules():
    def test_iterator(self):
        mock_listdir = Mock(return_value=['file.py', 'nonfile.txt',
                                          'prefix.py'])
        mock_import = Mock(return_value="prefix_imported")
        with patch('calculator.os.listdir', mock_listdir):
            with patch('calculator.import_file', mock_import):
                r = load_modules("/tmp", "prefix")
                assert list(r) == ["prefix_imported"]

    def test_exception(self):
        mock_listdir = Mock(return_value=['prefix.py'])
        mock_import = Mock(side_effect=Exception)
        with patch('calculator.os.listdir', mock_listdir):
            with patch('calculator.import_file', mock_import):
                assert list(load_modules("/tmp", "prefix")) == []


class TestRunModule():
    def test_no_score(self):
        mock_mod = MagicMock(spec=[u'__name__'])
        assert run_module(mock_mod) is None

    def test_score(self):
        mock_mod = MagicMock(spec=[u'__name__', u'score'])
        mock_mod.score.return_value = 10
        assert run_module(mock_mod) == 10

    def test_exception(self):
        mock_mod = MagicMock(spec=[u'__name__', u'score'])
        mock_mod.score.side_effect = Exception
        # speed up tests, ignore sleep
        with patch("calculator.time", Mock()):
            assert run_module(mock_mod) is None