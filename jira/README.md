### jira 统计分析

方法:

  - 从jira 定制查询你的query     
  - export all field to CSV
  - 运行脚本，如: 

    ```
        python3 point-bar.py story-point.csv 
        python3 project.py project-point.csv
    ``` 

注意：此方案当初是为了练习python plot，非最佳方案（jira 上直接写script, 直连jira 的数据库）

todo:

  -   图：pythonEchart
  -   html : 页面搞点排版 
  -   自动下载 
