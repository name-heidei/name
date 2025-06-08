import easygui as ei
#coding:utf-8
class ku:
    def __init__(self):
        pass
    def return1(self,dizhi):
        self.dizhi=dizhi
        with open(self.dizhi, 'r', encoding='utf-8') as f:
            self.c = f.read()
            if len(self.c) in [0,1]:
                ei.msgbox('你当前仓库没有数据')

            return self.c
    def addend(self,dizhi):
        try:
            self.dizhi=dizhi
            with open(self.dizhi, 'r', encoding='utf-8') as f:

                cs = eval(f.read())  # 读取原有列表

        except  (FileNotFoundError, SyntaxError, TypeError, AssertionError) as e:
                ei.msgbox(f"数据异常可能是空的{e}")
                cs = []

        r = ei.enterbox(msg='请输入您想添加的商品',default='')
        r1 = ei.enterbox(msg='请输入你商品专属id值',default='')
        nameid = ei.enterbox(msg='请告诉我你需要输入进去的商品什么类型比如食物生活用品或者衣服',default='')
        if nameid=='生活':
            r1+='ds'
        elif nameid=='食物':
            r1+='dw'
        elif nameid=='衣服':
            r1+='df'
        print(type(cs))
        print(cs)
        an = False

        for i in cs:
            for j in i:
                if j == nameid:
                    an = True
                    break
            if an:
                name_val = {r1: r}
                i[j].update(name_val)
                break
        if an != True:
            cl = {nameid: {r1: r}}
            try:
                cs.append(cl)
            except AttributeError:
                cs.append(cl)
            print(cl)

        with open(self.dizhi, 'w', encoding='utf-8') as f:
            try:

                if an != True:
                    f.write(str(cs))
                    ei.msgbox('添加成功')
                else:
                    f.write(str(cs))
                    ei.msgbox('添加成功')
            except  (FileNotFoundError, SyntaxError):

                pass

    def shanchu(self,dizhi):
        self.dizhi=dizhi
        with open(self.dizhi, 'w', encoding='utf-8') as f:
            f.write('')
            ei.msgbox('操作完成库已经清空')
    def xiugai(self,dizhi):
        try:
            self.dizhi=dizhi
            with open(self.dizhi, 'r', encoding='utf-8') as f:
                a = f.read()
                print(a)
                a = eval(a)

                ass={}
                for i in a:

                    ass.update(i)

                i2 = ei.enterbox(msg=f'请输入你想修改的值的主属性的数据\n具体数据{a}')
                i = ei.enterbox(msg=f'请输入你需要修改的值id\n具体数据{a}')
                i1 = ei.enterbox(msg=f'请输入你想要修改后的\n具体数据{a}')
                if None in [i2,i,i1]:
                    ei.msgbox('操作员没有输入数据')
                    return None

                self.fuxie(ass, i, i1, i2,self.dizhi)
        except SyntaxError as e:

            ei.msgbox(f'你的仓库是空的请添加了数据再来{e}')
    def fuxie(self,name,name1,name2,i2,dizhi):
        self.dizhi=dizhi
        self.c=name

        try:
            self.c[i2][name1]=name2
            with open(self.dizhi, 'w', encoding='utf-8') as f:
                self.c=[self.c]
                f.write(str(self.c))
        except KeyError as e:
            ei.msgbox(f'你想要修改的值不存在{e}')

    def del_val(self,dizhi):

        try:
            self.dizhi=dizhi
            with open(self.dizhi, 'r', encoding='utf-8') as f:
                cs = f.read()
                # print(cs)
            if len(cs) in [0, 1]:
                ei.msgbox('当前仓库没有数据请添加数据再来')
                return ('当前仓库没有数据请添加数据再来')
            try:
                cs = eval(cs)

            except  (FileNotFoundError, SyntaxError, TypeError, AssertionError):
                ei.msgbox('数据解析异常请重新检测数据格式')
                return '数据解析异常请重新检测数据格式'

            i3 = ei.enterbox(msg=f'请输入你需要删除的数据的大类，如生活，食物的\n具体数据有{cs}')
            i1 = ei.enterbox(msg=f'请输入你需要删除数据的专属id\n具体数据{cs}')
            if None in [i3,i1]:
                ei.msgbox('程序错误操作员没有加入数据')
                return None
            csw = True
            c=0
            vc=0
            try:

                cql=0
                cql1 = 0
                for j in cs:
                    for i in j:
                        if i3 == i:
                            print(i)
                            cql1 = 1
                            break
                        cql += 1
                    if cql1 == 1:
                        for i in cs[cql]:
                            for ij in cs[cql][i]:
                                if i1 == ij:
                                    del cs[cql][i][ij]
                                    cql1 = 2
                                    break
                            if cql1 == 2:
                                break
                    if cql1 == 2:
                        break
            except KeyError:
                return '你需要删除的数据不存在'

            cs = str(cs)
            with open(self.dizhi, 'w', encoding='utf-8') as f:
                if len(cs) in [0, 1]:
                    ei.msgbox('当前的数据当中已经没有东西了你都删除完了')
                    return '当前的数据当中已经没有东西了你都删除完了'
                f.write(cs)
        except(FileNotFoundError, SyntaxError, TypeError, AssertionError) as e:
            ei.msgbox('你的仓库没有数据了请先添加在来')
            return '你的仓库没有数据了请先添加在来'
    def erfen(self,dizhi):
        self.dizhi=dizhi
        with open(self.dizhi, 'r', encoding='utf-8') as f:
            cs = f.read()
            cs=eval(cs)
        anda=ei.choicebox(msg='请问你想要查找的是总类还是子类',title='选择器',choices=['大类','小类'])
        if anda=='大类':
            c=0
            cname=ei.enterbox(msg='请输入你需要查找的数据')
            print(cname)
            for i in cs:
                print(i)
                for j in i:
                    c+=1
                    if j == cname:
                        print('你查找的数据的索引位置',c)
                        print('您查找的数据里面包含有')
                        for ji in i:
                            print(i[ji])
            else:
                return '你输入的值不存在'
        elif anda=='小类':
            bname=0
            cname=ei.enterbox(msg='请输入你想要查找的数据')
            for i in cs:
                for j in i:
                    for ji in i[j]:
                        if i[j][ji] == cname:
                            print('您查找的数据存在')
                            print('他存在于',j,ji)
                            bname=1
                    if bname==1:
                        break
                if bname == 1:
                    break
            if bname==0:
                print('没有查找到你需要的数据')




