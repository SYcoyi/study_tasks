Feature: 安徽社区个人端创建/取消名优特惠订单

  Scenario:创建/取消普通名优特惠订单
    When 手机个人端密码登录   ##需增加接口
    Then 创建普通名优特惠订单         ##原接口名称：生成团购商品##/api/user/order/generate  团购/名优/预售订单创建使用同一个接口
    Then app取消订单

  Scenario:创建/取消仅限信用卡名优特惠订单
    When 手机个人端密码登录   ##需增加接口
    Then 创建仅限信用卡名优特惠订单          ##依ProductID进行区分
    Then app取消订单