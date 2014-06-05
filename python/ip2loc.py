import IP2Location;

IP2LocObj = IP2Location.IP2Location();
IP2LocObj.open("data/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE-TIMEZONE-ISP-DOMAIN-NETSPEED-AREACODE-WEATHER-MOBILE-ELEVATION-USAGETYPE-SAMPLE.BIN");
rec = IP2LocObj.get_all("19.5.10.1");

print rec.country_short
print rec.country_long
print rec.region
print rec.city
print rec.isp
print rec.latitude
print rec.longitude
print rec.domain
print rec.zipcode
print rec.timezone
print rec.netspeed
print rec.idd_code
print rec.area_code
print rec.weather_code
print rec.weather_name
print rec.mcc
print rec.mnc
print rec.mobile_brand
print rec.elevation
print rec.usage_type
