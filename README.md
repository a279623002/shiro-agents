##### 基于hello-agents
> https://github.com/datawhalechina/hello-agents.git

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
        ```

