import copy
import dataclasses
import io
import logging
from typing import List
from typing import Optional
import zipfile

import pandas as pd
import psycopg2
import requests
import sqlalchemy

from cloud_validol.loader.lib import cot

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class CftcDownloadConfig:
    year_download_url: str
    initial_download_url: Optional[str] = None
    initial_date_format: Optional[str] = None


def _make_derivative_configs() -> List[cot.DerivativeConfig]:
    cftc_date_format = '%Y-%m-%d'

    cftc_disaggregated_futures_only = cot.DerivativeConfig(
        source='cftc_disaggregated_futures_only',
        table_name='cot_disaggregated_data',
        platform_code_col='CFTC_Market_Code',
        derivative_name_col='Market_and_Exchange_Names',
        date_col='Report_Date_as_YYYY-MM-DD',
        date_format=cftc_date_format,
        data_cols={
            'Open_Interest_All': 'oi',
            'Prod_Merc_Positions_Long_All': 'pmpl',
            'Prod_Merc_Positions_Short_All': 'pmps',
            'Swap_Positions_Long_All': 'sdpl',
            'Swap__Positions_Short_All': 'sdps',
            'M_Money_Positions_Long_All': 'mmpl',
            'M_Money_Positions_Short_All': 'mmps',
            'Other_Rept_Positions_Long_All': 'orpl',
            'Other_Rept_Positions_Short_All': 'orps',
            'NonRept_Positions_Long_All': 'nrl',
            'NonRept_Positions_Short_All': 'nrs',
            'Conc_Gross_LE_4_TDR_Long_All': 'x_4gl_percent',
            'Conc_Gross_LE_4_TDR_Short_All': 'x_4gs_percent',
            'Conc_Gross_LE_8_TDR_Long_All': 'x_8gl_percent',
            'Conc_Gross_LE_8_TDR_Short_All': 'x_8gs_percent',
            'Conc_Net_LE_4_TDR_Long_All': 'x_4l_percent',
            'Conc_Net_LE_4_TDR_Short_All': 'x_4s_percent',
            'Conc_Net_LE_8_TDR_Long_All': 'x_8l_percent',
            'Conc_Net_LE_8_TDR_Short_All': 'x_8s_percent',
            'Swap__Positions_Spread_All': 'sdp_spr',
            'M_Money_Positions_Spread_All': 'mmp_spr',
            'Other_Rept_Positions_Spread_All': 'orp_spr',
        },
        report_type='futures_only',
        initial_from_year=2017,
        download_config=CftcDownloadConfig(
            year_download_url='http://www.cftc.gov/files/dea/history/fut_disagg_txt_{year}.zip',
            initial_download_url='http://www.cftc.gov/files/dea/history/fut_disagg_txt_hist_2006_2016.zip',
        ),
    )

    cftc_disaggregated_combined = copy.deepcopy(cftc_disaggregated_futures_only)
    cftc_disaggregated_combined.source = (
        'cftc_disaggregated_futures_and_options_combined'
    )
    cftc_disaggregated_combined.download_config.year_download_url = (
        'http://www.cftc.gov/files/dea/history/com_disagg_txt_{year}.zip'
    )
    cftc_disaggregated_combined.download_config.initial_download_url = (
        'http://www.cftc.gov/files/dea/history/com_disagg_txt_hist_2006_2016.zip'
    )
    cftc_disaggregated_combined.report_type = 'combined'

    cftc_financial_futures_only = cot.DerivativeConfig(
        source='cftc_financial_futures_futures_only',
        table_name='cot_financial_futures_data',
        platform_code_col='CFTC_Market_Code',
        derivative_name_col='Market_and_Exchange_Names',
        date_col='Report_Date_as_YYYY-MM-DD',
        date_format=cftc_date_format,
        data_cols={
            'Open_Interest_All': 'oi',
            'Dealer_Positions_Long_All': 'dipl',
            'Dealer_Positions_Short_All': 'dips',
            'Dealer_Positions_Spread_All': 'dip_spr',
            'Asset_Mgr_Positions_Long_All': 'ampl',
            'Asset_Mgr_Positions_Short_All': 'amps',
            'Asset_Mgr_Positions_Spread_All': 'amp_spr',
            'Lev_Money_Positions_Long_All': 'lmpl',
            'Lev_Money_Positions_Short_All': 'lmps',
            'Lev_Money_Positions_Spread_All': 'lmp_spr',
            'Other_Rept_Positions_Long_All': 'orpl',
            'Other_Rept_Positions_Short_All': 'orps',
            'Other_Rept_Positions_Spread_All': 'orp_spr',
            'NonRept_Positions_Long_All': 'nrl',
            'NonRept_Positions_Short_All': 'nrs',
        },
        report_type='futures_only',
        initial_from_year=2017,
        download_config=CftcDownloadConfig(
            year_download_url='http://www.cftc.gov/files/dea/history/fut_fin_txt_{year}.zip',
            initial_download_url='http://www.cftc.gov/files/dea/history/fin_fut_txt_2006_2016.zip',
            initial_date_format='%m/%d/%Y 12:00:00 AM',
        ),
    )

    cftc_financial_combined = copy.deepcopy(cftc_financial_futures_only)
    cftc_financial_combined.source = 'cftc_financial_futures_combined'
    cftc_financial_combined.download_config.year_download_url = (
        'http://www.cftc.gov/files/dea/history/com_fin_txt_{year}.zip'
    )
    cftc_financial_combined.download_config.initial_download_url = (
        'http://www.cftc.gov/files/dea/history/fin_com_txt_2006_2016.zip'
    )
    cftc_financial_combined.report_type = 'combined'

    cftc_futures_only = cot.DerivativeConfig(
        source='cftc_futures_only',
        table_name='cot_futures_only_data',
        platform_code_col='CFTC Market Code in Initials',
        derivative_name_col='Market and Exchange Names',
        date_col='As of Date in Form YYYY-MM-DD',
        date_format='%Y-%m-%d',
        data_cols={
            'Open Interest (All)': 'oi',
            'Noncommercial Positions-Long (All)': 'ncl',
            'Noncommercial Positions-Short (All)': 'ncs',
            'Commercial Positions-Long (All)': 'cl',
            'Commercial Positions-Short (All)': 'cs',
            'Nonreportable Positions-Long (All)': 'nrl',
            'Nonreportable Positions-Short (All)': 'nrs',
            'Concentration-Net LT =4 TDR-Long (All)': 'x_4l_percent',
            'Concentration-Net LT =4 TDR-Short (All)': 'x_4s_percent',
            'Concentration-Net LT =8 TDR-Long (All)': 'x_8l_percent',
            'Concentration-Net LT =8 TDR-Short (All)': 'x_8s_percent',
        },
        report_type='futures_only',
        initial_from_year=2017,
        download_config=CftcDownloadConfig(
            year_download_url='http://www.cftc.gov/files/dea/history/deacot{year}.zip',
            initial_download_url='http://www.cftc.gov/files/dea/history/deacot1986_2016.zip',
        ),
    )

    return [
        cftc_futures_only,
        cftc_disaggregated_futures_only,
        cftc_disaggregated_combined,
        cftc_financial_futures_only,
        cftc_financial_combined,
    ]


