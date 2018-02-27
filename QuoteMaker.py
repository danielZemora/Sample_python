import csv
from tkinter import *
xspacing = 200
yspacing = 50
xflat = 150
yflat = 100
global_list = []
global_type = []
class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        primarymenu = self.primaryMenu()        
        x = primarymenu.get()
        okay = Button(self, text = "Okay", command = lambda: Window.wholemenulist(self,primarymenu))
        okay.grid(row=0,column=0)
        saveme = Button(self, text = "Save", command = lambda: Window.getgot(global_list))
        saveme.place(x=300,y=300)
    def init_window(self):
        self.master.title("Zemoz Tile Take-Off Document")
        self.pack(fill=BOTH, expand=1)
    def global_list_append(self,list):
        global_list.clear()
        for x in list:
            global_list.append(x)
    def getgot(list):
        mylist = []
        myvar = StringVar(root)
        get = myvar.get()
        novavar = StringVar()
        for x in list:
            novavar = x.get()
            if novavar == "":
                novavar = "Null"
            mylist.append(novavar)
        menulist = ['Reg-Drains','Line-Drains','Heating-Products','Sub-floors','Water-Proofing','Prep-Work','Function-Products','Tile']
        for x in global_type:
           p = x
        if p == menulist[0]:
            costlist1 = reg_drain.drain(mylist)
        elif p == menulist[1]:
            costlist1 = line_drain.drain(mylist)
        elif p == menulist[2]:
            costlist1 = heating_products.heating(mylist)
        elif p == menulist[3]:
            costlist1 = subfloors.prep(mylist)
        elif p == menulist[4]:
            costlist1 = waterproofing.waterproofing(mylist)
        elif p == menulist[5]:
            costlist1 = prepwork.prep_work(mylist)
        elif p == menulist[6]:
            costlist1 = funcproducts.func_products(mylist)
        elif p == menulist[7]:
            costlist1 = tilecost.tile_cost(mylist)
        else:
            print('something went wrong')
        print(costlist1)
        return costlist1
    def wholemenulist(self,input):
        mylist = []
        myvar = StringVar(root)
        get = myvar.get()
        novavar = StringVar()
        novavar = input.get()
        p = novavar
        global_type.clear()
        global_type.append(p)
        menulist = ['Reg-Drains','Line-Drains','Heating-Products','Sub-floors','Water-Proofing','Prep-Work','Function-Products','Tile']
        if p == menulist[0]:
            itemlist = self.regdrain(1)
        elif p == menulist[1]:
            itemlist = self.linedrain(1)
        elif p == menulist[2]:
            itemlist = self.heatingproducts(1)
        elif p == menulist[3]:
            itemlist = self.subfloors(1)
        elif p == menulist[4]:
            itemlist = self.waterproofing(1)
        elif p == menulist[5]:
            itemlist = self.prepwork(1)
        elif p == menulist[6]:
            itemlist = self.funcproducts(1)
        elif p == menulist[7]:
            itemlist = self.tile(1)
        else:
            itemlist = 0

        return itemlist
    def showText(self, textinput,xVar,yVar):
        text = Label(self, text=str(textinput))
        text.place(x=xVar,y=yVar)
    def primaryMenu(self):
        maindropdown = ['Reg-Drains','Line-Drains','Heating-Products','Sub-floors','Water-Proofing','Prep-Work','Function-Products','Tile']
        mainmenudata = self.menubutton(maindropdown,0,1)
        return mainmenudata
        #tilecost = [tilequantitylist1,tilequantitylist2,...,tilequantitylist5]
            #tilequantitylist = [sqft,l1,l2,tilesupplier,tilecode]
    def menubutton(self,dropdown,xVar,yVar):
        variable = StringVar(self)
        button = OptionMenu(self,variable,*dropdown)
        button.grid(row=xVar,column = yVar)
        return variable
    def inputbox(self,xVar,yVar):
        v = StringVar(root)
        e = Entry(self,textvariable=v)
        e.grid(row=xVar,column=yVar)
        return e
    def regdrain(self,ygap):
        drain_finish = ['Tileable','Stainless Steel','Chrome','Oil Rubbed Bronze','Brushed Brass','Brushed Copper','Brushed Nickel'] #some of this data is just stored here so I can look at it while im writing.
        drain_type = ['ABS','PVC','Stainless Steel']
        drain_type_size = ['2"','4"']
        drain_finish_size = ['4"','6"']
        pan_size = ['48"X48"','72"X72"','32"X60"','38"X38"','48"X72"']
        #regdrain = [drainfinish,draintype,draintypesize,drainfinishsize,pansize]
        x1 = self.menubutton(drain_finish,xflat,yflat*ygap)
        x2 = self.menubutton(drain_type,xflat+xspacing*1,yflat*ygap)
        x3 = self.menubutton(drain_type_size,xflat+xspacing*2,yflat*ygap)
        x4 = self.menubutton(drain_finish_size,xflat+xspacing*3,yflat*ygap)
        x5 = self.menubutton(pan_size,xflat+xspacing*4,yflat*ygap)
        self.global_list_append([x1,x2,x3,x4,x5])
        return
    def linedrain(self,ygap):
        drain_finish = ['Stainless Steel','Brushed Stainless Steel','Chrome','Tileable','Off-Set']
        drain_finish_option = ['Non-Perforated','Perforated']
        drain_finish_size = [50,60,70,80,90,100,110,120,130,140,150,160,170,180]
        pan_size = ['39"X39"','55"X55"','Custom Sizing']
        pan_type = ['Wall Drain Placement','Center Drain Placement']
        #line drain = [drainfinish,drainfinishoption,drainfinishsize,pansize, pantype]
        x1 = self.menubutton(drain_finish,xflat,yflat)
        x2 = self.menubutton(drain_finish_option,xflat+xspacing,yflat*ygap)
        x3 = self.menubutton(drain_finish_size,xflat+xspacing*2,yflat*ygap)
        x4 = self.menubutton(pan_size,xflat+xspacing*3,yflat*ygap)
        x5 = self.menubutton(pan_type,xflat+xspacing*4,yflat*ygap)
        self.global_list_append([x1,x2,x3,x4,x5])
        return
    def heatingproducts(self,ygap):
        #heating products = [wire_ID,themostat_type]
        heatlist = ['22.6 sqft 120V','33.9 sqft 120V','43.4 sqft 120V','58.4 sqft 120V','68.8 sqft 120V','78.8 sqft 120V','90.6 sqft 120V','103.2 sqft 120V','115.8 sqft 120V','10.6 sqft 240V','21.4 sqft 240V','30.2 sqft 240V','36.8 sqft 240V','44.7 sqft 240V','52.2 sqft 240V','58.9 sqft 240V','66.1 sqft 240V','73 sqft 240V','84.4 sqft 240V','95.1 sqft 240V','104.2 sqft 240V','114.6 sqft 240V','135.8 sqft 240V','155.8 sqft 240V','179.5 sqft 240V','204.9 sqft 240V','230.5 sqft 240V']
        thermostatlist = ['Elements (Non-Prog)','Home Series (Prog/Touch)','Signature (Prog/Touch/Wifi)']
        x1 = self.menubutton(heatlist,xflat,yflat*ygap)
        x2 = self.menubutton(thermostatlist,xflat+xspacing,yflat*ygap)
        self.global_list_append([x1,x2])
        return 
    def subfloors(self,ygap):
        #subfloors = [item,quantity]
        items = ['Anti Fracture Membrane','Uncoupling Membrane','Xl Uncoupling Membrane','Heated Uncoupling']
        x1 = self.menubutton(items,xflat,yflat*ygap)
        quantity = self.inputbox(xflat+xspacing,yflat*ygap)
        self.global_list_append([x1,quantity])
        return 
    def waterproofing(self,ygap):
        #waterproofing = [item, quantity]
        myitems = ['Liquid Waterproofing (per shower)','Kerdi waterproof','Kerdi Board Curb','Kerdi Bench','Niche cubby (unit install only)']
        x1 = self.menubutton(myitems,xflat,yflat*ygap)
        quantity = self.inputbox(xflat+xspacing,yflat*ygap)
        self.global_list_append([x1,quantity])
        return 
    def prepwork(self,ygap):
        #prepwork = [item,quantity]
        items = ['hourly','self_leveler']
        x1 = self.menubutton(items,xflat,yflat*ygap)
        quantity = self.inputbox(xflat+xspacing,yflat*ygap)
        self.global_list_append([x1,quantity])
        return 
    def funcproducts(self,ygap):
        #funcproducts = [type,data]
            ##data = [heights, widths]
            #heights = [x1,x2,...] 
            ##widths = [x1,x2,...]
        items = ['Bench','Insert']
        type = self.menubutton(items,xflat,yflat*ygap)
        self.showText("Heights Box (x1,x2,...)",xflat+xspacing,yflat*ygap-yspacing)
        heights = self.inputbox(xflat+xspacing,yflat*ygap)
        self.showText("Widths Box (x1,x2,...)",xflat+xspacing,yflat*ygap-yspacing)
        widths = self.inputbox(xflat+xspacing*3,yflat*ygap)
        self.global_list_append([type,heights,widths])
        return 
    def tile(self,ygap):
        #tilequantitylist = [sqft,l1,l2,tilesupplier,tilecode]
        ## self = [tilequantitylist1,tilequantitylist2,...,tilequantitylist5]
        list_of_suppliers = ['Ames','Julian','Ceramstone','Olympia','StoneTile','AnnSacks']
        sqft = self.inputbox(1,2)
        self.showText('Sqft',1,1)
        l1 = self.inputbox(2,2)
        self.showText('L1',2,1)
        l2 = self.inputbox(3,2)
        self.showText('L2',3,1)
        tilesupplier = self.menubutton(list_of_suppliers,4,1)
        tilecode = self.inputbox(4,2)
        listofoutput = [sqft,l1,l2,tilesupplier,tilecode]
        self.global_list_append(listofoutput)
        return
