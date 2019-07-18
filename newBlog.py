# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:01:23 2019

@author: levon
"""

data1 = r'''<!DOCTYPE html>
<html class="theme-next mist use-motion">

<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <meta http-equiv="Cache-Control" content="no-transform">
    <meta http-equiv="Cache-Control" content="no-siteapp">
    <link href="app.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" id="hexo.configuration">
        var NexT = window.NexT || {};
        var CONFIG = {
            scheme: 'Mist',
            sidebar: { "position": "left", "display": "post" },
            fancybox: true,
            motion: true,
            duoshuo: {
                userId: undefined,
                author: 'levon'
            }
        };
    </script>
    <title> 标签 | levon's Blog </title>
</head>

<body itemscope="" itemtype="http://schema.org/WebPage" class="" style="padding-right: 0px;" lang="zh-Hans">
    <div class="container one-collumn sidebar-position-left page-post-detail ">
        <div class="headband"></div>
         <header id="header" class="header" itemscope itemtype="http://schema.org/WPHeader">
            <div class="header-inner">
                <div class="site-meta ">
                    <div class="custom-logo-site-title"> <a href="/novel" class="brand" rel="start">
                            <span class="logo-line-before"><i></i></span> <span class="site-title">Levon's Blog</span>
                            <span class="logo-line-after"><i></i></span> </a> </div>
                    <p class="site-subtitle"></p>
                </div>
                <nav class="site-nav">
                    <ul id="menu" class="menu">
                        <li class="menu-item menu-item-about"> <a href="/novel" rel="section"> <i
                                    class="menu-item-icon fa fa-fw fa-user"></i> <br />
                                目录 </a> </li>
                    </ul>
                </nav>
            </div>
        </header>
        <main id="main" class="main">
            <div class="main-inner">
                <div class="content-wrap">
                    <div id="content" class="content">
                        <div id="posts" class="posts-expand">
                            <article class="post post-type-normal" itemscope="" itemtype="http://schema.org/Article"
                                style="opacity: 1; display: block; transform: translateY(0px);">
                                <header class="post-header">
                                    <h1 class="post-title" itemprop="name headline">
                                        标题
                                    </h1>
                                    <div class="post-meta">
                                        <span class="post-time">
                                            <span class="post-meta-item-icon">
                                                <i class="fa fa-calendar-o"></i>
                                            </span>
                                            <span class="post-meta-item-text">发表于</span>
                                            <time itemprop="dateCreated" datetime="2017-07-03T21:33:12+08:00"
                                                content="2017-07-03">
                                                2019-07-03
                                            </time>
                                        </span>
                                    </div>
                                </header>

                                <div class="post-body" itemprop="articleBody">
                                    <p>hello world!</p>
                                </div>
                                <footer class="post-footer">
                                    <div class="post-nav">
                                        <div class="post-nav-next post-nav-item"> <a href="index'''

data2 = r'''.html" rel="next"> 上一篇
                                            </a> </div>
                                        <div class="post-nav-prev post-nav-item"> <a href="index'''
data3 = r'''.html" rel="prev"> 下一篇
                                            </a> </div>
                                    </div>
                                </footer>
                            </article>
                        </div>
                    </div>
                </div>
            </div>
        </main>
        <footer id="footer" class="footer">
            <div class="footer-inner">
                <div class="copyright">

                    © 2019 -
                    <span itemprop="copyrightYear">2019</span>
                    <span class="author" itemprop="copyrightHolder">Levon</span>
                </div>
                <div class="powered-by">
                    由 <a class="theme-link" href="http://hexo.io/">Hexo</a> 强力驱动
                </div>
                <div class="theme-info">
                    主题 -
                    <a class="theme-link" href="https://github.com/iissnan/hexo-theme-next">
                        NexT.Mist
                    </a>
                </div>
            </div>
        </footer>
        <div class="back-to-top back-to-top-on">
            <svg class="Zi Zi--BackToTop" title="回到顶部" fill="currentColor" viewBox="0 0 24 24" width="24" height="24">
                <path
                    d="M16.036 19.59a1 1 0 0 1-.997.995H9.032a.996.996 0 0 1-.997-.996v-7.005H5.03c-1.1 0-1.36-.633-.578-1.416L11.33 4.29a1.003 1.003 0 0 1 1.412 0l6.878 6.88c.782.78.523 1.415-.58 1.415h-3.004v7.005z">
                </path>
            </svg>
        </div>
    </div>
    <script type="text/javascript" src="index.js"></script>
    <script type="text/javascript" src="jquery.js"></script>
    <script type="text/javascript" src="velocity.js"></script>
    <script type="text/javascript" src="velocity_002.js"></script>
    <script type="text/javascript" src="jquery_002.js"></script>
    <script type="text/javascript" src="utils.js"></script>
    <script type="text/javascript" src="motion.js"></script>
    <script type="text/javascript" src="scrollspy.js"></script>
    <script type="text/javascript" src="bootstrap.js"></script>
</body>

</html>'''

from bs4 import BeautifulSoup

with open('index.html', 'r+') as f:
    page = f.read()
    
    html = BeautifulSoup(page,"html.parser")
    ctx = html.find('div', class_='post-body')
    i = len(ctx.find_all('a')) + 1
    
    br = html.new_tag('br')
    ctx.append(br)

    newAddr = html.new_tag('a')
    newAddr.attrs["href"] = "index" + str(i) + ".html"
    newAddr.string = 'new blog title' + str(i)
    
    ctx.append(newAddr)
    f.seek(0)
    f.truncate()
    f.write(str(html.prettify()))

filename = 'index' + str(i) + '.html'
with open(filename, 'w') as f:
    f.write(data1+str(i-1)+data2+str(i+1)+data3)


