import enum


class FileFormats(enum.Enum):
    JSON = 'json'


class Timeframe(enum.Enum):
    YEAR = '1Y'
    MONTH = '1M'
    DAY = '1d'
    HOUR = '1h'
    MINUTE = '1m'


FREQUENCY = {
    Timeframe.YEAR: 'y',
    Timeframe.MONTH: 'm',
    Timeframe.DAY: 'D',
    Timeframe.HOUR: 'h',
    Timeframe.MINUTE: '1min'
}


class PlotType(enum.Enum):
    CANDLE_PLOTS = 'candle_plots'
    SUB_PLOTS = 'sub_plots'

