# -*- coding:utf-8 -*-
# _author: Damion.zeng
# Email: Damion.zeng@akmmv.com
# date: 2022/8/22
# @desc:
import requests
import json
import datetime as dt
import zhdate
import random



class DataSource(object):
    """数据源"""
    data = {}    # 存储数据的字典

    @classmethod
    def base_data(cls):
        """
        获取基本数据：今天的日期，生日，纪念日，
        :return:
        """
        td = dt.datetime.now()
        td_str = str(td.month)+'月'+str(td.day)+'日'  # 今天阳历日期
        td_zh = zhdate.ZhDate.today()  # 农历日期
        td_zh_str = str(td_zh.lunar_month) + '-' + str(td_zh.lunar_day)
        week_list = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
        td_week = week_list[td.date().weekday()]  # 星期
        baby_birthday = zhdate.ZhDate(td.year, 6, 18) if td_zh.to_datetime() < zhdate.ZhDate(td.year, 6,
                                                                                             18).to_datetime() \
            else zhdate.ZhDate(td.year + 1, 6, 18)
        cd_day = baby_birthday - td_zh  # 下一次生日天数
        # 在一起天数
        love_day = (td-dt.datetime.strptime('2022-2-1','%Y-%m-%d')).days
        # my birthday
        birthday2 = zhdate.ZhDate(td.year, 12, 25) if td_zh.to_datetime() < zhdate.ZhDate(td.year, 12,
                                                                                             25).to_datetime() \
            else zhdate.ZhDate(td.year + 1, 12, 25)
        cd_day_2 = birthday2 - td_zh  # 下一次生日天数
        # 更加时间生成，早上、中午、下午、晚上
        if td.hour >= 3 and td.hour<9:
            greet = "乖໌້ᮨ乖໌້ᮨ,早上好呀！美好的一天开始啦，记得多喝水喔"
        elif td.hour>=9 and td.hour<12:
            greet = "老໌້ᮨ婆໌້ᮨ,上午开始啦，还不起床就要晒屁屁了喔！还有，早餐吃了吗？"
        elif td.hour>=12 and td.hour<13:
            greet = "宝໌້ᮨ贝໌້ᮨ，现在是吃饭时间喔，记得吃午饭，我爱你！"
        elif td.hour>=13 and td.hour<18:
            greet = '瑶໌້ᮨ宝໌້ᮨ,下午也要多喝水喔，不可以忘记了'
        elif td.hour >=18 and td.hour<23:
            greet = '亲໌້ᮨ亲໌້ᮨ,晚上时间到啦，想我了吗？我可想你了呢'
        else:
            greet = 'h໌້ᮨo໌້ᮨn໌້ᮨe໌້ᮨy໌້ᮨ,快点睡觉觉喔，我爱你，老婆'
        # 将数据传入data
        cls.data['date'] = td_str
        cls.data['lunar'] = td_zh_str
        cls.data['week'] = td_week
        cls.data['birthday1'] = str(cd_day)
        cls.data['birthday2'] = str(cd_day_2)
        cls.data['love_day'] = str(love_day)
        cls.data['greet'] =greet
        return cls.data

    @classmethod
    def get_weather_data(cls,key,city_code):
        """获取当前的最低气温和最高气温以及天气状况"""
        BaseUrl = 'https://restapi.amap.com/v3/weather/weatherInfo?key={}&city={}&extensions=all&out=JSON'.format(key,city_code)
        response = requests.get(BaseUrl)
        today_temper = json.loads(response.text)['forecasts'][0]
        cls.data['city'] = today_temper['city']
        cls.data['min_temp'] = today_temper['casts'][0]['nighttemp'] + '℃'
        cls.data['max_temp'] = today_temper['casts'][0]['daytemp']+ '℃'
        cls.data['weather'] = today_temper['casts'][0]['dayweather'] if  today_temper['casts'][0]['dayweather'] == today_temper['casts'][0]['nightweather'] \
            else today_temper['casts'][0]['dayweather'] + ' 转 ' + today_temper['casts'][0]['nightweather']
        return cls.data

    @classmethod
    def get_random_word(cls):
        today = dt.datetime.now().strftime('%Y-%m-%d')
        yd_url = "https://dict.youdao.com/infoline?mode=publish&date=" + today + "&update=auto&apiversion=5.0"
        for record in requests.get(yd_url).json()[today]:
            if record['type'] == '壹句':
                cls.data['content'] = record['title']
                cls.data['translation'] = record['summary']
                break
        return cls.data

    @classmethod
    def main(cls,key,city_code):
        cls.base_data()
        cls.get_random_word()
        cls.get_weather_data(key,city_code)
        return cls.data

