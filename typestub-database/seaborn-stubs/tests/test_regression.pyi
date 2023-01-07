from ..palettes import color_palette as color_palette
from typing import Any

rs: Any

class TestLinearPlotter:
    rs: Any
    df: Any
    def test_establish_variables_from_frame(self) -> None: ...
    def test_establish_variables_from_series(self) -> None: ...
    def test_establish_variables_from_array(self) -> None: ...
    def test_establish_variables_from_lists(self) -> None: ...
    def test_establish_variables_from_mix(self) -> None: ...
    def test_establish_variables_from_bad(self) -> None: ...
    def test_dropna(self) -> None: ...

class TestRegressionPlotter:
    rs: Any
    grid: Any
    n_boot: int
    bins_numeric: int
    bins_given: Any
    df: Any
    bw_err: Any
    p: Any
    def test_variables_from_frame(self) -> None: ...
    def test_variables_from_series(self) -> None: ...
    def test_variables_from_mix(self) -> None: ...
    def test_variables_must_be_1d(self) -> None: ...
    def test_dropna(self) -> None: ...
    def test_singleton(self, x, y) -> None: ...
    def test_ci(self) -> None: ...
    def test_fast_regression(self) -> None: ...
    def test_regress_poly(self) -> None: ...
    def test_regress_logx(self) -> None: ...
    def test_regress_n_boot(self) -> None: ...
    def test_regress_without_bootstrap(self) -> None: ...
    def test_regress_bootstrap_seed(self) -> None: ...
    def test_numeric_bins(self) -> None: ...
    def test_provided_bins(self) -> None: ...
    def test_bin_results(self) -> None: ...
    def test_scatter_data(self) -> None: ...
    def test_estimate_data(self) -> None: ...
    def test_estimate_cis(self) -> None: ...
    def test_estimate_units(self) -> None: ...
    def test_partial(self) -> None: ...
    def test_logistic_regression(self) -> None: ...
    def test_logistic_perfect_separation(self) -> None: ...
    def test_robust_regression(self) -> None: ...
    def test_lowess_regression(self) -> None: ...
    def test_regression_options(self) -> None: ...
    def test_regression_limits(self) -> None: ...

class TestRegressionPlots:
    rs: Any
    df: Any
    bw_err: Any
    def test_regplot_basic(self) -> None: ...
    def test_regplot_selective(self) -> None: ...
    def test_regplot_scatter_kws_alpha(self) -> None: ...
    def test_regplot_binned(self) -> None: ...
    def test_lmplot_no_data(self) -> None: ...
    def test_lmplot_basic(self) -> None: ...
    def test_lmplot_hue(self) -> None: ...
    def test_lmplot_markers(self) -> None: ...
    def test_lmplot_marker_linewidths(self) -> None: ...
    def test_lmplot_facets(self) -> None: ...
    def test_lmplot_hue_col_nolegend(self) -> None: ...
    def test_lmplot_scatter_kws(self) -> None: ...
    def test_lmplot_facet_truncate(self, sharex) -> None: ...
    def test_lmplot_sharey(self) -> None: ...
    def test_lmplot_facet_kws(self) -> None: ...
    def test_residplot(self) -> None: ...
    def test_residplot_lowess(self) -> None: ...
    def test_three_point_colors(self) -> None: ...
    def test_regplot_xlim(self) -> None: ...