class guanli:
    def __init__(self,dizhi):
        self.dizhi=dizhi
        self.ku=ku()
        while True:
            anname=ei.choicebox(msg='请选择你需要的操作有 1,添加商品 2,查看 3,修改 4,退出 5,删除 6,指定查询',title='仓库管理系统',choices=['1,添加','2,查看','3,修改','4,退出','5,删除','删库跑路','指定查询'])

            if anname in ['1','添加','1,添加']:

                self.ku.addend(self.dizhi)

            elif anname in ['2','查看','2,查看']:

                self.shujuchakan(self.dizhi)

            elif anname in ['指定查询']:

                self.ku.erfen(self.dizhi)

            elif anname in ['3','修改','3,修改']:
                c=self.ku.xiugai(self.dizhi)
                if c==None:
                    ei.msgbox('请操作员重新操作')
            elif anname in ['4','退出','4,退出']:

                ei.msgbox('《《感谢使用》》本操作系统欢迎下次使用')
                break
            elif anname in ['5','删除','5,删除']:

                c=self.ku.del_val(self.dizhi)
                if c==None:
                    ei.msgbox('请操作员重新操作')

            elif anname in ['删除所有','scxd',23923,'删库跑路']:

                i=ei.enterbox('你当前选择的操作非常危险我需要确定一下权限密钥')

                if i=='23923':
                    print('你好管理员')
                    print('你确定使用当前的操作吗这是最后的一次询问')
                    ida=ei.enterbox(f'你好管理员\n你确定使用当前的操作吗这是最后的一次询问\n！！！！！！！！！！如果确定请输入确定或者是')
                    # ida=input('')
                    if ida in ['是','确定','我同意']:
                        self.ku.shanchu(self.dizhi)
                        ei.msgbox('英雄不问出处,技术不问来路，江湖再见我先跑了不然老板要找我麻烦了')
                        break
            elif anname==None:
                print('用户取消了操作')
                break
            else:
                print('你输入的操作错误请重新输入')

    def shujuchakan(self,dizhi):
        self.dizhi=dizhi
        name=self.ku.return1(self.dizhi).__str__()
        if name not in [0,1]:
            try:
                name = eval(name)
                if type(self.ku.return1(self.dizhi)) == str:
                    print('数据主要组成数据为字符串')
                print(type(self.ku.return1(self.dizhi)))
                print('主要数据有')
                print('数据综合有', name)
                list1 = []
                list2 = []
                for i in name:
                    for j in i:
                        print('主要大类有:', j)
                        list2.append(j)
                        for ji in i[j]:
                            print('内部有', i[j][ji])
                            list1.append(i[j][ji])
                ei.msgbox(f"主要大类有\n{list2}\n内部内容为\n{list1}", title='数据展示')
            except(SyntaxError):
                pass
#请把这里的地址改为你需要操作的文件的绝对地址记得字符串外面加r转义不然把单斜杠改为双斜杠
dizhi=r'C:\Users\hp\Desktop\ces.txt'
a=guanli(dizhi)


