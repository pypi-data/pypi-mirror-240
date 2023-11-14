import abc
import logging
import pathlib
import typing as t

from testbrain.repository.models import Commit
from testbrain.repository.types import T_SHA, PathLike, T_Branch, T_File

if t.TYPE_CHECKING:
    from testbrain.terminal import Process


logger = logging.getLogger(__name__)


class BaseVCS(abc.ABC):
    _repo_dir: PathLike
    _repo_name: t.Optional[str] = None

    def __init__(
        self,
        repo_dir: t.Optional[PathLike] = None,
        repo_name: t.Optional[str] = None,
    ):
        if repo_dir is None:
            repo_dir = pathlib.Path(".").resolve()

        self._repo_dir = pathlib.Path(repo_dir).resolve()
        self._repo_name = repo_name

    @property
    @abc.abstractmethod
    def process(self) -> "Process":
        raise NotImplementedError()

    @property
    def repo_dir(self) -> PathLike:
        return self._repo_dir

    @property
    def repo_name(self) -> str:
        if self._repo_name is None:
            self._repo_name = self._get_repo_name()
        return self._repo_name

    @abc.abstractmethod
    def _get_repo_name(self) -> str:
        raise NotImplementedError()

    @abc.abstractmethod
    def get_current_branch(self) -> T_Branch:
        raise NotImplementedError()

    @abc.abstractmethod
    def commits(
        self,
        number: int,
        reverse: t.Optional[bool] = True,
        numstat: t.Optional[bool] = True,
        raw: t.Optional[bool] = True,
        patch: t.Optional[bool] = True,
    ) -> t.List[Commit]:
        raise NotImplementedError()

    @abc.abstractmethod
    def file_tree(self, branch: T_Branch) -> t.Optional[t.List[T_File]]:
        raise NotImplementedError()
