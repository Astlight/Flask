import json
from pprint import pprint

data = {"datalist":{"2018-06":[{"port_code":"166001","rate":38.38,"asset":24090723.17,"tdate":"2018-06","fundname":"趋势A"},{"port_code":"166006","rate":61.62,"asset":38677160.67,"tdate":"2018-06","fundname":"行业成长A"}],"2018-07":[{"port_code":"166001","rate":29.49,"asset":23514289.17,"tdate":"2018-07","fundname":"趋势A"},{"port_code":"166006","rate":70.51,"asset":56235042.23,"tdate":"2018-07","fundname":"行业成长A"}],"2018-08":[{"port_code":"166001","rate":29.76,"asset":22666040.77,"tdate":"2018-08","fundname":"趋势A"},{"port_code":"166006","rate":70.24,"asset":53492789.27,"tdate":"2018-08","fundname":"行业成长A"}],"2018-09":[{"port_code":"166001","rate":29.53,"asset":22497328.39,"tdate":"2018-09","fundname":"趋势A"},{"port_code":"166006","rate":70.47,"asset":53692127.89,"tdate":"2018-09","fundname":"行业成长A"}],"2018-10":[{"port_code":"166001","rate":29.39,"asset":20411855.81,"tdate":"2018-10","fundname":"趋势A"},{"port_code":"166006","rate":70.61,"asset":49042689.16,"tdate":"2018-10","fundname":"行业成长A"}],"2018-11":[{"port_code":"166001","rate":0,"asset":0,"tdate":"2018-11","fundname":"趋势A"},{"port_code":"166006","rate":0,"asset":0,"tdate":"2018-11","fundname":"行业成长A"}]},"datalistTotal":[{"asset":62767883.84,"tdate":"2018-06"},{"asset":79749331.4,"tdate":"2018-07"},{"asset":76158830.04,"tdate":"2018-08"},{"asset":76189456.28,"tdate":"2018-09"},{"asset":69454544.97,"tdate":"2018-10"},{"asset":0,"tdate":"2018-11"}]}

data=json.loads(data)
pprint(data["datalist"])
print(data["datalist"]["2018-06"])
