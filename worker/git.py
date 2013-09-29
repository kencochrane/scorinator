import tempfile
import logging

from dulwich import index
from dulwich.client import get_transport_and_path
from dulwich.repo import Repo

logger = logging.getLogger(__name__)


def clone_tmp(repo_url, branch='master', base_dir="/tmp/repos/"):
    logger.debug("clone repo_url={0}, branch={1}".format(repo_url, branch))
    folder = tempfile.mkdtemp(dir=base_dir)
    logger.debug("folder = {0}".format(folder))
    rep = Repo.init(folder)
    client, relative_path = get_transport_and_path(repo_url)
    logger.debug("client={0}".format(client))

    remote_refs = client.fetch(relative_path, rep)
    rep['HEAD'] = remote_refs['refs/heads/{0}'.format(branch)]
    indexfile = rep.index_path()
    tree = rep["HEAD"].tree
    index.build_index_from_tree(rep.path, indexfile, rep.object_store, tree)
    logger.debug("done")
    return folder
