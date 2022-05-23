Feature: 安徽社区团购商品提货人信息

  Scenario: 新增团购提货人
    When 手机个人端密码登录
    Then 新增团购提货人    #/api/user/receiver/update


  Scenario:团购提货人列表展示
    When 手机个人端密码登录
    Then 团购提货人列表    #/api/user/receiver/list