from .model import Producer, Station, Buffer

PRODUCERS = [
    Producer("P01","Nord",-14,22,420,0.085,0.100),
    Producer("P02","Nord",-10,18,260,0.090,0.100),
    Producer("P03","Nord",-7,25,310,0.075,0.100),
    Producer("P04","Centre",2,4,520,0.092,0.100),
    Producer("P05","Centre",5,-1,340,0.080,0.100),
    Producer("P06","Centre",-3,-5,280,0.088,0.100),
    Producer("P07","Est",22,4,600,0.090,0.100),
    Producer("P08","Est",26,9,450,0.095,0.105),
    Producer("P09","Est",19,-6,360,0.082,0.100),
    Producer("P10","Sud",5,-27,300,0.080,0.100),
    Producer("P11","Sud",10,-31,380,0.090,0.105),
    Producer("P12","Sud",1,-34,260,0.075,0.095),
]
STATIONS = [
    Station("S_N","Nord",-18,31,2500,0.65),
    Station("S_C","Centre",0,2,1800,0.55),
    Station("S_E","Est",31,1,2600,0.65),
    Station("S_S","Sud",8,-42,1800,0.75),
]
FIXED_HUB = Buffer("H0","Hub",0,0,3000)
MOBILE_BUFFERS = {
    "Nord":Buffer("B_N","Nord",-10,22,3000),
    "Centre":Buffer("B_C","Centre",2,0,3000),
    "Est":Buffer("B_E","Est",23,3,3000),
    "Sud":Buffer("B_S","Sud",6,-30,3000),
}
