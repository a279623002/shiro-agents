##### 基于hello-agents
> git clone https://gitclone.com/github.com/datawhalechina/hello-agents.git


##### env
* miniconda
  1. python 3.11
  2. name shiro-agents
        ```
        # 查看版本
        conda --version
        # 查看安装包
        conda list
        # 配置国内镜像源
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
        conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
        conda config --set show_channel_urls yes
        # 删除镜像
        conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ 
        conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/ 
        conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/ 
        conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/ 
        conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro/
        # 创建环境
        conda create -n shiro-agents python=3.11
        # 查看环境
        conda env list
        # 删除环境
        conda env remove -n shiro-agents
        # 退出环境
        conda deactivate
        # 激活环境
        conda activate shiro-agents
        # 在环境中安装包
        conda install numpy pandas matplotlib
        # 或者
        pip install tensorflow
        # 临时更改镜像
        pip install SomePackage -i https://mirrors.aliyun.com/pypi/simple/
        ```
* tavily
  1. AI搜索API客户端
  2. 官网：https://www.tavily.com/
  3. 安装依赖库
    ```
    pip install tavily
    ```
* openai
  1. 用于调用GPT等大语言模型
  2. 安装依赖库
    ```
    pip install openai
    ```
* ModelScope
  > https://modelscope.cn/docs/model-service/API-Inference/intro
* requests
  1. 用于发送HTTP请求
  2. 安装依赖库
    ```
    pip install requests
    ```