class reg_drain:
    
    def __init__(self):
        pass
    def openfile():
        with open('reg_drains.csv','r') as regdrain:
            regdrainpricinglist = {}
            reader = csv.reader(regdrain)
            for x in reader:
                regdrainpricinglist[x[0]] = float(x[1]) 
            return regdrainpricinglist
    def drain(self):
        drain_finish = ['Tileable','Stainless Steel','Chrome','Oil Rubbed Bronze','Brushed Brass','Brushed Copper','Brushed Nickel'] #some of this data is just stored here so I can look at it while im writing.
        drain_type = ['ABS','PVC','Stainless Steel']
        drain_type_size = ['2"','4"']
        drain_finish_size = ['4"','6"']
        pan_size = ['48"X48"','72"X72"','32"X60"','38"X38"','48"X72"']
        pricingdict = reg_drain.openfile()
        # self will be a list of finish, type, type size, finish size. self = [drainfinish,draintype,draintypesize,drainfinishsize,pansize]
        #indexing may largely be useless except for drain type index
        steeldraincode = self[4] + '_S'
        if self[0] == "":
            return
        else:
            drain_finish_index = drain_finish.index(self[0])
            drain_type_index = drain_type.index(self[1])
            drain_type_size_index = drain_type_size.index(self[2])
            drain_finish_size_index = drain_finish_size.index(self[3])
            pan_size_index = pan_size.index(self[4])
        #applying cost address

        regdraincode = self[4]
        if drain_type_index == [2]:
            cost = pricingdict[steeldraincode]
        else:
            cost = pricingdict[regdraincode]

        data = ['Drain Internal Size: '+self[2],'Drain Exteral Size: '+self[3],'Drain Finish Type: '+self[1]]
        returnlist = [cost,data]
        return returnlist
