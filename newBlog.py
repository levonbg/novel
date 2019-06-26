# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:01:23 2019

@author: levon
"""

data1 = r'''<!DOCTYPE html>
<html data-theme="light" data-focus-visible="" lang="zh">

<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <title>你好，世界！</title>
    <link href="app.css" rel="stylesheet">
</head>

<body class="WhiteBg-body">
    <div id="root">
        <div class="App" data-reactroot="">
            <main role="main" class="App-main">
                <div class="Post-content">
                    <article class="Post-Main Post-NormalMain" tabindex="-1">
                        <header class="Post-Header">
                            <h1 class="Post-Title">你好世界</h1>
                        </header>
                        <div class="Post-RichTextContainer">
                            <div class="RichText ztext Post-RichText">
                                <p>你好世界</p>
                            </div>
                        </div>
                        <div class="ContentItem-time">发布于 2019-06-13</div>
                        <div class="Post-topicsAndReviewer">
                            <div class="TopicList Post-Topics">
                                <div class="Tag Topic"> <span class="Tag-content"><a class="TopicLink"
                                            href="index'''

data2 = r'''.html">
                                            <div class="Popover">
                                                <div id="Popover4-toggle" aria-haspopup="true" aria-expanded="false"
                                                    aria-owns="Popover4-content">上一篇</div>
                                            </div>
                                        </a></span></div>
                                <div class="Tag Topic"> <span class="Tag-content"><a class="TopicLink"
                                            href="index'''
data3 = r'''.html">
                                            <div class="Popover">
                                                <div id="Popover4-toggle" aria-haspopup="true" aria-expanded="false"
                                                    aria-owns="Popover4-content">下一篇</div>
                                            </div>
                                        </a></span></div>
                            </div>
                        </div>
                    </article>
                </div>
            </main>
        </div>
    </div>
</body>

</html>'''

from bs4 import BeautifulSoup

with open('index.html', 'r+') as f:
    page = f.read()
    
    html = BeautifulSoup(page,"html.parser")
    ctx = html.find('div', class_='RichText ztext Post-RichText')
    i = len(ctx.find_all('p')) + 1
    
    newAddr = html.new_tag('a')
    newAddr.attrs["href"] = "index" + str(i) + ".html"
    newAddr.string = 'new blog title' + str(i)
    
    newBlog = html.new_tag('p')
    newBlog.append(newAddr)
    ctx.append(newBlog)
    f.seek(0)
    f.truncate()
    f.write(str(html.prettify()))

filename = 'index' + str(i) + '.html'
with open(filename, 'w') as f:
    f.write(data1+str(i-1)+data2+str(i+1)+data3)


