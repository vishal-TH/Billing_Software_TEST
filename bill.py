# Made By Vishal 

from tkinter import*
import math, random, os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color='#999999'
        title = Label(self.root, text="TH_Billing_Software_Test_1",bd=12, relief=GROOVE, bg=bg_color, fg="black", font= ("times new rman", 30, "bold"),pady=2).pack(fill=X)

        # ========== Variables ==========

        # ========== Cosmetics ==========

        self.soap = IntVar()
        self.face_wash = IntVar()
        self.face_cream = IntVar()
        self.hair_spray = IntVar()
        self.bdy_ltn = IntVar()
        self.hair_gell = IntVar()

        #========== Grocery ==========

        self.rice = IntVar()
        self.dal = IntVar()
        self.wheat = IntVar()
        self.mst_oil = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ========== Cold Drinks ==========

        self.mnt_dwe = IntVar()
        self.ppsi = IntVar()
        self.limca = IntVar()
        self.sprit = IntVar()
        self.red_bull = IntVar()
        self.lassi = IntVar()

        # ========== Total Product Price ==========

        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drink_price = StringVar()

        # ========== Total Product Tax ==========

        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drink_tax = StringVar()

        # ========== Customer ==========

        self.c_name = StringVar()
        self.c_id = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()


        # ========== Customer Details Frame ==========

        F1 = LabelFrame(self.root,bd=10, relief=GROOVE, text="Customer Details", font=("times new roman", 15, "bold"), fg = "gold", bg = bg_color)
        F1.place(x=0, y=70, relwidth=1)

        cname_lbl = Label(F1, text="Customer Name :",bg = bg_color, fg="black" ,font=("times new roman", 18, "bold")).grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=13, textvariable=self.c_name, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        c_id_lbl = Label(F1, text="Customer ID :",bg = bg_color, fg="black" ,font=("times new roman", 18, "bold")).grid(row=0, column=2, padx=20, pady=5)
        c_id_txt = Entry(F1, width=13, textvariable=self.c_id, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        cphone_lbl = Label(F1, text="Phone No. :",bg = bg_color, fg="black" ,font=("times new roman", 18, "bold")).grid(row=0, column=4, padx=20, pady=5)
        cphone_txt = Entry(F1, width=13, textvariable=self.c_phone, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=5, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number: ",bg = bg_color, fg="black" ,font=("times new roman", 18, "bold")).grid(row=0, column=6, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=13, textvariable=self.search_bill, font="arial 15", bd=4, relief=SUNKEN).grid(row=0, column=7, pady=5, padx=10)

        bill_btn = Button(F1, text = "Search", command=self.find_bill, width=5, bd = 4, fg="black", font = "arial 12 bold").grid(row=0, column=8, padx=10, pady=10)


        # ========== ITEMS FRAME 1 ==========

        F2 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cosmetics", font=("times new roman", 15, "bold"), fg = "gold", bg = bg_color)
        F2.place(x=5, y=152, width=300, height=380)

        i_1_lbl = Label(F2, text="Bath Soap", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        i_1_txt = Entry(F2, width=18, textvariable=self.soap, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        i_2_lbl = Label(F2, text="Face Wash", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        i_2_txt = Entry(F2, width=18, textvariable=self.face_wash, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        i_3_lbl = Label(F2, text="Face Cream", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        i_3_txt = Entry(F2, width=18, textvariable=self.face_cream, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        i_4_lbl = Label(F2, text="Hair Spray", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        i_4_txt = Entry(F2, width=18, textvariable=self.hair_spray, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        i_5_lbl = Label(F2, text="Body Lotion", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        i_5_txt = Entry(F2, width=18, textvariable=self.bdy_ltn, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        i_6_lbl = Label(F2, text="Hair Gell", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        i_6_txt = Entry(F2, width=18, textvariable=self.hair_gell, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)


        # ========== ITEMS FRAME 2 ==========

        F3 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Grocery", font=("times new roman", 15, "bold"), fg = "gold", bg = bg_color)
        F3.place(x=310, y=152, width=300, height=380)

        i_7_lbl = Label(F3, text="Rice", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        i_7_txt = Entry(F3, width=18, textvariable=self.rice, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        i_8_lbl = Label(F3, text="Dal", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        i_8_txt = Entry(F3, width=18, textvariable=self.dal, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        i_9_lbl = Label(F3, text="Wheat", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        i_9_txt = Entry(F3, width=18, textvariable=self.wheat, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        i_10_lbl = Label(F3, text="Mst Oil", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        i_10_txt = Entry(F3, width=18, textvariable=self.mst_oil, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        i_11_lbl = Label(F3, text="Sugar", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        i_11_txt = Entry(F3, width=18, textvariable=self.sugar, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        i_12_lbl = Label(F3, text="Tea", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        i_12_txt = Entry(F3, width=18, textvariable=self.tea, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)

        # ========== ITEMS FRAME 3 ==========

        F4 = LabelFrame(self.root, bd=10, relief=GROOVE, text="Cold Drinks", font=("times new roman", 15, "bold"), fg = "gold", bg = bg_color)
        F4.place(x=615, y=152, width=300, height=380)

        i_13_lbl = Label(F4, text="Mnt Dwe", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        i_13_txt = Entry(F4, width=18, textvariable=self.mnt_dwe, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=0, column=1, pady=10, padx=10)

        i_14_lbl = Label(F4, text="Pepsi", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        i_14_txt = Entry(F4, width=18, textvariable=self.ppsi, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=1, column=1, pady=10, padx=10)

        i_15_lbl = Label(F4, text="Limca", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        i_15_txt = Entry(F4, width=18, textvariable=self.limca, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=2, column=1, pady=10, padx=10)

        i_16_lbl = Label(F4, text="Sprit", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        i_16_txt = Entry(F4, width=18, textvariable=self.sprit, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=3, column=1, pady=10, padx=10)

        i_17_lbl = Label(F4, text="Red Bull", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        i_17_txt = Entry(F4, width=18, textvariable=self.red_bull, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=4, column=1, pady=10, padx=10)

        i_18_lbl = Label(F4, text="Lassi", font=("times new roman",16, "bold"),bg=bg_color, fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        i_18_txt = Entry(F4, width=18, textvariable=self.lassi, font=("times new roman", 16, "bold"),bd=5, relief=SUNKEN).grid(row=5, column=1, pady=10, padx=10)


        # ========== Bill Area ==========

        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=920, y=152, width=430, height=380)

        bill_title = Label(F5, text="Bill Area", font="arial 15 bold", bd=7, relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)


        # ========== Buttom Frame ==========

        F6= LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu", font=("times new roman", 15, "bold"), fg = "gold", bg = bg_color)
        F6.place(x=0, y=535, relwidth=1, height=140)

        m1_lbl = Label(F6, text="Total Cosmetics Price",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=0, column=0, padx=20, pady=1,sticky="w")
        m1_txt = Entry(F6, width=18, textvariable=self.cosmetic_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=1,padx=10, pady=1)

        m2_lbl = Label(F6, text="Total Grocery Price",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=1, column=0, padx=20, pady=1,sticky="w")
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=1,padx=10, pady=1)

        m3_lbl = Label(F6, text="Total Clod Drinks Price",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=2, column=0, padx=20, pady=1,sticky="w")
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drink_price, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=1,padx=10, pady=1)



        c1_lbl = Label(F6, text="Cosmetics Tax",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=0, column=2, padx=20, pady=1,sticky="w")
        c1_txt = Entry(F6, width=18, textvariable=self.cosmetic_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=0,column=3,padx=10, pady=1)

        c2_lbl = Label(F6, text="Grocery Tax",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=1, column=2, padx=20, pady=1,sticky="w")
        c2_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=1,column=3,padx=10, pady=1)

        c3_lbl = Label(F6, text="Cold Drink Tax",bg=bg_color,fg="black", font=("times new roman", 14, "bold")).grid(row=2, column=2, padx=20, pady=1,sticky="w")
        c3_txt = Entry(F6, width=18, textvariable=self.cold_drink_tax, font="arial 10 bold", bd=7, relief=SUNKEN).grid(row=2,column=3,padx=10, pady=1)


        btn_F =Frame(F6, bd=7, relief=GROOVE)
        btn_F.place(x=750, width=575, height=105)


        total_btn = Button(btn_F, command=self.total, text="Total", bg="cadetblue", fg="white",bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=0, padx=5, pady=5)

        GBill_btn = Button(btn_F, text="Generate Bill", command=self.bill_area, bg="cadetblue", fg="white",bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=1, padx=5, pady=5)

        Clear_btn = Button(btn_F, text="Clear", command=self.clear_data, bg="cadetblue", fg="white",bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=2, padx=5, pady=5)

        Exit_btn = Button(btn_F, text="Exit", command=self.Exit_app, bg="cadetblue", fg="white",bd=2, pady=15, width=10, font="arial 15 bold").grid(row=0, column=3, padx=5, pady=5)

        self.welcome_bill()

    def total(self):

        self.c_s_p = self.soap.get()*40
        self.c_fw_p = self.face_wash.get()*140
        self.c_fc_p = self.face_cream.get()*70
        self.c_hs_p = self.hair_spray.get()*180
        self.c_bl_p = self.bdy_ltn.get()*200
        self.c_hg_p = self.hair_gell.get()*20

        self.total_cosmetic_price = float(
                                        self.c_s_p +
                                        self.c_fw_p +
                                        self.c_fc_p +
                                        self.c_hs_p +
                                        self.c_bl_p +
                                        self.c_hg_p
                                    )

        self.cosmetic_price.set("Rs." + str(self.total_cosmetic_price))  # This calculates the total cosmetics price

        self.c_tax = round((self.total_cosmetic_price * 0.05), 2)        # This calculates the total cosmetics tax

        self.cosmetic_tax.set("Rs." + str(self.c_tax))    


        self.g_r_p = self.rice.get()*75
        self.g_d_p = self.dal.get()*90
        self.g_w_p = self.wheat.get()*80
        self.g_mo_p = self.mst_oil.get()*200
        self.g_s_p = self.sugar.get()*45
        self.g_t_p = self.tea.get()*20
        
        self.total_grocery_price = float(
                                        self.g_r_p +
                                        self.g_d_p +
                                        self.g_w_p +
                                        self.g_mo_p +
                                        self.g_s_p +
                                        self.g_t_p
                                    )

        self.grocery_price.set("Rs." + str(self.total_grocery_price))   # This calculates the total grocery price

        self.g_tax = round((self.total_grocery_price * 0.1), 2)         # This calculates the total grocery tax

        self.grocery_tax.set("Rs." + str(self.g_tax))


        self.d_md_p = self.mnt_dwe.get()*60
        self.d_p_p = self.ppsi.get()*45
        self.d_l_p = self.limca.get()*45
        self.d_s_p = self.sprit.get()*65
        self.d_rd_p = self.red_bull.get()*110
        self.d_la_p = self.lassi.get()*20
        
        self.total_drinks_price = float(
                                        self.d_md_p +
                                        self.d_p_p +
                                        self.d_l_p +
                                        self.d_s_p +
                                        self.d_rd_p +
                                        self.d_la_p
                                    )

        self.cold_drink_price.set("Rs." + str(self.total_drinks_price))

        self.d_tax = round((self.total_drinks_price * 0.05), 2)

        self.cold_drink_tax.set("Rs." + str(self.d_tax))


        self.Total_bill = float(  self.total_cosmetic_price +
                                  self.total_grocery_price +
                                  self.total_drinks_price +
                                  self.c_tax +
                                  self.g_tax +
                                  self.d_tax

                                )


    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\t            Welcome TH_Retil\n")
        self.txtarea.insert(END, f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Customer ID : {self.c_id.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END, f"\n=======================================================")
        self.txtarea.insert(END, f"\n Products\t\t\tQuantity\t\t\tPrice")
        self.txtarea.insert(END, f"\n=======================================================")


    def bill_area(self):

        if self.c_name.get() == "" or self.c_phone.get() == "" or self.c_id.get() == "" :
            messagebox.showerror("Error", "Customer details are must")

        elif self.cosmetic_price.get() == "Rs.0.0" and self.grocery_price.get() == "Rs.0.0" and self.cold_drink_price.get() == "Rs.0.0":
            messagebox.showerror("Error", "No Product Purchased")

        else:
            self.welcome_bill()

            #========== Cosmetics ==========
            if self.soap.get() != 0:
                self.txtarea.insert(END, f"\n Bath Soap\t\t\t   {self.soap.get()}\t\t\t {self.c_s_p}")

            if self.face_wash.get() != 0:
                self.txtarea.insert(END, f"\n Face Wash\t\t\t   {self.face_wash.get()}\t\t\t {self.c_fw_p}")

            if self.face_cream.get() != 0:
                self.txtarea.insert(END, f"\n Face Cream\t\t\t   {self.face_cream.get()}\t\t\t {self.c_fc_p}")

            if self.hair_spray.get() != 0:
                self.txtarea.insert(END, f"\n Hair Spray\t\t\t   {self.hair_spray.get()}\t\t\t {self.c_hs_p}")

            if self.bdy_ltn.get() != 0:
                self.txtarea.insert(END, f"\n Body Lotion\t\t\t   {self.bdy_ltn.get()}\t\t\t {self.c_bl_p}")

            if self.hair_gell.get() != 0:
                self.txtarea.insert(END, f"\n Hair Gell\t\t\t   {self.hair_gell.get()}\t\t\t {self.c_hg_p}")


            #========== Grocery ==========
            if self.rice.get() != 0:
                self.txtarea.insert(END, f"\n Rice\t\t\t   {self.rice.get()}\t\t\t {self.g_r_p}")

            if self.dal.get() != 0:
                self.txtarea.insert(END, f"\n Dal\t\t\t   {self.dal.get()}\t\t\t {self.g_d_p}")

            if self.wheat.get() != 0:
                self.txtarea.insert(END, f"\n Wheat\t\t\t   {self.wheat.get()}\t\t\t {self.g_w_p}")

            if self.mst_oil.get() != 0:
                self.txtarea.insert(END, f"\n Mustard Oil\t\t\t   {self.mst_oil.get()}\t\t\t {self.g_mo_p}")

            if self.sugar.get() != 0:
                self.txtarea.insert(END, f"\n Sugar\t\t\t   {self.sugar.get()}\t\t\t {self.g_s_p}")

            if self.tea.get() != 0:
                self.txtarea.insert(END, f"\n Tea\t\t\t   {self.tea.get()}\t\t\t {self.g_t_p}")


            #========== Cold Drinks ==========
            if self.mnt_dwe.get() != 0:
                self.txtarea.insert(END, f"\n Mountain Dew\t\t\t   {self.mnt_dwe.get()}\t\t\t {self.d_md_p}")

            if self.ppsi.get() != 0:
                self.txtarea.insert(END, f"\n Pepsi\t\t\t   {self.ppsi.get()}\t\t\t {self.d_p_p}")

            if self.limca.get() != 0:
                self.txtarea.insert(END, f"\n Limca\t\t\t   {self.limca.get()}\t\t\t {self.d_l_p}")

            if self.sprit.get() != 0:
                self.txtarea.insert(END, f"\n Sprit\t\t\t   {self.sprit.get()}\t\t\t {self.d_s_p}")

            if self.red_bull.get() != 0:
                self.txtarea.insert(END, f"\n Red Bull\t\t\t   {self.red_bull.get()}\t\t\t {self.d_rd_p}")

            if self.lassi.get() != 0:
                self.txtarea.insert(END, f"\n Lassi\t\t\t   {self.lassi.get()}\t\t\t {self.d_la_p}")


            self.txtarea.insert(END, f"\n*******************************************************")

            if self.cosmetic_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Cosmetic Tax\t\t\t\t\t     {self.cosmetic_tax.get()}")

            if self.grocery_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Grocery Tax\t\t\t\t\t     {self.grocery_tax.get()}")

            if self.cold_drink_tax.get() != "Rs.0.0":
                self.txtarea.insert(END, f"\n Cold Drink Tax\t\t\t\t\t     {self.cold_drink_tax.get()}")

            self.txtarea.insert(END, f"\n Total Bill : \t\t\t\t\t     Rs.{self.Total_bill}")
            self.txtarea.insert(END, f"\n*******************************************************")
            self.save_bill()



    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the Bill ?")
        if op>0:

            self.bill_data =self.txtarea.get('1.0', END)
            f1 = open("Bills/" + str(self.bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no. {self.bill_no.get()} Saved Successfully")

        else:
            return

    def find_bill(self):
        present = "no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Bills/{i}","r")
                self.txtarea.delete('1.0', END)
                for d in f1:
                    self.txtarea.insert(END, d)
                f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No.")


    def clear_data(self):

        op = messagebox.askyesno("Clear", "Do you really want to clear ?")
        if op>0:
        
            # ========== Cosmetics ==========

            self.soap.set(0)
            self.face_wash.set(0)
            self.face_cream.set(0)
            self.hair_spray.set(0)
            self.bdy_ltn.set(0)
            self.hair_gell.set(0)

            #========== Grocery ==========

            self.rice.set(0)
            self.dal.set(0)
            self.wheat.set(0)
            self.mst_oil.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ========== Cold Drinks ==========

            self.mnt_dwe.set(0)
            self.ppsi.set(0)
            self.limca.set(0)
            self.sprit.set(0)
            self.red_bull.set(0)
            self.lassi.set(0)

            # ========== Total Product Price ==========

            self.cosmetic_price.set(" ")
            self.grocery_price.set(" ")
            self.cold_drink_price.set(" ")

            # ========== Total Product Tax ==========

            self.cosmetic_tax.set(" ")
            self.grocery_tax.set(" ")
            self.cold_drink_tax.set(" ")

            # ========== Customer ==========

            self.c_name.set(" ")
            self.c_id.set(" ")
            self.c_phone.set(" ")
            self.bill_no.set(" ")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))
            self.search_bill.set(" ")
            self.welcome_bill()



    def Exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit ?")
        if op>0:
            self.root.destroy()




root = Tk()
obj = Bill_App(root)
root.mainloop()
