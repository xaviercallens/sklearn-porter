# -*- coding: utf-8 -*-

from typing import Union, Optional, Callable
from logging import Logger, ERROR

from sklearn.neighbors.classification import KNeighborsClassifier \
    as KNeighborsClassifierClass

from sklearn_porter.EstimatorApiABC import EstimatorApiABC
from sklearn_porter.estimator.EstimatorBase import EstimatorBase
from sklearn_porter.utils import get_logger


class KNeighborsClassifier(EstimatorBase, EstimatorApiABC):
    """
    Extract model data and port a KNeighborsClassifier classifier.

    See also
    --------
    http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
    """
    estimator = None  # type: KNeighborsClassifierClass

    def __init__(
            self,
            estimator: KNeighborsClassifierClass,
            logger: Union[Logger, int] = ERROR
    ):
        super().__init__(estimator)
        self.logger = get_logger(__name__, logger=logger)
        self.logger.info('Create specific estimator `%s`.', self.estimator_name)
        est = self.estimator  # alias

        # TODO: Export and prepare model data from estimator.

    def port(
            self,
            method: str = 'predict',
            to: Union[str] = 'java',  # language
            with_num_format: Callable[[object], str] = lambda x: str(x),
            with_class_name: Optional[str] = None,
            with_method_name: Optional[str] = None
    ) -> str:
        temps = self.load_templates(language=to)

        print(temps.keys())

        return str(self.estimator)