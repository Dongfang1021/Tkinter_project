import tkinter
import tkinter.messagebox

# 创建应用程序窗口
root = tkinter.Tk()

# 在窗口上创建标签组件
labelName = tkinter.Label(root,
                          text='User Name:',
                          justify=tkinter.RIGHT,
                          width=80)
labelName.place(x=10, y=5, width=80, height=20)

# 创建字符串变量和文本框组件，同时设置关联的变量
varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root,
                          width=80,
                          textvariable=varName)
entryName.place(x=100, y=5, width=80, height=20)

labelPwd = tkinter.Label(root,
                         text='User Pwd:',
                         justify=tkinter.RIGHT,
                         width=80)
labelPwd.place(x=10, y=30, width=80, height=20)

# 创建密码文本框
varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root,
                         show='*',
                         width=80,
                         textvariable=varPwd)
entryPwd.place(x=100, y=30, width=80, height=20)

# 登录按钮事件处理函数
def login():
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    if name=='admin' and pwd=='123456':
        tkinter.messagebox.showinfo(title='恭喜',
                                    message='登录成功！')
    else:
        tkinter.messagebox.showerror('警告',
                                     message='用户名或密码错误')
# 创建按钮组件，同时设置按钮事件处理函数
buttonOk = tkinter.Button(root,
                          text='Login',
                          command=login)
buttonOk.place(x=30, y=70, width=50, height=20)

# 取消按钮的事件处理函数
def cancel():
    #清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')
buttonCancel = tkinter.Button(root,
                              text='Cancel',
                              command=cancel)
buttonCancel.place(x=90, y=70, width=50, height=20)

#启动消息循环
root.mainloop()
