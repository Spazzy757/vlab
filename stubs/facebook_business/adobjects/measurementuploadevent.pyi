from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class MeasurementUploadEvent(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        aggregation_level: str = ...
        conversion_end_date: str = ...
        conversion_start_date: str = ...
        event_status: str = ...
        id: str = ...
        lookback_window: str = ...
        match_universe: str = ...
        partner: str = ...
        timezone: str = ...
        upload_tag: str = ...
    class AggregationLevel:
        daily: str = ...
        none: str = ...
        weekly: str = ...
    class EventStatus:
        cancelcompleted: str = ...
        canceled: str = ...
        completed: str = ...
        failed: str = ...
        started: str = ...
        uploaded: str = ...
    class LookbackWindow:
        days30: str = ...
        days45: str = ...
        days60: str = ...
        days90: str = ...
    class MatchUniverse:
        full: str = ...
        pii: str = ...
        pixel: str = ...
    class Timezone:
        tz_africa_accra: str = ...
        tz_africa_cairo: str = ...
        tz_africa_casablanca: str = ...
        tz_africa_johannesburg: str = ...
        tz_africa_lagos: str = ...
        tz_africa_nairobi: str = ...
        tz_africa_tunis: str = ...
        tz_america_anchorage: str = ...
        tz_america_argentina_buenos_aires: str = ...
        tz_america_argentina_salta: str = ...
        tz_america_argentina_san_luis: str = ...
        tz_america_asuncion: str = ...
        tz_america_atikokan: str = ...
        tz_america_belem: str = ...
        tz_america_blanc_sablon: str = ...
        tz_america_bogota: str = ...
        tz_america_campo_grande: str = ...
        tz_america_caracas: str = ...
        tz_america_chicago: str = ...
        tz_america_costa_rica: str = ...
        tz_america_dawson: str = ...
        tz_america_dawson_creek: str = ...
        tz_america_denver: str = ...
        tz_america_detroit: str = ...
        tz_america_edmonton: str = ...
        tz_america_el_salvador: str = ...
        tz_america_guatemala: str = ...
        tz_america_guayaquil: str = ...
        tz_america_halifax: str = ...
        tz_america_hermosillo: str = ...
        tz_america_iqaluit: str = ...
        tz_america_jamaica: str = ...
        tz_america_la_paz: str = ...
        tz_america_lima: str = ...
        tz_america_los_angeles: str = ...
        tz_america_managua: str = ...
        tz_america_mazatlan: str = ...
        tz_america_mexico_city: str = ...
        tz_america_montevideo: str = ...
        tz_america_nassau: str = ...
        tz_america_new_york: str = ...
        tz_america_noronha: str = ...
        tz_america_panama: str = ...
        tz_america_phoenix: str = ...
        tz_america_port_of_spain: str = ...
        tz_america_puerto_rico: str = ...
        tz_america_rainy_river: str = ...
        tz_america_regina: str = ...
        tz_america_santiago: str = ...
        tz_america_santo_domingo: str = ...
        tz_america_sao_paulo: str = ...
        tz_america_st_johns: str = ...
        tz_america_tegucigalpa: str = ...
        tz_america_tijuana: str = ...
        tz_america_toronto: str = ...
        tz_america_vancouver: str = ...
        tz_america_winnipeg: str = ...
        tz_asia_amman: str = ...
        tz_asia_baghdad: str = ...
        tz_asia_bahrain: str = ...
        tz_asia_bangkok: str = ...
        tz_asia_beirut: str = ...
        tz_asia_colombo: str = ...
        tz_asia_dhaka: str = ...
        tz_asia_dubai: str = ...
        tz_asia_gaza: str = ...
        tz_asia_hong_kong: str = ...
        tz_asia_ho_chi_minh: str = ...
        tz_asia_irkutsk: str = ...
        tz_asia_jakarta: str = ...
        tz_asia_jayapura: str = ...
        tz_asia_jerusalem: str = ...
        tz_asia_kamchatka: str = ...
        tz_asia_karachi: str = ...
        tz_asia_kathmandu: str = ...
        tz_asia_kolkata: str = ...
        tz_asia_krasnoyarsk: str = ...
        tz_asia_kuala_lumpur: str = ...
        tz_asia_kuwait: str = ...
        tz_asia_magadan: str = ...
        tz_asia_makassar: str = ...
        tz_asia_manila: str = ...
        tz_asia_muscat: str = ...
        tz_asia_nicosia: str = ...
        tz_asia_omsk: str = ...
        tz_asia_qatar: str = ...
        tz_asia_riyadh: str = ...
        tz_asia_seoul: str = ...
        tz_asia_shanghai: str = ...
        tz_asia_singapore: str = ...
        tz_asia_taipei: str = ...
        tz_asia_tokyo: str = ...
        tz_asia_vladivostok: str = ...
        tz_asia_yakutsk: str = ...
        tz_asia_yekaterinburg: str = ...
        tz_atlantic_azores: str = ...
        tz_atlantic_canary: str = ...
        tz_atlantic_reykjavik: str = ...
        tz_australia_broken_hill: str = ...
        tz_australia_melbourne: str = ...
        tz_australia_perth: str = ...
        tz_australia_sydney: str = ...
        tz_europe_amsterdam: str = ...
        tz_europe_athens: str = ...
        tz_europe_belgrade: str = ...
        tz_europe_berlin: str = ...
        tz_europe_bratislava: str = ...
        tz_europe_brussels: str = ...
        tz_europe_bucharest: str = ...
        tz_europe_budapest: str = ...
        tz_europe_copenhagen: str = ...
        tz_europe_dublin: str = ...
        tz_europe_helsinki: str = ...
        tz_europe_istanbul: str = ...
        tz_europe_kaliningrad: str = ...
        tz_europe_kiev: str = ...
        tz_europe_lisbon: str = ...
        tz_europe_ljubljana: str = ...
        tz_europe_london: str = ...
        tz_europe_luxembourg: str = ...
        tz_europe_madrid: str = ...
        tz_europe_malta: str = ...
        tz_europe_moscow: str = ...
        tz_europe_oslo: str = ...
        tz_europe_paris: str = ...
        tz_europe_prague: str = ...
        tz_europe_riga: str = ...
        tz_europe_rome: str = ...
        tz_europe_samara: str = ...
        tz_europe_sarajevo: str = ...
        tz_europe_skopje: str = ...
        tz_europe_sofia: str = ...
        tz_europe_stockholm: str = ...
        tz_europe_tallinn: str = ...
        tz_europe_vienna: str = ...
        tz_europe_vilnius: str = ...
        tz_europe_warsaw: str = ...
        tz_europe_zagreb: str = ...
        tz_europe_zurich: str = ...
        tz_indian_maldives: str = ...
        tz_indian_mauritius: str = ...
        tz_num_timezones: str = ...
        tz_pacific_auckland: str = ...
        tz_pacific_easter: str = ...
        tz_pacific_galapagos: str = ...
        tz_pacific_honolulu: str = ...
    @classmethod
    def get_endpoint(cls): ...
    def api_create(self, parent_id: Any, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_update(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
