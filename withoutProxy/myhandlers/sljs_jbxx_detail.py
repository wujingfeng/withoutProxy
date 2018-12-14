#张峻珲
#全国水利建设(业绩信息+信用评价)

import re
import time
import requests
from lxml import etree
import pymysql
from withoutProxy.config.database import *

#访问get
def get(url):
    i = 0
    while True:
        try:
            requests1 = requests.get(url,timeout=60)
            if requests1.status_code != 200:
                i = 1 / 0
            return requests1
        except:
            print("访问链接失败重试..."+url+"")
            i = i+1
            if i == 10:
                break
            pass

def sljs_jbxx_detail(response):
    rtn_data = {}
    data_list = []

    #数据库配置
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        db=MYSQL_DB,
        charset=MYSQL_CHATSET,
        port=MYSQL_PORT
    )
    cursor = conn.cursor()

    url_id = re.findall(r'id=(.*?)$',response.url,re.S)[0]
    url = 'http://rcpu.cwun.org/UInfo.aspx?id=%s'%(url_id)
    requests1 = get(url)
    requests1.encoding = "utf-8"
    html = requests1.text
    content = etree.HTML(html)
    #爬取数据
    #水利局公司基本信息采集表id
    print('基本信息...')
    cj_id = url_id
    #公司名称
    try:
        gsmc = content.xpath('//*[@id="ContentPlaceHolder1_lbUNCHNM"]/text()')[0].strip()
    except:
        gsmc = ''

    #所属省市
    try:
        ssss = content.xpath('//*[@id="ContentPlaceHolder1_lbPNAME"]/text()')[0].strip()
    except:
        ssss = ''

    #单位性质
    try:
        dwxz = content.xpath('//*[@id="ContentPlaceHolder1_lbATTR"]/text()')[0].strip()
    except:
        dwxz = ''

    #办公/生产/经营场地
    try:
        jycd = content.xpath('//*[@id="ContentPlaceHolder1_lbADDRESS"]/text()')[0].strip()
    except:
        jycd = ''

    #面积
    mj = ''

    #营业执照_经营范围
    try:
        yyzz_jyfw = content.xpath('//*[@id="ContentPlaceHolder1_lbSCOPE"]/text()')[0].strip()
    except:
        yyzz_jyfw = ''

    #营业执照_成立日期
    try:
        yyzz_clrq = content.xpath('//*[@id="ContentPlaceHolder1_lbSTTIME"]/text()')[0].strip()
    except:
        yyzz_clrq = ''

    #营业执照_注册资本金（万元）
    try:
        yyzz_zczbj = content.xpath('//*[@id="ContentPlaceHolder1_lbCAPTIAL"]/text()')[0].strip('万元')
    except:
        yyzz_zczbj = ''

    #营业执照_发证机关
    try:
        yyzz_fzjg = content.xpath('//*[@id="ContentPlaceHolder1_lbORGAN"]/text()')[0].strip()
    except:
        yyzz_fzjg = ''

    #营业执照_登记注册类型
    try:
        yyzz_djzclx = content.xpath('//*[@id="ContentPlaceHolder1_lbATTR"]/text()')[0].strip()
    except:
        yyzz_djzclx = ''

    #营业执照_注册号或（统一社会信用代码）
    try:
        yyzz_zch = content.xpath('//*[@id="ContentPlaceHolder1_lbUNSTID"]/text()')[0].strip()
    except:
        yyzz_zch = ''

    #营业执照_法定代表人
    try:
        yyzz_fddbr = content.xpath('//*[@id="ContentPlaceHolder1_lbLR"]/text()')[0].strip()
    except:
        yyzz_fddbr = ''


    content = etree.HTML(response.text)
    #组织机构代码证
    zzjgdmz_zzjgdmzh = ''
    #组织机构代码证_发证机关
    zzjgdmz_fzjg = ''
    #组织机构代码证_有效期至
    zzjgdmz_yxqz = ''
    #税务登记证_发证日期
    swdjz_fzrq = ''
    #税务登记证_税务登记证号
    swdjz_swdjzh = ''
    #税务登记证_发证机关
    swdjz_fzjg = ''

    #安全生产许可证_发证机关
    try:
        aqscxkz_fzjg = content.xpath('//*[@id="lbSAFEORGAN"]/text()')[0].strip()
    except:
        aqscxkz_fzjg = ''

    #安全生产许可证
    try:
        aqscxkz_aqscxk = content.xpath('//*[@id="lbSAFEID"]/text()')[0].strip()
    except:
        aqscxkz_aqscxk = ''

    # 社保登记证号_发证机关
    try:
        sbdjh_fzjg = content.xpath('//*[@id="lbSOCIALJG"]/text()')[0].strip()
    except:
        sbdjh_fzjg = ''

    # 社保登记证号
    try:
        sbdjh_sbdjz = content.xpath('//*[@id="lbSOCAILID"]/text()')[0].strip()
    except:
        sbdjh_sbdjz = ''

    # 可查询网站链接
    try:
        wzlink = content.xpath('//*[@id="lbHTTP"]/text()')[0].strip()
    except:
        wzlink = ''

    # 管理制度
    try:
        glzd = content.xpath('//*[@id="lbMANZD"]/text()')[0].strip()
    except:
        glzd = ''

    # 信用建设_是否有专职信用管理工作人员
    try:
        xyjs_is_glry = content.xpath('//*[@id="lbbCREDPER"]/text()')[0].strip()
    except:
        xyjs_is_glry = ''

    #信用建设_是否建立信用管理部门
    try:
        xyjs_is_jlglbm = content.xpath('//*[@id="lbbCREDIT"]/text()')[0].strip()
    except:
        xyjs_is_jlglbm = ''

    #信用建设信用建设_是否明确信用管理归口部门
    try:
        xyjs_is_mqglbm = content.xpath('//*[@id="lbbCREDZD"]/text()')[0].strip()
    except:
        xyjs_is_mqglbm = ''

    #注册地址
    try:
        zcdz_zcdz = content.xpath('//*[@id="lbREGADDRESS"]/text()')[0].strip()
    except:
        zcdz_zcdz = ''

    #注册地址_邮政编码
    try:
        zcdz_yzbm = content.xpath('//*[@id="lbREGPSCODE"]/text()')[0].strip()
    except:
        zcdz_yzbm = ''

    #经营地址
    jydz_zcdz = ''
    #经营地址_邮政编码
    jydz_yzbm = ''

    #单位网址
    try:
        wz_dwwz = content.xpath('//*[@id="lbWEBSITE"]/text()')[0].strip()
    except:
        wz_dwwz = ''

    #报告披露网址
    wz_plwz = ''
    #披露时间
    wz_plsj = ''

    #主营业务
    try:
        zyyw = content.xpath('//*[@id="MAINYW"]/text()')[0].strip()
    except:
        zyyw = ''

    # 子/分公司
    try:
        zfgs = ''
        for con in content.xpath('//*[@id="tb1"]/tr[1]/td/table/tbody/tr[*]'):
            id = con.xpath('td[1]/text()')[0].strip()
            lb = con.xpath('td[2]/text()')[0].strip()
            name = con.xpath('td[3]/text()')[0].strip()
            zcdz = con.xpath('td[4]/text()')[0].strip()
            gqbl = con.xpath('td[5]/text()')[0].strip()
            zfgs = zfgs + id + ',' + lb + ',' + name + ',' + zcdz + ',' + gqbl + ';'
    except:
        zfgs = ''

    # 管理认证体系
    try:
        glrztx = ''
        for con in content.xpath('//*[@id="tb2"]/tr[1]/td/table/tbody/tr[*]'):
            id = con.xpath('td[1]/text()')[0].strip()
            name = con.xpath('td[2]/text()')[0].strip()
            yer = con.xpath('td[3]/text()')[0].strip()
            yer2 = con.xpath('td[3]/text()')[0].strip()
            glrztx = glrztx + id + ',' + name + ',' + yer + ',' + yer2 + ';'

    except:
        glrztx = ''

    #单位历史沿革
    try:
        dwlsyg = ''
        for con in content.xpath('//*[@id="tb3"]/tr[1]/td/table/tbody/tr[*]'):
            id = con.xpath('td[1]/text()')[0].strip()
            name = con.xpath('td[2]/text()')[0].strip()
            yer = con.xpath('td[3]/text()')[0].strip()
            yer2 = con.xpath('td[3]/text()')[0].strip()
            dwlsyg = dwlsyg + id + ',' + name + ',' + yer + ',' + yer2 + ';'
    except:
        dwlsyg = ''

    #信息来源
    xxly = '全国水利建设市场信用信息平台'

    # 企业链接
    try:
        link = url
    except:
        link = ''
    #公司id
    sql = 'SELECT id FROM sc_gss_his where gsmc = %s'
    cursor.execute(sql, gsmc)
    gs_id = cursor.fetchall()

    #信用评价
    list_data = {}
    list = []
    print('信用评价...')
    url = 'http://rcpu.cwun.org/General/NJUDGE.aspx?id=%s'%(url_id)
    requests1 = get(url)
    requests1.encoding = "utf-8"
    html = requests1.text
    content = etree.HTML(html)
    for con in content.xpath('//*[@id="form1"]/table/tbody/tr[*]'):
        #类别
        try:
            lb = con.xpath('td[2]/text()')[0].strip()
        except:
            lb = ''
        #评价结果
        try:
            pjjg = con.xpath('td[3]/text()')[0].strip()
        except:
            pjjg = ''
        # 评价日期
        try:
            pjrq = con.xpath('td[4]/text()')[0].strip()
        except:
            pjrq = ''
        # 评价机构
        try:
            pjjgg = con.xpath('td[5]/text()')[0].strip()
        except:
            pjjgg = ''
        # 有效期至
        try:
            yxq = con.xpath('td[6]/text()')[0].strip()
        except:
            yxq = ''
        list_data = {
            'gs_id':gs_id,
            'gsmc': gsmc,
            'lb': lb,
            'pjjg': pjjg,
            'pjrq': pjrq,
            'pjjgg':pjjgg,
            'yxq': yxq,
            'link': link,
        }
        list.append(list_data)

    rtn_data = {
        'cj_id':cj_id,
        'gs_id':gs_id,
        'gsmc': gsmc,
        'ssss': ssss,
        'dwxz': dwxz,
        'jycd': jycd,
        'mj': mj,
        'yyzz_jyfw': yyzz_jyfw,
        'yyzz_clrq': yyzz_clrq,
        'yyzz_zczbj': yyzz_zczbj,
        'yyzz_fzjg': yyzz_fzjg,
        'yyzz_djzclx': yyzz_djzclx,
        'yyzz_zch': yyzz_zch,
        'yyzz_fddbr': yyzz_fddbr,
        'zfgs': zfgs,
        'zzjgdmz_zzjgdmzh': zzjgdmz_zzjgdmzh,
        'zzjgdmz_fzjg': zzjgdmz_fzjg,
        'zzjgdmz_yxqz': zzjgdmz_yxqz,
        'swdjz_fzrq': swdjz_fzrq,
        'swdjz_swdjzh': swdjz_swdjzh,
        'swdjz_fzjg': swdjz_fzjg,
        'aqscxkz_fzjg': aqscxkz_fzjg,
        'aqscxkz_aqscxk': aqscxkz_aqscxk,
        'sbdjh_fzjg': sbdjh_fzjg,
        'sbdjh_sbdjz': sbdjh_sbdjz,
        'wzlink': wzlink,
        'glrztx': glrztx,
        'glzd': glzd,
        'xyjs_is_glry': xyjs_is_glry,
        'xyjs_is_jlglbm': xyjs_is_jlglbm,
        'xyjs_is_mqglbm': xyjs_is_mqglbm,
        'zcdz_zcdz': zcdz_zcdz,
        'zcdz_yzbm': zcdz_yzbm,
        'jydz_zcdz': jydz_zcdz,
        'jydz_yzbm': jydz_yzbm,
        'wz_dwwz': wz_dwwz,
        'wz_plwz': wz_plwz,
        'wz_plsj': wz_plsj,
        'zyyw': zyyw,
        'dwlsyg': dwlsyg,
        'xxly': xxly,
        'link': link,
        'list':list
    }

    data_list.append(rtn_data)

    if rtn_data == {}:
        rtn_data = {
            'msg': 'find empty comp: ' + response.url
        }
        return rtn_data

    if ('items' not in rtn_data):
        rtn_data['items'] = []
    rtn_data['items'].append({'data': data_list})
    return rtn_data