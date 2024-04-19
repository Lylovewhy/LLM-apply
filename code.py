import dashscope
from dashscope import Generation
import json
import os

# 在这里加上api
dashscope.api_key = "sk-51f1c43097e841da9702aa7dd3909e65"

def get_response_product_manager(messages):
    response = Generation.call("qwen-turbo",
                                   messages=messages,
                                   result_format='message'
    )
    choice_message = response['output']['choices'][0]['message']

    # 从message中提取content的值
    extracted_text = choice_message['content']
    return response, extracted_text

def get_response_front_end_developer(messages):
    response = Generation.call("qwen-plus",
                                    messages=messages,
                                    result_format='code'
    )
    return response, response.output.text

def get_response_back_end_developer(messages):
    response = Generation.call("qwen-max",
                                    messages=messages,
                                    result_format='code'
    )
    return response, response.output.text

messages1 = [{'role': 'system', 'content': '你是一名产品经理，需要分析客户的需求并将其转化为具体的项目需求。'}]
messages2 = [{'role': 'system', 'content': '你是一名前端程序员，需要根据产品经理的需求来设计和实现用户界面，使用HTML/CSS/JS等语言生成代码并输出。'}]
messages3 = [{'role': 'system', 'content': '你是一名后端程序员，需要根据产品经理的需求以及前端工程师的界面来设计和实现服务器端逻辑，使用Java语言生成代码并输出'}]

print('欢迎来到Happpy软件公司，我们将共同开发新的项目。请输入您的需求，产品经理、前端程序员和后端程序员将为你提供解答。输入\'exit\'退出。')

# 读取输入文件
with open("input.json", 'r', encoding='utf-8') as file:
    requirements = json.load(file)

# 初始化输出文件
with open("./output_product_manager.json", 'w', encoding='utf-8') as write_f:
    write_f.write('[\n')
with open("./output_front_end_developer.json", 'w', encoding='utf-8') as write_f:
    write_f.write('[\n')
with open("./output_back_end_developer.json", 'w', encoding='utf-8') as write_f:
    write_f.write('[\n')

# 读取需求并分析
for i in range(len(requirements)):
    user_requirement = requirements[i]['requirement']

    if user_requirement == 'exit':
        print('感谢您的参与，期待下次合作。')
        break

    # 产品经理的分析
    messages1.append({'role': 'user', 'content': user_requirement})
    product_manager_response, product_manager_output = get_response_product_manager(messages1)
    messages1.append({'role': 'assistant', 'content': product_manager_output})

    print(f'用户需求：{user_requirement}')
    print(f'产品经理：{product_manager_output}\n')

    # 前端程序员的设计
    messages2.append({'role': 'user', 'content': product_manager_output})
    front_end_response, front_end_output = get_response_front_end_developer(messages2)
    messages2.append({'role': 'assistant', 'content': front_end_output})

    print(f'前端程序员：{front_end_output}\n')

    # 后端程序员的实现
    messages3.append({'role': 'user', 'content': product_manager_output})
    messages3.append({'role': 'user', 'content': front_end_output})
    back_end_response, back_end_output = get_response_back_end_developer(messages3)
    messages3.append({'role': 'assistant', 'content': back_end_output})

    print(f'后端程序员：{back_end_output}\n')

    # 写入文件
    with open("./output_product_manager.json", 'a', encoding='utf-8') as write_f:
        write_f.write(json.dumps({'step': '产品经理分析', 'content': product_manager_output}, indent=4, ensure_ascii=False) + ',\n')
    with open("./output_front_end_developer.json", 'a', encoding='utf-8') as write_f:
        write_f.write(json.dumps({'step': '前端代码实现', 'content': front_end_output}, indent=4, ensure_ascii=False) + ',\n')
    with open("./output_back_end_developer.json", 'a', encoding='utf-8') as write_f:
        write_f.write(json.dumps({'step': '后端代码实现', 'content': back_end_output}, indent=4, ensure_ascii=False) + ',\n')

# 结束文件
with open("./output_product_manager.json", 'rb+') as write_f:
    write_f.seek(-2, os.SEEK_END)
    write_f.truncate()
with open("./output_front_end_developer.json", 'rb+') as write_f:
    write_f.seek(-2, os.SEEK_END)
    write_f.truncate()
with open("./output_back_end_developer.json", 'rb+') as write_f:
    write_f.seek(-2, os.SEEK_END)
    write_f.truncate()

with open("./output_product_manager.json", 'a', encoding='utf-8') as write_f:
    write_f.write('\n]')
with open("./output_front_end_developer.json", 'a', encoding='utf-8') as write_f:
    write_f.write('\n]')
with open("./output_back_end_developer.json", 'a', encoding='utf-8') as write_f:
    write_f.write('\n]')