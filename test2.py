class saham:
    def __init__(self,EpsOrPbv,mean,currentPrice):
        self.a=EpsOrPbv
        self.b=mean
        self.c=currentPrice


    def per(self):
        wajar= self.a * self.b
        print("wajar eps : ",wajar)
        print("harga saat ini : ", self.c)
        disc= 1-(self.c/wajar)
        print("diskon : ",disc*100 ," %" )

    def pbv(self):
        wajar = self.a * self.b
        print("wajar pbv : ", wajar)
        print("harga saat ini : ", self.c)
        disc = 1 - (self.c / wajar)
        print("diskon : ", disc * 100, " %")

    def growthPredict(self,eps10yearsAgo):
        Govbond=6.43
        Corpbond=8.2
        const=7
        GrowthCAGR= (((self.a / eps10yearsAgo) ** (1/6)) -1)
        GrowthRate = GrowthCAGR * 100
        print("Growth(CAGR) : ",GrowthCAGR * 100," %")
        intrinsic= (self.a*(const+GrowthRate)*Govbond)/Corpbond
        print("nilai intrinsik : ", intrinsic)
        print("harga saat ini : ", self.c)
        disc=1-(self.c/intrinsic)
        print("diskon : ", disc*100, " %")

#INPUT DISINI

CurrentPrice =2670 #Harga saat ini
#PER
EPS=286.6 #EPS TTM
MeanPE= 13.06#MEAN per


#PBV
PBV=1591.99 #PBV
MeanPBV=2.52 #MEAN PBV

#GROWTH GRAHAM
last10yearsEPS= 119.03 #EPS 10 TAHUN LALU

#METODE PER
print("METODE PBV")
cobaPer=saham(EPS,MeanPE,CurrentPrice)
cobaPer.per()

print("="*30)

#METODE PER
print("METODE PER")
cobaPbv=saham(PBV,MeanPBV,CurrentPrice)
cobaPbv.pbv()

print("="*30)

#METODE BENJAMIN GRAHAM
print("METODE BENJAMIN GRAHAM")
cobaGrowth =saham(EPS,0,CurrentPrice)# EPS TTM  , 0 , HARGA SAAT INI
cobaGrowth.growthPredict(last10yearsEPS) # eps 10 tahun yang lalu


