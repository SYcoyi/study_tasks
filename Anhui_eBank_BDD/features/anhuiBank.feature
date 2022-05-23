Feature: 安徽社区e银行_银行端自动化用例集


  Scenario: 审核系列列表
    When 获取图片验证码
    Then 银行端法人登陆
    Then 待审核商户列表
    Then 商户分类
    Then 待审核品牌列表
    Then 待审核团购列表
    Then 待审核线下礼品列表
    Then 待审核名优特惠列表
    Then 待审核预售列表

  Scenario: 审核箱详情页面接口
    When 获取图片验证码
    Then 银行端法人登陆
    Then 审核监控列表
    Then 审核监控详情
    Then 综合查询列表
    Then 综合查询详情

  Scenario: 积分对端系列接口
    When 获取图片验证码
    Then 银行端法人登陆
    Then 积分礼品列表
    Then 积分礼品详情
    Then 积分礼品新增
    Then 积分礼品图片上传探测
    Then 待审核线下礼品列表
    Then 积分礼品审核详情
    Then 积分礼品审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 积分礼品审核详情
    Then 积分礼品审核
    Then 积分礼品下架
    Then 积分礼品上架
    Then 积分礼品下架
    Then 积分礼品删除

  Scenario: 各模块列表页面请求
    When 获取图片验证码
    Then 银行端法人登陆
    Then 团购订单列表
    Then 团购列表详情
    Then 预售订单列表
    Then 预售订单详情
    Then 预售订单限时特价详情
    Then 面对面订单列表
    Then 面对面订单详情
    Then 名优特惠订单列表
    Then 名优特惠订单详情
    Then 名优特惠订单限时特价详情
    Then 积分兑换订单列表
    Then 积分兑换订单详情
    Then 积分报表中购物订单明细
    Then 积分报表银行积分总计
    Then 积分报表商户总和
    Then 精品商城订单列表
    Then 积分报表列表
    Then 异常订单管理列表
    Then 结算查询列表
    Then 结算查询详情

  Scenario: 交易列表页面请求
    When 获取图片验证码
    Then 银行端法人登陆
    Then 支付查询列表
    Then 退款查询列表
    Then 退款查询详情
    Then 预售账单查询
    Then 账单查询
    Then 退款审核
    Then 商户管理列表
    Then 商户详情
    Then 商户新增所属分类查询
    Then 商户新增之商户类型
    Then 附加功能列表
    Then 商户新增之所属机构
    Then 商户信息

  Scenario: 商品互动列表页面请求
    When 获取图片验证码
    Then 银行端法人登陆
    Then 商户新增之地址
    Then 门店管理列表
    Then 商户聊天记录列表
    Then 商户星级管理列表
    Then 商品星级管理列表
    Then 物流评价列表
    Then 银行商户评价列表
    Then 银行商品评价列表
    Then 点赞汇总统计列表
    Then 预售商品列表
    Then 提货查询列表
    Then 提货查询列表导出
    Then 团购商品信息列表
    Then 团购商品信息详情
    Then 团购商品信息上下架
    Then 团购商品信息列表
    Then 团购商品信息上下架


  Scenario: 组织相关列表页面请求
    When 获取图片验证码
    Then 银行端法人登陆
    Then 名优特惠商品列表
    Then 新增之发货商户查询
    Then 品牌管理列表
    Then 品牌管理广告列表
    Then 品牌排序列表
    Then 操作日志列表
    Then 新增组织之组织信息获取
    Then 新增组织之用户列表查询
    Then 新增组织之地址查询
    Then 新增用户之角色查询
    Then 组织查询
    Then 授权资源列表
    Then 用户信息查询

  Scenario: 广告列表页面请求
    When 获取图片验证码
    Then 银行端法人登陆
    Then 广告管理查询
    Then 广告详情之地区查询
    Then 广告详情之广告位查询

  Scenario: 新增操作接口
    When 获取图片验证码
    Then 银行端法人登陆
    Then 新增商户
    Then 精品预售商品新增
    Then 线下券码导入之获取商品信息
    Then 名优特惠商品新增
    Then 新增组织机构
    Then 银行端编辑组织
    Then 银行端新增用户
    Then 角色新增

  Scenario: 查询接口批量请求需要省联社操作部分
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核限时特价活动列表
    Then 限时特价活动列表

  Scenario: 新增商户全流程接口-涉及品牌
    When 获取图片验证码
    Then 银行端法人登陆
    Then 新增商户
    Then 待审核商户列表-依赖查询
    Then 待审核商户详情
    Then 商户的审核-法人审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核商户列表-省联社依赖查询
    Then 商户的审核-省联社审核
    When 获取图片验证码
    Then 银行端法人登陆
    Then 银行端商户编辑
    Then 待审核商户列表-依赖查询
    Then 商户的审核-法人审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核商户列表-省联社依赖查询
    Then 商户的审核-省联社审核
    When 获取图片验证码
    Then 银行端法人登陆
    Then 银行端商户重置密码
    Then 品牌新增
    Then 待审核品牌列表-名称查询
    Then 品牌详情
    Then 品牌审核-法人行社
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核品牌列表-名称查询-省联社查询
    Then 品牌详情
    Then 品牌审核-省联社
    Given 商户端登陆
    Then 商户端添加团购商品
    When 获取图片验证码
    Then 银行端法人登陆
    Then 待审核团购列表
    Then 待审核团购详情
    Then 团购审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核团购列表
    Then 团购审核

  Scenario: 名优特惠审核系列
    When 获取图片验证码
    Then 银行端法人登陆
    Then 名优特惠商品新增
    Then 待审核名优特惠列表
    Then 待审核名优特惠详情
    Then 名优特惠审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核名优特惠详情
    Then 名优特惠审核
    Then 名优特惠商品列表
    Then 名优特惠商品下架
    Then 名优特惠商品上架
    Then 名优特惠商品详情
#    Then 名优特惠商品修改
    Then 名优特惠商品下架
    Then 名优特惠商品删除

  Scenario: 精品预售审核系列
    When 获取图片验证码
    Then 银行端法人登陆
    Then 精品预售商品新增
    Then 待审核预售列表
    Then 待审核精品预售详情
    Then 精品预售审核
    When 获取图片验证码
    Then 银行端省联社登录
    Then 待审核精品预售详情
    Then 精品预售审核
    Then 预售商品列表
    Then 精品预售商品详情
#    Then 精品预售商品修改
    Then 商户管理列表
    Then 精品预售商品上架
    Then 精品预售商品下架

    Then 银行端商户禁用
    Then 银行端商户启用
    Then 银行端商户解约
    Then 精品预售商品删除


  Scenario: 门店相关
    When 获取图片验证码
    Then 银行端法人登陆
    Then 门店详情

##  Scenario: 系统设置类操作 # 请勿执行
##    When 获取图片验证码
##    Then 银行端法人登陆
##    Then 银行端修改密码旧
