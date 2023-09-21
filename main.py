from tkinter import *
from tkinter import messagebox


def click_numbers(number):
    cur_num = e.get()
    e.delete(0, END)
    global new_num
    new_num = cur_num + number
    lenght_num = len(new_num)
    while lenght_num > 1 and new_num[0] == '0':
        new_num = new_num[1 :]
    if lenght_num > 2 and new_num[lenght_num - 3 : lenght_num - 1] == ' 0':
        new_num = new_num[:lenght_num - 2] + new_num[lenght_num - 1]
    e.insert(0, new_num)
    # print(f'cur_num = {cur_num}, new_num = {new_num}')
    return new_num

def click_clear():
    e.delete(0, END)
    l['text'] = ''

def click_add():
    first_num = new_num
    global view
    view = f'{first_num} + '
    e.delete(0, END)
    e.insert(0, view)
    # print(f'view = {view}')
    return view

def click_equal():
    nums = e.get()
    l['text'] = f'{nums} ='
    nums = [int(num) for num in (nums).split(' + ') if num]
    print(nums)
    global total
    total = sum(nums)
    global new_num
    new_num = total
    e.delete(0, END)
    e.insert(0, total)
    # print(f'total = {total}')
    return total, new_num


window_width = 310
window_height = 506
window_size = f'{window_width}x{window_height}'

root = Tk()
root.iconbitmap('calc.ico')
root.title('Barbie Calculator')
root.geometry(window_size)
root.resizable(width=False, height=False)
main_frame = Frame(root, bg='white')
main_frame.place(relwidth=1, relheight=1)

# results
result_frame_height = 122
result_frame = Frame(root, bg='#F1AAD5')
result_frame.place(width=window_width, height=result_frame_height)

e = Entry(result_frame, width=window_width, borderwidth=0,
          bg='#F1AAD5', fg='white', font=('Arial', 32, 'bold'))
e.place(x=25, y=61)
e.insert(0, '0')

l = Label(result_frame, text='', bg='#F1AAD5',
          fg='white', font=('Arial', 16))
l.place(x=25, y=25)

# sizes for buttons
btn_size = 60
pad = 14
y_for_rows = result_frame_height + pad
btn_and_pad = btn_size + pad

# row 0
row_0 = Frame(main_frame, bg='white')
row_0.place(x=pad, y=y_for_rows, height=btn_and_pad, relwidth=1)

btn_eq = Button(row_0, text='═', bg='#F377C2', relief='flat',
                font=('Arial', 20, 'bold'), fg="white", command=click_equal)
btn_eq.place(width=208, height=btn_size)

btn_c = Button(row_0, text='C', bg='#F377C2', relief='flat',
               font=('Arial', 20, 'bold'), fg="white", command=click_clear)
btn_c.place(x=208 + 14, width=btn_size, height=btn_size)

# row 1
row_1 = Frame(main_frame, bg='white')
row_1.place(x=pad, y=y_for_rows + btn_and_pad, height=btn_and_pad, relwidth=1)

btn_1 = Button(row_1, text='1', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('1'))
btn_1.place(width=btn_size, height=btn_size)

btn_2 = Button(row_1, text='2', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('2'))
btn_2.place(x=btn_and_pad, width=btn_size, height=btn_size)

btn_3 = Button(row_1, text='3', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('3'))
btn_3.place(x=btn_and_pad * 2, width=btn_size, height=btn_size)

btn_add = Button(row_1, text='+', font=('Arial', 20, 'bold'), relief='flat',
                 bg='#F1AAD5', fg="white", command=click_add)
btn_add.place(x=btn_and_pad * 3, width=btn_size, height=btn_size)

# row 2
row_2 = Frame(main_frame, bg='white')
row_2.place(x=pad, y=y_for_rows + btn_and_pad * 2, height=btn_and_pad, relwidth=1)

btn_4 = Button(row_2, text='4', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('4'))
btn_4.place(width=btn_size, height=btn_size)

btn_5 = Button(row_2, text='5', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('5'))
btn_5.place(x=btn_and_pad, width=btn_size, height=btn_size)

btn_6 = Button(row_2, text='6', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('6'))
btn_6.place(x=btn_and_pad * 2, width=btn_size, height=btn_size)

btn_dif = Button(row_2, text='-', font=('Arial', 20, 'bold'), relief='flat',
                 bg='#F1AAD5', fg="white", command=lambda: click_numbers(1))
btn_dif.place(x=btn_and_pad * 3, width=btn_size, height=btn_size)

# row 3
row_3 = Frame(main_frame, bg='white')
row_3.place(x=pad, y=y_for_rows + btn_and_pad * 3, height=btn_and_pad, relwidth=1)

btn_7 = Button(row_3, text='7', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('7'))
btn_7.place(width=btn_size, height=btn_size)

btn_8 = Button(row_3, text='8', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('8'))
btn_8.place(x=btn_and_pad, width=btn_size, height=btn_size)

btn_9 = Button(row_3, text='9', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('9'))
btn_9.place(x=btn_and_pad * 2, width=btn_size, height=btn_size)

btn_mul = Button(row_3, text='×', font=('Arial', 20, 'bold'), relief='flat',
                 bg='#F1AAD5', fg="white", command=lambda: click_numbers(1))
btn_mul.place(x=btn_and_pad * 3, width=btn_size, height=btn_size)

# row 4
row_4 = Frame(main_frame, bg='white')
row_4.place(x=pad, y=y_for_rows + btn_and_pad * 4, height=btn_and_pad, relwidth=1)

btn_pow = Button(row_4, text='^', font=('Arial', 20, 'bold'), relief='flat',
                 bg='#F1AAD5', fg="white", command=lambda: click_numbers(1))
btn_pow.place(width=btn_size, height=btn_size)

btn_0 = Button(row_4, text='0', font=('Arial', 20), relief='flat',
               bg='#F377C2', fg="white", command=lambda: click_numbers('0'))
btn_0.place(x=btn_and_pad, width=btn_size, height=btn_size)

btn_sqrt = Button(row_4, text='√', font=('Arial', 20, 'bold'), relief='flat',
                  bg='#F1AAD5', fg="white", command=lambda: click_numbers(1))
btn_sqrt.place(x=btn_and_pad * 2, width=btn_size, height=btn_size)

btn_div = Button(row_4, text='/', font=('Arial', 20, 'bold'), relief='flat',
                 bg='#F1AAD5', fg="white", command=lambda: click_numbers(1))
btn_div.place(x=btn_and_pad * 3, width=btn_size, height=btn_size)


root.mainloop()
