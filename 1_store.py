from brian import *
from time import time
stdp_gmax=10.0
stdp2_a_step=1
stdp1_a_step=1
conn1_init_weight=3.0
nw_arch=[32,100,100]

conn2_init_weight=3.0
stdp_tau=100.0
dt_=0.1
sim_dur_ff=30.0
conn1_prob=0.7
conn2_prob=0.7

spike_times_iter_stdp=[[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,138.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,1078.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[16.0,36.0,58.0,10060.0,10080.0,117.0,133.0,10140.0,174.0,194.0,10200.0,10220.0,254.0,277.0,296.0,10300.0,334.0,10340.0,374.0,10380.0,416.0,434.0,454.0,478.0,497.0,514.0,10520.0,556.0,576.0,597.0,617.0,638.0,656.0,673.0,698.0,714.0,736.0,10740.0,774.0,10780.0,10800.0,838.0,856.0,874.0,10880.0,916.0,933.0,10940.0,977.0,10980.0,11000.0,1036.0,11040.0,1073.0,11080.0,11100.0,1137.0,11140.0,11160.0,1197.0,1217.0,1238.0,11240.0,1278.0,11280.0,1315.0,1334.0,1354.0,1378.0,1398.0,1414.0,1437.0,1457.0,1477.0,11480.0],[16.0,36.0,58.0,10060.0,10080.0,117.0,133.0,10140.0,174.0,194.0,10200.0,10220.0,254.0,277.0,296.0,10300.0,334.0,10340.0,374.0,10380.0,416.0,434.0,454.0,478.0,497.0,514.0,10520.0,556.0,576.0,597.0,617.0,638.0,656.0,673.0,698.0,714.0,736.0,10740.0,774.0,10780.0,10800.0,838.0,856.0,874.0,10880.0,916.0,933.0,10940.0,977.0,10980.0,11000.0,1036.0,11040.0,1073.0,11080.0,11100.0,1137.0,11140.0,11160.0,1197.0,1217.0,1238.0,11240.0,1278.0,11280.0,1315.0,1334.0,1354.0,1378.0,1398.0,1414.0,1437.0,1457.0,1477.0,11480.0],[13.0,34.0,53.0,73.0,93.0,113.0,137.0,153.0,175.0,195.0,218.0,233.0,255.0,273.0,294.0,315.0,335.0,355.0,375.0,393.0,413.0,435.0,455.0,473.0,493.0,516.0,533.0,553.0,573.0,593.0,613.0,633.0,653.0,677.0,693.0,716.0,733.0,753.0,775.0,793.0,814.0,833.0,853.0,875.0,893.0,914.0,937.0,953.0,973.0,995.0,1013.0,1034.0,1054.0,1077.0,1094.0,1116.0,1133.0,1153.0,1174.0,1193.0,1213.0,1233.0,1253.0,1273.0,1293.0,1314.0,1335.0,1356.0,1373.0,1393.0,1415.0,1433.0,1453.0,1473.0,1498.0],[10000.0,10020.0,58.0,76.0,96.0,118.0,10120.0,157.0,10160.0,10180.0,213.0,237.0,10240.0,278.0,10280.0,314.0,10320.0,354.0,10360.0,397.0,10400.0,10420.0,10440.0,478.0,498.0,10500.0,536.0,10540.0,10560.0,598.0,618.0,637.0,10640.0,10660.0,697.0,10700.0,10720.0,757.0,10760.0,797.0,816.0,837.0,10840.0,10860.0,896.0,10900.0,10920.0,956.0,978.0,995.0,1017.0,11020.0,1055.0,11060.0,1095.0,1113.0,1138.0,1157.0,1175.0,1198.0,1218.0,1238.0,1256.0,1278.0,1296.0,11300.0,11320.0,11340.0,1377.0,1397.0,11400.0,1438.0,1458.0,1478.0,1493.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,217.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,1497.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[18.0,37.0,57.0,76.0,96.0,118.0,135.0,156.0,176.0,195.0,217.0,235.0,256.0,276.0,298.0,316.0,337.0,356.0,376.0,396.0,417.0,437.0,456.0,476.0,496.0,517.0,536.0,556.0,576.0,595.0,617.0,636.0,656.0,676.0,697.0,717.0,735.0,756.0,776.0,795.0,816.0,836.0,855.0,876.0,896.0,917.0,937.0,956.0,976.0,996.0,1016.0,1038.0,1056.0,1076.0,1096.0,1116.0,1136.0,1155.0,1175.0,1196.0,1216.0,1235.0,1256.0,1275.0,1296.0,1317.0,1335.0,1356.0,1376.0,1396.0,1417.0,1436.0,1456.0,1476.0,1496.0],[18.0,37.0,57.0,76.0,96.0,118.0,135.0,156.0,176.0,195.0,217.0,235.0,256.0,276.0,298.0,316.0,337.0,356.0,376.0,396.0,417.0,437.0,456.0,476.0,496.0,517.0,536.0,556.0,576.0,595.0,617.0,636.0,656.0,676.0,697.0,717.0,735.0,756.0,776.0,795.0,816.0,836.0,855.0,876.0,896.0,917.0,937.0,956.0,976.0,996.0,1016.0,1038.0,1056.0,1076.0,1096.0,1116.0,1136.0,1155.0,1175.0,1196.0,1216.0,1235.0,1256.0,1275.0,1296.0,1317.0,1335.0,1356.0,1376.0,1396.0,1417.0,1436.0,1456.0,1476.0,1496.0],[15.0,36.0,56.0,76.0,97.0,115.0,138.0,156.0,177.0,198.0,216.0,238.0,256.0,277.0,296.0,316.0,336.0,356.0,376.0,396.0,416.0,436.0,457.0,477.0,497.0,516.0,537.0,558.0,577.0,598.0,616.0,637.0,657.0,676.0,696.0,716.0,738.0,757.0,777.0,798.0,817.0,838.0,858.0,876.0,897.0,916.0,936.0,957.0,978.0,997.0,1017.0,1036.0,1057.0,1077.0,1096.0,1117.0,1137.0,1158.0,1178.0,1197.0,1217.0,1238.0,1256.0,1278.0,1297.0,1316.0,1338.0,1357.0,1377.0,1397.0,1416.0,1437.0,1456.0,1477.0,1498.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,118.0,138.0,10140.0,10160.0,10180.0,10200.0,10220.0,258.0,10260.0,298.0,10300.0,338.0,10340.0,10360.0,10380.0,418.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,936.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,1078.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10.0,33.0,10040.0,10060.0,10080.0,109.0,129.0,10140.0,171.0,10180.0,10200.0,10220.0,249.0,10260.0,289.0,10300.0,329.0,10340.0,373.0,10380.0,409.0,430.0,450.0,10460.0,10480.0,515.0,10520.0,10540.0,10560.0,10580.0,613.0,10620.0,10640.0,670.0,10680.0,712.0,10720.0,10740.0,772.0,10780.0,10800.0,10820.0,10840.0,870.0,10880.0,911.0,928.0,10940.0,10960.0,10980.0,11000.0,1033.0,11040.0,1069.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,1310.0,11320.0,1350.0,11360.0,11380.0,1412.0,11420.0,11440.0,11460.0,11480.0],[10.0,33.0,10040.0,10060.0,10080.0,109.0,129.0,10140.0,171.0,10180.0,10200.0,10220.0,249.0,10260.0,289.0,10300.0,329.0,10340.0,373.0,10380.0,409.0,430.0,450.0,10460.0,10480.0,515.0,10520.0,10540.0,10560.0,10580.0,613.0,10620.0,10640.0,670.0,10680.0,712.0,10720.0,10740.0,772.0,10780.0,10800.0,10820.0,10840.0,870.0,10880.0,911.0,928.0,10940.0,10960.0,10980.0,11000.0,1033.0,11040.0,1069.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,1310.0,11320.0,1350.0,11360.0,11380.0,1412.0,11420.0,11440.0,11460.0,11480.0],[12.0,29.0,10040.0,10060.0,10080.0,114.0,133.0,10140.0,171.0,196.0,10200.0,10220.0,254.0,10260.0,293.0,10300.0,333.0,10340.0,369.0,10380.0,413.0,432.0,452.0,10460.0,10480.0,508.0,10520.0,10540.0,10560.0,10580.0,609.0,10620.0,10640.0,672.0,10680.0,710.0,10720.0,10740.0,770.0,10780.0,10800.0,10820.0,10840.0,872.0,10880.0,911.0,936.0,10940.0,10960.0,10980.0,11000.0,1029.0,11040.0,1073.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,1312.0,1338.0,1352.0,11360.0,11380.0,1410.0,11420.0,11440.0,11460.0,11480.0],[10000.0,38.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,188.0,10200.0,238.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,378.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,517.0,10520.0,558.0,577.0,10580.0,618.0,638.0,10640.0,10660.0,10680.0,10700.0,733.0,10740.0,10760.0,10780.0,10800.0,10820.0,855.0,10860.0,10880.0,10900.0,10920.0,958.0,976.0,10980.0,11000.0,1038.0,1058.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,1215.0,1236.0,11240.0,11260.0,11280.0,11300.0,1329.0,11340.0,11360.0,1396.0,11400.0,1437.0,11440.0,1477.0,11480.0],[10000.0,10020.0,51.0,78.0,10080.0,10100.0,10120.0,10140.0,10160.0,196.0,10200.0,230.0,10240.0,276.0,10280.0,10300.0,10320.0,353.0,10360.0,393.0,10400.0,10420.0,10440.0,474.0,496.0,10500.0,10520.0,550.0,568.0,596.0,10600.0,629.0,655.0,10660.0,698.0,10700.0,730.0,755.0,10760.0,796.0,812.0,10820.0,849.0,10860.0,10880.0,10900.0,10920.0,949.0,968.0,10980.0,1016.0,11020.0,1050.0,11060.0,11080.0,11100.0,1136.0,1155.0,11160.0,1191.0,1209.0,1228.0,1251.0,1276.0,1298.0,11300.0,1334.0,11340.0,1373.0,1388.0,11400.0,1428.0,1454.0,1469.0,11480.0],[10000.0,10020.0,52.0,69.0,90.0,10100.0,10120.0,155.0,10160.0,10180.0,218.0,233.0,10240.0,268.0,10280.0,312.0,10320.0,350.0,10360.0,390.0,10400.0,10420.0,10440.0,469.0,488.0,10500.0,531.0,553.0,576.0,588.0,10600.0,634.0,649.0,10660.0,690.0,10700.0,738.0,749.0,10760.0,788.0,811.0,831.0,857.0,10860.0,891.0,10900.0,10920.0,954.0,977.0,990.0,1008.0,11020.0,1053.0,11060.0,1092.0,1113.0,1128.0,1149.0,1173.0,1192.0,1217.0,1237.0,1252.0,1268.0,1289.0,11300.0,11320.0,11340.0,1370.0,1397.0,11400.0,1436.0,1449.0,1475.0,11480.0],[10000.0,10020.0,10040.0,74.0,92.0,10100.0,10120.0,148.0,10160.0,10180.0,209.0,10220.0,10240.0,276.0,10280.0,310.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,478.0,496.0,10500.0,531.0,10540.0,10560.0,597.0,10600.0,10620.0,657.0,10660.0,693.0,10700.0,10720.0,757.0,10760.0,797.0,10800.0,831.0,10840.0,10860.0,891.0,10900.0,10920.0,10940.0,10960.0,992.0,1016.0,11020.0,11040.0,11060.0,1090.0,1109.0,1136.0,1157.0,1169.0,11180.0,11200.0,11220.0,11240.0,1277.0,1294.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,1458.0,11460.0,1494.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,178.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,1358.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[15.0,35.0,57.0,78.0,97.0,115.0,135.0,158.0,175.0,196.0,218.0,236.0,255.0,277.0,295.0,318.0,335.0,356.0,375.0,397.0,415.0,435.0,455.0,477.0,497.0,515.0,538.0,556.0,576.0,598.0,615.0,636.0,658.0,675.0,698.0,715.0,736.0,757.0,775.0,797.0,817.0,836.0,856.0,875.0,898.0,915.0,935.0,956.0,976.0,998.0,1017.0,1035.0,1056.0,1075.0,1098.0,1117.0,1137.0,1157.0,1177.0,1196.0,1216.0,1236.0,1257.0,1277.0,1297.0,1315.0,1336.0,1355.0,1376.0,1396.0,1415.0,1436.0,1457.0,1476.0,1498.0],[15.0,35.0,57.0,78.0,97.0,115.0,135.0,158.0,175.0,196.0,218.0,236.0,255.0,277.0,295.0,318.0,335.0,356.0,375.0,397.0,415.0,435.0,455.0,477.0,497.0,515.0,538.0,556.0,576.0,598.0,615.0,636.0,658.0,675.0,698.0,715.0,736.0,757.0,775.0,797.0,817.0,836.0,856.0,875.0,898.0,915.0,935.0,956.0,976.0,998.0,1017.0,1035.0,1056.0,1075.0,1098.0,1117.0,1137.0,1157.0,1177.0,1196.0,1216.0,1236.0,1257.0,1277.0,1297.0,1315.0,1336.0,1355.0,1376.0,1396.0,1415.0,1436.0,1457.0,1476.0,1498.0],[18.0,38.0,56.0,75.0,96.0,118.0,138.0,155.0,178.0,197.0,216.0,236.0,258.0,276.0,298.0,315.0,338.0,356.0,378.0,396.0,418.0,438.0,458.0,476.0,496.0,518.0,535.0,557.0,576.0,596.0,618.0,636.0,656.0,678.0,695.0,718.0,737.0,756.0,778.0,796.0,816.0,836.0,857.0,878.0,895.0,918.0,938.0,956.0,977.0,995.0,1016.0,1038.0,1056.0,1078.0,1095.0,1116.0,1136.0,1156.0,1176.0,1196.0,1217.0,1237.0,1256.0,1276.0,1296.0,1318.0,1337.0,1358.0,1376.0,1396.0,1418.0,1437.0,1456.0,1476.0,1495.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0],[10000.0,10020.0,10040.0,10060.0,10080.0,10100.0,10120.0,10140.0,10160.0,10180.0,10200.0,10220.0,10240.0,10260.0,10280.0,10300.0,10320.0,10340.0,10360.0,10380.0,10400.0,10420.0,10440.0,10460.0,10480.0,10500.0,10520.0,10540.0,10560.0,10580.0,10600.0,10620.0,10640.0,10660.0,10680.0,10700.0,10720.0,10740.0,10760.0,10780.0,10800.0,10820.0,10840.0,10860.0,10880.0,10900.0,10920.0,10940.0,10960.0,10980.0,11000.0,11020.0,11040.0,11060.0,11080.0,11100.0,11120.0,11140.0,11160.0,11180.0,11200.0,11220.0,11240.0,11260.0,11280.0,11300.0,11320.0,11340.0,11360.0,11380.0,11400.0,11420.0,11440.0,11460.0,11480.0]]
spike_times_iter_ff3d=[[[10000.0],[18.0],[18.0],[13.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[12.0],[10000.0],[10000.0],[17.0],[17.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[15.0],[15.0],[14.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[18.0],[18.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[11.0],[11.0],[10000.0],[10000.0],[10000.0],[10000.0],[18.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[13.0],[13.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[11.0],[11.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[10000.0],[10000.0],[15.0],[14.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[8.0],[16.0],[10000.0],[18.0],[18.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[16.0],[16.0],[13.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[12.0],[10000.0],[10000.0],[17.0],[17.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[10000.0],[10000.0],[15.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[14.0],[9.0],[10000.0],[18.0],[18.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[18.0],[13.0],[13.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10.0],[10.0],[12.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[16.0],[16.0],[14.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[17.0],[17.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[11.0],[11.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[14.0],[14.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[17.0],[17.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[11.0],[11.0],[11.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[16.0],[16.0],[13.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[15.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[8.0],[17.0],[10000.0],[10000.0],[16.0],[16.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[10000.0],[10000.0],[14.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[12.0],[10.0],[10000.0],[18.0],[18.0],[15.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[15.0],[15.0],[14.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[15.0],[9.0],[17.0],[10000.0],[10000.0],[16.0],[16.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[17.0],[17.0],[13.0],[18.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[17.0],[9.0],[15.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[10000.0],[10000.0],[14.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[17.0],[8.0],[15.0],[10000.0],[18.0],[18.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]],[[10000.0],[10000.0],[10000.0],[18.0],[13.0],[17.0],[10000.0],[10000.0],[10000.0],[16.0],[16.0],[17.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[10000.0],[12.0],[10000.0],[18.0],[18.0],[16.0],[10000.0],[10000.0],[10000.0],[10000.0]]]
ip_pattern_idx=[68,32,3,141,66,143,8,10,19,53,144,59,95,147,122]
iter = 1
sim_dur_stdp=1500.0 * iter
#
#

k=0.571/ms/mV
a=0.13
b=-2.714
d=111.506
C=81.2
vR=-60.5*mV
vT=-34.8*mV
vPeak=42.4*mV
c=-60.0*mV
Is=0

eta = 0.1

model9pEqs= Equations('''
		dV/dt=(k*((V-vR)*(V-vT))-U+I)/(C) : volt
		dU/dt=a*((b*(V-vR)/ms/ms)-(U/ms)) : volt/second
		I : mV/ms
		''')

eqs_stdp='''
dA_pre/dt=-A_pre/tau : 1
dA_post/dt=-A_post/tau : 1
'''

simclock = Clock(dt=dt_*ms)
spikeTimes = [(i, t*ms) for i in xrange(len(spike_times_iter_stdp)) for t in spike_times_iter_stdp[i]]

inputLayer = SpikeGeneratorGroup(nw_arch[0], spikeTimes, clock=simclock)
hiddenLayer = NeuronGroup(nw_arch[1], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
outputLayer = NeuronGroup(nw_arch[2], model=model9pEqs, threshold="V>vPeak", reset="V=c;U+=d", method= "RK", clock=simclock)
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0

conn1 = Connection(inputLayer, hiddenLayer, 'V', weight=conn1_init_weight*mV, sparseness=conn1_prob)
#conn11 = Connection(inputLayer, hiddenLayer, 'V', weight=-conn1_init_weight*mV, sparseness=0.05)
conn2 = Connection(hiddenLayer, outputLayer, 'V', weight=conn2_init_weight*mV, sparseness=conn2_prob)
#conn22 = Connection(hiddenLayer, outputLayer, 'V', weight=-conn2_init_weight*mV, sparseness=0.05)

tau = stdp_tau*ms
stdp1=STDP(conn1,eqs=eqs_stdp,pre='A_pre+=stdp1_a_step*mV;w+=A_post*eta',post='A_post+=stdp1_a_step*mV;w+=A_pre*eta',wmax=stdp_gmax*mV, clock=simclock)
#stdp11=STDP(conn1,eqs=eqs_stdp,pre='A_pre+=stdp1_a_step*mV;w+=A_post',post='A_post+=stdp1_a_step*mV;w+=A_pre',wmax=stdp_gmax*mV, clock=simclock)
stdp2=STDP(conn2,eqs=eqs_stdp,pre='A_pre+=stdp2_a_step*mV;w+=A_post*eta',post='A_post+=stdp2_a_step*mV;w+=A_pre*eta',wmax=stdp_gmax*mV, clock=simclock)
#stdp22=STDP(conn22,eqs=eqs_stdp,pre='A_pre+=stdp2_a_step*mV;w+=A_post',post='A_post+=stdp2_a_step*mV;w+=A_pre',wmax=stdp_gmax*mV, clock=simclock)

SMO = SpikeMonitor(outputLayer)

SMI = SpikeMonitor(inputLayer)
SM = SpikeMonitor(hiddenLayer)
VM = StateMonitor(outputLayer, 'V', record=True, clock=simclock) 
Mpr = PopulationRateMonitor(outputLayer, bin=dt_*ms)

run(sim_dur_stdp*ms)
colors=[0,0,0]
subplot(311)
raster_plot(SMI, title='Input Layer')
axis([0, sim_dur_stdp, 0, nw_arch[0]])
subplot(312)
raster_plot(SM, title='Hidden Layer')
axis([0, sim_dur_stdp, 0, nw_arch[1]])
subplot(313)
raster_plot(SMO, title='Output Layer')
axis([0, sim_dur_stdp, 0, nw_arch[2]])
show()
#
#
doPlotSub = True
def feed_forward(spikeTimesIterList, ipPatternIdx, gridCell):
    reinit(states=False)
    spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIterList)) for t in spikeTimesIterList[i]]
    inputLayer.spiketimes=spikeTimes
    t1 = time()
    run(sim_dur_ff*ms)
    t2 = time()
    
#    print "#$ip_pattern_idx:", ipPatternIdx
#    print "$op_layer_pop_rates:", " ".join(str(p) for p in Mpr.rate)
#    print "$sim_time:", t2 - t1, "s"
#    print "$op_layer_spike_times:"
#    for i in xrange(0, nw_arch[len(nw_arch)-1]):
#        print " ".join(str(p) for p in SMO[i])+","

	
	
    if doPlotSub:
        colors=[0,0,0]
        subplot(3,nCols,gridCell) 
#        plot(Mpr.times/ms, Mpr.rate/Hz)
        raster_plot(SMO, title='Output for ptn#.'+str(ipPatternIdx))
        axis([0, sim_dur_ff, 0, nw_arch[2]])
        
        

stdp1 = None
stdp2=None
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0

nCols=5
gridRow1 = 1
gridRow2 = nCols+1
gridRow3 = (nCols*2)+1

for i in xrange(0, len(spike_times_iter_ff3d)):
    if(ip_pattern_idx[i]<50):
        gridCell = gridRow1
        gridRow1+=1
    else:
        if(ip_pattern_idx[i]<100):
            gridCell = gridRow2
            gridRow2+=1
        else:
            if(ip_pattern_idx[i]<150):
                gridCell = gridRow3
                gridRow3+=1     
    feed_forward(spikeTimesIterList = spike_times_iter_ff3d[i], ipPatternIdx = ip_pattern_idx[i], gridCell=gridCell)
show()
