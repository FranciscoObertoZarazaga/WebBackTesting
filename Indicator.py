from ta.trend import *
from ta.momentum import *
from ta.volatility import *
from ta.volume import *
from ta.others import *
from SqueezeMomentumIndicator import SqueezeMomentumIndicator


def sm(kline, *args, **kwargs):
    print('hola')
    return SqueezeMomentumIndicator(kline, *args, **kwargs)

# MOMENTUM INDICATORS
def ao(kline, *args, **kwargs):
    ao = AwesomeOscillatorIndicator(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return ao.awesome_oscillator()


def kama(kline, *args, **kwargs):
    kama = KAMAIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return kama.kama()


def ppo(kline, *args, **kwargs):
    ppo = PercentagePriceOscillator(kline['Close'], *args, **kwargs, fillna=False)
    return ppo.ppo()


def pvo(kline, *args, **kwargs):
    pvo = PercentageVolumeOscillator(kline['Volume'], *args, **kwargs, fillna=False)
    return pvo.pvo()


def roc(kline, *args, **kwargs):
    roc = ROCIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return roc.roc()


def rsi(kline, *args, **kwargs):
    rsi = RSIIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return rsi.rsi()


def stochrsi(kline, *args, **kwargs):
    stochrsi = StochRSIIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return stochrsi.stochrsi()


def stoch(kline, *args, **kwargs):
    stoch = StochasticOscillator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return stoch.stoch()


def tsi(kline, *args, **kwargs):
    tsi = TSIIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return tsi.tsi()


def uo(kline, *args, **kwargs):
    uo = UltimateOscillator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return uo.ultimate_oscillator()


def wi(kline, *args, **kwargs):
    wi = WilliamsRIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return wi.williams_r()


# VOLUME INDICATORS
def adi(kline):
    adi = AccDistIndexIndicator(kline['High'], kline['Low'], kline['Close'], kline['Volume'], fillna=False)
    return adi.acc_dist_index()


def cmf(kline, *args, **kwargs):
    cmf = ChaikinMoneyFlowIndicator(kline['High'], kline['Low'], kline['Close'], kline['Volume'], *args, **kwargs, fillna=False)
    return cmf.chaikin_money_flow()


def eom(kline, *args, **kwargs):
    eom = EaseOfMovementIndicator(kline['High'], kline['Low'], kline['Volume'], *args, **kwargs, fillna=False)
    return eom.ease_of_movement()


def fi(kline, *args, **kwargs):
    fi = ForceIndexIndicator(kline['Close'], kline['Volume'], *args, **kwargs, fillna=False)
    return fi.force_index()


def mfi(kline, *args, **kwargs):
    mfi = MFIIndicator(kline['High'], kline['Low'], kline['Close'], kline['Volume'], *args, **kwargs, fillna=False)
    return mfi.money_flow_index()


def nvi(kline):
    nvi = NegativeVolumeIndexIndicator(kline['Close'], kline['Volume'], fillna=False)
    return nvi.negative_volume_index()


def obv(kline):
    obv = OnBalanceVolumeIndicator(kline['Close'], kline['Volume'], fillna=False)
    return obv.on_balance_volume()


def vpt(kline):
    vpt = VolumePriceTrendIndicator(kline['Close'], kline['Volume'], fillna=False)
    return vpt.volume_price_trend()


def vwap(kline, *args, **kwargs):
    vwap = VolumeWeightedAveragePrice(kline['High'], kline['Low'], kline['Close'], kline['Volume'], *args, **kwargs, fillna=False)
    return vwap.volume_weighted_average_price()


# VOLATILITY INDICATORS
def atr(kline, *args, **kwargs):
    atr = AverageTrueRange(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return atr.average_true_range()


def bbh(kline, *args, **kwargs):
    bbh = BollingerBands(kline['Close'], *args, **kwargs, fillna=False)
    return bbh.bollinger_hband()


def bbl(kline, *args, **kwargs):
    bbl = BollingerBands(kline['Close'], *args, **kwargs, fillna=False)
    return bbl.bollinger_lband()


def bbm(kline, *args, **kwargs):
    bbm = BollingerBands(kline['Close'], *args, **kwargs, fillna=False)
    return bbm.bollinger_mavg()


def dch(kline, *args, **kwargs):
    dch = DonchianChannel(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return dch.donchian_channel_hband()


def dcl(kline, *args, **kwargs):
    dcl = DonchianChannel(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return dcl.donchian_channel_lband()


def dcm(kline, *args, **kwargs):
    dcm = DonchianChannel(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return dcm.donchian_channel_mband()

def ui(kline, *args, **kwargs):
    ui = UlcerIndex(kline['Close'], *args, **kwargs, fillna=False)
    return ui.ulcer_index()


# TREND INDICATORS
def adx(kline, *args, **kwargs):
    adx = ADXIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return adx.adx()


def ai(kline, *args, **kwargs):
    ai = AroonIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return ai.aroon_indicator()


def cci(kline, *args, **kwargs):
    cci = CCIIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return cci.cci()


def dpo(kline, *args, **kwargs):
    dpo = DPOIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return dpo.dpo()


def ema(kline, *args, **kwargs):
    ema = EMAIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return ema.ema_indicator()


def iia(kline, *args, **kwargs):
    iia = IchimokuIndicator(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return iia.ichimoku_a()


def iib(kline, *args, **kwargs):
    iib = IchimokuIndicator(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return iib.ichimoku_b()


def iiks(kline, *args, **kwargs):
    iiks = IchimokuIndicator(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return iiks.ichimoku_base_line()


def iits(kline, *args, **kwargs):
    iits = IchimokuIndicator(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return iits.ichimoku_conversion_line()


def kst(kline, *args, **kwargs):
    kst = KSTIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return kst.kst()


def macd(kline, *args, **kwargs):
    macd = MACD(kline['Close'], *args, **kwargs, fillna=False)
    return macd.macd()


def mi(kline, *args, **kwargs):
    mi = MassIndex(kline['High'], kline['Low'], *args, **kwargs, fillna=False)
    return mi.mass_index()


def psar(kline, *args, **kwargs):
    psar = PSARIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return psar.psar()


def sma(kline, window=14):
    sma = SMAIndicator(kline['Close'], window, fillna=False)
    return sma.sma_indicator()


def stc(kline, *args, **kwargs):
    stc = STCIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return stc.stc()


def trix(kline, *args, **kwargs):
    trix = TRIXIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return trix.trix()


def vip(kline, *args, **kwargs):
    vip = VortexIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return vip.vortex_indicator_pos()


def vin(kline, *args, **kwargs):
    vin = VortexIndicator(kline['High'], kline['Low'], kline['Close'], *args, **kwargs, fillna=False)
    return vin.vortex_indicator_neg()


def wma(kline, *args, **kwargs):
    wma = WMAIndicator(kline['Close'], *args, **kwargs, fillna=False)
    return wma.wma()


# OTHER INDICATORS
def cr(kline):
    cr = CumulativeReturnIndicator(kline['Close'], fillna=False)
    return cr.cumulative_return()


def dlr(kline):
    dlr = DailyLogReturnIndicator(kline['Close'], fillna=False)
    return dlr.daily_log_return()


def dr(kline):
    dr = DailyReturnIndicator(kline['Close'], fillna=False)
    return dr.daily_return()


indicators = ['ao', 'kama', 'ppo', 'pvo', 'roc', 'rsi', 'stochrsi', 'stoch', 'tsi', 'uo', 'wi', 'adi', 'cmf', 'eom', 'fi', 'mfi', 'nvi', 'obv', 'vpt', 'vwap', 'atr', 'bbh', 'bbl', 'bbm', 'dch', 'dcl', 'dcm', 'ui', 'adx', 'ai', 'cci', 'dpo', 'ema', 'iia', 'iib', 'iiks', 'iits', 'kst', 'macd', 'mi', 'psar', 'sma', 'sm', 'stc', 'trix', 'vip', 'vin', 'wma', 'cr', 'dlr', 'dr']
