# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-09-26 8:29
# @Author : 张杰
# @Software: PyCharm

import requests

def get_dm(aid):
    page_text = requests.get(url=f"https://m.runoob.com/{aid}/").text
    
    
    return page_text

if __name__ == '__main__':
    st.write("hello")
    aid = st.text_input("请输入搜索词")
    title_list=get_dm(aid)
    st.write(title_list)
    st.write("over")
