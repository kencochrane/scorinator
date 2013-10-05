from attributes.attrib_travisci import (run, score, WEIGHT,
                                        ATTRIBUTE_SLUG)
from mock import Mock, patch


class TestAttribTravisciRun(object):
    def test_no_dir(self):
        r = run({})
        assert r is None

    def test_os_error(self):
        mock_listdir = Mock(side_effect=OSError)
        with patch("attributes.attrib_travisci.os.listdir", mock_listdir):
            r = run({"project_directory": "/tmp"})
            assert r is None

    def test_no_travisci(self):
        mock_listdir = Mock(return_value=['license.rst', 'setup.py'])
        with patch("attributes.attrib_travisci.os.listdir", mock_listdir):
            r = run({"project_directory": "/tmp"})
            assert r == {'name': ATTRIBUTE_SLUG, 'value': False}

    def test_travisci(self):
        mock_listdir = Mock(return_value=['.travis.yml', 'license.txt'])
        with patch("attributes.attrib_travisci.os.listdir", mock_listdir):
            r = run({"project_directory": "/tmp"})
            assert r == {'name': ATTRIBUTE_SLUG, 'value': True}


class TestAttribTravisciScore():
    def test_score_none(self):
        assert score({}) == []

    def test_score_false(self):
        project = [{'name': ATTRIBUTE_SLUG, 'value': 0,
                   'project_score_attribute_id': 23}]
        assert score(project) == [(ATTRIBUTE_SLUG, 0, 23, 0)]

    def test_score(self):
        project = [
            {'name': ATTRIBUTE_SLUG, 'value': 5,
             'project_score_attribute_id': 23}
        ]
        assert score(project) == [
            (ATTRIBUTE_SLUG, WEIGHT, 23, 5),
        ]
