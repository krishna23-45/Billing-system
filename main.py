from tkinter import *
from tkinter import ttk
import math
import random
from tkinter import messagebox as msg
import os

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()
        self.title("Biling system")
        self.geometry("1350x700+0+0")
        self.bg_colour = "#074463"
        # Variable
        self.config(bg='green')

        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshen = IntVar()     

        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()  

        self.maze = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()  


        self.cosmetics_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()     

        self.cosmetics_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()   

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        self.x = random.randint(1000,99999)
        self.bill_no.set(int(self.x))
        
        self.search_bill = StringVar()    

        self.title = Label(text="Billing software",fg="white",bd=12,bg=self.bg_colour,relief=GROOVE,font=("times new roman",30,"bold"))
        self.title.pack(pady=10,fill=BOTH)


        self.f1 = LabelFrame(self,text="Customer Details",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=self.bg_colour)
        self.f1.place(x=0,y=80,relwidth=1)

        self.f2 = LabelFrame(self,text="Cosmetics",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=self.bg_colour)
        self.f2.place(x=0,y=159,width=325,height=380)

        
        self.f3 = LabelFrame(self,text="Grocery",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=self.bg_colour)
        self.f3.place(x=325,y=159,width=325,height=380)

        self.f4 = LabelFrame(self,text="Cold Drinks",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=self.bg_colour)
        self.f4.place(x=650,y=159,width=325,height=380)

        
        self.f5 = LabelFrame(self,bd=7,relief=GROOVE)
        self.f5.place(x=971,y=159,width=381,height=380)

        self.f6 = LabelFrame(self,text="Bill Menu",bd=7,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg=self.bg_colour)
        self.f6.place(x=0,y=538,relwidth=1,height=160)


        self.frame1()
        self.frame2()
        self.frame3()
        self.frame4()
        self.bill_title()
        self.button_menu()
        
        

    def frame1(self):
        self.cname_label = Label(self.f1,text="Customer Name",bg=self.bg_colour,fg="white",font=("times new roman",18,"bold"))
        self.cname_label.grid(column=0,row=0,padx=20,pady=7)
        self.cname_entry = Entry(self.f1,font="arial 15",textvariable=self.c_name,width=15,bd=5,relief=SUNKEN)
        self.cname_entry.focus()
        self.cname_entry.grid(column=1,row=0)

        self.cphone_label = Label(self.f1,text="Customer Phone No",bg=self.bg_colour,fg="white",font=("times new roman",18,"bold"))
        self.cphone_label.grid(column=2,row=0,padx=20,pady=7)
        self.cphone_entry = Entry(self.f1,textvariable=self.c_phone,font="arial 15",width=15,bd=5,relief=SUNKEN)
        self.cphone_entry.focus()
        self.cphone_entry.grid(column=3,row=0)

        self.cbill_label = Label(self.f1,text="Bill Number",bg=self.bg_colour,fg="white",font=("times new roman",18,"bold"))
        self.cbill_label.grid(column=4,row=0,padx=20,pady=7)
        self.cbill_entry = Entry(self.f1,textvariable=self.search_bill,font="arial 15",width=15,bd=5,relief=SUNKEN)
        self.cbill_entry.focus()
        self.cbill_entry.grid(column=5,row=0)


        self.bill_btn = Button(self.f1,command=self.find_bill,text="Search",width=10,bd=7)
        self.bill_btn.grid(column=6,row=0,padx=40)

    def frame2(self):
        self.bath_lable = Label(self.f2,text="Bath Soap",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.bath_lable.grid(column=0,row=0,padx=10,pady=10,sticky="w")
        self.bath_entry = Entry(self.f2,textvariable=self.soap,font="arial 15",width=10,bd=5,relief=SUNKEN)
        self.bath_entry.focus()
        self.bath_entry.grid(column=1,row=0,padx=10,pady=10)

        self.facec_lable = Label(self.f2,text="Face Cream",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.facec_lable.grid(column=0,row=1,padx=10,pady=10,sticky="w")
        self.facec_entry = Entry(self.f2,font="arial 15",textvariable=self.face_cream,width=10,bd=5,relief=SUNKEN)
        self.facec_entry.focus()
        self.facec_entry.grid(column=1,row=1,padx=10,pady=10)

        self.facew_lable = Label(self.f2,text="Face Wash",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.facew_lable.grid(column=0,row=2,padx=10,pady=10,sticky="w")
        self.facew_entry = Entry(self.f2,font="arial 15",textvariable=self.face_wash,width=10,bd=5,relief=SUNKEN)
        self.facew_entry.focus()
        self.facew_entry.grid(column=1,row=2,padx=10,pady=10)

        self.hairs_lable = Label(self.f2,text="Hair Spray",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.hairs_lable.grid(column=0,row=3,padx=10,pady=10,sticky="w")
        self.hairs_entry = Entry(self.f2,font="arial 15",textvariable=self.spray,width=10,bd=5,relief=SUNKEN)
        self.hairs_entry.focus()
        self.hairs_entry.grid(column=1,row=3,padx=10,pady=10)

        self.hairg_lable = Label(self.f2,text="Hair Gell",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.hairg_lable.grid(column=0,row=4,padx=10,pady=10,sticky="w")
        self.hairg_entry = Entry(self.f2,font="arial 15",textvariable=self.gell,width=10,bd=5,relief=SUNKEN)
        self.hairg_entry.focus()
        self.hairg_entry.grid(column=1,row=4,padx=10,pady=10)


        self.bodyl_lable = Label(self.f2,text="Body Loshen",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.bodyl_lable.grid(column=0,row=5,padx=10,pady=10,sticky="w")
        self.bodyl_entry = Entry(self.f2,textvariable=self.loshen,font="arial 15",width=10,bd=5,relief=SUNKEN)
        self.bodyl_entry.focus()
        self.bodyl_entry.grid(column=1,row=5,padx=10,pady=10)

    def frame3(self):
        self.rice_lable = Label(self.f3,text="Rice",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.rice_lable.grid(column=0,row=0,padx=10,pady=10,sticky="w")
        self.rice_entry = Entry(self.f3,font="arial 15",textvariable=self.rice,width=10,bd=5,relief=SUNKEN)
        self.rice_entry.focus()
        self.rice_entry.grid(column=1,row=0,padx=10,pady=10)

        self.food_oil_lable = Label(self.f3,text="Food Oil",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.food_oil_lable.grid(column=0,row=1,padx=10,pady=10,sticky="w")
        self.food_oil_entry = Entry(self.f3,font="arial 15",textvariable=self.food_oil,width=10,bd=5,relief=SUNKEN)
        self.food_oil_entry.focus()
        self.food_oil_entry.grid(column=1,row=1,padx=10,pady=10)

        self.daal_lable = Label(self.f3,text="Daal",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.daal_lable.grid(column=0,row=2,padx=10,pady=10,sticky="w")
        self.daal_entry = Entry(self.f3,font="arial 15",textvariable=self.daal,width=10,bd=5,relief=SUNKEN)
        self.daal_entry.focus()
        self.daal_entry.grid(column=1,row=2,padx=10,pady=10)

        self.Wheat_lable = Label(self.f3,text="Wheat",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.Wheat_lable.grid(column=0,row=3,padx=10,pady=10,sticky="w")
        self.Wheat_entry = Entry(self.f3,font="arial 15",textvariable=self.wheat,width=10,bd=5,relief=SUNKEN)
        self.Wheat_entry.focus()
        self.Wheat_entry.grid(column=1,row=3,padx=10,pady=10)

        self.Sugar_lable = Label(self.f3,text="Sugar",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.Sugar_lable.grid(column=0,row=4,padx=10,pady=10,sticky="w")
        self.Sugar_entry = Entry(self.f3,font="arial 15",textvariable=self.sugar,width=10,bd=5,relief=SUNKEN)
        self.Sugar_entry.focus()
        self.Sugar_entry.grid(column=1,row=4,padx=10,pady=10)


        self.tea_lable = Label(self.f3,text="Tea",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.tea_lable.grid(column=0,row=5,padx=10,pady=10,sticky="w")
        self.tea_entry = Entry(self.f3,font="arial 15",textvariable=self.tea,width=10,bd=5,relief=SUNKEN)
        self.tea_entry.focus()
        self.tea_entry.grid(column=1,row=5,padx=10,pady=10)



    def frame4(self):
        self.maze_lable = Label(self.f4,text="Maze",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.maze_lable.grid(column=0,row=0,padx=10,pady=10,sticky="w")
        self.maze_entry = Entry(self.f4,font="arial 15",textvariable=self.maze,width=10,bd=5,relief=SUNKEN)
        self.maze_entry.focus()
        self.maze_entry.grid(column=1,row=0,padx=10,pady=10)

        self.coke_oil_lable = Label(self.f4,text="Coke",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.coke_oil_lable.grid(column=0,row=1,padx=10,pady=10,sticky="w")
        self.coke_oil_entry = Entry(self.f4,font="arial 15",textvariable=self.coke,width=10,bd=5,relief=SUNKEN)
        self.coke_oil_entry.focus()
        self.coke_oil_entry.grid(column=1,row=1,padx=10,pady=10)

        self.frooti_lable = Label(self.f4,text="Frooti",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.frooti_lable.grid(column=0,row=2,padx=10,pady=10,sticky="w")
        self.frooti_entry = Entry(self.f4,font="arial 15",textvariable=self.frooti,width=10,bd=5,relief=SUNKEN)
        self.frooti_entry.focus()
        self.frooti_entry.grid(column=1,row=2,padx=10,pady=10)

        self.Thumbs_up_lable = Label(self.f4,text="Thumbs Up",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.Thumbs_up_lable.grid(column=0,row=3,padx=10,pady=10,sticky="w")
        self.Thumbs_up_entry = Entry(self.f4,font="arial 15",textvariable=self.thumbsup,width=10,bd=5,relief=SUNKEN)
        self.Thumbs_up_entry.focus()
        self.Thumbs_up_entry.grid(column=1,row=3,padx=10,pady=10)

        self.Limca_lable = Label(self.f4,text="Limca",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.Limca_lable.grid(column=0,row=4,padx=10,pady=10,sticky="w")
        self.Limca_entry = Entry(self.f4,font="arial 15",textvariable=self.limca,width=10,bd=5,relief=SUNKEN)
        self.Limca_entry.focus()
        self.Limca_entry.grid(column=1,row=4,padx=10,pady=10)


        self.sprite_lable = Label(self.f4,text="Sprite",font=("times new roman",18,"bold"),bg=self.bg_colour,fg='lightgreen')
        self.sprite_lable.grid(column=0,row=5,padx=10,pady=10,sticky="w")
        self.sprite_entry = Entry(self.f4,font="arial 15",textvariable=self.sprite,width=10,bd=5,relief=SUNKEN)
        self.sprite_entry.focus()
        self.sprite_entry.grid(column=1,row=5,padx=10,pady=10)

    def bill_title(self):
        self.bill_lable = Label(self.f5,text="Bill Area",font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        self.bill_lable.pack(fill=X)
        self.scroll_y = Scrollbar(self.f5,orient=VERTICAL)
        self.txtarea = Text(self.f5,yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        

    def button_menu(self):
        self.botton_lable = Label(self.f6,text="Total Cosmetic Price",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.botton_lable.grid(column=0,row=0)
        self.txt_m1 = Entry(self.f6,textvariable=self.cosmetics_price,font="arial 15",width=10,bd=5,relief=SUNKEN)
        self.txt_m1.grid(column=1,row=0,padx=10,pady=5)

        self.botton1_lable = Label(self.f6,text="Total Grocery Price",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.botton1_lable.grid(column=0,row=1)
        self.txt_m2 = Entry(self.f6,textvariable=self.grocery_price,font="arial 15",width=10,bd=5,relief=SUNKEN)
        self.txt_m2.grid(column=1,row=1,padx=10,pady=5)


        self.botton_lable = Label(self.f6,text="Total Cold Drinks Price",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.botton_lable.grid(column=0,row=2)
        self.txt_m1 = Entry(self.f6,font="arial 15",textvariable=self.cold_drinks_price,width=10,bd=5,relief=SUNKEN)
        self.txt_m1.grid(column=1,row=2,padx=10,pady=5)



        self.bottona_lable = Label(self.f6,text="Cosmetic Tax",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.bottona_lable.grid(column=2,row=0)
        self.txt_ma = Entry(self.f6,font="arial 15",textvariable=self.cosmetics_tax,width=10,bd=5,relief=SUNKEN)
        self.txt_ma.grid(column=3,row=0,padx=10,pady=5)

        self.bottonb_lable = Label(self.f6,text="Grocery Tax",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.bottonb_lable.grid(column=2,row=1)
        self.txt_mb = Entry(self.f6,font="arial 15",textvariable=self.grocery_tax,width=10,bd=5,relief=SUNKEN)
        self.txt_mb.grid(column=3,row=1,padx=10,pady=5)


        self.bottonc_lable = Label(self.f6,text="Cold Drinks Tax",font=("times new roman",15,"bold"),bg=self.bg_colour)
        self.bottonc_lable.grid(column=2,row=2)
        self.txt_mc = Entry(self.f6,font="arial 15",textvariable=self.cold_drinks_tax,width=10,bd=5,relief=SUNKEN)
        self.txt_mc.grid(column=3,row=2,padx=10,pady=5)


        self.btn_f = Frame(self.f6,bd=7,relief=GROOVE)
        self.btn_f.place(x=625,width=720,height=130)


        self.total_btn = Button(self.btn_f,command=self.total,text='Total',bd=5,bg="cadetblue",fg="white",pady=15,width=11,font=("arial",15,"bold"))
        self.total_btn.grid(column=0,row=0,pady=25,padx=20)

        self.total3_btn = Button(self.btn_f,command=self.bill_area,text='Generate Bill',bd=5,bg="cadetblue",fg="white",pady=15,width=11,font=("arial",15,"bold"))
        self.total3_btn.grid(column=1,row=0,pady=25,padx=10)

        self.total1_btn = Button(self.btn_f,command=self.exit_window,text='Exit',bd=5,bg="cadetblue",fg="white",pady=15,width=11,font=("arial",15,"bold"))
        self.total1_btn.grid(column=3,row=0,pady=25,padx=10)

        self.total2_btn = Button(self.btn_f,text='Clear',command=self.clear_variable,bd=5,bg="cadetblue",fg="white",pady=15,width=11,font=("arial",15,"bold"))
        self.total2_btn.grid(column=2,row=0,pady=25,padx=10)
        self.welcome_bill()


    def total(self):
        self.c_s_p = self.soap.get()*40
        self.c_fc_p = self.face_cream.get()*120
        self.c_fw_p = self.face_wash.get()*60
        self.c_hs_p = self.spray.get()*180
        self.c_hg_p = self.gell.get()*140
        self.c_bl_p = self.loshen.get()*180

        self.total_cosmetic_price = float(
                                      self.c_s_p + 
                                      self.c_fc_p+
                                      self.c_fw_p+
                                      self.c_hs_p+
                                      self.c_hg_p+
                                      self.c_bl_p
        )
        self.cosmetics_price.set('Rs. ' + str(self.total_cosmetic_price))
        self.cosmetics_tax.set(('Rs. ' + str(round((self.total_cosmetic_price*0.05)))))
        self.cs_tax = ((int(round((self.total_cosmetic_price*0.05)))))


        self.g_r_p = (self.rice.get()*80)
        self.g_f_p = (self.food_oil.get()*120)
        self.g_d_p = (self.daal.get()*80)
        self.g_w_p = (self.wheat.get()*200)
        self.g_s_p = (self.sugar.get()*100)
        self.g_t_p = (self.tea.get()*180)

        self.total_grocery_price = float(
                                      self.g_r_p + 
                                      self.g_f_p+
                                      self.g_d_p+
                                      self.g_w_p+
                                      self.g_s_p+
                                      self.g_t_p
        )
        self.grocery_price.set('Rs. ' + str(self.total_grocery_price))
        self.g_tax = (int(round((self.total_grocery_price*0.07))))
        self.grocery_tax.set('Rs. ' + str(round((self.total_grocery_price*0.07))))

        self.d_m_p = (self.maze.get()*60)
        self.d_c_p =  (self.coke.get()*60)
        self.d_f_p = (self.frooti.get()*80)
        self.d_t_p = (self.thumbsup.get()*70)
        self.d_l_p = (self.limca.get()*40)
        self.d_s_p = (self.sprite.get()*80)


        self.total_cold_price = float(
                                      self.d_m_p+ 
                                      self.d_c_p+
                                      self.d_f_p+
                                      self.d_t_p+
                                      self.d_l_p+
                                      self.d_s_p
        )
        self.cold_drinks_price.set('Rs. ' + str(self.total_cold_price))
        self.cold_drinks_tax.set('Rs. ' + str(round((self.total_cold_price*0.04))))
        self.c_tax = (int(round((self.total_cold_price*0.04))))



        self.zin = float(
                          self.total_cosmetic_price+
                          self.c_tax+
                          self.total_grocery_price + 
                          self.g_tax +
                          self.cs_tax +
                          self.total_cold_price
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome to the oeken retailer\n")
        self.txtarea.insert(END,f"\nBill Number :{self.bill_no.get()}")
        self.txtarea.insert(END,f"\nCustomer Name :{self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone Number : {self.c_phone.get()}\n")
        self.txtarea.insert(END,f"===========================================")
        self.txtarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n===========================================")
    def bill_area(self):
        # if self.c_name.get()=="" or self.c_phone().get()=="":
        #     msg.showerror("Error","Customer details are must be filled")
        # elif self.cosmetics_price.get() == 'Rs. 0.0' and self.grocery_price.get() == 'Rs. 0.0' and self.cold_drinks_price.get() == 'Rs. 0.0':
        #     msg.showerror("Error","Item is not selected")

        self.welcome_bill()
        if self.soap.get() != 0:
                self.txtarea.insert(END,f"\nBath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        
        if self.face_cream.get() != 0:
                self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        
        if self.face_wash.get() != 0:
                self.txtarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.spray.get() != 0:
                self.txtarea.insert(END,f"\nHair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")

        if self.gell.get() != 0:
                self.txtarea.insert(END,f"\nHair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")


        if self.loshen.get() != 0:
                self.txtarea.insert(END,f"\nBody Loshen\t\t{self.loshen.get()}\t\t{self.c_bl_p}")

            # grocery
        if self.rice.get() != 0:
            self.txtarea.insert(END,f"\nRice \t\t{self.rice.get()}\t\t{self.g_r_p}")
        
        if self.food_oil.get() != 0:
                self.txtarea.insert(END,f"\nFood Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
        
        if self.daal.get() != 0:
                self.txtarea.insert(END,f"\nFace Wash\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.wheat.get() != 0:
                self.txtarea.insert(END,f"\nHair Spray\t\t{self.wheat.get()}\t\t{self.g_w_p}")

        if self.tea.get() != 0:
                self.txtarea.insert(END,f"\nHair Gell\t\t{self.tea.get()}\t\t{self.g_t_p}")


        if self.sugar.get() != 0:
                self.txtarea.insert(END,f"\nBody Loshen\t\t{self.sugar.get()}\t\t{self.g_s_p}")

##

        if self.maze.get() != 0:
            self.txtarea.insert(END,f"\nMaze \t\t{self.maze.get()}\t\t{self.d_m_p}")
        
        if self.coke.get() != 0:
                self.txtarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t\t{self.d_c_p}")
        
        if self.frooti.get() != 0:
                self.txtarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
        if self.thumbsup.get() != 0:
                self.txtarea.insert(END,f"\nThumbs upt\t{self.thumbsup.get()}\t\t{self.d_t_p}")

        if self.limca.get() != 0:
                self.txtarea.insert(END,f"\nLimca\t\t{self.limca.get()}\t\t{self.d_l_p}")

        if self.sprite.get() != 0:
                self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")

        ####
        if self.cosmetics_tax.get() != 'Rs. 0':
            self.txtarea.insert(END,f"\n------------------------------------------")
            self.txtarea.insert(END,f"\nCosmetic Tax\t\t\t\t{self.cosmetics_tax.get()}")

        if self.grocery_tax.get() != 'Rs. 0':
            self.txtarea.insert(END,f"\n------------------------------------------")
            self.txtarea.insert(END,f"\nGrocery Tax\t\t\t\t{self.grocery_tax.get()}")

        if self.cold_drinks_tax != 'Rs. 0':
            self.txtarea.insert(END,f"\n------------------------------------------")
            self.txtarea.insert(END,f"\nCold Drink Tax\t\t\t\t{self.cold_drinks_tax.get()}")
            self.txtarea.insert(END,f"\n------------------------------------------")
        self.txtarea.insert(END,f"\nTotal Bill \t\t\t\tRs. {self.zin}")
        self.save_bill()

    def save_bill(self):
        op = msg.askyesno("Save Bill",'Do you want to save the Bill')
        if op == 1:
            self.bill_data = self.txtarea.get(1.0,END)
            f1 = open("bill/"+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            f1.close()
            msg.showinfo('Bill Saved',"Your Bill saved Successfully")
        else:
            return
    def find_bill(self):
        self.present = 'no'
        for i in os.listdir("bill/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"bill/{i}",'r')
                self.data = f1.read()
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,self.data)
                f1.close()
                self.present = "yes"

        if self.present == 'no':
            msg.showerror("Error","Invalide bill number")

    def clear_variable(self):
        ser = msg.askyesno('Clear','Do you want to clear?')
        if ser == 1:
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshen.set(0)    

            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0) 

            self.maze.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.thumbsup.set(0)
            self.limca.set(0)
            self.sprite.set(0)



            
            self.cosmetics_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")     

            self.cosmetics_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")   

            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")
            self.x = random.randint(1000,99999)
            self.bill_no.set(int(self.x))
            
            self.search_bill.set("")
            self.welcome_bill()
    def exit_window(self):
        se = msg.askyesno('Exit','Do you want to exit?')
        if se == 1:
            self.destroy()

        

window = Window()
window.mainloop()