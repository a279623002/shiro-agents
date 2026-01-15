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
* vllm
  1. 用于部署和运行大语言模型
  2. 安装依赖库
    ```
    # conda activate qwen2.5
    pip install pydantic==1.10.13
    # pip show vllm 0.13.0
    pip install vllm

    python -m vllm.entrypoints.openai.api_server \
      --model /Users/shiro/.cache/modelscope/hub/models/Qwen/Qwen1.5-0.5B-Chat \
      --trust-remote-code \
      --host 0.0.0.0 \
      --port 8001 \
      --served-model-name qwen1.5-0.5b-chat
    ```     
## git 命令
* 查看当前状态（可查看当前所在分支和修改添加后的文件）
  ```sh
  git status
  ```
* 提交所有文件
  ```sh
  git add .
  ```
* 提交文件到本地暂存区
  ```sh
  git commit -m "提交信息"
  ```
* 推送到仓库
  ```sh
  git push origin main
  ```
## Linux 命令
* 查看当前目录
  ```sh
  pwd
  ```
* 查看当前目录下的文件
  ```sh
  ls
  ```
* 查看当前目录下的文件（包含隐藏文件）
  ```sh
  ls -a
  ```
* 切换目录
  ```sh
  cd 目录名
  ```
* 切换到上一级目录
  ```sh
  cd ..
  ```
* 切换到根目录
  ```sh
  cd /
  ``` 
* 切换到当前用户的主目录
  ```sh
  cd ~
  ```
* 查看当前用户
  ```sh
  whoami
  ```
## vim 编辑器
* 打开文件
  ```sh
  vim 文件名
  ```
* 进入插入模式
  ```sh
  i
  ```
* 退出插入模式
  ```sh
  Esc
  ```
* 保存并退出
  ```sh
  :wq
  ```
* 仅退出不保存
  ```sh
  :q!
  ```
## conda 命令
* 查看当前环境
  ```sh
  conda env list
  ```
* 激活环境
  ```sh
  conda activate 环境名
  ```
* 退出环境
  ```sh
  conda deactivate
  ```
* 创建环境
  ```sh
  conda create -n 环境名 python=3.11
  ```
* 删除环境
  ```sh
  conda env remove -n 环境名
  ```
* pip 安装依赖库
  ```sh
  pip install 依赖库名 -i https://mirrors.aliyun.com/pypi/simple/
  ```



