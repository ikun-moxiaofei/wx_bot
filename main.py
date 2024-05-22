# -*- coding: utf-8 -*-
import sys
from datetime import datetime
from time import sleep
import xml.etree.ElementTree as ET

import ntchat

from mapper.msgMapper import insert_data
from utils.GroupUtils import getGroupName, isGroup1, isGroupTest
from utils.ImageUtils import imageDecode

wechat = ntchat.WeChat()

wechat.open(smart=True)


# # 图片消息通知
# MT_RECV_IMAGE_MSG = 11047
# MT_RECV_PICTURE_MSG = 11047
@wechat.msg_register(ntchat.MT_ALL)
# @wechat.msg_register(ntchat.MT_RECV_TEXT_MSG)
# @wechat.msg_register(ntchat.MT_RECV_IMAGE_MSG)
# @wechat.msg_register(ntchat.MT_RECV_PICTURE_MSG)
def on_recv_text_msg(wechat: ntchat.WeChat, message):
    # print(message)
    data = message["data"]
    # msg = data["msg"]
    # 发送人id
    from_wxid = data["from_wxid"]
    # 群聊id
    room_wxid = data["room_wxid"]
    # 自己的id
    self_wxid = wechat.get_login_info()["wxid"]
    # 获取当前时间
    now = datetime.now()
    # 格式化时间为指定的格式：年-月-日 时:分:秒
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

    if from_wxid == self_wxid:
        return

    # isGroup = isGroupTest(room_wxid)
    isGroup = isGroup1(room_wxid)
    if isGroup == 0:
        # print("不属于范围")
        return

    '''
    2024-05-17 16:59:08,644 - WeChatInstance - DEBUG - on recv message: 
    {
        'data': 
        {
         'from_wxid': 'wxid_51v4e8ejxhkg22',
         'image': 'D:\\w\\WeChat Files\\wxid_rizc5bcmmtre12\\FileStorage\\Image\\2024-05\\5eb4da0713045ba71baad0d1614bb1c6.dat', 
         'image_thumb': 'D:\\w\\WeChat Files\\wxid_rizc5bcmmtre12\\FileStorage\\Image\\Thumb\\2024-05\\cc70c3bcad7f953aada23825ab022011_t.dat', 
         'is_pc': 0, 
         'msgid': '8491203577896293711',
         'raw_msg': '<?xml version="1.0"?>\n<msg>\n\t<img aeskey="2bb5ef2f2434ec7706f846f809a15456" encryver="1" cdnthumbaeskey="2bb5ef2f2434ec7706f846f809a15456" cdnthumburl="3057020100044b30490201000204801c865102032f4f5502043ade512a020466471b73042431336239303633322d343364642d346663392d626263632d613830393635343834303134020405290a020201000405004c575d00" cdnthumblength="4051" cdnthumbheight="120" cdnthumbwidth="68" cdnmidheight="0" cdnmidwidth="0" cdnhdheight="0" cdnhdwidth="0" cdnmidimgurl="3057020100044b30490201000204801c865102032f4f5502043ade512a020466471b73042431336239303633322d343364642d346663392d626263632d613830393635343834303134020405290a020201000405004c575d00" length="59080" md5="e8ececca1ab53211460eb01b523ce53f" hevc_mid_size="59080" originsourcemd5="12fb2c5b2299e1f0aa3e9f42b2461036" />\n\t<platform_signature></platform_signature>\n\t<imgdatahash></imgdatahash>\n\t<ImgSourceInfo>\n\t\t<ImgSourceUrl></ImgSourceUrl>\n\t\t<BizType>0</BizType>\n\t</ImgSourceInfo>\n</msg>\n', 
         'room_wxid': '45834099286@chatroom', 
         'timestamp': 1715936347,
         'to_wxid': '45834099286@chatroom', 
         'wx_type': 3, 'xor_key': 195
          },
        'type': 11047
    }
    '''
    # print(data)
    '''
    {
    'from_wxid': 'wxid_51v4e8ejxhkg22', 
    'is_pc': 0, 
    'msgid': '6590943200766961721',
    'raw_msg': '<?xml version="1.0"?>\n<msg>\n\t<appmsg appid="" sdkver="0">\n\t\t<title>这是一个引用</title>\n\t\t<des />\n\t\t<username />\n\t\t<action>view</action>\n\t\t<type>57</type>\n\t\t<showtype>0</showtype>\n\t\t<content />\n\t\t<url />\n\t\t<lowurl />\n\t\t<forwardflag>0</forwardflag>\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<contentattr>0</contentattr>\n\t\t<streamvideo>\n\t\t\t<streamvideourl />\n\t\t\t<streamvideototaltime>0</streamvideototaltime>\n\t\t\t<streamvideotitle />\n\t\t\t<streamvideowording />\n\t\t\t<streamvideoweburl />\n\t\t\t<streamvideothumburl />\n\t\t\t<streamvideoaduxinfo />\n\t\t\t<streamvideopublishid />\n\t\t</streamvideo>\n\t\t<canvasPageItem>\n\t\t\t<canvasPageXml><![CDATA[]]></canvasPageXml>\n\t\t</canvasPageItem>\n\t\t<refermsg>\n\t\t\t<type>1</type>\n\t\t\t<svrid>7074553605650522041</svrid>\n\t\t\t<fromusr>45834099286@chatroom</fromusr>\n\t\t\t<chatusr>wxid_51v4e8ejxhkg22</chatusr>\n\t\t\t<displayname>莫筱菲</displayname>\n\t\t\t<msgsource>&lt;msgsource&gt;&lt;pua&gt;1&lt;/pua&gt;&lt;/msgsource&gt;</msgsource>\n\t\t\t<content>111</content>\n\t\t\t<strid />\n\t\t\t<createtime>1716208025</createtime>\n\t\t</refermsg>\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<cdnattachurl />\n\t\t\t<emoticonmd5></emoticonmd5>\n\t\t\t<aeskey></aeskey>\n\t\t\t<fileext />\n\t\t\t<islargefilemsg>0</islargefilemsg>\n\t\t</appattach>\n\t\t<extinfo />\n\t\t<androidsource>0</androidsource>\n\t\t<thumburl />\n\t\t<mediatagname />\n\t\t<messageaction><![CDATA[]]></messageaction>\n\t\t<messageext><![CDATA[]]></messageext>\n\t\t<emoticongift>\n\t\t\t<packageflag>0</packageflag>\n\t\t\t<packageid />\n\t\t</emoticongift>\n\t\t<emoticonshared>\n\t\t\t<packageflag>0</packageflag>\n\t\t\t<packageid />\n\t\t</emoticonshared>\n\t\t<designershared>\n\t\t\t<designeruin>0</designeruin>\n\t\t\t<designername>null</designername>\n\t\t\t<designerrediretcturl><![CDATA[null]]></designerrediretcturl>\n\t\t</designershared>\n\t\t<emotionpageshared>\n\t\t\t<tid>0</tid>\n\t\t\t<title>null</title>\n\t\t\t<desc>null</desc>\n\t\t\t<iconUrl><![CDATA[null]]></iconUrl>\n\t\t\t<secondUrl>null</secondUrl>\n\t\t\t<pageType>0</pageType>\n\t\t\t<setKey>null</setKey>\n\t\t</emotionpageshared>\n\t\t<webviewshared>\n\t\t\t<shareUrlOriginal />\n\t\t\t<shareUrlOpen />\n\t\t\t<jsAppId />\n\t\t\t<publisherId />\n\t\t\t<publisherReqId />\n\t\t</webviewshared>\n\t\t<template_id />\n\t\t<md5 />\n\t\t<websearch>\n\t\t\t<rec_category>0</rec_category>\n\t\t\t<channelId>0</channelId>\n\t\t</websearch>\n\t\t<weappinfo>\n\t\t\t<username />\n\t\t\t<appid />\n\t\t\t<appservicetype>0</appservicetype>\n\t\t\t<secflagforsinglepagemode>0</secflagforsinglepagemode>\n\t\t\t<videopageinfo>\n\t\t\t\t<thumbwidth>0</thumbwidth>\n\t\t\t\t<thumbheight>0</thumbheight>\n\t\t\t\t<fromopensdk>0</fromopensdk>\n\t\t\t</videopageinfo>\n\t\t</weappinfo>\n\t\t<statextstr />\n\t\t<musicShareItem>\n\t\t\t<musicDuration>0</musicDuration>\n\t\t</musicShareItem>\n\t\t<finderLiveProductShare>\n\t\t\t<finderLiveID><![CDATA[]]></finderLiveID>\n\t\t\t<finderUsername><![CDATA[]]></finderUsername>\n\t\t\t<finderObjectID><![CDATA[]]></finderObjectID>\n\t\t\t<finderNonceID><![CDATA[]]></finderNonceID>\n\t\t\t<liveStatus><![CDATA[]]></liveStatus>\n\t\t\t<appId><![CDATA[]]></appId>\n\t\t\t<pagePath><![CDATA[]]></pagePath>\n\t\t\t<productId><![CDATA[]]></productId>\n\t\t\t<coverUrl><![CDATA[]]></coverUrl>\n\t\t\t<productTitle><![CDATA[]]></productTitle>\n\t\t\t<marketPrice><![CDATA[0]]></marketPrice>\n\t\t\t<sellingPrice><![CDATA[0]]></sellingPrice>\n\t\t\t<platformHeadImg><![CDATA[]]></platformHeadImg>\n\t\t\t<platformName><![CDATA[]]></platformName>\n\t\t\t<shopWindowId><![CDATA[]]></shopWindowId>\n\t\t\t<flashSalePrice><![CDATA[0]]></flashSalePrice>\n\t\t\t<flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>\n\t\t\t<ecSource><![CDATA[]]></ecSource>\n\t\t\t<sellingPriceWording><![CDATA[]]></sellingPriceWording>\n\t\t\t<platformIconURL><![CDATA[]]></platformIconURL>\n\t\t\t<firstProductTagURL><![CDATA[]]></firstProductTagURL>\n\t\t\t<firstProductTagAspectRatioString><![CDATA[0.0]]></firstProductTagAspectRatioString>\n\t\t\t<secondProductTagURL><![CDATA[]]></secondProductTagURL>\n\t\t\t<secondProductTagAspectRatioString><![CDATA[0.0]]></secondProductTagAspectRatioString>\n\t\t\t<firstGuaranteeWording><![CDATA[]]></firstGuaranteeWording>\n\t\t\t<secondGuaranteeWording><![CDATA[]]></secondGuaranteeWording>\n\t\t\t<thirdGuaranteeWording><![CDATA[]]></thirdGuaranteeWording>\n\t\t\t<isPriceBeginShow>false</isPriceBeginShow>\n\t\t\t<lastGMsgID><![CDATA[]]></lastGMsgID>\n\t\t\t<promoterKey><![CDATA[]]></promoterKey>\n\t\t\t<discountWording><![CDATA[]]></discountWording>\n\t\t\t<priceSuffixDescription><![CDATA[]]></priceSuffixDescription>\n\t\t\t<showBoxItemStringList />\n\t\t</finderLiveProductShare>\n\t\t<finderOrder>\n\t\t\t<appID><![CDATA[]]></appID>\n\t\t\t<orderID><![CDATA[]]></orderID>\n\t\t\t<path><![CDATA[]]></path>\n\t\t\t<priceWording><![CDATA[]]></priceWording>\n\t\t\t<stateWording><![CDATA[]]></stateWording>\n\t\t\t<productImageURL><![CDATA[]]></productImageURL>\n\t\t\t<products><![CDATA[]]></products>\n\t\t\t<productsCount><![CDATA[0]]></productsCount>\n\t\t</finderOrder>\n\t\t<finderShopWindowShare>\n\t\t\t<finderUsername><![CDATA[]]></finderUsername>\n\t\t\t<avatar><![CDATA[]]></avatar>\n\t\t\t<nickname><![CDATA[]]></nickname>\n\t\t\t<commodityInStockCount><![CDATA[]]></commodityInStockCount>\n\t\t\t<appId><![CDATA[]]></appId>\n\t\t\t<path><![CDATA[]]></path>\n\t\t\t<appUsername><![CDATA[]]></appUsername>\n\t\t\t<query><![CDATA[]]></query>\n\t\t\t<liteAppId><![CDATA[]]></liteAppId>\n\t\t\t<liteAppPath><![CDATA[]]></liteAppPath>\n\t\t\t<liteAppQuery><![CDATA[]]></liteAppQuery>\n\t\t\t<platformTagURL><![CDATA[]]></platformTagURL>\n\t\t\t<saleWording><![CDATA[]]></saleWording>\n\t\t\t<lastGMsgID><![CDATA[]]></lastGMsgID>\n\t\t\t<profileTypeWording><![CDATA[]]></profileTypeWording>\n\t\t\t<reputationInfo>\n\t\t\t\t<hasReputationInfo>0</hasReputationInfo>\n\t\t\t\t<reputationScore>0</reputationScore>\n\t\t\t\t<reputationWording />\n\t\t\t\t<reputationTextColor />\n\t\t\t\t<reputationLevelWording />\n\t\t\t\t<reputationBackgroundColor />\n\t\t\t</reputationInfo>\n\t\t\t<productImageURLList />\n\t\t</finderShopWindowShare>\n\t\t<findernamecard>\n\t\t\t<username />\n\t\t\t<avatar><![CDATA[]]></avatar>\n\t\t\t<nickname />\n\t\t\t<auth_job />\n\t\t\t<auth_icon>0</auth_icon>\n\t\t\t<auth_icon_url />\n\t\t\t<ecSource><![CDATA[]]></ecSource>\n\t\t\t<lastGMsgID><![CDATA[]]></lastGMsgID>\n\t\t</findernamecard>\n\t\t<finderGuarantee>\n\t\t\t<scene><![CDATA[0]]></scene>\n\t\t</finderGuarantee>\n\t\t<directshare>0</directshare>\n\t\t<gamecenter>\n\t\t\t<namecard>\n\t\t\t\t<iconUrl />\n\t\t\t\t<name />\n\t\t\t\t<desc />\n\t\t\t\t<tail />\n\t\t\t\t<jumpUrl />\n\t\t\t</namecard>\n\t\t</gamecenter>\n\t\t<patMsg>\n\t\t\t<chatUser />\n\t\t\t<records>\n\t\t\t\t<recordNum>0</recordNum>\n\t\t\t</records>\n\t\t</patMsg>\n\t\t<secretmsg>\n\t\t\t<issecretmsg>0</issecretmsg>\n\t\t</secretmsg>\n\t\t<referfromscene>0</referfromscene>\n\t\t<gameshare>\n\t\t\t<liteappext>\n\t\t\t\t<liteappbizdata />\n\t\t\t\t<priority>0</priority>\n\t\t\t</liteappext>\n\t\t\t<appbrandext>\n\t\t\t\t<litegameinfo />\n\t\t\t\t<priority>-1</priority>\n\t\t\t</appbrandext>\n\t\t\t<gameshareid />\n\t\t\t<sharedata />\n\t\t\t<isvideo>0</isvideo>\n\t\t\t<duration>-1</duration>\n\t\t\t<isexposed>0</isexposed>\n\t\t\t<readtext />\n\t\t</gameshare>\n\t\t<mpsharetrace>\n\t\t\t<hasfinderelement>0</hasfinderelement>\n\t\t\t<lastgmsgid />\n\t\t</mpsharetrace>\n\t\t<wxgamecard>\n\t\t\t<framesetname />\n\t\t\t<mbcarddata />\n\t\t\t<minpkgversion />\n\t\t\t<mbcardheight>0</mbcardheight>\n\t\t\t<isoldversion>0</isoldversion>\n\t\t</wxgamecard>\n\t\t<liteapp>\n\t\t\t<id>null</id>\n\t\t\t<path />\n\t\t\t<query />\n\t\t</liteapp>\n\t</appmsg>\n\t<fromusername>wxid_51v4e8ejxhkg22</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname />\n\t</appinfo>\n\t<commenturl />\n</msg>\n',
    'room_wxid': '45834099286@chatroom', 
    'timestamp': 1716208093,
    'to_wxid': '45834099286@chatroom', 
    'wx_sub_type': 57, 'wx_type': 49
    }

    '''
    if 'raw_msg' in data:
        raw_msg = data["raw_msg"]
        root = ET.fromstring(raw_msg)
        title_element = root.find('.//title')
        if title_element is not None:
            title_text = title_element.text
            print(title_text)
            groupnum = getGroupName(room_wxid)
            result = insert_data(from_wxid, title_text, groupnum, formatted_now, 0)
            print(result)
        else:
            print("<title>标签未找到")

    if 'msg' in data:
        msg = data["msg"]
        print(msg)
        groupnum = getGroupName(room_wxid)
        result = insert_data(from_wxid, msg, groupnum, formatted_now, 0)
        print(result)
        if msg == "hello123":
            wechat.send_text(to_wxid=room_wxid, content=f"world456")

    if 'image' in data:
        temp_path = data['image'].strip()
        sleep(1)
        msg = imageDecode(temp_path)
        groupnum = getGroupName(room_wxid)
        result = insert_data(from_wxid, msg, groupnum, formatted_now, 1)
        print(result)


try:
    while True:
        pass
except KeyboardInterrupt:
    ntchat.exit_()
    sys.exit()
