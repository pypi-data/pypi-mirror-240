# 知识库异步处理服务
## 1. 项目介绍

- 负责监听事件，执行相应任务.

- 事件来源于数据库和消息队列.




## 2. 使用Milvus来构建向量库
- default DB下的Collection
  * Collection - pub_knowledge_collection : 用于存放文档片段的向量化表示

- knowledge_saas DB下的Collection
  * Collection - user_knowledge_collection : 用于存放用户知识库的向量化表示