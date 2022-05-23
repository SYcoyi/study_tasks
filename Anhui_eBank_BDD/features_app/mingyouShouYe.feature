Feature: 安徽社区团购商品展示

  Scenario:首页热门团购商品
    When 首页热门团购商品  #/api/user/product/top

  Scenario: 团购商品列表
    When 首页查看更多团购商品   #/api/user/product/group/search
    Then 团购商品列表页_筛选   #/api/user/product/group/search  筛选类型：商品类别、位置、排序方式
    Then 团购商品列表页_商品搜索   #/anhui/m/cheapList

