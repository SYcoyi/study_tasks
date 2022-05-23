Feature: 安徽社区app用户端

  Scenario: 退款流程以及银行端手动退款等接口
    When 手机个人端登录获取验证码
    Then 手机个人端登录
    Then 生成团购商品
    Then 团购支付
    Then app团购退款
    When 获取图片验证码
    Then 银行端法人登陆
    Then 退款审核
    Then 银行端退款详情
    Then 银行端批量退款初审
    Then 银行端批量退款复审

  Scenario: 团购流程
    When 手机个人端登录获取验证码
    Then 手机个人端登录
    Then 生成团购商品
    Then 团购支付
    Then 获取团购码
    Given 商户端登陆
    Then 团购提货
    Then 团购客户评价
    Then 商品评价列表
    Then 商品评价回复

  Scenario: 名优特惠基础流程
    When 手机个人端登录获取验证码
    Then 手机个人端登录
    Then 生成名优特惠订单
    Then 名优特惠支付
    Given 商户端登陆
    Then 名优特惠发货
    Then 名优特惠确认收货
    Then 名优特惠物流评价
    Then 名优特惠客户评价
    Then 商品评价列表
    Then 商品评价回复

  Scenario: 二维码C扫B现金
    Given 商户端登陆
    Then 创建二维码订单
    When 手机个人端登录获取验证码
    Then 手机个人端登录
    Then 二维码现金支付

  Scenario: 二维码C扫B积分
    When 手机个人端登录获取验证码
    Then 手机个人端登录
    Then 积分商品支付

#  Scenario: 基础模块
#    When 手机个人端登录获取验证码
#    Then 手机个人端登录
#    When 手机个人端密码登录
#
#
#   Scenario: 修改用户密码
#     When 点击忘记密码
#     When 首次点击找回登陆密码
#     When 首次点击找回登陆密码，更新页面及图片验证码
#     When 找回登陆密码页面获取短信验证码