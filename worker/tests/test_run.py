import json
import pytest

from run import (load_modules, run_module, process_result, run_analytics,
                 clean_repo_url, clone_project, pre_job, post_job,
                 handle_job, run, REPO_DIR, mkdir_p)
from mock import patch, Mock, MagicMock


class TestMkdir():
    def test_mkdir(self):
        pdir = "/tmp"
        mock_os = Mock()
        with patch("run.os", mock_os):
            mkdir_p(pdir)
            mock_os.makedirs.assert_called_with(pdir)

    def test_exception(self):
        pdir = "/tmp"
        mock_os = Mock(side_effect=OSError)
        with patch("run.os.makedirs", mock_os):
            with pytest.raises(OSError):
                mkdir_p(pdir)


class TestLoadModules():
    def test_iterator(self):
        mock_listdir = Mock(return_value=['file.py', 'nonfile.txt',
                                          'prefix.py'])
        mock_import = Mock(return_value="prefix_imported")
        with patch('run.os.listdir', mock_listdir):
            with patch('run.import_file', mock_import):
                r = load_modules("/tmp", "prefix")
                assert list(r) == ["prefix_imported"]

    def test_exception(self):
        mock_listdir = Mock(return_value=['prefix.py'])
        mock_import = Mock(side_effect=Exception)
        with patch('run.os.listdir', mock_listdir):
            with patch('run.import_file', mock_import):
                assert list(load_modules("/tmp", "prefix")) == []


class TestRunModule():
    def test_no_run(self):
        mock_mod = MagicMock(spec=[u'__name__'])
        assert run_module(mock_mod) is None

    def test_run(self):
        mock_mod = MagicMock(spec=[u'__name__', u'run'])
        mock_mod.run.return_value = 10
        assert run_module(mock_mod) == 10

    def test_exception(self):
        mock_mod = MagicMock(spec=[u'__name__', u'run'])
        mock_mod.run.side_effect = Exception
        # speed up tests, ignore sleep
        with patch("run.time", Mock()):
            assert run_module(mock_mod) is None


class TestProcessResult():
    def test_process(self):
        mock_mod = MagicMock(spec=[u'__name__'])
        mock_load_modules = Mock(return_value=["loaded"])
        mock_run_module = Mock()
        mock_time = Mock(return_value=1)
        with patch('run.load_modules', mock_load_modules):
            with patch('run.run_module', mock_run_module):
                with patch('run.time.time', mock_time):
                    process_result(mock_mod, "project", {})
                    mock_load_modules.assert_called_with('hooks', 'hook')
                    mock_run_module.assert_called_with("loaded", "project",
                                                       {"timestamp": 1})


class TestRunAnalytics():
    def test_no_result(self):
        project = {}
        mock_mod = MagicMock(spec=[u'__name__'])
        mock_load_modules = Mock(return_value=[mock_mod])
        mock_run_module = Mock(return_value=None)
        with patch('run.load_modules', mock_load_modules):
            with patch('run.run_module', mock_run_module):
                assert run_analytics(project) == []
                mock_load_modules.assert_called_with("attributes", "attrib")
                mock_run_module.assert_called_with(mock_mod, project)

    def test_list(self):
        project = {}
        mod = "loaded"
        run_result = "run_result"
        process_result = "process_result"
        mock_load_modules = Mock(return_value=[mod])
        mock_run_module = Mock(return_value=[run_result])
        mock_process_result = Mock(return_value=process_result)
        with patch("run.load_modules", mock_load_modules):
            with patch("run.run_module", mock_run_module):
                with patch("run.process_result", mock_process_result):
                    assert run_analytics(project) == [process_result]
                    mock_load_modules.assert_called_with(
                        "attributes", "attrib")
                    mock_run_module.assert_called_with(mod, project)
                    mock_process_result.assert_called_with(
                        mod, project, run_result)

    def test_single(self):
        project = {}
        mod = "loaded"
        run_result = "run_result"
        process_result = "process_result"
        mock_load_modules = Mock(return_value=[mod])
        mock_run_module = Mock(return_value=run_result)
        mock_process_result = Mock(return_value=process_result)
        with patch("run.load_modules", mock_load_modules):
            with patch("run.run_module", mock_run_module):
                with patch("run.process_result", mock_process_result):
                    assert run_analytics(project) == [process_result]
                    mock_load_modules.assert_called_with(
                        "attributes", "attrib")
                    mock_run_module.assert_called_with(mod, project)
                    mock_process_result.assert_called_with(
                        mod, project, run_result)


