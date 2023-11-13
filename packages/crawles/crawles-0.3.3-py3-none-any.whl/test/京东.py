# coding = utf-8
import crawles

url = 'https://search.jd.com/Search'

cookies = { 
    '3AB9D23F7A4B3C9B': 'C57LGLCOMD3AHPV7BUVSQFFE56XTV3BR24D56MU5JQAVHNK6RGE42G5O2E5YXNQU2EDUMNYJLM4DUT4SQJQAJQAKF4',
    '3AB9D23F7A4B3CSS': 'jdd03C57LGLCOMD3AHPV7BUVSQFFE56XTV3BR24D56MU5JQAVHNK6RGE42G5O2E5YXNQU2EDUMNYJLM4DUT4SQJQAJQAKF4AAAAMLY6PT24YAAAAAC7N4PUT4REIYWMX',
    '__jda': '122270672.1460188919.1699511817.1699511821.1699860952.2',
    '__jdb': '122270672.9.1460188919|2.1699860952',
    '__jdc': '122270672',
    '__jdu': '1460188919',
    '__jdv': '76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9f0247191e0c4dffa49742b8d941b82b|1699860951556',
    '_gia_d': '1',
    '_pst': 'kjk1752',
    '_tp': 'YOB7fXaeSAYMArWv%2Bs4waA%3D%3D',
    'areaId': '18',
    'avif': '1',
    'flash': '2_ZXbwpdvSmkQCrBDarEzOk9BAzUEBdG2fr9Mo6SCz19lfZxx84PSrucVYCDivFiQwfbh2UnHh36JPx0191yy1OYwHJMYAoutCc0jTM9-hvTj*',
    'ipLoc-djd': '18-1482-0-0',
    'jsavif': '1',
    'logintype': 'qq',
    'mba_muid': '1460188919',
    'npin': 'kjk1752',
    'pin': 'kjk1752',
    'pinId': '6fwFXniv4p0',
    'qrsc': '3',
    'rkv': '1.0',
    'shshshfpa': '3c29e8d5-ab68-3248-a927-7bac20aea56c-1671285449',
    'shshshfpb': 'AAkc-n8eLEino1atoMkipJ3usIK6lbBZxKFRJRQAAAAA',
    'shshshfpx': '3c29e8d5-ab68-3248-a927-7bac20aea56c-1671285449',
    'shshshsID': '2b47b1f2483873e9acd8d78e81aefb55_5_1699861184444',
    'thor': '03CB7BD47C9FE7833977FB3D80270D58C8AA64993C456CB06CC7C6B6DBA7F43504BD93E98A9992F000A0B11406B9E6AB073D1568110BA3EC01255E8A7FF219CBBEB48641CEF77D0898713A060805ED1CE678C77B3DFF5BB03B7164B4EBF7F89CC1E6E9804EE5494195582222E6D413D15FFD1A763552DC73B53F26188A185A9EC1881BFF33F81931F636022D6715E5F3',
    'unick': 'kjk1752',
    'unpl': 'JF8EAK9nNSttUBxVBh4EGxoQH1wGWwhfHEcGZ2EAVw5RHlwAG1ESEUN7XlVdXxRLFx9vZRRUWVNJUA4fAysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrAh4VEUtUXVZdAHsWM2hXNWRYW09XAxIyGiIRex8AAlgNQhcLImcAU1xYQl0NGworEyBI',
    'wlfstk_smdl': 'proqlqseg4wxkg9h2qwo2xgj4ehypr8e',
    'xapieid': 'jdd03C57LGLCOMD3AHPV7BUVSQFFE56XTV3BR24D56MU5JQAVHNK6RGE42G5O2E5YXNQU2EDUMNYJLM4DUT4SQJQAJQAKF4AAAAMLY6PT24YAAAAAC7N4PUT4REIYWMX',
}

headers = { 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authority': 'search.jd.com',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=6649edc02a8f43cf8e9fe33111af8702',
    'sec-ch-ua': '\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

params = { 
    'enc': 'utf-8',
    'keyword': '手机',
    'pvid': '2edd4c590726492fb40fbe136cef28ad',
    'wq': '手机',
}


# 当前时间戳: 1699861643.3519866
response = crawles.get(url, headers=headers, params=params, cookies=cookies)
print(response.text)
import re
price = re.findall('<em>￥</em><i data-price=".*">(.*?)</i>',response.text)
print(price,len(price))
