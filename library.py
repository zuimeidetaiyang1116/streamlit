# -*- codeing = utf-8 -*-
# 中文乱码问题
# @Time : 2022-09-26 8:29
# @Author : 张杰
# @Software: PyCharm

import requests
from lxml import etree

def get_dm(aid):
    page_text = requests.get(url=f"https://m.runoob.com/{aid}/").text
    # print(page_text)
    tree=etree.HTML(page_text)
    content_list=tree.xpath('//*[@class="post_box"]')
    title_list = []
    for content in content_list:
        title_list.extend(content.xpath('a/h2/text()'))
    return title_list

if __name__ == '__main__':
    st.header("hello")
    aid = st.text_input("请输入搜索词")
    title_list=get_dm(aid)
    st.write(title_list)
    st.write("over")
