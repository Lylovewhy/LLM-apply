1、实验环境：python。
2、所需要安装的包： dashscope。
3、需要去通义千问官网注册以获得api key。
4、prompt.txt是对三种模型的系统提示。
5、input.json是用户的输入。
4、我们的多智能体协作框架主要应用在软件开发场景，qwen-turbo作为产品开发模型，qwen-plus作为前端程序员模型，qwen-max作为后端程序员模型。
运行code.py代码可以实现这个场景。三种模型的输出分别在output_product_manager.json、output_front_end_developer.json、output_back_end_developer.json文件中。
5、作为对照实验，用普通的单一的qwen-turbo模型来完成整个软件开发的流程。运行single.py可以实现。模型的输出在output_single.json文件中。
