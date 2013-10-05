import json

from api import API_URL, AUTH
from calculator import (load_modules, run_module, process_result, run_scorer,
                        post_job, handle_job, run)
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


class TestProcessResult():
    def test_process(self):
        mock_mod = MagicMock(spec=[u'__name__'])
        mock_load_modules = Mock(return_value=["loaded"])
        mock_run_module = Mock()
        with patch('calculator.load_modules', mock_load_modules):
            with patch('calculator.run_module', mock_run_module):
                process_result(mock_mod, "project", ["result"])
                mock_load_modules.assert_called_with('score_hooks', 'hook')
                mock_run_module.assert_called_with("loaded", "project",
                                                   "result")


class TestRunScorer():
    def test_no_results(self):
        mock_mod = MagicMock(spec=[u'__name__'])
        mock_load_modules = Mock(return_value=[mock_mod])
        mock_run_module = Mock(return_value=None)
        with patch("calculator.load_modules", mock_load_modules):
            with patch("calculator.run_module", mock_run_module):
                assert run_scorer({"results": []}) == []
                mock_load_modules.assert_called_with("attributes", "attrib")
                mock_run_module.assert_called_with(mock_mod, [])

    def test_results(self):
        project = {"results": ["res"]}
        mock_mod = MagicMock(spec=[u'__name__'])
        mock_load_modules = Mock(return_value=[mock_mod])
        mock_run_module = Mock(return_value=["score1"])
        mock_process_result = Mock()
        with patch("calculator.load_modules", mock_load_modules):
            with patch("calculator.run_module", mock_run_module):
                with patch("calculator.process_result", mock_process_result):
                    r = run_scorer(project)
                    assert r == ["score1"]
                    mock_load_modules.assert_called_with(
                        "attributes", "attrib")
                    mock_run_module.assert_called_with(mock_mod, ["res"])
                    mock_process_result.assert_called_with(
                        mock_mod, project, r)


class TestPostJob():
    def test_no_project_score_id(self):
        post_results = [("attribute", 10, "blank1", "blank2")]
        project = {"project": {"project_id": 1}}
        assert post_job(project, post_results) is None

    def test_put(self):
        post_results = [("attribute", 10, "blank1", "blank2")]
        project = {"project": {"project_id": 1, "project_score_id": 2}}
        mock_requests = Mock()
        with patch("calculator.requests.put", mock_requests):
            post_job(project, post_results)
            mock_requests.assert_called_with(
                "{0}project-scores/{1}/".format(API_URL, 2),
                data={"project_score": 2, "project": 1, "total_score": 10},
                auth=AUTH
            )


class TestHandleJob():
    def test_job(self):
        project = {}
        project_json = json.dumps(project)
        mock_run_scorer = Mock(return_value=["results"])
        mock_post_job = Mock()
        with patch("calculator.run_scorer", mock_run_scorer):
            with patch("calculator.post_job", mock_post_job):
                handle_job(project_json)
                mock_run_scorer.assert_called_with(project)
                mock_post_job.assert_called_with(project, ["results"])


class TestRun():
    def test_queue(self):
        mock_queue = Mock()
        with patch("calculator.queue_score_daemon", mock_queue):
            run()
            mock_queue.assert_called_with(handle_job)

    def test_exception(self):
        mock_queue = Mock(side_effect=Exception)
        mock_logger = Mock()
        with patch("calculator.queue_score_daemon", mock_queue):
            with patch("calculator.logger", mock_logger):
                run()
                mock_queue.assert_called_with(handle_job)
                mock_logger.call_count == 1
