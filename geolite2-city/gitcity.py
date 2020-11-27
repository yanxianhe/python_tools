# -*- coding: utf-8 -*-
'''
@Author  :   yanxianhe
@Time    :   2020/11/27 13:43:06
@Contact :   xianhe_yan@sina.com
'''

# pip3 install geoip2==3.0.0
# pip3 install python-geoip-geolite2==2015.303


import os
import geoip2.database
abspath = os.path.dirname(os.path.dirname(__file__))
filepath = (abspath + "\\geolite2-city\\GeoLite2-City.mmdb")

reader = geoip2.database.Reader(filepath)

def encode_utf8(string) :
    return string.encode('utf-8')

def decode_utf8(string) :
    return unicode(string, encoding='utf-8')

# 查询IP地址对应的物理地址
def ip_get_location(ip_address):
    # 载入指定IP相关数据
    response = reader.city(ip_address)

    #读取国家代码
    Country_IsoCode = response.country.iso_code
    #读取国家名称
    Country_Name = response.country.name
    #读取国家名称(中文显示)
    Country_NameCN = response.country.names['zh-CN']
    #读取州(国外)/省(国内)名称
    Country_SpecificName = response.subdivisions.most_specific.name
    #读取州(国外)/省(国内)代码
    Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
    #读取城市名称
    City_Name = response.city.name
    #读取邮政编码
    City_PostalCode = response.postal.code
    #获取纬度
    Location_Latitude = response.location.latitude
    #获取经度
    Location_Longitude = response.location.longitude

    if(Country_IsoCode == None):
        Country_IsoCode = "None"
    if(Country_Name == None):
        Country_Name = "None"
    if(Country_NameCN == None):
        Country_NameCN = "None"
    if(Country_SpecificName == None):
        Country_SpecificName = "None"
    if(Country_SpecificIsoCode == None):
        Country_SpecificIsoCode = "None"
    if(City_Name == None):
        City_Name = "None"
    if(City_PostalCode == None):
        City_PostalCode = "None"
    if(Location_Latitude == None):
        Location_Latitude = "None"
    if(Location_Longitude == None):
        Location_Longitude = "None"
    print("************* %s *************" % str(ip_address))
    print(" 国家编码: %s " % str(Country_IsoCode))
    print(" 国家名称: %s " % str(Country_Name))
    print(" 国家中文名称 : %s " % str(Country_NameCN))
    print(" 省份或州名称: %s " % str(Country_SpecificName))
    print(" 省份或州编码: %s " % str(Country_SpecificIsoCode))
    print(" 城市名称: %s " % str(City_Name))
    print(" 城市邮编: %s " % str(City_PostalCode))
    print(" 纬度: %s " % str(Location_Latitude))
    print(" 经度: %s " % str(Location_Longitude))

if __name__ == '__main__' :
    ip_get_location(str("100.10.2.2"))
    ip_get_location(str("13.126.1.174"))
    ip_get_location(str("61.1.200.142"))