from functools import reduce

import numpy as np
import matplotlib as mpl

from sklearn.base import is_regressor
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import _safe_indexing, check_matplotlib_support
from sklearn.utils.validation import (
    _is_arraylike_not_scalar,
    _num_features,
    check_is_fitted,
)
from sklearn.inspection import DecisionBoundaryDisplay


def _check_boundary_response_method(estimator, response_method, plot_method):
    """Return prediction method from the `response_method` for decision boundary.

    note: `sklearn.inspection._plot.decision_boundary._check_boundary_response_method`에서
    multiclass에 `decision_function` 허용하도록 수정

    Parameters
    ----------
    estimator : object
        Fitted estimator to check.

    response_method : {'auto', 'predict_proba', 'decision_function', 'predict'}
        Specifies whether to use :term:`predict_proba`,
        :term:`decision_function`, :term:`predict` as the target response.
        If set to 'auto', the response method is tried in the following order:
        :term:`decision_function`, :term:`predict_proba`, :term:`predict`.

    Returns
    -------
    prediction_method: callable
        Prediction method of estimator.
    """
    has_classes = hasattr(estimator, "classes_")
    if has_classes and _is_arraylike_not_scalar(estimator.classes_[0]):
        msg = "Multi-label and multi-output multi-class classifiers are not supported"
        raise ValueError(msg)

    if has_classes and len(estimator.classes_) > 2 and plot_method != "pcolormesh":
        if response_method not in {"auto", "predict"}:
            msg = (
                "Multiclass classifiers are only supported when response_method is"
                " 'predict' or 'auto'"
            )
            raise ValueError(msg)
        methods_list = ["predict"]
    elif response_method == "auto":
        methods_list = ["decision_function", "predict_proba", "predict"]
    else:
        methods_list = [response_method]

    prediction_method = [getattr(estimator, method, None) for method in methods_list]
    prediction_method = reduce(lambda x, y: x or y, prediction_method)
    if prediction_method is None:
        raise ValueError(
            f"{estimator.__class__.__name__} has none of the following attributes: "
            f"{', '.join(methods_list)}."
        )

    return prediction_method