class TestCleanRepoURL():
    def test_no_repo_url(self):
        assert clean_repo_url({}) is None

    def test_github_no_git_extension(self):
        r = clean_repo_url({"repo_url": "https://github.com/example"})
        assert r == "https://github.com/example.git"

    def test_github(self):
        r = clean_repo_url({"repo_url": "https://github.com/example.git"})
        assert r == "https://github.com/example.git"


class TestCloneProject():
    def test_clone(self):
        pdir = "/cloned"
        mock_clone_tmp = Mock(return_value=pdir)
        with patch("run.clone_tmp", mock_clone_tmp):
            assert clone_project({}) == pdir


class TestPreJob():
    def test_pre(self):
        pdir = "/cloned"
        mock_clone_project = Mock(return_value=pdir)
        with patch("run.clone_project", mock_clone_project):
            assert pre_job({}) == {"project_directory": pdir}


class TestPostJob():
    def test_no_project_dir(self):
        assert post_job({}, []) is None

    def test_enqueue(self):
        pdir = "/cloned"
        post_results = []
        project = {"project_directory": pdir}
        mock_path = Mock(return_value=True)
        mock_shutil = Mock()
        mock_enqueue_score = Mock()
        mock_json = Mock(return_value="json")
        with patch("run.os.path", mock_path):
            with patch("run.shutil", mock_shutil):
                with patch("run.enqueue_score", mock_enqueue_score):
                    with patch("run.json", mock_json):
                        post_job(project, post_results)
                        mock_path.isdir.assert_called_with(pdir)
                        mock_path.exists.assert_called_with(pdir)
                        mock_shutil.rmtree.assert_called_with(pdir)
                        # mock_enqueue_score.assert_called_with("json")
                        mock_json.dumps.assert_called_with(
                            {'project': project, 'results': post_results})


class TestHandleJob():
    def test_job(self):
        project = {}
        project_json = json.dumps(project)
        pre_job_result = project
        analytics_results = ["results"]
        mock_run_analytics = Mock(return_value=analytics_results)
        mock_pre_job = Mock(return_value=project)
        mock_post_job = Mock()
        with patch("run.run_analytics", mock_run_analytics):
            with patch("run.pre_job", mock_pre_job):
                with patch("run.post_job", mock_post_job):
                    handle_job(project_json)
                    mock_pre_job.assert_called_with(project)
                    mock_run_analytics.assert_called_with(pre_job_result)
                    mock_post_job.assert_called_with(
                        project, analytics_results)


class TestRun():
    def test_queue(self):
        mock_queue = Mock()
        mock_mkdir = Mock()
        with patch("run.queue_analytics_daemon", mock_queue):
            with patch("run.mkdir_p", mock_mkdir):
                run()
                mock_queue.assert_called_with(handle_job)
                mock_mkdir.assert_called_with(REPO_DIR)

    def test_exception(self):
        mock_queue = Mock(side_effect=Exception)
        mock_logger = Mock()
        mock_mkdir = Mock()
        with patch("run.queue_analytics_daemon", mock_queue):
            with patch("run.mkdir_p", mock_mkdir):
                with patch("run.logger", mock_logger):
                    run()
                    mock_queue.assert_called_with(handle_job)
                    mock_logger.call_count == 2
