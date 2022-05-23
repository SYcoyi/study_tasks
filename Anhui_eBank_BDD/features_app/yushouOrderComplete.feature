Feature: 安徽社区个人端精品预售订单流程

  Scenario:精品预售订单流程
    When 手机个人端密码登录       ##需增加接口
    Then 创建普通精品预售订单_配送方式         ##/api/user/order/generate  团购/名优/预售订单创建使用同一个接口  参数不同
    Then 现金支付     #/api/user/cashier/payOrders
    Then 