class line_drain:
    def __init__():
        pass
    def openfile():
        with open('line_drains.csv','r') as ld:
            linedrainpricing = {}
            reader = csv.reader(ld)
            for x in reader:
                linedrainpricing[x[0]] = float(x[1])
            return linedrainpricing
    def drain(self):
        pricingdict = line_drain.openfile()
        # self = [drainfinish,drainfinishoption,drainfinishsize,pansize, pantype]
        drain_finish = ['Stainless Steel','Brushed Stainless Steel','Chrome','Tileable','Off-Set']
        drain_finish_option = ['Non-Perforated','Perforated']
        drain_finish_size = [50,60,70,80,90,100,110,120,130,140,150,160,170,180]
        pan_size = ['39"X39"','55"X55"','Custom Sizing']
        pan_type = ['Wall Drain Placement','Center Drain Placement']
        # applying cost
        if self[0] == "":
            return
        else:
            drainsizecost = pricingdict[self[2]]
            pansizecost = pricingdict[self[3]]
        totalcost = float(drainsizecost) + float(pansizecost)
        data = ['Drain Finish: '+self[0]+" "+self[1],'Pan size and type: '+self[3]+' '+self[4]]
        returnlist = [totalcost,[data]]
        return returnlist
class heating_products:
    def __init__():
        pass
    def openfile():
        with open('heating_options.csv','r') as ho:
            heating_pricing = {}
            reader = csv.reader(ho)
            for x in reader:
                heating_pricing[x[0]] = float(x[1])
            return heating_pricing
    def heating(self):
        pricingdict = heating_products.openfile()
        #self = [wire_ID,themostat_type]
        if self[0]== "":
            return
        else: 
            wirecost = pricingdict[self[0]]
            thermostatcost = pricingdict[self[1]]
        totalcost = wirecost+thermostatcost
        data = ['Wire Size and Type: '+self[0],'Thermostat type'+self[1]]
        returnvalue = [totalcost,data]
        return returnvalue
