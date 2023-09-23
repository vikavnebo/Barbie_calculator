from tkinter import *
from tkinter import messagebox


# def on_num(number):
#     cur_num = e.get()
#     e.delete(0, END)
#     global new_num
#     new_num = cur_num + number
#     lenght_num = len(new_num)
#     while lenght_num > 1 and new_num[0] == '0':
#         new_num = new_num[1 :]
#     if lenght_num > 2 and new_num[lenght_num - 3 : lenght_num - 1] == ' 0':
#         new_num = new_num[:lenght_num - 2] + new_num[lenght_num - 1]
#     e.insert(0, new_num)
#     # print(f'cur_num = {cur_num}, new_num = {new_num}')
#     return new_num
#
# def on_clear():
#     e.delete(0, END)
#     l['text'] = ''
#
# def on_add():
#     first_num = new_num
#     global view
#     view = f'{first_num} + '
#     e.delete(0, END)
#     e.insert(0, view)
#     # print(f'view = {view}')
#     return view
#
# def on_equal():
#     nums = e.get()
#     l['text'] = f'{nums} ='
#     nums = [int(num) for num in (nums).split(' + ') if num]
#     print(nums)
#     global total
#     total = sum(nums)
#     global new_num
#     new_num = total
#     e.delete(0, END)
#     e.insert(0, total)
#     # print(f'total = {total}')
#     return total, new_num


colors = {'dark_color': '#F377C2',  # for bg btns of numbers, = and C
          'light_color': '#F1AAD5', # for bg btns of signs and result frame
          'bg_behind_btns': '#FFFFFF',
          'font_color': '#FFFFFF'}

window_width = 310
window_height = 506

root = Tk()
root.iconbitmap('calc.ico')
root.title('Barbie Calculator')
root.geometry(f'{window_width}x{window_height}')
root.resizable(width=False, height=False)
main_frame = Frame(root, bg='white')
main_frame.place(relwidth=1, relheight=1)

# results
result_frame_height = 122
result_frame = Frame(root, bg=colors['light_color'])
result_frame.place(width=window_width, height=result_frame_height)

result_lable = Label(result_frame, text='0', bg=colors['light_color'],
                     fg='white', font=('Arial', 32, 'bold'))
result_lable.place(x=25, y=61)

history = Label(result_frame, text='', bg=colors['light_color'],
                fg='white', font=('Arial', 16))
history.place(x=25, y=25)


btn_side = 60
pad = 14
y_for_rows = result_frame_height + pad
btn_and_pad = btn_side + pad


# for row in range(5):
#     row_frame = Frame(main_frame, bg=colors['font_color'])
#     row_frame.place(x=pad, y=(y_for_rows + btn_and_pad * row),
#                     height=btn_and_pad, relwidth=1)
#     if row == 0:
#         eq_btn.place(width=208, height=btn_side)
#         c_btn.place(x=208 + 14, width=btn_side, height=btn_side)
    # elif row == 1:


def set_style(btn, type):
    global colors
    if type == 'num':
        btn['bg'] = colors['dark_color']
        btn['relief'] = 'flat'
        btn['font'] = ('Arial', 20)
        btn['fg'] = colors['font_color']
        btn['command'] = lambda x: True
    elif type == 'sign':
        btn['bg'] = colors['light_color']
        btn['relief'] = 'flat'
        btn['font'] = ('Arial', 20, 'bold')
        btn['fg'] = colors['font_color']
    return btn


'''creation rows'''
row_0 = Frame(main_frame, bg=colors['bg_behind_btns'])
row_1 = Frame(main_frame, bg=colors['bg_behind_btns'])
row_2 = Frame(main_frame, bg=colors['bg_behind_btns'])
row_3 = Frame(main_frame, bg=colors['bg_behind_btns'])
row_4 = Frame(main_frame, bg=colors['bg_behind_btns'])

'''creation buttons'''
# row 0
btn_eq = Button(row_0, text='═')
btn_eq = set_style(btn_eq, type='sign')
btn_eq['bg'] = colors['dark_color']
btn_eq['command'] = lambda x: True
btn_eq.place(width=208, height=btn_side)

btn_c = Button(row_0, text='C')
btn_c = set_style(btn_c, type='sign')
btn_c['bg'] = colors['dark_color']
btn_c['command'] = lambda x: True
btn_c.place(x=208 + 14, width=btn_side, height=btn_side)

