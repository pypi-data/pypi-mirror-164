import datetime
import json
import os
import pandas as pd
from sqlalchemy.orm import sessionmaker, Query
from sqlalchemy import and_, create_engine, func
from sqlalchemy.sql import exists
import shlex
import subprocess
from open_mastr.settings import DB_ENGINE

from open_mastr.soap_api.config import (
    setup_logger,
    create_data_dir,
    get_filenames,
    get_data_version_dir,
    column_renaming,
)
from open_mastr.soap_api.download import MaStRDownload, _flatten_dict, to_csv
from open_mastr import orm
from open_mastr.soap_api.metadata.create import datapackage_meta_json
from open_mastr.utils.helpers import session_scope

from decimal import Decimal


log = setup_logger()


basic_units =  [
{'EinheitMastrNummer': 'SEE940146675093', 'DatumLetzeAktualisierung': datetime.datetime(2021, 1, 22, 8, 15, 47, 464243), 'Name': 'WEA 5', 'Einheitart': 'Stromerzeugungseinheit', 'Einheittyp': 'Windeinheit', 'Standort': '37247 Großalmerode', 'Bruttoleistung': Decimal('3000'), 'Erzeugungsleistung': None, 'EinheitBetriebsstatus': 'InBetrieb', 'Anlagenbetreiber': 'ABR930129817008', 'EegMastrNummer': 'EEG951718125489', 'KwkMastrNummer': None, 'SpeMastrNummer': None, 'GenMastrNummer': 'SGE961876398816', 'BestandsanlageMastrNummer': None, 'NichtVorhandenInMigriertenEinheiten': None},
{'EinheitMastrNummer': 'SEE973767078653', 'DatumLetzeAktualisierung': datetime.datetime(2021, 6, 10, 6, 0, 3, 245437), 'Name': 'WEA 2 / 1150775', 'Einheitart': 'Stromerzeugungseinheit', 'Einheittyp': 'Windeinheit', 'Standort': '23824 Damsdorf', 'Bruttoleistung': Decimal('3000'), 'Erzeugungsleistung': None, 'EinheitBetriebsstatus': 'InBetrieb', 'Anlagenbetreiber': 'ABR929036363364', 'EegMastrNummer': 'EEG912885854947', 'KwkMastrNummer': None, 'SpeMastrNummer': None, 'GenMastrNummer': 'SGE918200258391', 'BestandsanlageMastrNummer': None, 'NichtVorhandenInMigriertenEinheiten': None},
{'EinheitMastrNummer': 'SEE914108319653', 'DatumLetzeAktualisierung': datetime.datetime(2021, 1, 22, 8, 14, 26, 387397), 'Name': 'WEA 4', 'Einheitart': 'Stromerzeugungseinheit', 'Einheittyp': 'Windeinheit', 'Standort': '37247 Großalmerode', 'Bruttoleistung': Decimal('3000'), 'Erzeugungsleistung': None, 'EinheitBetriebsstatus': 'InBetrieb', 'Anlagenbetreiber': 'ABR930129817008', 'EegMastrNummer': 'EEG996216581153', 'KwkMastrNummer': None, 'SpeMastrNummer': None, 'GenMastrNummer': 'SGE961876398816', 'BestandsanlageMastrNummer': None, 'NichtVorhandenInMigriertenEinheiten': None}

]

print(basic_units)

for basic_units_chunk in basic_units:
    # Make sure that no duplicates get inserted into database (would result in an error)
    # Only new data gets inserted or data with newer modification date gets updated

    # Remove duplicates returned from API
    print("s")

    #basic_units_chunk_unique = [unit for unit in enumerate(basic_units_chunk)]
    #print(f'basic_units_chunk_unique: {basic_units_chunk_unique}')
    basic_units_chunk_unique = [unit for n, unit in enumerate(basic_units_chunk)]
    #basic_units_chunk_unique = [unit for n, unit in enumerate(basic_units_chunk) if unit["EinheitMastrNummer"] not in [_["EinheitMastrNummer"] for _ in basic_units_chunk[n + 1:]]]


    basic_units_chunk_unique_ids = [_["EinheitMastrNummer"] for _ in basic_units_chunk_unique]

    # Find units that are already in the DB
    common_ids = [
        _.EinheitMastrNummer
        for _ in session.query(orm.BasicUnit.EinheitMastrNummer).filter(
            orm.BasicUnit.EinheitMastrNummer.in_(
                basic_units_chunk_unique_ids
            )
        )
    ]

    # Create instances for new data and for updated data
    insert = []
    updated = []
    for unit in basic_units_chunk_unique:
        # In case data for the unit already exists, only update if new data is newer
        if unit["EinheitMastrNummer"] in common_ids:
            if session.query(
                    exists().where(
                        and_(
                            orm.BasicUnit.EinheitMastrNummer
                            == unit["EinheitMastrNummer"],
                            orm.BasicUnit.DatumLetzeAktualisierung
                            < unit["DatumLetzeAktualisierung"],
                        )
                    )
            ).scalar():
                updated.append(unit)
                session.merge(orm.BasicUnit(**unit))
        # In case of new data, just insert
        else:
            insert.append(unit)
    session.bulk_save_objects([orm.BasicUnit(**u) for u in insert])
    inserted_and_updated = insert + updated

    # Submit additional data requests
    extended_data = []
    eeg_data = []
    kwk_data = []
    permit_data = []

    for basic_unit in inserted_and_updated:
        # Extended unit data
        extended_data.append(
            {
                "EinheitMastrNummer": basic_unit["EinheitMastrNummer"],
                "additional_data_id": basic_unit["EinheitMastrNummer"],
                "technology": self.unit_type_map[
                    basic_unit["Einheittyp"]
                ],
                "data_type": "unit_data",
                "request_date": datetime.datetime.now(
                    tz=datetime.timezone.utc
                ),
            }
        )

        # EEG unit data
        if basic_unit["EegMastrNummer"]:
            eeg_data.append(
                {
                    "EinheitMastrNummer": basic_unit[
                        "EinheitMastrNummer"
                    ],
                    "additional_data_id": basic_unit["EegMastrNummer"],
                    "technology": self.unit_type_map[
                        basic_unit["Einheittyp"]
                    ],
                    "data_type": "eeg_data",
                    "request_date": datetime.datetime.now(
                        tz=datetime.timezone.utc
                    ),
                }
            )

        # KWK unit data
        if basic_unit["KwkMastrNummer"]:
            kwk_data.append(
                {
                    "EinheitMastrNummer": basic_unit[
                        "EinheitMastrNummer"
                    ],
                    "additional_data_id": basic_unit["KwkMastrNummer"],
                    "technology": self.unit_type_map[
                        basic_unit["Einheittyp"]
                    ],
                    "data_type": "kwk_data",
                    "request_date": datetime.datetime.now(
                        tz=datetime.timezone.utc
                    ),
                }
            )

        # Permit unit data
        if basic_unit["GenMastrNummer"]:
            permit_data.append(
                {
                    "EinheitMastrNummer": basic_unit[
                        "EinheitMastrNummer"
                    ],
                    "additional_data_id": basic_unit["GenMastrNummer"],
                    "technology": self.unit_type_map[
                        basic_unit["Einheittyp"]
                    ],
                    "data_type": "permit_data",
                    "request_date": datetime.datetime.now(
                        tz=datetime.timezone.utc
                    ),
                }
            )