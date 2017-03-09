'''
Created on 2017年3月9日

@author: lecea1995
'''

## -*- coding: utf-8 -*-

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas=[]#列表

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')#输出到output.html中,w为写模式
        fout.write('<html>')
        fout.write("<head><meta charset='utf-8' \></head>")
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            fout.write('<tr>')
            fout.write("<td> %s </td>" % data['url'])
            fout.write("<td> %s </td>" % data['title'])
            fout.write("<td> %s </td>" % data['summary'])
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        fout.close()
    
    
    
    



