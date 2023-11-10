### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from typing import List, Literal, Union

import numpy
import pandas
import typing_extensions
from annotated_types import Ge, Gt
from openbb_core.app.model.obbject import OBBject
from openbb_core.app.static.container import Container
from openbb_core.app.static.decorators import validate
from openbb_core.app.static.filters import filter_inputs
from openbb_provider.abstract.data import Data


class ROUTER_ta(Container):
    """/ta
    ad
    adosc
    adx
    aroon
    atr
    bbands
    cci
    cg
    clenow
    cones
    demark
    donchian
    ema
    fib
    fisher
    hma
    ichimoku
    kc
    macd
    obv
    rsi
    sma
    stoch
    vwap
    wma
    zlma
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate(config=dict(arbitrary_types_allowed=True))
    def ad(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        The Accumulation/Distribution Line is similar to the On Balance
        Volume (OBV), which sums the volume times +1/-1 based on whether the close is
        higher than the previous close. The Accumulation/Distribution indicator, however
        multiplies the volume by the close location value (CLV). The CLV is based on the
        movement of the issue within a single bar and can be +1, -1 or zero.


        The Accumulation/Distribution Line is interpreted by looking for a divergence in
        the direction of the indicator relative to price. If the Accumulation/Distribution
        Line is trending upward it indicates that the price may follow. Also, if the
        Accumulation/Distribution Line becomes flat while the price is still rising (or falling)
        then it signals an impending flattening of the price.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        offset : int, optional
            Offset of the AD, by default 0.

        Returns
        -------
        OBBject[List[Data]]

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> ad_data = obb.ta.ad(data=stock_data.results,offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/ad",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def adosc(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        fast: typing_extensions.Annotated[int, Gt(gt=0)] = 3,
        slow: typing_extensions.Annotated[int, Gt(gt=0)] = 10,
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        Accumulation/Distribution Oscillator, also known as the Chaikin Oscillator
        is essentially a momentum indicator, but of the Accumulation-Distribution line
        rather than merely price. It looks at both the strength of price moves and the
        underlying buying and selling pressure during a given time period. The oscillator
        reading above zero indicates net buying pressure, while one below zero registers
        net selling pressure. Divergence between the indicator and pure price moves are
        the most common signals from the indicator, and often flag market turning points.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        fast : PositiveInt, optional
            Number of periods to be used for the fast calculation, by default 3.
        slow : PositiveInt, optional
            Number of periods to be used for the slow calculation, by default 10.
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> adosc_data = obb.ta.adosc(data=stock_data.results, fast=3, slow=10, offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            fast=fast,
            slow=slow,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/adosc",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def adx(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: int = 50,
        scalar: float = 100.0,
        drift: int = 1,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The ADX is a Welles Wilder style moving average of the Directional Movement Index (DX).
        The values range from 0 to 100, but rarely get above 60. To interpret the ADX, consider
        a high number to be a strong trend, and a low number, a weak trend.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods for the ADX, by default 50.
        scalar : float, optional
            Scalar value for the ADX, by default 100.0.
        drift : int, optional
            Drift value for the ADX, by default 1.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> adx_data = obb.ta.adx(data=stock_data.results,length=50,scalar=100.0,drift=1)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            scalar=scalar,
            drift=drift,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/adx",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def aroon(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: int = 25,
        scalar: int = 100,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The word aroon is Sanskrit for "dawn's early light." The Aroon
        indicator attempts to show when a new trend is dawning. The indicator consists
        of two lines (Up and Down) that measure how long it has been since the highest
        high/lowest low has occurred within an n period range.

        When the Aroon Up is staying between 70 and 100 then it indicates an upward trend.
        When the Aroon Down is staying between 70 and 100 then it indicates an downward trend.
        A strong upward trend is indicated when the Aroon Up is above 70 while the Aroon Down is below 30.
        Likewise, a strong downward trend is indicated when the Aroon Down is above 70 while
        the Aroon Up is below 30. Also look for crossovers. When the Aroon Down crosses above
        the Aroon Up, it indicates a weakening of the upward trend (and vice versa).

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index: str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 25.
        scalar : int, optional
            Scalar to be used for the calculation, by default 100.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> aroon_data = obb.ta.aroon(data=stock_data.results, length=25, scalar=100)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            scalar=scalar,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/aroon",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def atr(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: typing_extensions.Annotated[int, Gt(gt=0)] = 14,
        mamode: Literal["rma", "ema", "sma", "wma"] = "rma",
        drift: typing_extensions.Annotated[int, Ge(ge=0)] = 1,
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        Average True Range is used to measure volatility, especially volatility caused by
        gaps or limit moves.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        length : PositiveInt, optional
            It's period, by default 14
        mamode : Literal["rma", "ema", "sma", "wma"], optional
            Moving average mode, by default "rma"
        drift : NonNegativeInt, optional
            The difference period, by default 1
        offset : int, optional
            How many periods to offset the result, by default 0

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> atr_data = obb.ta.atr(data=stock_data.results)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            mamode=mamode,
            drift=drift,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/atr",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def bbands(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        std: typing_extensions.Annotated[float, Ge(ge=0)] = 2,
        mamode: Literal["sma", "ema", "wma", "rma"] = "sma",
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        Bollinger Bands consist of three lines. The middle band is a simple
        moving average (generally 20 periods) of the typical price (TP). The upper and lower
        bands are F standard deviations (generally 2) above and below the middle band.
        The bands widen and narrow when the volatility of the price is higher or lower,
        respectively.

        Bollinger Bands do not, in themselves, generate buy or sell signals;
        they are an indicator of overbought or oversold conditions. When the price is near the
        upper or lower band it indicates that a reversal may be imminent. The middle band
        becomes a support or resistance level. The upper and lower bands can also be
        interpreted as price targets. When the price bounces off of the lower band and crosses
        the middle band, then the upper band becomes the price target.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        std : NonNegativeFloat, optional
            Standard deviation to be used for the calculation, by default 2.
        mamode : Literal["sma", "ema", "wma", "rma"], optional
            Moving average mode to be used for the calculation, by default "sma".
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> bbands = obb.ta.bbands(
        >>>     data=stock_data.results, target="close", length=50, std=2, mamode="sma", offset=0
        >>> )
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            std=std,
            mamode=mamode,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/bbands",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def cci(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: typing_extensions.Annotated[int, Gt(gt=0)] = 14,
        scalar: typing_extensions.Annotated[float, Gt(gt=0)] = 0.015,
    ) -> OBBject[List[Data]]:
        """
        The CCI is designed to detect beginning and ending market trends.
        The range of 100 to -100 is the normal trading range. CCI values outside of this
        range indicate overbought or oversold conditions. You can also look for price
        divergence in the CCI. If the price is making new highs, and the CCI is not,
        then a price correction is likely.

        Parameters
        ----------
        data : List[Data]
            The data to use for the CCI calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : PositiveInt, optional
            The length of the CCI, by default 14.
        scalar : PositiveFloat, optional
            The scalar of the CCI, by default 0.015.

        Returns
        -------
        OBBject[List[Data]]
            The CCI data.
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            scalar=scalar,
            data_processing=True,
        )

        return self._run(
            "/ta/cci",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def cg(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: typing_extensions.Annotated[int, Gt(gt=0)] = 14,
    ) -> OBBject[List[Data]]:
        """
        The Center of Gravity indicator, in short, is used to anticipate future price movements
        and to trade on price reversals as soon as they happen. However, just like other oscillators,
        the COG indicator returns the best results in range-bound markets and should be avoided when
        the price is trending. Traders who use it will be able to closely speculate the upcoming
        price change of the asset.

        Parameters
        ----------
        data : List[Data]
            The data to use for the COG calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : PositiveInt, optional
            The length of the COG, by default 14

        Returns
        -------
        OBBject[List[Data]]
            The COG data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> cg_data = obb.ta.cg(data=stock_data.results, length=14)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            data_processing=True,
        )

        return self._run(
            "/ta/cg",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def clenow(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        target: str = "close",
        period: typing_extensions.Annotated[int, Gt(gt=0)] = 90,
    ) -> OBBject[List[Data]]:
        """
        Clenow Volatility Adjusted Momentum.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        target : str, optional
            Target column name, by default "close".
        period : PositiveInt, optional
            Number of periods for the momentum, by default 90.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> clenow_data = obb.ta.clenow(data=stock_data.results,period=90)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            target=target,
            period=period,
            data_processing=True,
        )

        return self._run(
            "/ta/clenow",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def cones(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        lower_q: float = 0.25,
        upper_q: float = 0.75,
        model: Literal[
            "STD",
            "Parkinson",
            "Garman-Klass",
            "Hodges-Tompkins",
            "Rogers-Satchell",
            "Yang-Zhang",
        ] = "STD",
        is_crypto: bool = False,
    ) -> OBBject[List[Data]]:
        """Calculate the realized volatility quantiles over rolling windows of time.

        The model for calculating volatility is selectable.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        lower_q : float, optional
            The lower quantile value for calculations
        upper_q : float, optional
            The upper quantile value for calculations
        model : Literal["STD", "Parkinson", "Garman-Klass", "Hodges-Tompkins", "Rogers-Satchell", "Yang-Zhang"], optional
            The model used to calculate realized volatility

                Standard deviation measures how widely returns are dispersed from the average return.
                It is the most common (and biased) estimator of volatility.

                Parkinson volatility uses the high and low price of the day rather than just close to close prices.
                It is useful for capturing large price movements during the day.

                Garman-Klass volatility extends Parkinson volatility by taking into account the opening and closing price.
                As markets are most active during the opening and closing of a trading session;
                it makes volatility estimation more accurate.

                Hodges-Tompkins volatility is a bias correction for estimation using an overlapping data sample.
                It produces unbiased estimates and a substantial gain in efficiency.

                Rogers-Satchell is an estimator for measuring the volatility with an average return not equal to zero.
                Unlike Parkinson and Garman-Klass estimators, Rogers-Satchell incorporates a drift term,
                mean return not equal to zero.

                Yang-Zhang volatility is the combination of the overnight (close-to-open volatility).
                It is a weighted average of the Rogers-Satchell volatility and the open-to-close volatility.
        is_crypto : bool, optional
            Whether the data is crypto or not. If True, volatility is calculated for 365 days instead of 252

        Returns
        -------
        OBBject[List[Data]]
            The cones data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> cones_data = obb.ta.cones(data=stock_data.results, lower_q=0.25, upper_q=0.75, model="STD")
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            lower_q=lower_q,
            upper_q=upper_q,
            model=model,
            is_crypto=is_crypto,
            data_processing=True,
        )

        return self._run(
            "/ta/cones",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def demark(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        target: str = "close",
        show_all: bool = True,
        asint: bool = True,
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        Demark sequential indicator

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        target : str, optional
            Target column name, by default "close".
        show_all : bool, optional
            Show 1 - 13. If set to False, show 6 - 9
        asint : bool, optional
            If True, fill NAs with 0 and change type to int, by default True.
        offset : int, optional
            How many periods to offset the result

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> demark_data = obb.ta.demark(data=stock_data.results,offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            target=target,
            show_all=show_all,
            asint=asint,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/demark",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def donchian(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        lower_length: typing_extensions.Annotated[int, Gt(gt=0)] = 20,
        upper_length: typing_extensions.Annotated[int, Gt(gt=0)] = 20,
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        Donchian Channels are three lines generated by moving average
        calculations that comprise an indicator formed by upper and lower
        bands around a midrange or median band. The upper band marks the
        highest price of a security over N periods while the lower band
        marks the lowest price of a security over N periods. The area
        between the upper and lower bands represents the Donchian Channel.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        lower_length : PositiveInt, optional
            Number of periods for the lower band, by default 20.
        upper_length : PositiveInt, optional
            Number of periods for the upper band, by default 20.
        offset : int, optional
            Offset of the Donchian Channel, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> donchian_data = obb.ta.donchian(data=stock_data.results,lower_length=20,upper_length=20,offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            lower_length=lower_length,
            upper_length=upper_length,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/donchian",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def ema(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The Exponential Moving Average is a staple of technical
        analysis and is used in countless technical indicators. In a Simple Moving
        Average, each value in the time period carries equal weight, and values outside
        of the time period are not included in the average. However, the Exponential
        Moving Average is a cumulative calculation, including all data. Past values have
        a diminishing contribution to the average, while more recent values have a greater
        contribution. This method allows the moving average to be more responsive to changes
        in the data.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : int, optional
            The length of the calculation, by default 50.
        offset : int, optional
            The offset of the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> ema_data = obb.ta.ema(data=stock_data.results,target="close",length=50,offset=0)

        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            offset=offset,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/ema",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def fib(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        close_column: Literal["close", "adj_close"] = "close",
        period: typing_extensions.Annotated[int, Gt(gt=0)] = 120,
        start_date: Union[str, None] = None,
        end_date: Union[str, None] = None,
    ) -> OBBject[List[Data]]:
        """Create Fibonacci Retracement Levels.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        period : PositiveInt, optional
            Period to calculate the indicator, by default 120

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> fib_data = obb.ta.fib(data=stock_data.results, period=120)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            close_column=close_column,
            period=period,
            start_date=start_date,
            end_date=end_date,
            data_processing=True,
        )

        return self._run(
            "/ta/fib",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def fisher(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: typing_extensions.Annotated[int, Gt(gt=0)] = 14,
        signal: typing_extensions.Annotated[int, Gt(gt=0)] = 1,
    ) -> OBBject[List[Data]]:
        """
        The Fisher Transform is a technical indicator created by John F. Ehlers
        that converts prices into a Gaussian normal distribution.1 The indicator
        highlights when prices have   moved to an extreme, based on recent prices.
        This may help in spotting turning points in the price of an asset. It also
        helps show the trend and isolate the price waves within a trend.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        length : PositiveInt, optional
            Fisher period, by default 14
        signal : PositiveInt, optional
            Fisher Signal period, by default 1

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> fisher_data = obb.ta.fisher(data=stock_data.results, length=14, signal=1)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            signal=signal,
            data_processing=True,
        )

        return self._run(
            "/ta/fisher",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def hma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The Hull Moving Average solves the age old dilemma of making a moving average
        more responsive to current price activity whilst maintaining curve smoothness.
        In fact the HMA almost eliminates lag altogether and manages to improve smoothing
        at the same time.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods for the HMA, by default 50.
        offset : int, optional
            Offset of the HMA, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> hma_data = obb.ta.hma(data=stock_data.results,target="close",length=50,offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            offset=offset,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/hma",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def ichimoku(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        conversion: typing_extensions.Annotated[int, Gt(gt=0)] = 9,
        base: typing_extensions.Annotated[int, Gt(gt=0)] = 26,
        lagging: typing_extensions.Annotated[int, Gt(gt=0)] = 52,
        offset: typing_extensions.Annotated[int, Gt(gt=0)] = 26,
        lookahead: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The Ichimoku Cloud, also known as Ichimoku Kinko Hyo, is a versatile indicator that
        defines support and resistance, identifies trend direction, gauges momentum and provides
        trading signals. Ichimoku Kinko Hyo translates into "one look equilibrium chart". With
        one look, chartists can identify the trend and look for potential signals within that trend.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        conversion : PositiveInt, optional
            Number of periods for the conversion line, by default 9.
        base : PositiveInt, optional
            Number of periods for the base line, by default 26.
        lagging : PositiveInt, optional
            Number of periods for the lagging span, by default 52.
        offset : PositiveInt, optional
            Number of periods for the offset, by default 26.
        lookahead : bool, optional
            drops the Chikou Span Column to prevent potential data leak
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            conversion=conversion,
            base=base,
            lagging=lagging,
            offset=offset,
            lookahead=lookahead,
            data_processing=True,
        )

        return self._run(
            "/ta/ichimoku",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def kc(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        length: typing_extensions.Annotated[int, Gt(gt=0)] = 20,
        scalar: typing_extensions.Annotated[float, Gt(gt=0)] = 20,
        mamode: Literal["ema", "sma", "wma", "hma", "zlma"] = "ema",
        offset: typing_extensions.Annotated[int, Ge(ge=0)] = 0,
    ) -> OBBject[List[Data]]:
        """
        Keltner Channels are volatility-based bands that are placed
        on either side of an asset's price and can aid in determining
        the direction of a trend.The Keltner channel uses the average
        true range (ATR) or volatility, with breaks above or below the top
        and bottom barriers signaling a continuation.

        Parameters
        ----------
        data : List[Data]
            The data to use for the Keltner Channels calculation.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : PositiveInt, optional
            The length of the Keltner Channels, by default 20
        scalar : PositiveFloat, optional
            The scalar to use for the Keltner Channels, by default 20
        mamode : Literal["ema", "sma", "wma", "hma", "zlma"], optional
            The moving average mode to use for the Keltner Channels, by default "ema"
        offset : NonNegativeInt, optional
            The offset to use for the Keltner Channels, by default 0

        Returns
        -------
        OBBject[List[Data]]
            The Keltner Channels data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> kc_data = obb.ta.kc(data=stock_data.results, length=20, scalar=20, mamode="ema", offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            length=length,
            scalar=scalar,
            mamode=mamode,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/kc",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def macd(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        fast: int = 12,
        slow: int = 26,
        signal: int = 9,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The Moving Average Convergence Divergence (MACD) is the difference
        between two Exponential Moving Averages. The Signal line is an Exponential Moving
        Average of the MACD.

        The MACD signals trend changes and indicates the start of new trend direction.
        High values indicate overbought conditions, low values indicate oversold conditions.
        Divergence with the price indicates an end to the current trend, especially if the
        MACD is at extreme high or low values. When the MACD line crosses above the
        signal line a buy signal is generated. When the MACD crosses below the signal line a
        sell signal is generated. To confirm the signal, the MACD should be above zero for a buy,
        and below zero for a sell.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        fast : int, optional
            Number of periods for the fast EMA, by default 12.
        slow : int, optional
            Number of periods for the slow EMA, by default 26.
        signal : int, optional
            Number of periods for the signal EMA, by default 9.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> macd_data = obb.ta.macd(data=stock_data.results,target="close",fast=12,slow=26,signal=9)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            fast=fast,
            slow=slow,
            signal=signal,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/macd",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def obv(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        The On Balance Volume (OBV) is a cumulative total of the up and
        down volume. When the close is higher than the previous close, the volume is added
        to the running total, and when the close is lower than the previous close, the volume
        is subtracted from the running total.

        To interpret the OBV, look for the OBV to move with the price or precede price moves.
        If the price moves before the OBV, then it is a non-confirmed move. A series of rising peaks,
        or falling troughs, in the OBV indicates a strong trend. If the OBV is flat, then the market
        is not trending.

        Parameters
        ----------
        data : List[Data]
            List of data to apply the indicator to.
        index : str, optional
            Index column name, by default "date"
        offset : int, optional
            How many periods to offset the result, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            List of data with the indicator applied.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> obv_data = obb.ta.obv(data=stock_data.results, offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/obv",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def rsi(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 14,
        scalar: float = 100.0,
        drift: int = 1,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The Relative Strength Index (RSI) calculates a ratio of the
        recent upward price movements to the absolute price movement. The RSI ranges
        from 0 to 100. The RSI is interpreted as an overbought/oversold indicator when
        the value is over 70/below 30. You can also look for divergence with price. If
        the price is making new highs/lows, and the RSI is not, it indicates a reversal.

        Parameters
        ----------
        data : List[Data]
            The data to use for the RSI calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date"
        length : int, optional
            The length of the RSI, by default 14
        scalar : float, optional
            The scalar to use for the RSI, by default 100.0
        drift : int, optional
            The drift to use for the RSI, by default 1

        Returns
        -------
        OBBject[List[Data]]
            The RSI data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> rsi_data = obb.ta.rsi(data=stock_data.results, target="close", length=14, scalar=100.0, drift=1)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            scalar=scalar,
            drift=drift,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/rsi",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def sma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        Moving Averages are used to smooth the data in an array to
        help eliminate noise and identify trends. The Simple Moving Average is literally
        the simplest form of a moving average. Each output value is the average of the
        previous n values. In a Simple Moving Average, each value in the time period carries
        equal weight, and values outside of the time period are not included in the average.
        This makes it less responsive to recent changes in the data, which can be useful for
        filtering out those changes.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        offset : int, optional
            Offset from the current period, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> sma_data = obb.ta.sma(data=stock_data.results,target="close",length=50,offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            offset=offset,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/sma",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def stoch(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        fast_k_period: typing_extensions.Annotated[int, Ge(ge=0)] = 14,
        slow_d_period: typing_extensions.Annotated[int, Ge(ge=0)] = 3,
        slow_k_period: typing_extensions.Annotated[int, Ge(ge=0)] = 3,
    ) -> OBBject[List[Data]]:
        """
        The Stochastic Oscillator measures where the close is in relation
        to the recent trading range. The values range from zero to 100. %D values over 75
        indicate an overbought condition; values under 25 indicate an oversold condition.
        When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses
        below, it is a sell signal. The Raw %K is generally considered too erratic to use
        for crossover signals.

        Parameters
        ----------
        data : List[Data]
            The data to use for the Stochastic Oscillator calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        fast_k_period : NonNegativeInt, optional
            The fast %K period, by default 14.
        slow_d_period : NonNegativeInt, optional
            The slow %D period, by default 3.
        slow_k_period : NonNegativeInt, optional
            The slow %K period, by default 3.

        Returns
        -------
        OBBject[List[Data]]
            The Stochastic Oscillator data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> stoch_data = obb.ta.stoch(data=stock_data.results, fast_k_period=14, slow_d_period=3, slow_k_period=3)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            fast_k_period=fast_k_period,
            slow_d_period=slow_d_period,
            slow_k_period=slow_k_period,
            data_processing=True,
        )

        return self._run(
            "/ta/stoch",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def vwap(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        index: str = "date",
        anchor: str = "D",
        offset: int = 0,
    ) -> OBBject[List[Data]]:
        """
        The Volume Weighted Average Price that measures the average typical price
        by volume.  It is typically used with intraday charts to identify general direction.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        index : str, optional
            Index column name to use with `data`, by default "date".
        anchor : str, optional
            Anchor period to use for the calculation, by default "D".
            See Timeseries Offset Aliases below for additional options:
            https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases
        offset : int, optional
            Offset from the current period, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> vwap_data = obb.ta.vwap(data=stock_data.results,anchor="D",offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            index=index,
            anchor=anchor,
            offset=offset,
            data_processing=True,
        )

        return self._run(
            "/ta/vwap",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def wma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        A Weighted Moving Average puts more weight on recent data and less on past data.
        This is done by multiplying each bar's price by a weighting factor. Because of its
        unique calculation, WMA will follow prices more closely than a corresponding Simple
        Moving Average.

        Parameters
        ----------
        data : List[Data]
            The data to use for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            The length of the WMA, by default 50.
        offset : int, optional
            The offset of the WMA, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The WMA data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> wma_data = obb.ta.wma(data=stock_data.results, target="close", length=50, offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            offset=offset,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/wma",
            **inputs,
        )

    @validate(config=dict(arbitrary_types_allowed=True))
    def zlma(
        self,
        data: Union[
            list,
            dict,
            pandas.DataFrame,
            List[pandas.DataFrame],
            pandas.core.series.Series,
            List[pandas.core.series.Series],
            numpy.ndarray,
            Data,
            List[Data],
        ],
        target: str = "close",
        index: str = "date",
        length: int = 50,
        offset: int = 0,
        chart: bool = False,
    ) -> OBBject[List[Data]]:
        """
        The zero lag exponential moving average (ZLEMA) indicator
        was created by John Ehlers and Ric Way. The idea is do a
        regular exponential moving average (EMA) calculation but
        on a de-lagged data instead of doing it on the regular data.
        Data is de-lagged by removing the data from "lag" days ago
        thus removing (or attempting to) the cumulative effect of
        the moving average.

        Parameters
        ----------
        data : List[Data]
            List of data to be used for the calculation.
        target : str
            Target column name.
        index : str, optional
            Index column name to use with `data`, by default "date".
        length : int, optional
            Number of periods to be used for the calculation, by default 50.
        offset : int, optional
            Offset to be used for the calculation, by default 0.

        Returns
        -------
        OBBject[List[Data]]
            The calculated data.

        Examples
        --------
        >>> from openbb import obb
        >>> stock_data = obb.stocks.load(symbol="TSLA", start_date="2023-01-01", provider="fmp")
        >>> zlma_data = obb.ta.zlma(data=stock_data.results, target="close", length=50, offset=0)
        """  # noqa: E501

        inputs = filter_inputs(
            data=data,
            target=target,
            index=index,
            length=length,
            offset=offset,
            chart=chart,
            data_processing=True,
        )

        return self._run(
            "/ta/zlma",
            **inputs,
        )
