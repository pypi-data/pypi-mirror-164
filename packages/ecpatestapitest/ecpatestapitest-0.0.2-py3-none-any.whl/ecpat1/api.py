"""Define an object to interact with the REST API."""
from ast import For
import asyncio
from datetime import date
from http.client import SWITCHING_PROTOCOLS
import logging
from typing import Any, Dict, List, Optional, cast

from aiohttp import ClientSession, ClientTimeout
from aiohttp.client_exceptions import ClientError

import requests
import json
# from const import LOGGER,DEFAULT_API_VERSION
# from errors import RequestError

from .const import DEFAULT_API_VERSION, LOGGER
from .errors import RequestError


REST_API_BASE = "https://apitest.ecowitt.net"

GW11268_API_LIVEDATA = "get_livedata_info"
GW11268_API_UNIT = "get_units_info"
GW11268_API_VER = "get_version"
GW11268_API_SENID_1		 = "get_sensors_info?page=1"
GW11268_API_SENID_2		 = "get_sensors_info?page=2"

DEFAULT_LIMIT = 288
DEFAULT_TIMEOUT = 10



class API:
    """Define the API object."""

    def __init__(
        self,
        application_key: str,
        api_key: str,
        ip: str,
        *,
        api_version: int = DEFAULT_API_VERSION,
        logger: logging.Logger = LOGGER,
        session: Optional[ClientSession] = None,
    ) -> None:
        """Initialize."""
        self._api_key: str = api_key
        self._ip: str = ip
        self._api_version: int = api_version
        self._application_key: str = application_key
        self._logger = logger
        self._session: Optional[ClientSession] = session

    async def _request(
        self, method: str, endpoint: str, **kwargs: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """Make a request against the API."""
        # 
        await asyncio.sleep(1)

        url = f"{REST_API_BASE}/api/v3/{endpoint}"

        kwargs.setdefault("params", {})
        kwargs["params"]["application_key"] = self._application_key
        kwargs["params"]["api_key"] = self._api_key

        use_running_session = self._session and not self._session.closed

        if use_running_session:
            session = self._session
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))

        assert session
        # print(url)
        # print(kwargs)
        try:
            async with session.request(method, url, **kwargs) as resp:
                resp.raise_for_status()
                data = await resp.json()
                # print(data)
        except ClientError as err:
            # print(err)
            raise RequestError(f"Error requesting data from {url}: {err}") from err
        finally:
            if not use_running_session:
                await session.close()
        self._logger.debug("Received data for %s: %s", endpoint, data)

        return cast(List[Dict[str, Any]], data)

    async def get_devices(self) -> List[Dict[str, Any]]:
        """Get all devices associated with an API key."""
        return await self._request("get", "device/list")

    async def get_data_real_time(
        self,
        mac_address: str,
    ) -> list:
        """Get details of a device by MAC address."""
        params: Dict[str, Any] = {"mac": mac_address,"call_back":"all"}
        resdata=await self._request("get", f"device/real_time/", params=params)
        
        defu={}
        resdata=resdata.get("data",defu)
        self._logger.info("Received data for : %s", resdata)
        # self._logger.info("temperature : %s", outdoor.get("tempesrature").get("value","--"))
        ld_soil=[]
        ld_tempch=[]
        ld_humich=[]
        ld_onlytempch=[]
        ld_leafch=[]  
        for i in range(8):
            ld_soil.append("--")
            ld_tempch.append("--")
            ld_humich.append("--")
            ld_onlytempch.append("--")
            ld_leafch.append("--")
        resjson={}
        for x in resdata.items():  
            print("%s=%s",x[0],x[1])
            if x[0]=="outdoor":
                if "temperature" in x[1]:
                    resjson["tempf"]=x[1].get("temperature").get("value")
                if "feels_like" in x[1]:
                    resjson["feellike"]=x[1].get("feels_like").get("value")
                if "dew_point" in x[1]:
                    resjson["dewpoint"]=x[1].get("dew_point").get("value")
                if "humidity" in x[1]:
                    resjson["humidity"]=x[1].get("humidity").get("value")
                continue
            if x[0]=="indoor":
                if "temperature" in x[1]:
                    resjson["tempinf"]=x[1].get("temperature").get("value")
                if "humidity" in x[1]:
                    resjson["humidityin"]=x[1].get("humidity").get("value")
                continue
            if x[0]=="solar_and_uvi":
                if "solar" in x[1]:
                    resjson["solarradiation"]=x[1].get("solar").get("value")
                if "uvi" in x[1]:
                    resjson["uv"]=x[1].get("uvi").get("value")
                continue
            if x[0]=="rainfall":
                if "rain_rate" in x[1]:
                    resjson["rainratein"]=x[1].get("rain_rate").get("value")
                if "event" in x[1]:
                    resjson["eventrainin"]=x[1].get("event").get("value")
                if "daily" in x[1]:
                    resjson["dailyrainin"]=x[1].get("daily").get("value")
                if "weekly" in x[1]:
                    resjson["weeklyrainin"]=x[1].get("weekly").get("value")
                if "monthly" in x[1]:
                    resjson["monthlyrainin"]=x[1].get("monthly").get("value")
                if "yearly" in x[1]:
                    resjson["yearlyrainin"]=x[1].get("yearly").get("value")
                continue
            if x[0]=="rainfall_piezo":
                if "rain_rate" in x[1]:
                    resjson["rrain_piezo"]=x[1].get("rain_rate").get("value")
                if "event" in x[1]:
                    resjson["erain_piezo"]=x[1].get("event").get("value")
                if "daily" in x[1]:
                    resjson["drain_piezo"]=x[1].get("daily").get("value")
                if "weekly" in x[1]:
                    resjson["wrain_piezo"]=x[1].get("weekly").get("value")
                if "monthly" in x[1]:
                    resjson["mrain_piezo"]=x[1].get("monthly").get("value")
                if "yearly" in x[1]:
                    resjson["yrain_piezo"]=x[1].get("yearly").get("value")
                continue
            if x[0]=="wind":
                if "wind_direction" in x[1]:
                    resjson["winddir"]=x[1].get("wind_direction").get("value")
                if "wind_speed" in x[1]:
                    resjson["windspeedmph"]=x[1].get("wind_speed").get("value")
                if "wind_gust" in x[1]:
                    resjson["windgustmph"]=x[1].get("wind_gust").get("value")
                continue
            if x[0]=="pressure":
                if "relative" in x[1]:
                    resjson["baromrelin"]=x[1].get("relative").get("value")
                if "absolute" in x[1]:
                    resjson["baromabsin"]=x[1].get("absolute").get("value")
                continue
            if x[0]=="lightning":
                if "lightning" in x[1]:
                    resjson["lightning"]=x[1].get("distance").get("value")
                    resjson["lightning_time"]=x[1].get("distance").get("time")
                if "absolute" in x[1]:
                    resjson["lightning_num"]=x[1].get("count").get("value")
                continue
            if x[0]=="indoor_co2":
                if "co2" in x[1]:
                    resjson["co2in"]=x[1].get("co2").get("value")
                if "24_hours_average" in x[1]:
                    resjson["co2in_24h"]=x[1].get("24_hours_average").get("value")
                continue
            if x[0]=="co2_aqi_combo":
                if "co2" in x[1]:
                    resjson["co2"]=x[1].get("co2").get("value")
                if "24_hours_average" in x[1]:
                    resjson["co2_24h"]=x[1].get("24_hours_average").get("value")  
                continue
            if x[0]=="pm25_aqi_combo":
                if "real_time_aqi" in x[1]:
                    resjson["pm25_aqi_co2"]=x[1].get("real_time_aqi").get("value")
                if "pm25" in x[1]:
                    resjson["pm25_co2"]=x[1].get("pm25").get("value")
                if "24_hours_aqi" in x[1]:
                    resjson["pm25_24h_co2"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="pm10_aqi_combo":
                if "real_time_aqi" in x[1]:
                    resjson["pm10_aqi_co2"]=x[1].get("real_time_aqi").get("value")
                if "pm10" in x[1]:
                    resjson["pm10_co2"]=x[1].get("pm10").get("value")
                if "24_hours_aqi" in x[1]:
                    resjson["pm10_24h_co2"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="t_rh_aqi_combo":
                if "temperature" in x[1]:
                    resjson["tf_co2"]=x[1].get("temperature").get("value")
                if "humidity" in x[1]:
                    resjson["humi_co2"]=x[1].get("humidity").get("value")
                continue
            if x[0]=="water_leak":
                if "leak_ch1" in x[1]:
                    resjson["leak_ch1"]=x[1].get("leak_ch1").get("value")
                if "leak_ch2" in x[1]:
                    resjson["leak_ch2"]=x[1].get("leak_ch2").get("value")
                if "leak_ch3" in x[1]:
                    resjson["leak_ch3"]=x[1].get("leak_ch3").get("value")
                if "leak_ch4" in x[1]:
                    resjson["leak_ch4"]=x[1].get("leak_ch4").get("value")
                continue
            if x[0]=="pm25_ch1":
                resjson["pm25_aqi_ch1"]=x[1].get("real_time_aqi").get("value")
                resjson["pm25_ch1"]=x[1].get("pm25").get("value")
                resjson["pm25_avg_24h_ch1"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="pm25_ch2":
                resjson["pm25_aqi_ch2"]=x[1].get("real_time_aqi").get("value")
                resjson["pm25_ch2"]=x[1].get("pm25").get("value")
                resjson["pm25_avg_24h_ch2"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="pm25_ch3":
                resjson["pm25_aqi_ch3"]=x[1].get("real_time_aqi").get("value")
                resjson["pm25_ch3"]=x[1].get("pm25").get("value")
                resjson["pm25_avg_24h_ch3"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="pm25_ch4":
                resjson["pm25_aqi_ch4"]=x[1].get("real_time_aqi").get("value")
                resjson["pm25_ch4"]=x[1].get("pm25").get("value")
                resjson["pm25_avg_24h_ch4"]=x[1].get("24_hours_aqi").get("value")
                continue
            if x[0]=="temp_and_humidity_ch1":
                ld_tempch[0]=x[1].get("temperature").get("value")
                ld_humich[0]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch2":
                ld_tempch[1]=x[1].get("temperature").get("value")
                ld_humich[1]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch3":
                ld_tempch[2]=x[1].get("temperature").get("value")
                ld_humich[2]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch4":
                ld_tempch[3]=x[1].get("temperature").get("value")
                ld_humich[3]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch5":
                ld_tempch[4]=x[1].get("temperature").get("value")
                ld_humich[4]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch6":
                ld_tempch[5]=x[1].get("temperature").get("value")
                ld_humich[5]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch7":
                ld_tempch[6]=x[1].get("temperature").get("value")
                ld_humich[6]=x[1].get("humidity").get("value")
                continue
            if x[0]=="temp_and_humidity_ch8":
                ld_tempch[7]=x[1].get("temperature").get("value")
                ld_humich[7]=x[1].get("humidity").get("value")
                continue
            if x[0]=="soil_ch1":
                ld_soil[0]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch2":
                ld_soil[1]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch3":
                ld_soil[2]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch4":
                ld_soil[3]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch5":
                ld_soil[4]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch6":
                ld_soil[5]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch7":
                ld_soil[6]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="soil_ch8":
                ld_soil[7]=x[1].get("soilmoisture").get("value")
                continue
            if x[0]=="temp_ch1":
                ld_onlytempch[0]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch2":
                ld_onlytempch[1]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch3":
                ld_onlytempch[2]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch4":
                ld_onlytempch[3]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch5":
                ld_onlytempch[4]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch6":
                ld_onlytempch[5]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch7":
                ld_onlytempch[6]=x[1].get("temperature").get("value")
                continue
            if x[0]=="temp_ch8":
                ld_onlytempch[7]=x[1].get("temperature").get("value")
                continue
            if x[0]=="leaf_ch1":
                ld_leafch[0]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch2":
                ld_leafch[1]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch3":
                ld_leafch[2]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch4":
                ld_leafch[3]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch5":
                ld_leafch[4]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch6":
                ld_leafch[5]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch7":
                ld_leafch[6]=x[1].get("leaf_wetness").get("value")
                continue
            if x[0]=="leaf_ch8":
                ld_leafch[7]=x[1].get("leaf_wetness").get("value")
                continue
        
        
        resjson["temp_ch"]=ld_tempch
        resjson["humidity_ch"]=ld_humich
        resjson["Soilmoisture_ch"]=ld_tempch
        resjson["tf_ch"]=ld_onlytempch
        resjson["leaf_ch"]=ld_leafch
        
        
        self._logger.info("temperature======================== : %s", resjson)
        
        
        outdoor=resdata.get("outdoor","--")
        indoor=resdata.get("indoor","--")
        solar_and_uvi=resdata.get("solar_and_uvi","--")
        rainfall=resdata.get("rainfall","--")
        rainfall_piezo=resdata.get("rainfall_piezo","--")
        wind=resdata.get("wind","--")
        pressure=resdata.get("pressure","--")
        lightning=resdata.get("lightning","--")
        indoor_co2=resdata.get("indoor_co2","--")
        co2_aqi_combo=resdata.get("co2_aqi_combo","--")
        pm25_aqi_combo=resdata.get("pm25_aqi_combo","--")
        pm10_aqi_combo=resdata.get("pm10_aqi_combo","--")
        t_rh_aqi_combo=resdata.get("t_rh_aqi_combo","--")
        water_leak=resdata.get("water_leak","--")
        pm25_ch1=resdata.get("pm25_ch1","--")
        pm25_ch2=resdata.get("pm25_ch2","--")
        pm25_ch3=resdata.get("pm25_ch3","--")
        pm25_ch4=resdata.get("pm25_ch4","--")
        temp_and_humidity_ch1=resdata.get("temp_and_humidity_ch1","--")
        temp_and_humidity_ch2=resdata.get("temp_and_humidity_ch2","--")
        temp_and_humidity_ch3=resdata.get("temp_and_humidity_ch3","--")
        temp_and_humidity_ch4=resdata.get("temp_and_humidity_ch4","--")
        temp_and_humidity_ch5=resdata.get("temp_and_humidity_ch5","--")
        temp_and_humidity_ch6=resdata.get("temp_and_humidity_ch6","--")
        temp_and_humidity_ch7=resdata.get("temp_and_humidity_ch7","--")
        temp_and_humidity_ch8=resdata.get("temp_and_humidity_ch8","--")
        soil_ch1=resdata.get("soil_ch1","--")
        soil_ch2=resdata.get("soil_ch2","--")
        soil_ch3=resdata.get("soil_ch3","--")
        soil_ch4=resdata.get("soil_ch4","--")
        soil_ch5=resdata.get("soil_ch5","--")
        soil_ch6=resdata.get("soil_ch6","--")
        soil_ch7=resdata.get("soil_ch7","--")
        soil_ch8=resdata.get("soil_ch8","--")
        temp_ch1=resdata.get("temp_ch1","--")
        temp_ch2=resdata.get("temp_ch2","--")
        temp_ch3=resdata.get("temp_ch3","--")
        temp_ch4=resdata.get("temp_ch4","--")
        temp_ch5=resdata.get("temp_ch5","--")
        temp_ch6=resdata.get("temp_ch6","--")
        temp_ch7=resdata.get("temp_ch7","--")
        temp_ch8=resdata.get("temp_ch8","--")
        leaf_ch1=resdata.get("leaf_ch1","--")
        leaf_ch2=resdata.get("leaf_ch2","--")
        leaf_ch3=resdata.get("leaf_ch3","--")
        leaf_ch4=resdata.get("leaf_ch4","--")
        leaf_ch5=resdata.get("leaf_ch5","--")
        leaf_ch6=resdata.get("leaf_ch6","--")
        leaf_ch7=resdata.get("leaf_ch7","--")
        leaf_ch8=resdata.get("leaf_ch8","--")
        battery=resdata.get("battery","--")
        
        # resjson={
        #     "tempinf":outdoor.get("temperature").get("value"),
        #     "humidityin":ld_inhumi,
        #     "baromrelin":ld_rel,
        #     "baromabsin":ld_abs,
        #     "tempf":ld_outtemp,
        #     "humidity":ld_outhumi,
        #     "winddir":ld_wdir,
        #     "windspeedmph":ld_ws,
        #     "windgustmph":ld_wg,
        #     "solarradiation":ld_sr,
        #     "uv":ld_uvi,
        #     "daywindmax":ld_daywindmax,
        #     "feellike":ld_feellike,
        #     "dewpoint":ld_dewpoint,
        #     "rainratein":ra_rate,
        #     "eventrainin":ra_event,
        #     "dailyrainin":ra_daily,
        #     "weeklyrainin":ra_weekly,
        #     "monthlyrainin":ra_month,
        #     "yearlyrainin":ra_year,
        #     "rrain_piezo":piezora_rate,
        #     "erain_piezo":piezora_event,
        #     "drain_piezo":piezora_daily,
        #     "wrain_piezo":piezora_weekly,
        #     "mrain_piezo":piezora_month,
        #     "yrain_piezo":piezora_year,
        #     "pm25_ch1":ld_pm25ch1,
        #     "pm25_ch2":ld_pm25ch2,
        #     "pm25_ch3":ld_pm25ch3,
        #     "pm25_ch4":ld_pm25ch4,
        #     "pm25_aqi_ch1":ld_pm25ch1_AQI,
        #     "pm25_aqi_ch2":ld_pm25ch2_AQI,
        #     "pm25_aqi_ch3":ld_pm25ch3_AQI,
        #     "pm25_aqi_ch4":ld_pm25ch4_AQI,
        #     "pm25_avg_24h_ch1":ld_pm25ch1_24AQI,
        #     "pm25_avg_24h_ch2":ld_pm25ch2_24AQI,
        #     "pm25_avg_24h_ch3":ld_pm25ch3_24AQI,
        #     "pm25_avg_24h_ch4":ld_pm25ch4_24AQI,
        #     "co2in":ld_co2_co2_in,
        #     "co2in_24h":ld_co2_co224_in,
        #     "co2":ld_co2_co2,
        #     "co2_24h":ld_co2_co224,
        #     "pm25_co2":ld_co2_pm25,
        #     "pm25_24h_co2":ld_co2_pm2524,
        #     "pm10_co2":ld_co2_pm10,
        #     "pm10_24h_co2":ld_co2_pm1024,
        #     "tf_co2":ld_co2_tf,
        #     "humi_co2":ld_co2_humi,
        #     "lightning":ld_lightning,
        #     "lightning_time":ld_lightning_time,
        #     "lightning_num":ld_lightning_power,
        #     "leak_ch1":ld_leakch1,
        #     "leak_ch2":ld_leakch2,
        #     "leak_ch3":ld_leakch3,
        #     "leak_ch4":ld_leakch4,
        #     "temp_ch":ld_tempch,
        #     "humidity_ch":ld_humich,
        #     "Soilmoisture_ch":ld_soil,
        #     "tf_ch":ld_onlytempch,
        #     "leaf_ch":ld_leafch,
        #     "ver":ver,
        #     "allbatt":ld_sen_batt,
        # }
        
        return resdata

    async def _request_MK2(
        self, url: str
    ) -> List[Dict[str, Any]]:
        """Make a request against the API."""
        use_running_session = self._session and not self._session.closed
        if use_running_session:
            session = self._session
        else:
            session = ClientSession(timeout=ClientTimeout(total=DEFAULT_TIMEOUT))
        assert session
        # print(url)
        # print(kwargs)
        try:
            async with session.request("get", url) as resp:
                resp.raise_for_status()
                data = await resp.json(content_type=None)
                # print(data)
        except ClientError as err:
            # print(err)
            raise RequestError(f"Error requesting data from {url}: {err}") from err
        finally:
            if not use_running_session:
                await session.close()
        self._logger.debug("_request_MK2 Received data for %s: %s", url, data)
        return cast(List[Dict[str, Any]], data)
    
    async def _request_loc_batt1(self) -> List[Dict[str, Any]]:
        url = f"http://{self._ip}/{GW11268_API_SENID_1}"
        return await self._request_MK2(url)
    
    async def _request_loc_batt2(self) -> List[Dict[str, Any]]:
        url = f"http://{self._ip}/{GW11268_API_SENID_2}"
        return await self._request_MK2(url)
    
    async def _request_loc_data(self) -> List[Dict[str, Any]]:
        url = f"http://{self._ip}/{GW11268_API_LIVEDATA}"
        return await self._request_MK2(url)
    
    async def _request_loc_info(self) -> List[Dict[str, Any]]:
        url = f"http://{self._ip}/{GW11268_API_VER}"
        return await self._request_MK2(url)
    
    async def _request_loc_unit(self) -> List[Dict[str, Any]]:
        url = f"http://{self._ip}/{GW11268_API_UNIT}"
        return await self._request_MK2(url)
    
    async def _request_loc_allinfo(self,) -> List[Dict[str, Any]]:
        ld_feellike= ''
        ld_dewpoint= ''
        ld_isid= ''
        ld_osid1= ''
        ld_osid2= ''
        ld_intemp= ''
        ld_inhumi= ''
        ld_outtemp= ''
        ld_outhumi= ''
        ld_abs= ''
        ld_rel= ''
        ld_wdir= ''
        ld_ws= ''
        ld_wg= ''
        ld_sr= ''
        ld_uv= ''
        ld_uvi= ''
        ld_hrr= ''
        ld_bs= ''
        ld_bs1= ''
        ld_bs2= ''
        ra_rate= ''
        ra_daily= ''
        ra_weekly= ''
        ra_month= ''
        ra_year= ''
        ra_event= ''
        piezora_rate= ''
        piezora_daily= ''
        piezora_weekly= ''
        piezora_month= ''
        piezora_year= ''
        piezora_event= ''

        cr_piezora_gain= []

        ra_prio=''
        ra_daily_retime= ''
        ra_weekly_retime= ''
        ra_year_retime= ''
        ld_is40= ''
        ld_is41= ''
        ld_is51= ''
        ld_AQI= ''
        ld_pm25ch1= ''
        ld_pm25ch2= ''
        ld_pm25ch3= ''
        ld_pm25ch4= ''
        ld_pm25ch1_AQI= ''
        ld_pm25ch2_AQI= ''
        ld_pm25ch3_AQI= ''
        ld_pm25ch4_AQI= ''
        ld_pm25ch1_24AQI= ''
        ld_pm25ch2_24AQI= ''
        ld_pm25ch3_24AQI= ''
        ld_pm25ch4_24AQI= ''
        ld_leakch1= ''
        ld_leakch2= ''
        ld_leakch3= ''
        ld_leakch4= ''
        ld_lightning= ''
        ld_lightning_time= ''
        ld_lightning_power= ''
        ld_daywindmax= ''
        ld_pm10= ''
        ld_soil= []
        ld_tempch= []
        ld_humich= []
        ld_onlytempch= []
        ld_leafch= []
        ld_co2_tf= ''
        ld_co2_humi= ''
        ld_co2_pm10= ''
        ld_co2_pm1024= ''
        ld_co2_pm25= ''
        ld_co2_pm2524= ''
        ld_co2_co2= ''
        ld_co2_co224= ''
        ld_co2_batt= ''
        ld_co2_pm10_AQI=''
        ld_co2_pm25_AQI=''

        ld_co2_co2_in= ''
        ld_co2_co224_in= ''

        ld_sen_batt=[]
        # url = f"http://{self._ip}/{GW11268_API_UNIT}"
        res_data = await self._request_loc_data()
        res_info = await self._request_loc_info()
        res_unit = await self._request_loc_unit()
        res_batt1 = await self._request_loc_batt1()
        res_batt2 = await self._request_loc_batt2()
        
        # print(res_data )
        print(res_info )
        print(res_unit )
        # print(res_batt1 )
        # print(res_batt2 )
        
        # res=(jsondata)
        print("_request_loc_unit  : %s", res_data["common_list"])
        # if res["common_list"]:
        if "common_list" in res_data:
            for index in range(len(res_data["common_list"])):
                if res_data["common_list"][index]["id"]=='0x02':
                    ld_outtemp=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x07':
                    ld_outhumi=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x03':
                    ld_dewpoint=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x0A':
                    ld_wdir=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x0B':
                    ld_ws=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x0C':
                    ld_wg=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x15':
                    ld_sr=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x17':
                    ld_uvi=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='0x19':
                    ld_daywindmax=res_data["common_list"][index]["val"]
                elif res_data["common_list"][index]["id"]=='3':
                    ld_feellike=res_data["common_list"][index]["val"]
            
        if "rain" in res_data:
            for index in range(len(res_data["rain"])):   
                if res_data["rain"][index]["id"]=='0x0D':
                    ra_event=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x0E':
                    ra_rate=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x10':
                    ra_daily=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x11':
                    ra_weekly=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x12':
                    ra_month=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x13':
                    ra_year=res_data["rain"][index]["val"]
        
        if "piezoRain" in res_data:
            for index in range(len(res_data["piezoRain"])):   
                if res_data["rain"][index]["id"]=='0x0D':
                    piezora_event=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x0E':
                    piezora_rate=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x10':
                    piezora_daily=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x11':
                    piezora_weekly=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x12':
                    piezora_month=res_data["rain"][index]["val"]
                elif res_data["rain"][index]["id"]=='0x13':
                    piezora_year=res_data["rain"][index]["val"]
                
        if "wh25" in res_data:
            ld_intemp=res_data["wh25"][0]["intemp"]
            ld_inhumi=res_data["wh25"][0]["inhumi"]
            ld_abs=res_data["wh25"][0]["abs"]
            ld_rel=res_data["wh25"][0]["rel"]
            if "CO2" in res_data["wh25"][0]:
                ld_co2_co2_in=res_data["wh25"][0]["CO2"]
            if "CO2" in res_data["wh25"][0]:
                ld_co2_co224_in=res_data["wh25"][0]["CO2_24H"]
                
        if "lightning" in res_data:
            ld_lightning=res_data["lightning"][0]["distance"]
            ld_lightning_time=res_data["lightning"][0]["timestamp"]
            ld_lightning_power=res_data["lightning"][0]["count"]
            
        if "co2" in res_data:
             ld_co2_tf=res_data["co2"][0]["temp"]
             ld_co2_humi=res_data["co2"][0]["humidity"]
             ld_co2_pm10=res_data["co2"][0]["PM10"]
             ld_co2_pm10_AQI=res_data["co2"][0]["PM10_RealAQI"]
             ld_co2_pm1024=res_data["co2"][0]["PM10_24HAQI"]
             ld_co2_pm25=res_data["co2"][0]["PM25"]
             ld_co2_pm25_AQI=res_data["co2"][0]["PM25_RealAQI"]
             ld_co2_pm2524=res_data["co2"][0]["PM25_24HAQI"]
             ld_co2_co2=res_data["co2"][0]["CO2"]
             ld_co2_co224=res_data["co2"][0]["CO2_24H"]
             
        if "ch_pm25" in res_data:
            for index in range(len(res_data["ch_pm25"])):   
                if res_data["ch_pm25"][index]["channel"]=='1':
                    ld_pm25ch1=res_data["ch_pm25"][index]["PM25"]
                    ld_pm25ch1_AQI=res_data["ch_pm25"][index]["PM25_RealAQI"]
                    ld_pm25ch1_24AQI=res_data["ch_pm25"][index]["PM25_24HAQI"]
                elif res_data["ch_pm25"][index]["channel"]=='2':
                    ld_pm25ch2=res_data["ch_pm25"][index]["PM25"]
                    ld_pm25ch2_AQI=res_data["ch_pm25"][index]["PM25_RealAQI"]
                    ld_pm25ch2_24AQI=res_data["ch_pm25"][index]["PM25_24HAQI"]
                elif res_data["ch_pm25"][index]["channel"]=='3':
                    ld_pm25ch3=res_data["ch_pm25"][index]["PM25"]
                    ld_pm25ch3_AQI=res_data["ch_pm25"][index]["PM25_RealAQI"]
                    ld_pm25ch3_24AQI=res_data["ch_pm25"][index]["PM25_24HAQI"]
                elif res_data["ch_pm25"][index]["channel"]=='4':
                    ld_pm25ch4=res_data["ch_pm25"][index]["PM25"]
                    ld_pm25ch4_AQI=res_data["ch_pm25"][index]["PM25_RealAQI"]
                    ld_pm25ch4_24AQI=res_data["ch_pm25"][index]["PM25_24HAQI"]
                    
        if "ch_leak" in res_data:
            for index in range(len(res_data["ch_leak"])):   
                if res_data["ch_leak"][index]["channel"]=='1':
                    ld_leakch1=res_data["ch_leak"][index]["status"]
                elif res_data["ch_leak"][index]["channel"]=='2':
                    ld_leakch2=res_data["ch_leak"][index]["status"]
                elif res_data["ch_leak"][index]["channel"]=='3':
                    ld_leakch3=res_data["ch_leak"][index]["status"]
                elif res_data["ch_leak"][index]["channel"]=='4':
                    ld_leakch4=res_data["ch_leak"][index]["status"]
               
        ld_soil=[]
        ld_tempch=[]
        ld_humich=[]
        ld_onlytempch=[]
        ld_leafch=[]  
        for i in range(8):
            ld_soil.append("--")
            ld_tempch.append("--")
            ld_humich.append("--")
            ld_onlytempch.append("--")
            ld_leafch.append("--")
        
        if "ch_aisle" in res_data:
            for index in range(len(res_data["ch_aisle"])):
                ch=int(res_data["ch_aisle"][index]["channel"])-1
                ld_tempch[ch]=res_data["ch_aisle"][index]["temp"]
                ld_humich[ch]=res_data["ch_aisle"][index]["humidity"]
                  
        if "ch_soil" in res_data:
            for index in range(len(res_data["ch_soil"])):
                ch=int(res_data["ch_soil"][index]["channel"])-1
                ld_soil[ch]=res_data["ch_soil"][index]["humidity"]
              
                
        if "ch_temp" in res_data:
            for index in range(len(res_data["ch_temp"])):
                ch=int(res_data["ch_temp"][index]["channel"])-1
                ld_onlytempch[ch]=res_data["ch_temp"][index]["temp"]
                
                
        if "ch_leaf" in res_data:
            for index in range(len(res_data["ch_leaf"])):
                ch=int(res_data["ch_leaf"][index]["channel"])-1
                ld_leafch[ch]=res_data["ch_leaf"][index]["humidity"]
                
        ld_sen_batt=[]
        for i in range(58):
            ld_sen_batt.append("--")
        
        
        for index in range(len(res_batt1)):
            ch=int(res_batt1[index]["type"])
            ld_sen_batt[ch]=res_batt1[index]["batt"]
            
        for index in range(len(res_batt2)):
            ch=int(res_batt2[index]["type"])
            ld_sen_batt[ch]=res_batt2[index]["batt"]
        
                
        ver=res_info["version"][9:]
        
        
                
        resjson={
            "tempinf":ld_intemp,
            "humidityin":ld_inhumi,
            "baromrelin":ld_rel,
            "baromabsin":ld_abs,
            "tempf":ld_outtemp,
            "humidity":ld_outhumi,
            "winddir":ld_wdir,
            "windspeedmph":ld_ws,
            "windgustmph":ld_wg,
            "solarradiation":ld_sr,
            "uv":ld_uvi,
            "daywindmax":ld_daywindmax,
            "feellike":ld_feellike,
            "dewpoint":ld_dewpoint,
            "rainratein":ra_rate,
            "eventrainin":ra_event,
            "dailyrainin":ra_daily,
            "weeklyrainin":ra_weekly,
            "monthlyrainin":ra_month,
            "yearlyrainin":ra_year,
            "rrain_piezo":piezora_rate,
            "erain_piezo":piezora_event,
            "drain_piezo":piezora_daily,
            "wrain_piezo":piezora_weekly,
            "mrain_piezo":piezora_month,
            "yrain_piezo":piezora_year,
            "pm25_ch1":ld_pm25ch1,
            "pm25_ch2":ld_pm25ch2,
            "pm25_ch3":ld_pm25ch3,
            "pm25_ch4":ld_pm25ch4,
            "pm25_aqi_ch1":ld_pm25ch1_AQI,
            "pm25_aqi_ch2":ld_pm25ch2_AQI,
            "pm25_aqi_ch3":ld_pm25ch3_AQI,
            "pm25_aqi_ch4":ld_pm25ch4_AQI,
            "pm25_avg_24h_ch1":ld_pm25ch1_24AQI,
            "pm25_avg_24h_ch2":ld_pm25ch2_24AQI,
            "pm25_avg_24h_ch3":ld_pm25ch3_24AQI,
            "pm25_avg_24h_ch4":ld_pm25ch4_24AQI,
            "co2in":ld_co2_co2_in,
            "co2in_24h":ld_co2_co224_in,
            "co2":ld_co2_co2,
            "co2_24h":ld_co2_co224,
            "pm25_co2":ld_co2_pm25,
            "pm25_24h_co2":ld_co2_pm2524,
            "pm10_co2":ld_co2_pm10,
            "pm10_24h_co2":ld_co2_pm1024,
            "pm10_aqi_co2":ld_co2_pm10_AQI,
            "pm25_aqi_co2":ld_co2_pm25_AQI,
            "tf_co2":ld_co2_tf,
            "humi_co2":ld_co2_humi,
            "lightning":ld_lightning,
            "lightning_time":ld_lightning_time,
            "lightning_num":ld_lightning_power,
            "leak_ch1":ld_leakch1,
            "leak_ch2":ld_leakch2,
            "leak_ch3":ld_leakch3,
            "leak_ch4":ld_leakch4,
            "temp_ch":ld_tempch,
            "humidity_ch":ld_humich,
            "Soilmoisture_ch":ld_soil,
            "tf_ch":ld_onlytempch,
            "leaf_ch":ld_leafch,
            "ver":ver,
            "allbatt":ld_sen_batt,
        }
               
        
                    
        
        print(ver )
        print(resjson )
        return res_data