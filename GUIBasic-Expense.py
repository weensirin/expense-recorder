#ttk is theme of botton

from tkinter import *
from tkinter import ttk, messagebox    #import popup message
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by Uncle Engineer')
GUI.geometry('500x800+50+50')

### Menu Bar####
menubar= Menu(GUI)
GUI.config(menu=menubar)

###File menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File', menu=filemenu) #label ต้องใช้ตัวอักษรพิมพ์เล็ก
filemenu.add_command(label='Import CSV')
filemenu.add_command(label='Export to Googlesheet')

#Help
def About():
	messagebox.showinfo('Abount','สวัสดีครับ โปรแกรมนี้คือโปรแกรมบันทึกข้อมูล\nสนใจบริจาคเราไหม? ขอ 1 BTC Address:	abc')
helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

#Donate
donatemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Donate',menu=donatemenu)

# B1 = ttk.Button(GUI, text='Hello')
# B1.pack(ipadx=50 ,ipady=20)     #ติดปุ่มเข้ากับ GUI

days = {'Mon':'จันทร์',
		'Tue': 'อังคาร',
		'Wed': 'พุธ',
		'Thu': 'พฤหัส',
		'Fri': 'ศุกร์',
		'Sat': 'เสาร์',
		'Sun': 'อาทิตย์'}

#สร้าง Tab
Tab = ttk.Notebook(GUI)
T1= Frame(Tab)
T2= Frame(Tab)
Tab.pack(fill=BOTH, expand=1)

icon_t1= PhotoImage(file='t1_expense.png').subsample(5)
icon_t2= PhotoImage(file='t2_expenselist.png').subsample(5)

Tab.add(T1, text=f'{"ค่าใช้จ่าย":^{30}}',image=icon_t1,compound='top')
Tab.add(T2, text=f'{"ค่าใช้จ่ายทั้งหมด":^{30}}',image=icon_t2,compound='top')

#มีการย้าย Frame จาก GUI เป็น T1 (Tab ที่สร้างใหม่)
F1 = Frame(T1)
#F1.place(x=100,y=50)
F1.pack() #ทำให้อยู่ตรงกลาง ใช้ pack แทน place

def Save(event=None):
	expense = v_expense.get()
	price = v_price.get()
	amount = v_amount.get()

	if expense == '':
		print('No data')
		messagebox.showinfo('Error','กรุณากรอกค่าใช้จ่าย')
		return
	elif price == '':
		messagebox.showinfo('Error','กรุณากรอกราคา')
	elif amount == '':
		amount = 1

	try:
		total = int(price)*int(amount)
		today = datetime.now().strftime('%a') #days['Mon']='จันทร์'
		dt= datetime.now().strftime('%Y-%m-%d, %H-%M-%S') 
		dt= days[today] + '-' + dt
		# .get() คือดึงค่ามาจาก V_expense = StringVar()
		print('รายการ: {} ราคา: {} จำนวน: {} รวมทั้งหมด: {} เวลา: {}'.format(expense,price,amount,total,dt))
		text='รายการ: {} ราคา: {}\n'.format(expense,price)
		text= text+'จำนวน: {} รวมทั้งหมด: {} บาท'.format(amount,total)
		v_result.set(text)
		
		# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_amount.set('')

		# บันทึกข้อมูลลง CSV อย่าลืม import CSV ด้วย
		with open('savedata.csv','a',encoding='utf-8' ,newline='') as f:
			# with คือสั่งเปิดไฟล์แล้วปิดอัติโนมัติ
			# 'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า ถ้าเป็น'w' บันทึกทับข้อมูลเก่า
			# newline= '' ทำให้ไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [expense,price,amount,total,dt]
			fw.writerow(data)

			#ทำให้cursor กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		update_table()

	except:
		print('error')
		messagebox.showerror('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showwarning('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
		#messagebox.showinfo('Error','กรุณากรอกข้อมูลใหม่ คุณกรอกตัวเลขผิด')
	# clear ข้อมูลเก่า
		v_expense.set('')
		v_price.set('')
		v_amount.set('')



# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None)

FONT1 = (None,20) #None เปลี่ยนเป็น 'Angsana New'

#----image---
main_icon = PhotoImage(file='icon_money.png')
Mainicon = Label(F1, image=main_icon)
Mainicon.pack()


#----text1------
	
L = ttk.Label(F1,text='รายการค่าใช้่จ่าย ',font=FONT1).pack()
v_expense= StringVar()
#StringVar () คือตัวเแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack() #คือเอาปุ่มไปติดกับ F1 

#----------------

#-----text2------
L = ttk.Label(F1,text='ราคา (บาท)',font=FONT1).pack()
v_price= StringVar()
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#-----------------

#------text3------
L = ttk.Label(F1,text='จำนวน', font=FONT1).pack()
v_amount= StringVar()
E3 = ttk.Entry(F1,textvariable=v_amount,font=FONT1)
E3.pack()
#------------------

#------text4-------
L = ttk.Label(F1,text='รวมทั้งหมด', font=FONT1).pack()
#-----------------

icon_b1 = PhotoImage(file='b_save.png').subsample(4)

B2 = ttk.Button(F1, text=f'{"Save": >{10}}',command=Save, image=icon_b1, compound='left')
B2.pack(ipadx=50, ipady=20, pady=20)
#ipadx คือ internal pad ความห่างภายใน, pady เป็นความห่างภายนอก

v_result = StringVar()
v_result.set('------ผลลัพท์-------')
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground='green')
result.pack(pady=20)

