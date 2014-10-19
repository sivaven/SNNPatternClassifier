from brian import *
from time import time
spike_times_iter_ff3d=[[[1510.0],[14.0],[14.0],[15.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[16.0],[16.0],[16.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[13.0],[13.0],[9.0],[18.0],[1510.0],[1510.0],[1510.0],[1510.0],[15.0],[15.0],[18.0],[1510.0],[1510.0],[1510.0],[1510.0]],[[1510.0],[18.0],[18.0],[13.0],[18.0],[1510.0],[1510.0],[1510.0],[1510.0],[15.0],[15.0],[18.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[16.0],[8.0],[17.0],[1510.0],[1510.0],[16.0],[16.0],[17.0],[1510.0],[1510.0],[1510.0],[1510.0]],[[1510.0],[1510.0],[1510.0],[18.0],[13.0],[18.0],[1510.0],[1510.0],[1510.0],[16.0],[16.0],[17.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[1510.0],[11.0],[1510.0],[18.0],[18.0],[15.0],[1510.0],[1510.0],[1510.0],[1510.0]]]
conn2_init_weight=5.0
stdp_gmax=100.0
ip_pattern_idx=[23,62,105]
conn1_init_weight=3.0
stdp_tau=10.0
spike_times_iter_stdp=[[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,158.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,678.0,2190.0,718.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,34.0,53.0,1570.0,94.0,116.0,137.0,153.0,1670.0,194.0,1710.0,234.0,1750.0,1770.0,297.0,318.0,337.0,354.0,374.0,397.0,414.0,1930.0,455.0,1970.0,498.0,513.0,537.0,554.0,574.0,595.0,616.0,634.0,656.0,673.0,694.0,713.0,2230.0,755.0,2270.0,795.0,2310.0,834.0,2350.0,878.0,898.0,918.0,2430.0,956.0,977.0,2490.0,2510.0,2530.0,2550.0,2570.0,1096.0,1116.0,1134.0,1156.0,1176.0,2690.0,1217.0,1237.0,1258.0,2770.0,2790.0,1314.0,2830.0,2850.0,2870.0,1397.0,1417.0,2930.0,2950.0,2970.0,1496.0],[1510.0,34.0,53.0,1570.0,94.0,116.0,137.0,153.0,1670.0,194.0,1710.0,234.0,1750.0,1770.0,297.0,318.0,337.0,354.0,374.0,397.0,414.0,1930.0,455.0,1970.0,498.0,513.0,537.0,554.0,574.0,595.0,616.0,634.0,656.0,673.0,694.0,713.0,2230.0,755.0,2270.0,795.0,2310.0,834.0,2350.0,878.0,898.0,918.0,2430.0,956.0,977.0,2490.0,2510.0,2530.0,2550.0,2570.0,1096.0,1116.0,1134.0,1156.0,1176.0,2690.0,1217.0,1237.0,1258.0,2770.0,2790.0,1314.0,2830.0,2850.0,2870.0,1397.0,1417.0,2930.0,2950.0,2970.0,1496.0],[13.0,35.0,57.0,75.0,95.0,114.0,133.0,157.0,176.0,195.0,213.0,236.0,253.0,278.0,293.0,313.0,333.0,355.0,375.0,393.0,415.0,434.0,454.0,473.0,493.0,516.0,533.0,556.0,575.0,594.0,613.0,635.0,653.0,677.0,695.0,717.0,735.0,754.0,775.0,794.0,814.0,835.0,853.0,873.0,893.0,913.0,934.0,953.0,973.0,995.0,1014.0,1033.0,1054.0,1073.0,1093.0,1113.0,1135.0,1153.0,1173.0,1193.0,1213.0,1233.0,1253.0,1274.0,1294.0,1315.0,1337.0,1358.0,1378.0,1393.0,1413.0,1434.0,1453.0,1478.0,1493.0],[16.0,1530.0,1550.0,74.0,1590.0,1610.0,138.0,1650.0,173.0,1690.0,216.0,1730.0,256.0,273.0,298.0,317.0,338.0,1850.0,1870.0,398.0,1910.0,435.0,1950.0,477.0,497.0,2010.0,538.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,734.0,2250.0,774.0,2290.0,815.0,2330.0,857.0,877.0,897.0,917.0,935.0,2450.0,978.0,995.0,1015.0,1037.0,1055.0,1077.0,2590.0,2610.0,2630.0,2650.0,2670.0,1197.0,1218.0,1238.0,1257.0,1276.0,1295.0,2810.0,1333.0,1353.0,1373.0,1398.0,1418.0,1435.0,1457.0,1473.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,277.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,1357.0,1377.0,2890.0,2910.0,2930.0,2950.0,1477.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[16.0,36.0,56.0,76.0,97.0,118.0,136.0,156.0,176.0,196.0,216.0,236.0,256.0,276.0,298.0,316.0,338.0,357.0,377.0,397.0,416.0,436.0,457.0,475.0,497.0,516.0,536.0,556.0,576.0,598.0,618.0,637.0,657.0,676.0,697.0,715.0,736.0,757.0,776.0,796.0,816.0,835.0,856.0,876.0,895.0,916.0,936.0,956.0,976.0,996.0,1016.0,1035.0,1056.0,1075.0,1095.0,1115.0,1135.0,1155.0,1176.0,1196.0,1216.0,1236.0,1256.0,1276.0,1295.0,1315.0,1336.0,1356.0,1377.0,1396.0,1415.0,1436.0,1456.0,1476.0,1496.0],[16.0,36.0,56.0,76.0,97.0,118.0,136.0,156.0,176.0,196.0,216.0,236.0,256.0,276.0,298.0,316.0,338.0,357.0,377.0,397.0,416.0,436.0,457.0,475.0,497.0,516.0,536.0,556.0,576.0,598.0,618.0,637.0,657.0,676.0,697.0,715.0,736.0,757.0,776.0,796.0,816.0,835.0,856.0,876.0,895.0,916.0,936.0,956.0,976.0,996.0,1016.0,1035.0,1056.0,1075.0,1095.0,1115.0,1135.0,1155.0,1176.0,1196.0,1216.0,1236.0,1256.0,1276.0,1295.0,1315.0,1336.0,1356.0,1377.0,1396.0,1415.0,1436.0,1456.0,1476.0,1496.0],[17.0,37.0,57.0,77.0,96.0,116.0,137.0,157.0,177.0,197.0,217.0,237.0,257.0,277.0,295.0,318.0,335.0,356.0,376.0,396.0,417.0,437.0,456.0,478.0,496.0,516.0,537.0,557.0,576.0,595.0,615.0,636.0,656.0,676.0,696.0,718.0,736.0,756.0,777.0,797.0,817.0,838.0,856.0,877.0,898.0,917.0,937.0,957.0,977.0,997.0,1017.0,1038.0,1057.0,1078.0,1098.0,1118.0,1138.0,1158.0,1177.0,1197.0,1217.0,1237.0,1257.0,1276.0,1298.0,1318.0,1337.0,1358.0,1376.0,1397.0,1418.0,1436.0,1457.0,1477.0,1497.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,298.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,578.0,2090.0,2110.0,2130.0,658.0,678.0,2190.0,718.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,30.0,51.0,1570.0,90.0,113.0,1630.0,150.0,1670.0,191.0,1710.0,230.0,1750.0,1770.0,289.0,1810.0,331.0,350.0,371.0,393.0,412.0,1930.0,451.0,1970.0,1990.0,512.0,2030.0,552.0,569.0,591.0,610.0,631.0,649.0,669.0,692.0,709.0,2230.0,751.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,30.0,51.0,1570.0,90.0,113.0,1630.0,150.0,1670.0,191.0,1710.0,230.0,1750.0,1770.0,289.0,1810.0,331.0,350.0,371.0,393.0,412.0,1930.0,451.0,1970.0,1990.0,512.0,2030.0,552.0,569.0,591.0,610.0,631.0,649.0,669.0,692.0,709.0,2230.0,751.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,32.0,51.0,1570.0,92.0,109.0,1630.0,152.0,1670.0,191.0,1710.0,232.0,1750.0,1770.0,294.0,1810.0,331.0,352.0,371.0,389.0,410.0,1930.0,451.0,1970.0,1990.0,510.0,2030.0,550.0,574.0,591.0,612.0,631.0,653.0,673.0,690.0,713.0,2230.0,751.0,2270.0,2290.0,2310.0,838.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,1138.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,118.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,398.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,795.0,2310.0,829.0,2350.0,2370.0,2390.0,916.0,938.0,2450.0,977.0,2490.0,2510.0,2530.0,1058.0,1078.0,1093.0,1114.0,1129.0,1156.0,1177.0,2690.0,1217.0,1237.0,1258.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,76.0,1590.0,1610.0,136.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,437.0,1950.0,476.0,498.0,2010.0,536.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,733.0,2250.0,775.0,789.0,812.0,834.0,853.0,873.0,891.0,908.0,930.0,951.0,968.0,994.0,1016.0,1035.0,1050.0,1070.0,1090.0,1109.0,1134.0,1148.0,1168.0,2690.0,1208.0,1229.0,1249.0,1276.0,2790.0,1311.0,2830.0,2850.0,2870.0,1396.0,1416.0,2930.0,1455.0,2970.0,1495.0],[10.0,1530.0,1550.0,68.0,1590.0,1610.0,128.0,1650.0,173.0,1690.0,211.0,1730.0,251.0,276.0,1790.0,311.0,1830.0,1850.0,1870.0,1890.0,1910.0,428.0,1950.0,468.0,490.0,2010.0,528.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,730.0,2250.0,769.0,797.0,811.0,2330.0,850.0,870.0,892.0,917.0,933.0,952.0,976.0,989.0,1008.0,1029.0,1053.0,1073.0,1098.0,1118.0,2630.0,1157.0,1176.0,1191.0,1216.0,1235.0,1254.0,1268.0,1293.0,1312.0,1338.0,2850.0,2870.0,1388.0,1408.0,1432.0,1449.0,2970.0,1489.0],[12.0,1530.0,1550.0,76.0,1590.0,1610.0,136.0,1650.0,169.0,1690.0,211.0,1730.0,251.0,268.0,1790.0,311.0,1830.0,1850.0,1870.0,1890.0,1910.0,435.0,1950.0,477.0,493.0,2010.0,536.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,777.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,998.0,1017.0,1037.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,1191.0,2710.0,2730.0,2750.0,1276.0,1289.0,2810.0,1329.0,1354.0,1372.0,1396.0,1417.0,1430.0,1457.0,1472.0,1497.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,198.0,1710.0,238.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,598.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[17.0,35.0,55.0,78.0,95.0,115.0,137.0,155.0,177.0,195.0,218.0,235.0,258.0,278.0,295.0,316.0,335.0,355.0,375.0,395.0,415.0,438.0,455.0,477.0,498.0,515.0,537.0,555.0,575.0,595.0,615.0,635.0,655.0,675.0,695.0,715.0,736.0,755.0,777.0,796.0,816.0,836.0,857.0,876.0,897.0,916.0,936.0,957.0,976.0,996.0,1017.0,1037.0,1056.0,1076.0,1096.0,1116.0,1136.0,1156.0,1176.0,1197.0,1216.0,1236.0,1256.0,1278.0,1297.0,1317.0,1337.0,1358.0,1378.0,1398.0,1418.0,1438.0,1457.0,1478.0,1498.0],[17.0,35.0,55.0,78.0,95.0,115.0,137.0,155.0,177.0,195.0,218.0,235.0,258.0,278.0,295.0,316.0,335.0,355.0,375.0,395.0,415.0,438.0,455.0,477.0,498.0,515.0,537.0,555.0,575.0,595.0,615.0,635.0,655.0,675.0,695.0,715.0,736.0,755.0,777.0,796.0,816.0,836.0,857.0,876.0,897.0,916.0,936.0,957.0,976.0,996.0,1017.0,1037.0,1056.0,1076.0,1096.0,1116.0,1136.0,1156.0,1176.0,1197.0,1216.0,1236.0,1256.0,1278.0,1297.0,1317.0,1337.0,1358.0,1378.0,1398.0,1418.0,1438.0,1457.0,1478.0,1498.0],[16.0,38.0,58.0,75.0,98.0,118.0,136.0,158.0,176.0,198.0,215.0,238.0,255.0,275.0,298.0,316.0,338.0,358.0,378.0,398.0,418.0,435.0,458.0,476.0,495.0,518.0,536.0,558.0,578.0,598.0,618.0,638.0,658.0,678.0,698.0,718.0,736.0,758.0,776.0,796.0,816.0,837.0,856.0,876.0,896.0,916.0,936.0,956.0,977.0,996.0,1016.0,1036.0,1056.0,1076.0,1097.0,1117.0,1137.0,1156.0,1176.0,1196.0,1216.0,1236.0,1256.0,1276.0,1296.0,1316.0,1336.0,1355.0,1375.0,1395.0,1416.0,1435.0,1456.0,1476.0,1496.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0],[1510.0,1530.0,1550.0,1570.0,1590.0,1610.0,1630.0,1650.0,1670.0,1690.0,1710.0,1730.0,1750.0,1770.0,1790.0,1810.0,1830.0,1850.0,1870.0,1890.0,1910.0,1930.0,1950.0,1970.0,1990.0,2010.0,2030.0,2050.0,2070.0,2090.0,2110.0,2130.0,2150.0,2170.0,2190.0,2210.0,2230.0,2250.0,2270.0,2290.0,2310.0,2330.0,2350.0,2370.0,2390.0,2410.0,2430.0,2450.0,2470.0,2490.0,2510.0,2530.0,2550.0,2570.0,2590.0,2610.0,2630.0,2650.0,2670.0,2690.0,2710.0,2730.0,2750.0,2770.0,2790.0,2810.0,2830.0,2850.0,2870.0,2890.0,2910.0,2930.0,2950.0,2970.0,2990.0]]
sim_dur_stdp=1500.0
stdp2_a_step=0.1
sim_dur_ff=500.0
stdp1_a_step=0.1
dt_=1.0
nw_arch=[32,20,3]
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

conn1 = Connection(inputLayer, hiddenLayer, 'V', weight=conn1_init_weight*mV, sparseness=1)
conn2 = Connection(hiddenLayer, outputLayer, 'V', weight=conn2_init_weight*mV, sparseness=1)
tau = stdp_tau*ms
stdp1=STDP(conn1,eqs=eqs_stdp,pre='A_pre+=stdp1_a_step*mV;w+=A_post',post='A_post+=stdp1_a_step*mV;w+=A_pre',wmax=stdp_gmax*mV, clock=simclock)
stdp2=STDP(conn2,eqs=eqs_stdp,pre='A_pre+=stdp2_a_step*mV;w+=A_post',post='A_post+=stdp2_a_step*mV;w+=A_pre',wmax=stdp_gmax*mV, clock=simclock)
SMO = SpikeMonitor(outputLayer)

SMI = SpikeMonitor(inputLayer)
SM = SpikeMonitor(hiddenLayer)
VM = StateMonitor(outputLayer, 'V', record=True, clock=simclock) 

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
def feed_forward(spikeTimesIterList, ipPatternIdx):
	reinit(states=False)
	spikeTimes = [(i, t*ms) for i in xrange(len(spikeTimesIterList)) for t in spikeTimesIterList[i]]
	inputLayer.spiketimes=spikeTimes
	t1 = time()
	run(sim_dur_ff*ms)
	t2 = time()
	print "#$ip_pattern_idx:", ipPatternIdx
	print "$sim_time:", t2 - t1, "s"
	print "$op_layer_spike_times:"
	for i in xrange(0, nw_arch[len(nw_arch)-1]):
		print " ".join(str(p) for p in SMO[i])+","

	
stdp1 = None
stdp2=None
hiddenLayer.V = vR 
hiddenLayer.U =0
outputLayer.V = vR 
outputLayer.U =0
for i in xrange(0, len(spike_times_iter_ff3d)):
	feed_forward(spikeTimesIterList = spike_times_iter_ff3d[i], ipPatternIdx = ip_pattern_idx[i])
