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


messages1 = [{'role': 'system', 'content': '你是一名产品经验丰富的程序员，请你分析用户的需求，并完成前后端代码的编程。'}]


print('欢迎来到Happpy软件公司，我们将共同开发新的项目。请输入您的需求，我们有经验丰富的程序员将为你提供解答。输入\'exit\'退出。')

# 读取输入文件
with open("input.json", 'r', encoding='utf-8') as file:
    requirements = json.load(file)

# 初始化输出文件
with open("./output_single.json", 'w', encoding='utf-8') as write_f:
    write_f.write('[\n')

# 读取需求并分析
for i in range(len(requirements)):
    user_requirement = requirements[i]['requirement']

    if user_requirement == 'exit':
        print('感谢您的参与，期待下次合作。')
        break


    messages1.append({'role': 'user', 'content': user_requirement})
    product_manager_response, product_manager_output = get_response_product_manager(messages1)
    messages1.append({'role': 'assistant', 'content': product_manager_output})

 

    # 写入文件
    with open("./output_single.json", 'a', encoding='utf-8') as write_f:
        write_f.write(json.dumps({'step': '产品经理分析', 'content': product_manager_output}, indent=4, ensure_ascii=False) + ',\n')
 

# 结束文件
with open("./output_single.json", 'rb+') as write_f:
    write_f.seek(-2, os.SEEK_END)
    write_f.truncate()


with open("./output_single.json", 'a', encoding='utf-8') as write_f:
    write_f.write('\n]')
