from matplotlib import rcParams as rcParams
from matplotlib.axes._base import _AxesBase
from matplotlib.axes._secondary_axes import SecondaryAxis as SecondaryAxis
from matplotlib.container import BarContainer as BarContainer, ErrorbarContainer as ErrorbarContainer, StemContainer as StemContainer
from typing import Any

class Axes(_AxesBase):
    def get_title(self, loc: str = ...): ...
    def set_title(self, label, fontdict: Any | None = ..., loc: Any | None = ..., pad: Any | None = ..., *, y: Any | None = ..., **kwargs): ...
    def get_legend_handles_labels(self, legend_handler_map: Any | None = ...): ...
    legend_: Any
    def legend(self, *args, **kwargs): ...
    def inset_axes(self, bounds, *, transform: Any | None = ..., zorder: int = ..., **kwargs): ...
    def indicate_inset(self, bounds, inset_ax: Any | None = ..., *, transform: Any | None = ..., facecolor: str = ..., edgecolor: str = ..., alpha: float = ..., zorder: float = ..., **kwargs): ...
    def indicate_inset_zoom(self, inset_ax, **kwargs): ...
    def secondary_xaxis(self, location, *, functions: Any | None = ..., **kwargs): ...
    def secondary_yaxis(self, location, *, functions: Any | None = ..., **kwargs): ...
    def text(self, x, y, s, fontdict: Any | None = ..., **kwargs): ...
    def annotate(self, text, xy, *args, **kwargs): ...
    def axhline(self, y: int = ..., xmin: int = ..., xmax: int = ..., **kwargs): ...
    def axvline(self, x: int = ..., ymin: int = ..., ymax: int = ..., **kwargs): ...
    def axline(self, xy1, xy2: Any | None = ..., *, slope: Any | None = ..., **kwargs): ...
    def axhspan(self, ymin, ymax, xmin: int = ..., xmax: int = ..., **kwargs): ...
    def axvspan(self, xmin, xmax, ymin: int = ..., ymax: int = ..., **kwargs): ...
    def hlines(self, y, xmin, xmax, colors: Any | None = ..., linestyles: str = ..., label: str = ..., **kwargs): ...
    def vlines(self, x, ymin, ymax, colors: Any | None = ..., linestyles: str = ..., label: str = ..., **kwargs): ...
    def eventplot(self, positions, orientation: str = ..., lineoffsets: int = ..., linelengths: int = ..., linewidths: Any | None = ..., colors: Any | None = ..., linestyles: str = ..., **kwargs): ...
    def plot(self, *args, scalex: bool = ..., scaley: bool = ..., data: Any | None = ..., **kwargs): ...
    def plot_date(self, x, y, fmt: str = ..., tz: Any | None = ..., xdate: bool = ..., ydate: bool = ..., **kwargs): ...
    def loglog(self, *args, **kwargs): ...
    def semilogx(self, *args, **kwargs): ...
    def semilogy(self, *args, **kwargs): ...
    def acorr(self, x, **kwargs): ...
    def xcorr(self, x, y, normed: bool = ..., detrend=..., usevlines: bool = ..., maxlags: int = ..., **kwargs): ...
    def step(self, x, y, *args, where: str = ..., data: Any | None = ..., **kwargs): ...
    def bar(self, x, height, width: float = ..., bottom: Any | None = ..., *, align: str = ..., **kwargs): ...
    def barh(self, y, width, height: float = ..., left: Any | None = ..., *, align: str = ..., **kwargs): ...
    def bar_label(self, container, labels: Any | None = ..., *, fmt: str = ..., label_type: str = ..., padding: int = ..., **kwargs): ...
    def broken_barh(self, xranges, yrange, **kwargs): ...
    def stem(self, *args, linefmt: Any | None = ..., markerfmt: Any | None = ..., basefmt: Any | None = ..., bottom: int = ..., label: Any | None = ..., use_line_collection: bool = ..., orientation: str = ...): ...
    def pie(self, x, explode: Any | None = ..., labels: Any | None = ..., colors: Any | None = ..., autopct: Any | None = ..., pctdistance: float = ..., shadow: bool = ..., labeldistance: float = ..., startangle: int = ..., radius: int = ..., counterclock: bool = ..., wedgeprops: Any | None = ..., textprops: Any | None = ..., center=..., frame: bool = ..., rotatelabels: bool = ..., *, normalize: bool = ...): ...
    def errorbar(self, x, y, yerr: Any | None = ..., xerr: Any | None = ..., fmt: str = ..., ecolor: Any | None = ..., elinewidth: Any | None = ..., capsize: Any | None = ..., barsabove: bool = ..., lolims: bool = ..., uplims: bool = ..., xlolims: bool = ..., xuplims: bool = ..., errorevery: int = ..., capthick: Any | None = ..., **kwargs): ...
    def boxplot(self, x, notch: Any | None = ..., sym: Any | None = ..., vert: Any | None = ..., whis: Any | None = ..., positions: Any | None = ..., widths: Any | None = ..., patch_artist: Any | None = ..., bootstrap: Any | None = ..., usermedians: Any | None = ..., conf_intervals: Any | None = ..., meanline: Any | None = ..., showmeans: Any | None = ..., showcaps: Any | None = ..., showbox: Any | None = ..., showfliers: Any | None = ..., boxprops: Any | None = ..., labels: Any | None = ..., flierprops: Any | None = ..., medianprops: Any | None = ..., meanprops: Any | None = ..., capprops: Any | None = ..., whiskerprops: Any | None = ..., manage_ticks: bool = ..., autorange: bool = ..., zorder: Any | None = ...): ...
    def bxp(self, bxpstats, positions: Any | None = ..., widths: Any | None = ..., vert: bool = ..., patch_artist: bool = ..., shownotches: bool = ..., showmeans: bool = ..., showcaps: bool = ..., showbox: bool = ..., showfliers: bool = ..., boxprops: Any | None = ..., whiskerprops: Any | None = ..., flierprops: Any | None = ..., medianprops: Any | None = ..., capprops: Any | None = ..., meanprops: Any | None = ..., meanline: bool = ..., manage_ticks: bool = ..., zorder: Any | None = ...): ...
    def scatter(self, x, y, s: Any | None = ..., c: Any | None = ..., marker: Any | None = ..., cmap: Any | None = ..., norm: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., alpha: Any | None = ..., linewidths: Any | None = ..., *, edgecolors: Any | None = ..., plotnonfinite: bool = ..., **kwargs): ...
    def hexbin(self, x, y, C: Any | None = ..., gridsize: int = ..., bins: Any | None = ..., xscale: str = ..., yscale: str = ..., extent: Any | None = ..., cmap: Any | None = ..., norm: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., alpha: Any | None = ..., linewidths: Any | None = ..., edgecolors: str = ..., reduce_C_function=..., mincnt: Any | None = ..., marginals: bool = ..., **kwargs): ...
    def arrow(self, x, y, dx, dy, **kwargs): ...
    def quiverkey(self, Q, X, Y, U, label, **kwargs): ...
    def quiver(self, *args, **kwargs): ...
    def barbs(self, *args, **kwargs): ...
    def fill(self, *args, data: Any | None = ..., **kwargs): ...
    def fill_between(self, x, y1, y2: int = ..., where: Any | None = ..., interpolate: bool = ..., step: Any | None = ..., **kwargs): ...
    def fill_betweenx(self, y, x1, x2: int = ..., where: Any | None = ..., step: Any | None = ..., interpolate: bool = ..., **kwargs): ...
    def imshow(self, X, cmap: Any | None = ..., norm: Any | None = ..., aspect: Any | None = ..., interpolation: Any | None = ..., alpha: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., origin: Any | None = ..., extent: Any | None = ..., *, interpolation_stage: Any | None = ..., filternorm: bool = ..., filterrad: float = ..., resample: Any | None = ..., url: Any | None = ..., **kwargs): ...
    def pcolor(self, *args, shading: Any | None = ..., alpha: Any | None = ..., norm: Any | None = ..., cmap: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., **kwargs): ...
    def pcolormesh(self, *args, alpha: Any | None = ..., norm: Any | None = ..., cmap: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., shading: Any | None = ..., antialiased: bool = ..., **kwargs): ...
    def pcolorfast(self, *args, alpha: Any | None = ..., norm: Any | None = ..., cmap: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., **kwargs): ...
    def contour(self, *args, **kwargs): ...
    def contourf(self, *args, **kwargs): ...
    def clabel(self, CS, levels: Any | None = ..., **kwargs): ...
    def hist(self, x, bins: Any | None = ..., range: Any | None = ..., density: bool = ..., weights: Any | None = ..., cumulative: bool = ..., bottom: Any | None = ..., histtype: str = ..., align: str = ..., orientation: str = ..., rwidth: Any | None = ..., log: bool = ..., color: Any | None = ..., label: Any | None = ..., stacked: bool = ..., **kwargs): ...
    def stairs(self, values, edges: Any | None = ..., *, orientation: str = ..., baseline: int = ..., fill: bool = ..., **kwargs): ...
    def hist2d(self, x, y, bins: int = ..., range: Any | None = ..., density: bool = ..., weights: Any | None = ..., cmin: Any | None = ..., cmax: Any | None = ..., **kwargs): ...
    def psd(self, x, NFFT: Any | None = ..., Fs: Any | None = ..., Fc: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ..., return_line: Any | None = ..., **kwargs): ...
    def csd(self, x, y, NFFT: Any | None = ..., Fs: Any | None = ..., Fc: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ..., return_line: Any | None = ..., **kwargs): ...
    def magnitude_spectrum(self, x, Fs: Any | None = ..., Fc: Any | None = ..., window: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale: Any | None = ..., **kwargs): ...
    def angle_spectrum(self, x, Fs: Any | None = ..., Fc: Any | None = ..., window: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., **kwargs): ...
    def phase_spectrum(self, x, Fs: Any | None = ..., Fc: Any | None = ..., window: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., **kwargs): ...
    def cohere(self, x, y, NFFT: int = ..., Fs: int = ..., Fc: int = ..., detrend=..., window=..., noverlap: int = ..., pad_to: Any | None = ..., sides: str = ..., scale_by_freq: Any | None = ..., **kwargs): ...
    def specgram(self, x, NFFT: Any | None = ..., Fs: Any | None = ..., Fc: Any | None = ..., detrend: Any | None = ..., window: Any | None = ..., noverlap: Any | None = ..., cmap: Any | None = ..., xextent: Any | None = ..., pad_to: Any | None = ..., sides: Any | None = ..., scale_by_freq: Any | None = ..., mode: Any | None = ..., scale: Any | None = ..., vmin: Any | None = ..., vmax: Any | None = ..., **kwargs): ...
    def spy(self, Z, precision: int = ..., marker: Any | None = ..., markersize: Any | None = ..., aspect: str = ..., origin: str = ..., **kwargs): ...
    def matshow(self, Z, **kwargs): ...
    def violinplot(self, dataset, positions: Any | None = ..., vert: bool = ..., widths: float = ..., showmeans: bool = ..., showextrema: bool = ..., showmedians: bool = ..., quantiles: Any | None = ..., points: int = ..., bw_method: Any | None = ...): ...
    def violin(self, vpstats, positions: Any | None = ..., vert: bool = ..., widths: float = ..., showmeans: bool = ..., showextrema: bool = ..., showmedians: bool = ...): ...
    table: Any
    stackplot: Any
    streamplot: Any
    tricontour: Any
    tricontourf: Any
    tripcolor: Any
    triplot: Any