# row 1
btn_1 = Button(row_1, text='1')
btn_1 = set_style(btn_1, type='num')

btn_2 = Button(row_1, text='2')
btn_2 = set_style(btn_2, type='num')

btn_3 = Button(row_1, text='3')
btn_3 = set_style(btn_3, type='num')

btn_add = Button(row_1, text='+')
btn_add = set_style(btn_add, type='sign')
btn_add['command'] = lambda x: True

# row 2
btn_4 = Button(row_2, text='4')
btn_4 = set_style(btn_4, type='num')

btn_5 = Button(row_2, text='5')
btn_5 = set_style(btn_5, type='num')

btn_6 = Button(row_2, text='6')
btn_6 = set_style(btn_6, type='num')

btn_dif = Button(row_2, text='-')
btn_dif = set_style(btn_dif, type='sign')
btn_dif['command'] = lambda x: True

# row 3
btn_7 = Button(row_3, text='7')
btn_7 = set_style(btn_7, type='num')

btn_8 = Button(row_3, text='8')
btn_8 = set_style(btn_8, type='num')

btn_9 = Button(row_3, text='9')
btn_9 = set_style(btn_9, type='num')

btn_mul = Button(row_3, text='×')
btn_mul = set_style(btn_mul, type='sign')
btn_mul['command'] = lambda x: True

# row 4
btn_pow = Button(row_4, text='^')
btn_pow = set_style(btn_pow, type='sign')
btn_pow['command'] = lambda x: True

btn_0 = Button(row_4, text='0')
btn_0 = set_style(btn_0, type='num')

btn_sqrt = Button(row_4, text='√')
btn_sqrt = set_style(btn_sqrt, type='sign')
btn_sqrt['command'] = lambda x: True

btn_div = Button(row_4, text='/')
btn_div = set_style(btn_div, type='sign')
btn_div['command'] = lambda x: True


'''placing rows'''
row_0.place(x=pad, y=y_for_rows + btn_and_pad * 0, height=btn_and_pad, relwidth=1)
row_1.place(x=pad, y=y_for_rows + btn_and_pad * 1, height=btn_and_pad, relwidth=1)
row_2.place(x=pad, y=y_for_rows + btn_and_pad * 2, height=btn_and_pad, relwidth=1)
row_3.place(x=pad, y=y_for_rows + btn_and_pad * 3, height=btn_and_pad, relwidth=1)
row_4.place(x=pad, y=y_for_rows + btn_and_pad * 4, height=btn_and_pad, relwidth=1)

'''placing buttons'''
# row 0
btn_eq.place(width=208, height=btn_side)
btn_c.place(x=208 + 14, width=btn_side, height=btn_side)

# row 1
btn_1.place(x=btn_and_pad * 0, width=btn_side, height=btn_side)
btn_2.place(x=btn_and_pad * 1, width=btn_side, height=btn_side)
btn_3.place(x=btn_and_pad * 2, width=btn_side, height=btn_side)
btn_add.place(x=btn_and_pad * 3, width=btn_side, height=btn_side)

# row 2
btn_4.place(x=btn_and_pad * 0, width=btn_side, height=btn_side)
btn_5.place(x=btn_and_pad * 1, width=btn_side, height=btn_side)
btn_6.place(x=btn_and_pad * 2, width=btn_side, height=btn_side)
btn_dif.place(x=btn_and_pad * 3, width=btn_side, height=btn_side)

# row 3
btn_7.place(x=btn_and_pad * 0, width=btn_side, height=btn_side)
btn_8.place(x=btn_and_pad * 1, width=btn_side, height=btn_side)
btn_9.place(x=btn_and_pad * 2, width=btn_side, height=btn_side)
btn_mul.place(x=btn_and_pad * 3, width=btn_side, height=btn_side)

# row 4
btn_pow.place(x=btn_and_pad * 0, width=btn_side, height=btn_side)
btn_0.place(x=btn_and_pad * 1, width=btn_side, height=btn_side)
btn_sqrt.place(x=btn_and_pad * 2, width=btn_side, height=btn_side)
btn_div.place(x=btn_and_pad * 3, width=btn_side, height=btn_side)


root.mainloop()