class subfloors:
    def __init__():
        pass
    def openfile():
        with open('subfloors.csv','r') as pw:
            prep_pricing = {}
            reader = csv.reader(pw)
            for x in reader:
                prep_pricing[x[0]] = float(x[1])
            return prep_pricing
    def prep(self):
        pricingdict = subfloors.openfile()
        #self = [item,quantity]
        if self[0]== "":
            return
        else:
            itemcost = pricingdict[self[0]]
            totalcost = float(itemcost) * float(self[1])
        data = ['Subfloor Type: '+self[0],'Subfloor Quantity: '+self[1]]
        returnvalue = [itemcost,totalcost,data]
        return returnvalue
class waterproofing:
    def __init__():
        pass
    def openfile():
        with open('waterproofing.csv','r') as wp:
            water_proofing = {}
            reader = csv.reader(wp)
            for x in reader:
                water_proofing[x[0]] = float(x[1])
            return water_proofing
    def waterproofing(self):
        pricingdict = waterproofing.openfile()
        #self = [item, quantity]
        if self[0] == "":
            return
        else:
            itemcost = pricingdict[self[0]]
            totalcost = float(itemcost) * float(self[1])
        data = ['Waterproofing Type: '+self[0],'Quantity: '+self[1]]
        returnvalue = [itemcost,totalcost,data]
        return returnvalue
class prepwork:
    def __init__():
        pass
    def openfile():
        with open('prep_work.csv','r') as pw:
            prep_work = {}
            reader = csv.reader(pw)
            for x in reader:
                prep_work[x[0]] = float(x[1])
            return prep_work
    def prep_work(self):
        pricingdict = prepwork.openfile()
        # self = [item,quantity]
        if self[0] == "":
            return
        else:
            itemcost = pricingdict[self[0]]
            totalcost = float(itemcost) * float(self[1])
        data = ['Work Type: '+self[0],'Quantity: '+self[1]]
        returnvalue = [itemcost,totalcost,data]
        return returnvalue
class funcproducts:
    def __init__():
        pass
    def openfile():
        with open('function_products.csv','r') as pw:
            prep_work = {}
            reader = csv.reader(pw)
            for x in reader:
                prep_work[x[0]] = float(x[1])
            return prep_work
    def func_products(self):
        pricingdict = funcproducts.openfile()
        #self = [insertlist,benchlist]
        #benchlist/insertlist = [heights, widths]
        #heights = [x1,x2,...]
        #widths = [x1,x2,...]
            #funcproducts = [type,data]
        ##data = [heights, widths]
        #heights = [x1,x2,...] 
        ##widths = [x1,x2,...]
        insert_height_cost = pricingdict['insert_H']
        insert_width_cost = pricingdict['insert_W']
        insert_flat_cost = pricingdict['insert_F']
        bench_height_cost = pricingdict['bench_length_L']
        bench_width_cost = pricingdict['bench_width_L']
        bench_flat_cost = pricingdict['bench_top_L']

        #options = ['Bench','Insert']
        type = self[0]
        measurement1 = float(self[1])
        measurement2 = float(self[2])
        cost_list = []
        if type == 'Bench':
            benchcost = ((measurement1 * (bench_width_cost*bench_height_cost) * measurement2) + bench_flat_cost)
            cost_list.append(benchcost)
        elif type == 'Insert':        
            insertcost = ((measurement1 * (insert_width_cost*insert_height_cost) * measurement2) + insert_flat_cost)
            cost_list.append(insertcost)
        else:
            cost_list.append(0)
        returnlist = [cost_list,[measurement1,measurement2]]
        return returnlist
class tilecost:
    def __init__():
        pass
    def tile_cost(self):
        #tilequantitylist = [sqft,l1,l2,tilesupplier,tilecode]
        ## self = [tilequantitylist1,tilequantitylist2,...,tilequantitylist5]
        print(self)
        costlist = []
        if self[0] == "":
            return
        tottilecost = 0
        listoflist = [self]
        for p in listoflist:
            x1 = float(p[1])
            x2 = float(p[2])
            lenlist = [x1,x2]
            singlecostlist = []
            for x in lenlist:
                costanalysis = (((-2.538*(10**-7))*(x**5))+((5.364*(10**-5))*(x**4))+((-0.003959)*(x**3))+((0.1286)*(x**2))+((-1.755)*(x))+(12.03))
                singlecostlist.append(costanalysis)
            for x in singlecostlist:
                tottilecost += x
            costlist.append(tottilecost)
        returnlist = [costlist,self]
        return returnlist
root = Tk()

root.geometry("1920x1080")

app = Window(root)

root.mainloop()