class WxApp(object):
    """
    微信公众号开发
    """
    def __init__(self,appId,secret,openId):
        """
        初始化，传入appId和secret
        :param appId:
        :param secret:
        :param openId: 用户的微信号
        """
        self.appId = appId
        self.secret = secret
        self.Token = ''
        self.openId = openId

    def get_access_token(self):
        """
        获取access_token(微信唯一认证)
        :return:
        """
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}'.format(self.appId,self.secret)
        response = requests.get(BaseUrl)
        access_token = json.loads(response.text)['access_token']
        # 将token 传回Token,并在之后的url均课调用此access_token
        self.Token=access_token
        return access_token

    def create_menu(self,body=None):
        """
        新增菜单
        :return:
        """
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token={}'.format(self.Token)
        # 示例菜单
        # body = {
        #     'button':[
        #         {"type":"click",
        #          "name":"今日课程",
        #          "key":"CLS_SCHEDULE_001"},
        #         {
        #             "name":"备忘录",
        #             "sub_button":[
        #                 {
        #                     "type":"click",
        #                     "name":"新建备忘录",
        #                     "key":"MEMO_001"
        #                 },
        #                 {
        #                     "type": "click",
        #                     "name": "查询备忘录",
        #                     "key": "MEMO_002"
        #                 }
        #             ]
        #         }
        #     ]
        # }
        header = {"Content-Type": "application/json",
                  "charset": "utf-8"}
        data = bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        response = requests.post(BaseUrl,data=data,headers=header)
        return response.text

    def query_menu(self):
        """
        查询菜单
        :return:
        """
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token={}'.format(self.Token)
        response = requests.get(BaseUrl)
        menu_data = json.loads(response.text)['selfmenu_info']['button']
        return menu_data

    def delete_all_menu(self):
        """删除所有菜单"""
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={}'.format(self.Token)
        response = requests.get(BaseUrl)
        return response.text

    def send_message(self,type,msg_object):
        """
        向用户发送数据
        :param type:数据类型
        :param msg_object: 数据信息--是一个对象
        :return:
        """
        print(self.Token)
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={}'.format(self.Token)
        body={
            "touser":self.openId,   # openId,也就是每个用户的唯一id
            "msgtype":type,
            type:msg_object
        }
        header = {"Content-Type": "application/json",
                  "charset":"utf-8"}
        data = bytes(json.dumps(body,ensure_ascii=False),encoding='utf-8')
        response = requests.post(BaseUrl,data=data,headers=header)
        return response.text

    @staticmethod
    def randomcolor():
        """随机生成颜色"""
        colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        color = ""
        for i in range(6):
            color += colorArr[random.randint(0, 14)]
        return "#" + color

    def send_model_message(self,data_dict,modelId):
        """发送模板数据"""
        BaseUrl = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}'.format(self.Token)
        send_data = {}
        for one_dict in data_dict:
            send_data[one_dict] = {
                "value":data_dict[one_dict],
                "color":self.randomcolor()
            }
        body = {
            "touser":self.openId,
            "template_id":modelId,
            "topcolor":"#00CCFF",
            "data":send_data
        }
        header = {"Content-Type": "application/json",
                  "charset":"utf-8"}
        data = bytes(json.dumps(body,ensure_ascii=False),encoding='utf-8')
        response = requests.post(BaseUrl,data=data,headers=header)
        return response.text