#####Tab2######

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		#ให้เปิด CSV ขึ้นมา แล้วตั้งชื่อว่า f 
		fr = csv.reader(f)
		#อยากอ่าน csv ใช้ print(fr) แต่อ่านไม่ออก เลยใช้ list มาช่วย หรืออาจใช้ pandas ก้ได้
		data = list(fr)
		#print(data)
		#print('-----')
		#print(data[0])
		#for d in data:
		#    print(d)
	return data
		# return จำเป็น เพราะเราต้องการข้อมูลที่ได้ไปใช้งานต่อ (ส่งต่อ data)

#สังเกตได้ว่าถ้าเรียกใช้ฟังชั้นเฉยๆไม่ขึ้น 
#read_csv()
#ต้องสร้างค่าขึ้นมา
#rs = read_csv()
#print(rs)

L = ttk.Label(T2,text='ตารางแสดงผลลัพท์ทั้งหมด',font=FONT1).pack(pady=10)

#สร้าง Table
header = ['รายการ','จำนวน','ราคา','รวมค่าใช้จ่าย','วัน-เวลา']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()

#ใส่ heading วิธี manual
#resulttable.heading(header[0],text=header[0])
#resulttable.heading(header[1],text=header[1])
#resulttable.heading(header[2],text=header[2])
#resulttable.heading(header[3],text=header[3])
#resulttable.heading(header[4],text=header[4])

#ใส่ heading วิธีที่ 1 for i in range
#for i in range(len(header)):
#    resulttable.heading(header[i],text=header[i])

#ใส่ heading วิธีที่ 2 for i
for h in header:
	resulttable.heading(h,text=h)

headerwidth = [60,60,60,60,150]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

#วิธีใส่ข้อมูลในตารางแบบ manual
#resulttable.insert('','end',value=['จันทร์','น้ำดื่ม',30,50,2])

def update_table():
	resulttable.delete(*resulttable.get_children())
	#resultable เป็น function ที่ดึงจาก library เอาไว้ใช้ delete data ก่อน update ข้อมูล

	#for c in resulttable.get_childern():
	#   resulttable.delete(c)

	data = read_csv()
	# run เลยไม่ได้ เนื่องจากเป็น list
	for d in data:
		resulttable.insert('',0,value=d)

update_table()
#print('GET CHILD:',resulttable.get_children())

GUI.mainloop()
