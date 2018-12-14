#张峻珲
#全国水利建设(业绩信息+信用评价)
from scrapy import Field, Item

class sljs_jbxx_detail_item(Item):
    cj_id = Field() #水利局公司基本信息采集表id
    gs_id = Field()  # 公司表id
    gsmc = Field()  # 公司名称
    ssss = Field()  # 所属省市
    dwxz = Field()  # 单位性质
    jycd = Field()  # 办公/生产/经营场地
    mj = Field()  # 面积
    yyzz_jyfw = Field()  # 营业执照_经营范围
    yyzz_clrq = Field()  # 营业执照_成立日期
    yyzz_zczbj = Field()  # 营业执照_注册资本金（万元）
    yyzz_fzjg = Field()  # 营业执照_发证机关
    yyzz_djzclx = Field()  # 营业执照_登记注册类型
    yyzz_zch = Field()  # 营业执照_注册号或（统一社会信用代码）
    yyzz_fddbr = Field()  # 营业执照_法定代表人
    zfgs = Field()  # 子/分公司
    zzjgdmz_zzjgdmzh = Field()  # 组织机构代码证
    zzjgdmz_fzjg = Field()  # 组织机构代码证_发证机关
    zzjgdmz_yxqz = Field()  # 组织机构代码证_有效期至
    swdjz_fzrq = Field()  # 税务登记证_发证日期
    swdjz_swdjzh = Field()  # 税务登记证_税务登记证号
    swdjz_fzjg = Field()  # 税务登记证_发证机关
    aqscxkz_fzjg = Field()  # 安全生产许可证_发证机关
    aqscxkz_aqscxk = Field()  # 安全生产许可证
    sbdjh_fzjg = Field()  # 社保登记证号_发证机关
    sbdjh_sbdjz = Field()  # 社保登记证号
    wzlink = Field()  # 可查询网站链接
    glrztx = Field()  # 管理认证体系
    glzd = Field()  # 管理制度
    xyjs_is_glry = Field()  # 信用建设_是否有专职信用管理工作人员
    xyjs_is_jlglbm = Field()  # 信用建设_是否建立信用管理部门
    xyjs_is_mqglbm = Field()  # 信用建设信用建设_是否明确信用管理归口部门
    zcdz_zcdz = Field()  # 注册地址
    zcdz_yzbm = Field()  # 注册地址_邮政编码
    jydz_zcdz = Field()  # 经营地址
    jydz_yzbm = Field()  # 经营地址_邮政编码
    wz_dwwz = Field()  # 单位网址
    wz_plwz = Field()  # 报告披露网址
    wz_plsj = Field()  # 披露时间
    zyyw = Field()  # 主营业务
    dwlsyg = Field()  # 单位历史沿革
    created = Field()  # 写入时间
    modified = Field()  # 修改时间
    valid = Field()  # 1：有效数据 0：无效
    xxly = Field()  # 信息来源
    link = Field()  # 企业链接
    items = Field()

    #信用评价
    lb = Field() #类别
    pjjg = Field()  # 评价结果
    pjrq = Field()  # 评价日期
    pjjgg = Field()  # 评价机构
    yxq = Field()  # 有效期至
    list = Field()


    pipline_func = Field()  # 每一个item中都默认加上




