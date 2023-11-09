# 工具介绍
FourthDimension（第四维度）由华中科技大学人工智能与嵌入式实验室联合言图科技研发，是一款基于大语言模型的智能知识问答系统，提供私域知识库、文档问答等多种服务。此外，FourthDimension提供便捷的本地部署方法，方便用户在本地环境中搭建属于自己的应用平台。

### 工具特点
可在线使用API或本地部署专属知识库，自定义embedding模型和答案生成模型，根据自己的需求进行定制和优化。

### 主要功能
* 简单高效，用户只需配置API即可进行知识问答
* 高度定制化和数据安全的私域知识库
* 基于私域知识库的文档问答

# 工具使用

### 前置依赖项
- python3  
- Anaconda3  

> 使用前请检查Anaconda是否安装，若未安装可参照以下教程  
> [Anaconda详细安装过程](https://blog.csdn.net/weixin_43858830/article/details/134310118?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134310118%22%2C%22source%22%3A%22weixin_43858830%22%7D)

### 快速上手

1. 克隆项目存储库
```
git clone https://gitee.com/hustai/FourthDimension
```
```
cd FourthDimension
```
2. 创建相应虚拟环境
```
conda create -n FourthDimension python==3.8
```

```
conda activate FourthDimension
```
3. 安装前置依赖
```
pip install -r requirements.txt
```
安装核心依赖
```
pip install FourthDimension
```

4. 下载和启动相关配置（Elasticsearch）
```
sh es_install.sh
```

5. 使用  
使用前请将config.json配置文件置于脚本文件同级目录下

示例代码  
* 存储及检索
``` python 
import FourthDimension
answer = FourthDimension.query_storage('您的问题', '文档路径')
print(answer)
```
* 单检索  
该检索方法目前仅支持elasticsearch检索方式
``` python 
import FourthDimension
answer = FourthDimension.query('您的问题')
print(answer)
```
### 配置文件说明

存储/检索方式: `Elasticsearch + Faiss`

大语言模型：`GPT3.5-turbo-16k`

以上配置均可以在配置文件调整

配置文件

```xml
{
  //文档文本存储方式
  "word_storage": "elasticsearch",

  //文档向量存储方式
  "embedding_storage": "faiss",

  //检索方式选择，目前提供以下三种方式：
  //1.elasticsearch
  //2.faiss
  //3.elasticsearch+faiss
  "search_select": "elasticsearch",

  //embedding模型
  "embedding_model": "bge-large-zh-v1.5",

  //答案生成模型
  "answer_generation_model": "gpt-3.5-turbo-16k",

  //openai配置
  "openai": {
    //请在此处配置您的api key
    "api_key": "",
    //默认使用openai官方接口，可根据需求进行修改
    "url": "https://api.openai.com/v1"
  },

  //文档划分设置
  "para_config": {
    //文档划分段落长度
    "chunk_size": 500,
    //文档划分重叠度
    "overlap": 20
  },

  //召回设置
  "recall_config": {
    //指定使用多少召回结果进行答案生成
    "top_k": 10
  },

  //Elasticsearch设置
  "elasticsearch_setting": {
    //默认索引名称，可根据需求进行修改
    "index_name": "index",
    //默认为localhost，可根据具体需求修改
    "host": "localhost",
    "port": 9200,
    //若存在安全认证，则填写用户名和密码
    "username": "",
    "password": "",
    //Elasticsearch分词器
    "analyzer": "standard"
  },

  //Faiss设置
  "faiss_setting": {
    //索引方式
    "retrieval_way": "IndexFlatL2"
  }
}
```





# 论坛交流
微信群二维码

# 相关知识
- [基于检索增强的文本生成](https://hustai.gitee.io/zh/posts/rag/RetrieveTextGeneration.html)

- [如何通过大模型实现外挂知识库优化](https://hustai.gitee.io/zh/posts/rag/LLMretrieval.html)

 [更多相关知识分享————网站链接](https://hustai.tech/zh/)