def decision_boundary_display_from_estimator(
    estimator,
    X,
    *,
    grid_resolution=100,
    eps=1.0,
    plot_method="pcolormesh",
    response_method="auto",
    decision_normalize_method="sigmoid",
    multiclass_mix_rest=False,
    multiclass_target_index=None,
    xlabel=None,
    ylabel=None,
    ax=None,
    **kwargs,
):
    """Plot decision boundary given an estimator.

    Read more in the :ref:`User Guide <visualizations>`.

    note: `DecisionBoundaryDisplay.from_estimator`를 multiclass에 `decision_function` 적용 가능하도록 수정
    - multiclass에 `predict_proba` 지정 시 sklearn.calibration.CalibratedClassifierCV 사용
    - `decision_normalize_method` 인자 추가 (decision_function 결과 정규화 방식)
    - `multiclass_mix_rest` 인자 추가 (멀티클래스 예측 클래스 외 나머지 클래스의 색상 표시 여부)
    - `multiclass_target_index` 인자 추가 (멀티클래스 특정 타겟의 결과값만 표시)
    - `plot_method` 인자 default 값을 `contourf`에서 `pcolormesh`로 변경

    Parameters
    ----------
    estimator : object
        Trained estimator used to plot the decision boundary.

    X : {array-like, sparse matrix, dataframe} of shape (n_samples, 2)
        Input data that should be only 2-dimensional.

    grid_resolution : int, default=100
        Number of grid points to use for plotting decision boundary.
        Higher values will make the plot look nicer but be slower to
        render.

    eps : float, default=1.0
        Extends the minimum and maximum values of X for evaluating the
        response function.

    plot_method : {'contourf', 'contour', 'pcolormesh'}, default='pcolormesh'
        Plotting method to call when plotting the response. Please refer
        to the following matplotlib documentation for details:
        :func:`contourf <matplotlib.pyplot.contourf>`,
        :func:`contour <matplotlib.pyplot.contour>`,
        :func:`pcolormesh <matplotlib.pyplot.pcolormesh>`.

    response_method : {'auto', 'predict_proba', 'decision_function', \
            'predict'}, default='auto'
        Specifies whether to use :term:`predict_proba`,
        :term:`decision_function`, :term:`predict` as the target response.
        If set to 'auto', the response method is tried in the following order:
        :term:`decision_function`, :term:`predict_proba`, :term:`predict`.
        For multiclass problems, :term:`predict` is selected when
        `response_method="auto"`.

    decision_normalize_method : {'sigmoid', 'minmax'}, default='sigmoid'
        decision_function 결과를 [0, 1] 사이로 정규화하는 방식
        (pcolormesh 사용시)
    
    multiclass_mix_rest: bool, default=False
        멀티클래스 예측 클래스 외 나머지 클래스의 색상 표시 여부
        (pcolormesh 사용시)
    
    multiclass_target_index: int, default=None
        멀티클래스 특정 타겟의 결과값만 표시
        (pcolormesh 사용시)
    
    xlabel : str, default=None
        The label used for the x-axis. If `None`, an attempt is made to
        extract a label from `X` if it is a dataframe, otherwise an empty
        string is used.

    ylabel : str, default=None
        The label used for the y-axis. If `None`, an attempt is made to
        extract a label from `X` if it is a dataframe, otherwise an empty
        string is used.

    ax : Matplotlib axes, default=None
        Axes object to plot on. If `None`, a new figure and axes is
        created.

    **kwargs : dict
        Additional keyword arguments to be passed to the
        `plot_method`.

    Returns
    -------
    display : :class:`~sklearn.inspection.DecisionBoundaryDisplay`
        Object that stores the result.

    See Also
    --------
    sklearn.inspection.DecisionBoundaryDisplay : Decision boundary visualization.
    sklearn.metrics.ConfusionMatrixDisplay.from_estimator : Plot the
        confusion matrix given an estimator, the data, and the label.
    sklearn.metrics.ConfusionMatrixDisplay.from_predictions : Plot the
        confusion matrix given the true and predicted labels.

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.linear_model import LogisticRegression
    >>> from visutil.decision_boundary import decision_boundary_display_from_estimator  # 임의 위치에 코드 추가
    >>> iris = load_iris()
    >>> X = iris.data[:, :2]
    >>> classifier = LogisticRegression().fit(X, iris.target)
    >>> disp = decision_boundary_display_from_estimator(
    ...     classifier, X, response_method="predict",
    ...     xlabel=iris.feature_names[0], ylabel=iris.feature_names[1],
    ...     alpha=0.5,
    ... )
    >>> disp.ax_.scatter(X[:, 0], X[:, 1], c=iris.target, edgecolor="k")
    <...>
    >>> plt.show()
    """
    check_matplotlib_support(f"decision_boundary_display_from_estimator")
    check_is_fitted(estimator)

    if not grid_resolution > 1:
        raise ValueError(
            "grid_resolution must be greater than 1. Got"
            f" {grid_resolution} instead."
        )

    if not eps >= 0:
        raise ValueError(
            f"eps must be greater than or equal to 0. Got {eps} instead."
        )

    possible_plot_methods = ("contourf", "contour", "pcolormesh")
    if plot_method not in possible_plot_methods:
        available_methods = ", ".join(possible_plot_methods)
        raise ValueError(
            f"plot_method must be one of {available_methods}. "
            f"Got {plot_method} instead."
        )

    num_features = _num_features(X)
    if num_features != 2:
        raise ValueError(
            f"n_features must be equal to 2. Got {num_features} instead."
        )

    x0, x1 = _safe_indexing(X, 0, axis=1), _safe_indexing(X, 1, axis=1)

    x0_min, x0_max = x0.min() - eps, x0.max() + eps
    x1_min, x1_max = x1.min() - eps, x1.max() + eps

    xx0, xx1 = np.meshgrid(
        np.linspace(x0_min, x0_max, grid_resolution),
        np.linspace(x1_min, x1_max, grid_resolution),
    )
    if hasattr(X, "iloc"):
        # we need to preserve the feature names and therefore get an empty dataframe
        X_grid = X.iloc[[], :].copy()
        X_grid.iloc[:, 0] = xx0.ravel()
        X_grid.iloc[:, 1] = xx1.ravel()
    else:
        X_grid = np.c_[xx0.ravel(), xx1.ravel()]

    pred_func = _check_boundary_response_method(estimator, response_method, plot_method)
    response = pred_func(X_grid)

    # convert classes predictions into integers
    has_classes = hasattr(estimator, "classes_")
    if pred_func.__name__ == "predict" and has_classes:
        encoder = LabelEncoder()
        encoder.classes_ = estimator.classes_
        response = encoder.transform(response)

    response_shape = xx0.shape
    
    if response.ndim == 2 and has_classes and len(estimator.classes_) > 2:
        # multiclass에 decision_function 또는 predict_proba 사용한 경우 response에 RGB 직접 할당해서 pcolormesh 전달
        if response.shape[1] != len(estimator.classes_):
            raise ValueError("response score 개수가 class 개수와 다름")

        if pred_func.__name__ == "decision_function":
            if decision_normalize_method == "sigmoid":
                # score를 [0,1] 정규화
                # TODO: 적당한 sigmoid 계수 찾기 (CalibratedClassifierCV predict_proba처럼 값이 잘 구분되도록)
                rmax = response.max()
                mean = np.mean(response)
                response = 1 / (1 + np.exp(-(response - mean) * 8 / (rmax - mean)))
            elif decision_normalize_method == "minmax":
                rmin = response.min()
                rmax = response.max()
                response = (response - rmin) / (rmax - rmin)
            else:
                raise ValueError(f"잘못된 decision_normalize_method {decision_normalize_method}. ('sigmoid', 'minmax') 중 하나여야 함.")
            
            # score 합이 1이 되도록 정규화
            norm = np.linalg.norm(response, ord=1, axis=1, keepdims=True)
            np.divide(response, norm, out=response, where = norm != 0)
        
        cmap = mpl.cm.get_cmap(kwargs.get("cmap", None))
        n_classes = len(estimator.classes_)
        class_colors = [np.array(cmap(c / (n_classes - 1))) for c in range(n_classes)]

        def get_color(proba):
            if multiclass_mix_rest:
                # proba 씩 만큼 class 색상 보간
                colors = np.array([class_colors[c] * p for c, p in enumerate(proba)])
                color = np.sum(colors, axis=0)
            elif multiclass_target_index is not None:
                # 특정 class 색상 보간
                c = multiclass_target_index
                w = proba[c]
                color = class_colors[c] * w + (1 - w)
            else:
                # predicted class 색상 보간
                min_p = 1 / n_classes
                c = proba.argmax()
                w = (proba[c] - min_p) / (1 - min_p)
                color = class_colors[c] * w + (1 - w)
            
            return np.clip(color, 0, 1)
        
        response = np.apply_along_axis(get_color, -1, response)
        response_shape += (4,)
    elif response.ndim != 1:
        if is_regressor(estimator):
            raise ValueError("Multi-output regressors are not supported")

        # TODO: Support pos_label
        response = response[:, 1]

    if xlabel is None:
        xlabel = X.columns[0] if hasattr(X, "columns") else ""

    if ylabel is None:
        ylabel = X.columns[1] if hasattr(X, "columns") else ""

    display = DecisionBoundaryDisplay(
        xx0=xx0,
        xx1=xx1,
        response=response.reshape(response_shape),
        xlabel=xlabel,
        ylabel=ylabel,
    )
    return display.plot(ax=ax, plot_method=plot_method, **kwargs)
