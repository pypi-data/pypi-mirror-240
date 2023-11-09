# Apache License 2.0

import pytest

import pathlib

from ostk.core.filesystem import Path
from ostk.core.filesystem import File


@pytest.fixture
def data_directory_path() -> str:
    return f"{pathlib.Path(__file__).parent.absolute()}/data"


@pytest.fixture
def cdm_file(data_directory_path: str) -> File:
    return File.path(Path.parse(f"{data_directory_path}/cdm.json"))


@pytest.fixture
def cdm_spacetrack_dictionary() -> dict:
    return {
        "CONSTELLATION": "Loft Orbital Solutions",
        "CDM_ID": "406320986",
        "FILENAME": "000048911_conj_000015331_2022361132859_62880.xml",
        "INSERT_EPOCH": "2022-12-25T03:16:57",
        "CCSDS_CDM_VERS": "1.0",
        "CREATION_DATE": "2022-12-25T00:33:16.000000",
        "ORIGINATOR": "CSpOC",
        "MESSAGE_FOR": "YAM-2",
        "MESSAGE_ID": "000048911_conj_000015331_2022361132859_35900400162880",
        # 'COMMENT_EMERGENCY_REPORTABLE': None,
        "TCA": "2022-12-27T13:28:59.516000",
        "MISS_DISTANCE": "974",
        "MISS_DISTANCE_UNIT": "m",
        "RELATIVE_SPEED": "2604",
        "RELATIVE_SPEED_UNIT": "m/s",
        "RELATIVE_POSITION_R": "-170.9",
        "RELATIVE_POSITION_R_UNIT": "m",
        "RELATIVE_POSITION_T": "-945",
        "RELATIVE_POSITION_T_UNIT": "m",
        "RELATIVE_POSITION_N": "165",
        "RELATIVE_POSITION_N_UNIT": "m",
        "RELATIVE_VELOCITY_R": "0.3",
        "RELATIVE_VELOCITY_R_UNIT": "m/s",
        "RELATIVE_VELOCITY_T": "-448.1",
        "RELATIVE_VELOCITY_T_UNIT": "m/s",
        "RELATIVE_VELOCITY_N": "-2566.1",
        "RELATIVE_VELOCITY_N_UNIT": "m/s",
        "COMMENT_SCREENING_OPTION": "Screening Option = Covariance",
        "COLLISION_PROBABILITY": "5.162516e-16",
        "COLLISION_PROBABILITY_METHOD": "FOSTER-1992",
        # 'SAT1_COMMENT_SCREENING_DATA_SOURCE': None,
        "SAT1_OBJECT": "OBJECT1",
        "SAT1_OBJECT_DESIGNATOR": "48911",
        "SAT1_CATALOG_NAME": "SATCAT",
        "SAT1_OBJECT_NAME": "YAM-2",
        "SAT1_INTERNATIONAL_DESIGNATOR": "2021-059AJ",
        "SAT1_OBJECT_TYPE": "PAYLOAD",
        "SAT1_OPERATOR_CONTACT_POSITION": "https: //www.space-track.org/expandedspacedata/query/class/organization/object/~~48911/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT1_OPERATOR_ORGANIZATION": "Loft Orbital Solutions",
        "SAT1_OPERATOR_PHONE": "https://www.space-track.org/expandedspacedata/query/class/organization/object/~~48911/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT1_OPERATOR_EMAIL": "https://www.space-track.org/expandedspacedata/query/class/organization/object/~~48911/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT1_EPHEMERIS_NAME": "NONE",
        "SAT1_COVARIANCE_METHOD": "CALCULATED",
        "SAT1_MANEUVERABLE": "N/A",
        "SAT1_REF_FRAME": "ITRF",
        "SAT1_GRAVITY_MODEL": "EGM-96: 36D 36O",
        "SAT1_ATMOSPHERIC_MODEL": "JBH09",
        "SAT1_N_BODY_PERTURBATIONS": "MOON,SUN",
        "SAT1_SOLAR_RAD_PRESSURE": "YES",
        "SAT1_EARTH_TIDES": "YES",
        "SAT1_INTRACK_THRUST": "NO",
        "SAT1_COMMENT_COVARIANCE_SCALE_FACTOR": "Covariance Scale Factor = 1.000000",
        "SAT1_COMMENT_EXCLUSION_VOLUME_RADIUS": "Exclusion Volume Radius = 5.000000 [m]",
        "SAT1_TIME_LASTOB_START": "2022-12-24T00:33:16.431000",
        "SAT1_TIME_LASTOB_END": "2022-12-25T00:33:16.431000",
        "SAT1_RECOMMENDED_OD_SPAN": "3.3",
        "SAT1_RECOMMENDED_OD_SPAN_UNIT": "d",
        "SAT1_ACTUAL_OD_SPAN": "3.3",
        "SAT1_ACTUAL_OD_SPAN_UNIT": "d",
        "SAT1_OBS_AVAILABLE": "100",
        "SAT1_OBS_USED": "100",
        "SAT1_RESIDUALS_ACCEPTED": "100",
        "SAT1_RESIDUALS_ACCEPTED_UNIT": "%",
        "SAT1_WEIGHTED_RMS": "0.991",
        "SAT1_COMMENT_APOGEE": "Apogee Altitude = 541   [km]",
        "SAT1_COMMENT_PERIGEE": "Perigee Altitude = 509   [km]",
        "SAT1_COMMENT_INCLINATION": "Inclination = 97.6  [deg]",
        # 'SAT1_COMMENT_OPERATOR_HARD_BODY_RADIUS': None,
        "SAT1_AREA_PC": "0.4374",
        "SAT1_AREA_PC_UNIT": "m**2",
        "SAT1_CD_AREA_OVER_MASS": "0.022156960363",
        "SAT1_CD_AREA_OVER_MASS_UNIT": "m**2/kg",
        "SAT1_CR_AREA_OVER_MASS": "0.003818998866",
        "SAT1_CR_AREA_OVER_MASS_UNIT": "m**2/kg",
        "SAT1_THRUST_ACCELERATION": "0",
        "SAT1_THRUST_ACCELERATION_UNIT": "m/s**2",
        "SAT1_SEDR": "0.00210992",
        "SAT1_SEDR_UNIT": "W/kg",
        "SAT1_X": "-4988.150232",
        "SAT1_X_UNIT": "km",
        "SAT1_Y": "-1691.825955",
        "SAT1_Y_UNIT": "km",
        "SAT1_Z": "-4469.421482",
        "SAT1_Z_UNIT": "km",
        "SAT1_X_DOT": "-5.122248844",
        "SAT1_X_DOT_UNIT": "km/s",
        "SAT1_Y_DOT": "0.054300816",
        "SAT1_Y_DOT_UNIT": "km/s",
        "SAT1_Z_DOT": "5.699434412",
        "SAT1_Z_DOT_UNIT": "km/s",
        "SAT1_COMMENT_DCP_DENSITY_FORECAST_UNCERTAINTY": "DCP Density Forecast Uncertainty = 2.290890030000000E-01",
        "SAT1_COMMENT_DCP_SENSITIVITY_VECTOR_POSITION": "DCP Sensitivity Vector RTN Pos = -1.636151334480493E+02 2.601909818284176E+04  -2.915438070510799E+00 [m]",
        "SAT1_COMMENT_DCP_SENSITIVITY_VECTOR_VELOCITY": "DCP Sensitivity Vector RTN Vel = -2.867115178813268E+01 1.435509187157564E-01  -1.287417157042207E-02 [m/sec]",
        "SAT1_CR_R": "1484.661743393455",
        "SAT1_CR_R_UNIT": "m**2",
        "SAT1_CT_R": "-231060.2636731259",
        "SAT1_CT_R_UNIT": "m**2",
        "SAT1_CT_T": "37086743.11901508",
        "SAT1_CT_T_UNIT": "m**2",
        "SAT1_CN_R": "24.40770013207214",
        "SAT1_CN_R_UNIT": "m**2",
        "SAT1_CN_T": "-4434.047461592475",
        "SAT1_CN_T_UNIT": "m**2",
        "SAT1_CN_N": "218.20805984514",
        "SAT1_CN_N_UNIT": "m**2",
        "SAT1_CRDOT_R": "254.5977232921239",
        "SAT1_CRDOT_R_UNIT": "m**2/s",
        "SAT1_CRDOT_T": "-40867.38377954393",
        "SAT1_CRDOT_T_UNIT": "m**2/s",
        "SAT1_CRDOT_N": "4.871821743729464",
        "SAT1_CRDOT_N_UNIT": "m**2/s",
        "SAT1_CRDOT_RDOT": "45.03346700955843",
        "SAT1_CRDOT_RDOT_UNIT": "m**2/s**2",
        "SAT1_CTDOT_R": "-1.311352116787324",
        "SAT1_CTDOT_R_UNIT": "m**2/s",
        "SAT1_CTDOT_T": "202.8294875506834",
        "SAT1_CTDOT_T_UNIT": "m**2/s",
        "SAT1_CTDOT_N": "-0.02128325918265576",
        "SAT1_CTDOT_N_UNIT": "m**2/s",
        "SAT1_CTDOT_RDOT": "-0.2234874511731791",
        "SAT1_CTDOT_RDOT_UNIT": "m**2/s**2",
        "SAT1_CTDOT_TDOT": "0.001160151615053103",
        "SAT1_CTDOT_TDOT_UNIT": "m**2/s**2",
        "SAT1_CNDOT_R": "0.1154310435542667",
        "SAT1_CNDOT_R_UNIT": "m**2/s",
        "SAT1_CNDOT_T": "-18.32204260863709",
        "SAT1_CNDOT_T_UNIT": "m**2/s",
        "SAT1_CNDOT_N": "-0.0533676327904924",
        "SAT1_CNDOT_N_UNIT": "m**2/s",
        "SAT1_CNDOT_RDOT": "0.02020021081010548",
        "SAT1_CNDOT_RDOT_UNIT": "m**2/s**2",
        "SAT1_CNDOT_TDOT": "-0.0001013570378449393",
        "SAT1_CNDOT_TDOT_UNIT": "m**2/s**2",
        "SAT1_CNDOT_NDOT": "0.00004789528123726022",
        "SAT1_CNDOT_NDOT_UNIT": "m**2/s**2",
        "SAT1_CDRG_R": "0",
        "SAT1_CDRG_R_UNIT": "m**3/kg",
        "SAT1_CDRG_T": "0",
        "SAT1_CDRG_T_UNIT": "m**3/kg",
        "SAT1_CDRG_N": "0",
        "SAT1_CDRG_N_UNIT": "m**3/kg",
        "SAT1_CDRG_RDOT": "0",
        "SAT1_CDRG_RDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CDRG_TDOT": "0",
        "SAT1_CDRG_TDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CDRG_NDOT": "0",
        "SAT1_CDRG_NDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CDRG_DRG": "0",
        "SAT1_CDRG_DRG_UNIT": "m**4/kg**2",
        "SAT1_CSRP_R": "0",
        "SAT1_CSRP_R_UNIT": "m**3/kg",
        "SAT1_CSRP_T": "0",
        "SAT1_CSRP_T_UNIT": "m**3/kg",
        "SAT1_CSRP_N": "0",
        "SAT1_CSRP_N_UNIT": "m**3/kg",
        "SAT1_CSRP_RDOT": "0",
        "SAT1_CSRP_RDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CSRP_TDOT": "0",
        "SAT1_CSRP_TDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CSRP_NDOT": "0",
        "SAT1_CSRP_NDOT_UNIT": "m**3/(kg*s)",
        "SAT1_CSRP_DRG": "0",
        "SAT1_CSRP_DRG_UNIT": "m**4/kg**2",
        "SAT1_CSRP_SRP": "0",
        "SAT1_CSRP_SRP_UNIT": "m**4/kg**2",
        # 'SAT2_COMMENT_SCREENING_DATA_SOURCE': None,
        "SAT2_OBJECT": "OBJECT2",
        "SAT2_OBJECT_DESIGNATOR": "15331",
        "SAT2_CATALOG_NAME": "SATCAT",
        "SAT2_OBJECT_NAME": "COSMOS 1602",
        "SAT2_INTERNATIONAL_DESIGNATOR": "1984-105A",
        "SAT2_OBJECT_TYPE": "PAYLOAD",
        "SAT2_OPERATOR_CONTACT_POSITION": "https://www.space-track.org/expandedspacedata/query/class/organization/object/~~15331/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT2_OPERATOR_ORGANIZATION": "- Whitelist-Show public CDMs",
        "SAT2_OPERATOR_PHONE": "https://www.space-track.org/expandedspacedata/query/class/organization/object/~~15331/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT2_OPERATOR_EMAIL": "https://www.space-track.org/expandedspacedata/query/class/organization/object/~~15331/orderby/ORG_NAME,INFO_ID/format/html/emptyresult/show/",
        "SAT2_EPHEMERIS_NAME": "NONE",
        "SAT2_COVARIANCE_METHOD": "CALCULATED",
        "SAT2_MANEUVERABLE": "N/A",
        "SAT2_REF_FRAME": "ITRF",
        "SAT2_GRAVITY_MODEL": "EGM-96: 36D 36O",
        "SAT2_ATMOSPHERIC_MODEL": "JBH09",
        "SAT2_N_BODY_PERTURBATIONS": "MOON,SUN",
        "SAT2_SOLAR_RAD_PRESSURE": "YES",
        "SAT2_EARTH_TIDES": "YES",
        "SAT2_INTRACK_THRUST": "NO",
        "SAT2_COMMENT_COVARIANCE_SCALE_FACTOR": "Covariance Scale Factor = 1.000000",
        "SAT2_COMMENT_EXCLUSION_VOLUME_RADIUS": "Exclusion Volume Radius = 5.000000 [m]",
        "SAT2_TIME_LASTOB_START": "2022-12-24T00:33:16.078000",
        "SAT2_TIME_LASTOB_END": "2022-12-25T00:33:16.078000",
        "SAT2_RECOMMENDED_OD_SPAN": "3.16",
        "SAT2_RECOMMENDED_OD_SPAN_UNIT": "d",
        "SAT2_ACTUAL_OD_SPAN": "3.16",
        "SAT2_ACTUAL_OD_SPAN_UNIT": "d",
        "SAT2_OBS_AVAILABLE": "106",
        "SAT2_OBS_USED": "106",
        "SAT2_RESIDUALS_ACCEPTED": "98.8",
        "SAT2_RESIDUALS_ACCEPTED_UNIT": "%",
        "SAT2_WEIGHTED_RMS": "0.872",
        "SAT2_COMMENT_APOGEE": "Apogee Altitude = 541   [km]",
        "SAT2_COMMENT_PERIGEE": "Perigee Altitude = 505   [km]",
        "SAT2_COMMENT_INCLINATION": "Inclination = 82.5  [deg]",
        # 'SAT2_COMMENT_OPERATOR_HARD_BODY_RADIUS': None,
        "SAT2_AREA_PC": "12.3163",
        "SAT2_AREA_PC_UNIT": "m**2",
        "SAT2_CD_AREA_OVER_MASS": "0.018619765396",
        "SAT2_CD_AREA_OVER_MASS_UNIT": "m**2/kg",
        "SAT2_CR_AREA_OVER_MASS": "0.010453768255",
        "SAT2_CR_AREA_OVER_MASS_UNIT": "m**2/kg",
        "SAT2_THRUST_ACCELERATION": "0",
        "SAT2_THRUST_ACCELERATION_UNIT": "m/s**2",
        "SAT2_SEDR": "0.00170015",
        "SAT2_SEDR_UNIT": "W/kg",
        "SAT2_X": "-4987.438723",
        "SAT2_X_UNIT": "km",
        "SAT2_Y": "-1691.585637",
        "SAT2_Y_UNIT": "km",
        "SAT2_Z": "-4470.042362",
        "SAT2_Z_UNIT": "km",
        "SAT2_X_DOT": "-4.287315771",
        "SAT2_X_DOT_UNIT": "km/s",
        "SAT2_Y_DOT": "-2.413206407",
        "SAT2_Y_DOT_UNIT": "km/s",
        "SAT2_Z_DOT": "5.701228642",
        "SAT2_Z_DOT_UNIT": "km/s",
        "SAT2_COMMENT_DCP_DENSITY_FORECAST_UNCERTAINTY": "DCP Density Forecast Uncertainty = 2.278816440000000E-01",
        "SAT2_COMMENT_DCP_SENSITIVITY_VECTOR_POSITION": "DCP Sensitivity Vector RTN Pos = -1.335248493856891E+02 2.014718153017551E+04  5.205380905166459E+00  [m]",
        "SAT2_COMMENT_DCP_SENSITIVITY_VECTOR_VELOCITY": "DCP Sensitivity Vector RTN Vel = -2.220377271541959E+01 1.148351592111829E-01  7.451338419472125E-03  [m/sec]",
        "SAT2_CR_R": "1462.221563767092",
        "SAT2_CR_R_UNIT": "m**2",
        "SAT2_CT_R": "-144222.644159393",
        "SAT2_CT_R_UNIT": "m**2",
        "SAT2_CT_T": "21679306.07289715",
        "SAT2_CT_T_UNIT": "m**2",
        "SAT2_CN_R": "-225.1714423010423",
        "SAT2_CN_R_UNIT": "m**2",
        "SAT2_CN_T": "5814.738923198461",
        "SAT2_CN_T_UNIT": "m**2",
        "SAT2_CN_N": "123.073683061929",
        "SAT2_CN_N_UNIT": "m**2",
        "SAT2_CRDOT_R": "158.6587476294616",
        "SAT2_CRDOT_R_UNIT": "m**2/s",
        "SAT2_CRDOT_T": "-23891.76994311345",
        "SAT2_CRDOT_T_UNIT": "m**2/s",
        "SAT2_CRDOT_N": "-6.293842325288276",
        "SAT2_CRDOT_N_UNIT": "m**2/s",
        "SAT2_CRDOT_RDOT": "26.33020326928547",
        "SAT2_CRDOT_RDOT_UNIT": "m**2/s**2",
        "SAT2_CTDOT_R": "-1.383068369249745",
        "SAT2_CTDOT_R_UNIT": "m**2/s",
        "SAT2_CTDOT_T": "124.4044756204814",
        "SAT2_CTDOT_T_UNIT": "m**2/s",
        "SAT2_CTDOT_N": "0.2395121366072169",
        "SAT2_CTDOT_N_UNIT": "m**2/s",
        "SAT2_CTDOT_RDOT": "-0.1367881107104898",
        "SAT2_CTDOT_RDOT_UNIT": "m**2/s**2",
        "SAT2_CTDOT_TDOT": "0.001327776662852765",
        "SAT2_CTDOT_TDOT_UNIT": "m**2/s**2",
        "SAT2_CNDOT_R": "-0.01076109815513279",
        "SAT2_CNDOT_R_UNIT": "m**2/s",
        "SAT2_CNDOT_T": "8.261715904589654",
        "SAT2_CNDOT_T_UNIT": "m**2/s",
        "SAT2_CNDOT_N": "-0.00996848842170098",
        "SAT2_CNDOT_N_UNIT": "m**2/s",
        "SAT2_CNDOT_RDOT": "-0.009119499172200366",
        "SAT2_CNDOT_RDOT_UNIT": "m**2/s**2",
        "SAT2_CNDOT_TDOT": "-0.000001041891040556171",
        "SAT2_CNDOT_TDOT_UNIT": "m**2/s**2",
        "SAT2_CNDOT_NDOT": "0.00004403494150689736",
        "SAT2_CNDOT_NDOT_UNIT": "m**2/s**2",
        "SAT2_CDRG_R": "0",
        "SAT2_CDRG_R_UNIT": "m**3/kg",
        "SAT2_CDRG_T": "0",
        "SAT2_CDRG_T_UNIT": "m**3/kg",
        "SAT2_CDRG_N": "0",
        "SAT2_CDRG_N_UNIT": "m**3/kg",
        "SAT2_CDRG_RDOT": "0",
        "SAT2_CDRG_RDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CDRG_TDOT": "0",
        "SAT2_CDRG_TDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CDRG_NDOT": "0",
        "SAT2_CDRG_NDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CDRG_DRG": "0",
        "SAT2_CDRG_DRG_UNIT": "m**4/kg**2",
        "SAT2_CSRP_R": "0",
        "SAT2_CSRP_R_UNIT": "m**3/kg",
        "SAT2_CSRP_T": "0",
        "SAT2_CSRP_T_UNIT": "m**3/kg",
        "SAT2_CSRP_N": "0",
        "SAT2_CSRP_N_UNIT": "m**3/kg",
        "SAT2_CSRP_RDOT": "0",
        "SAT2_CSRP_RDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CSRP_TDOT": "0",
        "SAT2_CSRP_TDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CSRP_NDOT": "0",
        "SAT2_CSRP_NDOT_UNIT": "m**3/(kg*s)",
        "SAT2_CSRP_DRG": "0",
        "SAT2_CSRP_DRG_UNIT": "m**4/kg**2",
        "SAT2_CSRP_SRP": "0",
        "SAT2_CSRP_SRP_UNIT": "m**4/kg**2",
        "GID": "682",
    }
