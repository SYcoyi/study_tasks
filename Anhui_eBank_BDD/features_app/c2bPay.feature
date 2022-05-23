Feature: 安徽社区个人端登录


  Scenario: 手机号密码登录成功
    Given 商户app端登录
    Then
    When 手机个人端密码登录     #/api/user/login/login
    Then 展示