def _download_doc(
    config: cot.DerivativeConfig,
    url: str,
) -> Optional[pd.DataFrame]:
    logger.info('Downloading %s for %s', url, config.source)

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 404:
        logger.error('%s is not found', url)

        return None

    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
        path = zip_file.namelist()[0]
        csv_buff = zip_file.read(path).decode('utf-8')

    return pd.read_csv(io.StringIO(csv_buff))


def update(engine: sqlalchemy.engine.base.Engine, conn: psycopg2.extensions.connection):
    logger.info('Start updating CFTC data')

    for config in _make_derivative_configs():
        update_interval = cot.get_interval(engine, config)

        if update_interval is None:
            continue

        dfs = []
        if update_interval.load_initial:
            raw_df = _download_doc(
                config,
                config.download_config.initial_download_url,
            )

            if raw_df is not None:
                dfs.append(
                    cot.process_raw_dataframe(
                        config,
                        config.download_config.initial_date_format
                        or config.date_format,
                        raw_df,
                    )
                )

        for year in update_interval.years_to_load:
            raw_df = _download_doc(
                config,
                config.download_config.year_download_url.format(year=year),
            )

            if raw_df is not None:
                dfs.append(
                    cot.process_raw_dataframe(config, config.date_format, raw_df)
                )

        df = pd.concat(dfs)

        cot.insert_platforms_derivatives(conn, config, df)
        cot.insert_data(engine, config, df)

    logger.info('Finish updating CFTC data')
