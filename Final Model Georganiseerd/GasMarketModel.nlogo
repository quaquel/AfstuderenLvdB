breed [countries country]
undirected-link-breed [borderpipes borderpipe]
undirected-link-breed [transferroutes transferroute]
undirected-link-breed [LNGroutes LNGroute]

globals [
  transferprice
  LNGprice
  potentialdeals
  dealsmade

  THcheck

  LNGexportingcountries
  LNGimportingcountries

  gasimportlist
  gasexportlist

  coalimportlist
  coalexportlist

  oilimportlist
  oilexportlist

  biofuelimportlist
  biofuelexportlist

  coaldemandlist
  oildemandlist
  biofueldemandlist

  gasimportcostslist
  eugasimportlist

  powerfactor

  price1
  price2
  price3
  price4
  price5
  price6
  price7

  EnergyUnion
  russiangaslist

  mindealsize

  eurussiangas
  euthcheck

  Time
  Capincrease
  Capincreasetime
  LNGCapincrease
  LNGCapincreasetime
]

countries-own [
  PP
  GS
  totalimport
  totalexport
  TH

  linkedcountries
  linkedTH
  linkedHUB

  TRUElinkedcountries

  LNGimportcapacity
  LNGexportcapacity
  LNGimportavailable
  LNGexportavailable

  planningtoexpandLNGim
  planningtoexpandLNGex
  endtimeLNGim
  endtimeLNGex

  inputtransferprice
  inputLNGprice
  inputTime
  inputCapincrease
  inputCapincreasetime
  inputLNGCapincrease
  inputLNGCapincreasetime
  inputpowerfactor
  inputprice1
  inputprice2
  inputprice3
  inputprice4
  inputprice5
  inputprice6
  inputprice7
  inputenergyunion

  Coalsurplus
  Oilsurplus
  Biofuelsurplus

  Coalimport
  Coalexport
  Oilimport
  Oilexport
  Biofuelimport
  Biofuelexport

  Coaldemand
  Oildemand
  Biofueldemand

  Gasimportcosts

  region
  EU
  regionalgasprice
  russiangas
  eugasimport
]

borderpipes-own [
  pipelineprice
  pipelinepriceS
  pipelinepriceR
  PPS
  PPR
  P4T
  W2TS
  W2TR
  Soffer
  Roffer
  Deal
  transfertype
  capacity
  capacityavailable

  planningtoexpand
  endtime
  gasprice

]

transferroutes-own [
  pipelineprice
  pipelinepriceS
  pipelinepriceR
  PPS
  PPR
  P4T
  W2TS
  W2TR
  Soffer
  Roffer
  Deal
  transfertype
  route
  capacityroute
  capacity
  LNG
  gasprice
]

LNGroutes-own [
  pipelineprice
  pipelinepriceS
  pipelinepriceR
  PPS
  PPR
  P4T
  W2TS
  W2TR
  Soffer
  Roffer
  Deal
  transfertype
  capacity12
  capacity21
  capacity
  gasprice

  transfercount
]

to setup
  show ("SETUP")
  clear-all
  reset-ticks
  ask links [die]
  ask countries [die]

;  import-drawing "kaarteurope.jpg"
  set-default-shape turtles "circle"
  createcountries
  resetlinks

  ask countries [
    if region = 1 [set color green]
    if EU = 1 [set color blue]
    if region = 2 [set color red]
    if region = 3 [set color red]
    if region = 4 [set color red]
    if region = 5 [set color red]
    if region = 6 [set color red]
    if region = 7 [set color red]
  ]

  set energyunion 0
  if energyunion = 1 [
    ask countries [
      if eu = 1 [
        set pp 10
      ]
    ]
  ]

  ask borderpipes [set planningtoexpand 0]
  ask countries [
    set planningtoexpandLNGim 0
    set planningtoexpandLNGex 0
  ]

end

to createcountries
  create-countries 1 [ ;Belgium 0
    set xcor 3;4.44699
    set ycor 29;50.5039
    set region 1
    set EU 1
    set PP 7.5
    set GS -4.692494e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 336765.936
    set LNGexportcapacity 0
    set coalsurplus -5.395574e+05
    set oilsurplus -9.024094e+05
    set biofuelsurplus -4.072203e+04	

    set inputpowerfactor 10
    set inputLNGprice 4
    set inputtransferprice 2
    set inputprice1 16837.099955
    set inputprice2 6701.390869
    set inputprice3 11717.227292
    set inputprice4 8747.836253
    set inputprice5 10632.79531
    set inputprice5 11294.093315
    set inputprice6 13325.201647
    set inputenergyunion 0
  ]

  create-countries 1 [ ;Bulgaria 1
    set xcor 26;25.4858
    set ycor 16;42.7339
    set region 1
    set EU 1
    set PP 9.4
    set GS -4.801858e+04	
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 150236.97073365818
    set oilsurplus -127924.14018001057
    set biofuelsurplus -685.8576260993077
  ]

  create-countries 1 [ ;Czech Republic 2
    set xcor 15;15.4730
    set ycor 28;49.9175
    set region 1
    set EU 1
    set PP 8.4
    set GS -2.848574e+05	
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 17306.422704143915
    set oilsurplus -355970.6989854333
    set biofuelsurplus -4059.9564811470623
  ]

  create-countries 1 [ ;Denmark 3
    set xcor 8;9.5018
    set ycor 36;56.2639
    set region 1
    set EU 1
    set PP 7.8
    set GS -1.954537e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -524110.41609387967
    set oilsurplus -496100.07116708386
    set biofuelsurplus -4280.410156741714
  ]

  create-countries 1 [ ;Germany 4
    set xcor 9;10.4515
    set ycor 30;51.1657
    set region 1
    set EU 1
    set PP 8.2
    set GS  -2.376071e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -1599113.8516704757
    set oilsurplus -4468495.553703555
    set biofuelsurplus 81960.9733448585
  ]

  create-countries 1 [ ;Estonia 5
    set xcor 27;25.0136
    set ycor 41;58.5953
    set region 1
    set EU 1
    set PP 7.7
    set GS -2.432706e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -36110.76924168874
    set oilsurplus -53299.26132993025
    set biofuelsurplus -292.81736128230926
  ]

  create-countries 1 [ ;Ireland 6
    set xcor -11;7.6921
    set ycor 32;53.1424
    set region 1
    set EU 1
    set PP 10
    set GS -3.202831e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -486854.1055260821
    set oilsurplus -741930.5693385106
    set biofuelsurplus -3966.5970953970136
  ]

  create-countries 1 [ ;Greece 7
    set xcor 24;21.8243
    set ycor 11;39.0742
    set region 1
    set EU 1
    set PP 8.1
    set GS -1.516271e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 92190.71
    set LNGexportcapacity 0
    set coalsurplus -9143.057354447199
    set oilsurplus -572220.9451334183
    set biofuelsurplus -2672.3459848946486
  ]

  create-countries 1 [ ;Spain 8
    set xcor -6;3.7492
    set ycor 13;40.4637
    set region 1
    set EU 1
    set PP 7.5
    set GS -1.002908e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 2601145.727
    set LNGexportcapacity 0
    set coalsurplus -595181.2668417274
    set oilsurplus -2390875.1482784036
    set biofuelsurplus 26679.89264653179
  ]

  create-countries 1 [ ;France 9
    set xcor 0;2.2137
    set ycor 23;46.2276
    set region 1
    set EU 1
    set PP 7.5
    set GS -1.627638e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 201355.748
    set LNGexportcapacity 0
    set coalsurplus -539045.8883629768
    set oilsurplus -3090658.119381621
    set biofuelsurplus 67488.73869983167
  ]

  create-countries 1 [ ;Croatia 10
    set xcor 15;15.2
    set ycor 19;45.1
    set region 1
    set EU 1
    set PP 7.8
    set GS -6.104795e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -89939.38418956334
    set oilsurplus -138879.30687014293
    set biofuelsurplus -743.369026430551
  ]

  create-countries 1 [ ;Italy 11
    set xcor 12;12.5674
    set ycor 16;41.8719
    set region 1
    set EU 1
    set PP 6.7
    set GS -1.492277e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 508387.038
    set LNGexportcapacity 0
    set coalsurplus -605933.1711298055
    set oilsurplus -2091270.092279894
    set biofuelsurplus 5246.793945947647
  ]

  create-countries 1 [ ;Cyprus 12
    set xcor 35;33.4299
    set ycor 6;35.1264
    set region 1
    set EU 1
    set PP 8.1
    set GS -2.457164e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -36398.01390537348
    set oilsurplus -53723.23259160269
    set biofuelsurplus -295.1465895493573
  ]

  create-countries 1 [ ;Latvia 13
    set xcor 26;24.6032
    set ycor 38;56.8796
    set region 1
    set EU 1
    set PP 8.8
    set GS -3.011305e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -42640.72942156566
    set oilsurplus -64946.68439877466
    set biofuelsurplus -354.5782045844281
  ]

  create-countries 1 [ ;Lithuania 14
    set xcor 25;23.8813
    set ycor 36;55.1694
    set region 1
    set EU 1
    set PP 7.3
    set GS -4.591541e+04	
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 14786
    set LNGexportcapacity 0
    set coalsurplus -68726.86946407643
    set oilsurplus -104196.00467999167
    set biofuelsurplus -560.9417816010811
  ]

  create-countries 1 [ ;luxembourg 15
    set xcor 5;6.1296
    set ycor 28;49.8153
    set region 1
    set EU 1
    set PP 7.5
    set GS -6.198091e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -95099.11730718646
    set oilsurplus -143881.07740684637
    set biofuelsurplus -769.683994830755
  ]

  create-countries 1 [ ;Hungary 16
    set xcor 18;19.5033
    set ycor 22;47.1625
    set region 1
    set EU 1
    set PP 7.1
    set GS -2.364592e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -49932.78343818064
    set oilsurplus -275352.9570247878
    set biofuelsurplus -2150.125620310141
  ]

  create-countries 1 [ ;Malta 17
    set xcor 14;14.3754
    set ycor 7;35.9375
    set region 1
    set EU 1
    set PP 6.7
    set GS -1.156089e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -17219.395050530336
    set oilsurplus -26911.116908579927
    set biofuelsurplus -141.5741648309297
  ]

  create-countries 1 [ ;Netherlands 18
    set xcor 4;5.2913
    set ycor 30;52.1326
    set region 1
    set EU 1
    set PP 7.5
    set GS 5.315481e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 35619.474
    set LNGexportcapacity 0
    set coalsurplus -469266.57684962347
    set oilsurplus -1448199.98229737
    set biofuelsurplus 57188.97767446631
  ]

  create-countries 1 [ ;Austria 19
    set xcor 11;14.5501
    set ycor 21;47.5162
    set region 1
    set EU 1
    set PP 6.6
    set GS -2.664552e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -152388.08029724818
    set oilsurplus -503183.39535947575
    set biofuelsurplus 10284.314975677997
  ]

  create-countries 1 [ ;Poland 20
    set xcor 17;19.1451
    set ycor 30;51.9194
    set region 1
    set EU 1
    set PP 7.7
    set GS -4.954531e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 288193.926
    set LNGexportcapacity 0
    set coalsurplus 165223.78398611885
    set oilsurplus -1042034.2423637618
    set biofuelsurplus 24159.91954747339
  ]

  create-countries 1 [ ;Portugal 21
    set xcor -11;8.2245
    set ycor 14;39.3999
    set region 1
    set EU 1
    set PP 7.5
    set GS -1.777998e+05
    set linkedcountries []
    set totalimport 19428.804
    set totalexport 0
    set LNGimportcapacity 18.56194378
    set LNGexportcapacity 0
    set coalsurplus -147742.76585465876
    set oilsurplus -454220.39963329467
    set biofuelsurplus 9037.791112065013
  ]

  create-countries 1 [ ;Romania 22
    set xcor 27;24.9668
    set ycor 20;45.9432
    set region 1
    set EU 1
    set PP 7.2
    set GS 2.434595e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -65489.14392379008
    set oilsurplus -199597.92997771627
    set biofuelsurplus -3292.1520885553796
  ]

  create-countries 1 [ ;Slovenia 23
    set xcor 14;14.9955
    set ycor 21;46.1512
    set region 1
    set EU 1
    set PP 6.4
    set GS -5.084689e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -74273.14311244182
    set oilsurplus -114389.49305702797
    set biofuelsurplus -614.697016264782
  ]

  create-countries 1 [ ;Slovakia 24
    set xcor 19;19.6990
    set ycor 24;48.6690
    set region 1
    set EU 1
    set PP 7.4
    set GS -1.029743e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -153709.70873892395
    set oilsurplus -238537.0323840399
    set biofuelsurplus -1267.8047678325897
  ]

  create-countries 1 [ ;Finland 25
    set xcor 25;25.7482
    set ycor 46;61.9241
    set region 1
    set EU 1
    set PP 6.5
    set GS -1.471898e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -170685.3026480496
    set oilsurplus -374755.4384766048
    set biofuelsurplus 12717.598567201992
  ]

  create-countries 1 [ ;Sweden 26
    set xcor 15;18.6435
    set ycor 42;60.1282
    set region 1
    set EU 1
    set PP 6.5
    set GS -2.234429e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -127771.74730424504
    set oilsurplus -565037.9693729922
    set biofuelsurplus 2610.769528160745
  ]

  create-countries 1 [ ;United Kingdom 27
    set xcor -3;-3.4360
    set ycor 30;55.3781
    set region 1
    set EU 1
    set PP 10
    set GS -6.389594e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 1217538.384
    set LNGexportcapacity 939058.86
    set coalsurplus -932893.1018341928
    set oilsurplus -1070252.810895356
    set biofuelsurplus -8416.719674838208
  ]

  create-countries 1 [ ;Norway 28
    set xcor 7;8.4689
    set ycor 43;60.4720
    set region 1
    set EU 0
    set PP 10
    set GS 3.741346e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 281717.658
    set coalsurplus -52626.325010836976
    set oilsurplus 3344438.7168786833
    set biofuelsurplus -4725.721013791823
  ]

  create-countries 1 [ ;Switzerland 29
    set xcor 5;8.2275
    set ycor 21;46.8182
    set region 1
    set EU 0
    set PP 6.6
    set GS -1.566047e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -29332.39855049063
    set oilsurplus -426656.9181310498
    set biofuelsurplus -2835.4781617839985
  ]

  create-countries 1 [ ;Non-EU Balkan 30
    set xcor 20;17.6791
    set ycor 17;43.9159
    set region 1
    set EU 0
    set PP 8.1
    set GS -8.819341e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 144312.73871813278
    set oilsurplus -220845.33693115084
    set biofuelsurplus -1174.4761963159215
  ]

  create-countries 1 [ ;Turkey & Georgia 31
    set xcor 34;35.2433
    set ycor 12;38.9637
    set region 1
    set EU 0
    set PP 8
    set GS -1.328541e+06
    set linkedcountries []
    set totalimport 1408588.29
    set totalexport 0
    set LNGimportcapacity 1345.740924
    set LNGexportcapacity 0
    set coalsurplus -921201.5881566396
    set oilsurplus -1695240.7378269802
    set biofuelsurplus -13779.93644372495
  ]

  create-countries 1 [ ;North America 32
    set xcor -29
    set ycor 13
    set region 2
    set EU 0
    set PP 9
    set GS -2.695848e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 340078
    set LNGexportcapacity 643191
    set coalsurplus 1110257.599303469
    set oilsurplus -5836797.774517149
    set biofuelsurplus 1027590.9185767432
  ]

  create-countries 1 [ ;South and Central America 33
    set xcor -29
    set ycor 2
    set region 3
    set EU 0
    set PP 8
    set GS 9.769398e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 510117
    set LNGexportcapacity 706031.5
    set coalsurplus 497497.10427398863
    set oilsurplus 2866212.873589605
    set biofuelsurplus 731021.4291883421
  ]

  create-countries 1 [ ;Russia 34
    set xcor 34;60
    set ycor 36;61.524
    set region 4
    set EU 0
    set PP 7.4
    set GS 1.358815e+07
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 572957.5
    set coalsurplus 4063557.9444440943
    set oilsurplus 16742813.901453026
    set biofuelsurplus -54077.01123753053
  ]

  create-countries 1 [ ;Ukraine 35
    set xcor 32;31.1656
    set ycor 25;48.3794
    set region 4
    set EU 0
    set PP 7.4
    set GS 4.775736e+04
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -436912.44876430917
    set oilsurplus -369859.56326912605
    set biofuelsurplus -6691.255945741589
  ]

  create-countries 1 [ ;Belarus 36
    set xcor 27;27.9534
    set ycor 32;53.7098
    set region 4
    set EU 0
    set PP 7.4
    set GS -3.025673e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -38917.29366597789
    set oilsurplus -268159.2160878776
    set biofuelsurplus -1807.1366123494645
  ]

  create-countries 1 [ ;Other CIS 37
    set xcor 60;71.2761
    set ycor 21;38.8610
    set region 4
    set EU 0
    set PP 7.4
    set GS 4.113665e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 709431.8040206919
    set oilsurplus 4669630.3208589945
    set biofuelsurplus -13396.616953567313
  ]

  create-countries 1 [ ;Middle East 38
    set xcor 58;53.6880
    set ycor 6;32.4279
    set region 5
    set EU 0
    set PP 9
    set GS 1.268579e+07
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 480545
    set LNGexportcapacity 4528212.5
    set coalsurplus -1128604.4408127489
    set oilsurplus 41928675.096010104
    set biofuelsurplus -88199.06756375372
  ]

  create-countries 1 [ ;Africa 39
    set xcor 3;1.6596
    set ycor 6;28.0339
    set region 6
    set EU 0
    set PP 7
    set GS 3.313444e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 303113
    set LNGexportcapacity 2047861
    set coalsurplus 2511055.594612755
    set oilsurplus 9056542.484651633
    set biofuelsurplus -43257.08396584252
  ]

  create-countries 1 [ ;Asia-Pacific 40
    set xcor 70
    set ycor 10
    set region 7
    set EU 0
    set PP 7
    set GS -1.038570e+07
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 10479577.5
    set LNGexportcapacity 555815831.4
    set coalsurplus 172753.38995949924
    set oilsurplus -44642694.98170611
    set biofuelsurplus -586183.6140476807
  ]
end

to resetlinks
  ask transferroutes [die]
  ask LNGroutes [die]
  ask countries [set linkedcountries []]

  ask country 0 [;Belgium
    create-borderpipe-with country 4 ;Germany
    set linkedcountries lput 4 linkedcountries
    ask country 4 [set linkedcountries lput 0 linkedcountries]

    create-borderpipe-with country 9 ;France
    set linkedcountries lput 9 linkedcountries
    ask country 9 [set linkedcountries lput 0 linkedcountries]

    create-borderpipe-with country 15 ;Luxembourg
    set linkedcountries lput 15 linkedcountries
    ask country 15 [set linkedcountries lput 0 linkedcountries]

    create-borderpipe-with country 18 ;Netherlands
    set linkedcountries lput 18 linkedcountries
    ask country 18 [set linkedcountries lput 0 linkedcountries]

    create-borderpipe-with country 27 ;United Kingdom
    set linkedcountries lput 27 linkedcountries
    ask country 27 [set linkedcountries lput 0 linkedcountries]
  ]

  ask country 1 [;Bulgaria
    create-borderpipe-with country 7 ;Greece
    set linkedcountries lput 7 linkedcountries
    ask country 7 [set linkedcountries lput 1 linkedcountries]

    create-borderpipe-with country 22;Romania
    set linkedcountries lput 22 linkedcountries
    ask country 22 [set linkedcountries lput 1 linkedcountries]

    create-borderpipe-with country 30 ;Non-EU Balkan
    set linkedcountries lput 30 linkedcountries
    ask country 30 [set linkedcountries lput 1 linkedcountries]

    create-borderpipe-with country 31 ;Turkey & Georgia
    set linkedcountries lput 31 linkedcountries
    ask country 31 [set linkedcountries lput 1 linkedcountries]
  ]

  ask country 2 [;Czech Republic
    create-borderpipe-with country 4 ;Germany
    set linkedcountries lput 4 linkedcountries
    ask country 4 [set linkedcountries lput 2 linkedcountries]

    create-borderpipe-with country 19 ;Austria
    set linkedcountries lput 19 linkedcountries
    ask country 19 [set linkedcountries lput 2 linkedcountries]

    create-borderpipe-with country 20 ;Poland
    set linkedcountries lput 20 linkedcountries
    ask country 20 [set linkedcountries lput 2 linkedcountries]

    create-borderpipe-with country 24 ;Slovakia
    set linkedcountries lput 24 linkedcountries
    ask country 24 [set linkedcountries lput 2 linkedcountries]
  ]

  ask country 3 [ ;Denmark
    create-borderpipe-with country 4 ;Germany
    set linkedcountries lput 4 linkedcountries
    ask country 4 [set linkedcountries lput 3 linkedcountries]

    create-borderpipe-with country 18 ;Netherlands
    set linkedcountries lput 18 linkedcountries
    ask country 18 [set linkedcountries lput 3 linkedcountries]

    create-borderpipe-with country 26 ;Sweden
    set linkedcountries lput 26 linkedcountries
    ask country 26 [set linkedcountries lput 3 linkedcountries]
  ]

  ask country 4 [;Germany
    create-borderpipe-with country 9 ;France
    set linkedcountries lput 9 linkedcountries
    ask country 9 [set linkedcountries lput 4 linkedcountries]

    create-borderpipe-with country 15 ;Luxembourg
    set linkedcountries lput 15 linkedcountries
    ask country 15 [set linkedcountries lput 4 linkedcountries]

    create-borderpipe-with country 18 ;Netherlands
    set linkedcountries lput 18 linkedcountries
    ask country 18 [set linkedcountries lput 4 linkedcountries]

    create-borderpipe-with country 19 ;Austria
    set linkedcountries lput 19 linkedcountries
    ask country 19 [set linkedcountries lput 4 linkedcountries]

    create-borderpipe-with country 20 ;Poland
    set linkedcountries lput 20 linkedcountries
    ask country 20 [set linkedcountries lput 4 linkedcountries]
  ]

  ask country 8 [;Spain
    create-borderpipe-with country 9 ;France
    set linkedcountries lput 9 linkedcountries
    ask country 9 [set linkedcountries lput 8 linkedcountries]

    create-borderpipe-with country 21 ;Portugal
    set linkedcountries lput 21 linkedcountries
    ask country 21 [set linkedcountries lput 8 linkedcountries]
  ]

  ask country 9 [;France
    create-borderpipe-with country 29 ;Switzerland
    set linkedcountries lput 29 linkedcountries
    ask country 29 [set linkedcountries lput 9 linkedcountries]
  ]

  ask country 10 [;Croatia
    create-borderpipe-with country 11 ;Italy
    set linkedcountries lput 11 linkedcountries
    ask country 11 [set linkedcountries lput 10 linkedcountries]
  ]

  ask country 11 [;Italy
    create-borderpipe-with country 19 ;Austria
    set linkedcountries lput 19 linkedcountries
    ask country 19 [set linkedcountries lput 11 linkedcountries]

    create-borderpipe-with country 23 ;Slovenia
    set linkedcountries lput 23 linkedcountries
    ask country 23 [set linkedcountries lput 11 linkedcountries]

    create-borderpipe-with country 29 ;Switzerland
    set linkedcountries lput 29 linkedcountries
    ask country 29 [set linkedcountries lput 11 linkedcountries]
  ]

  ask country 13 [;Latvia
    create-borderpipe-with country 5 ;Estonia
    set linkedcountries lput 5 linkedcountries
    ask country 5 [set linkedcountries lput 13 linkedcountries]

    create-borderpipe-with country 14 ;Lithuania
    set linkedcountries lput 14 linkedcountries
    ask country 14 [set linkedcountries lput 13 linkedcountries]

    create-borderpipe-with country 34 ;Russia
    set linkedcountries lput 34 linkedcountries
    ask country 34 [set linkedcountries lput 13 linkedcountries]
  ]

  ask country 14 [;Lithuania
    create-borderpipe-with country 34 ;Russia
    set linkedcountries lput 34 linkedcountries
    ask country 34 [set linkedcountries lput 14 linkedcountries]

    create-borderpipe-with country 36 ;Belarus
    set linkedcountries lput 36 linkedcountries
    ask country 36 [set linkedcountries lput 14 linkedcountries]
  ]

  ask country 16 [;Hungary
    create-borderpipe-with country 19 ;Austria
    set linkedcountries lput 19 linkedcountries
    ask country 19 [set linkedcountries lput 16 linkedcountries]

    create-borderpipe-with country 22 ;Romania
    set linkedcountries lput 22 linkedcountries
    ask country 22 [set linkedcountries lput 16 linkedcountries]

    create-borderpipe-with country 24 ;Slovakia
    set linkedcountries lput 24 linkedcountries
    ask country 24 [set linkedcountries lput 16 linkedcountries]

    create-borderpipe-with country 30 ;Non-EU Balkan
    set linkedcountries lput 30 linkedcountries
    ask country 30 [set linkedcountries lput 16 linkedcountries]

    create-borderpipe-with country 35 ;Ukraine
    set linkedcountries lput 35 linkedcountries
    ask country 35 [set linkedcountries lput 16 linkedcountries]
  ]

  ask country 18 [;Netherlands
    create-borderpipe-with country 27 ;United Kingdom
    set linkedcountries lput 27 linkedcountries
    ask country 27 [set linkedcountries lput 18 linkedcountries]

    create-borderpipe-with country 28 ;Norway
    set linkedcountries lput 28 linkedcountries
    ask country 28 [set linkedcountries lput 18 linkedcountries]
  ]

  ask country 19 [;Austria
    create-borderpipe-with country 23 ;Slovenia
    set linkedcountries lput 23 linkedcountries
    ask country 23 [set linkedcountries lput 19 linkedcountries]

    create-borderpipe-with country 24 ;Slovakia
    set linkedcountries lput 24 linkedcountries
    ask country 24 [set linkedcountries lput 19 linkedcountries]

    create-borderpipe-with country 29 ;Switzerland
    set linkedcountries lput 29 linkedcountries
    ask country 29 [set linkedcountries lput 19 linkedcountries]
  ]

  ask country 20 [;Poland
    create-borderpipe-with country 35 ;Ukraine
    set linkedcountries lput 35 linkedcountries
    ask country 35 [set linkedcountries lput 20 linkedcountries]
  ]

  ask country 23 [;Slovenia
    create-borderpipe-with country 10 ;Croatia
    set linkedcountries lput 10 linkedcountries
    ask country 10 [set linkedcountries lput 23 linkedcountries]
  ]

  ask country 24 [;Slovakia
    create-borderpipe-with country 35 ;Ukraine
    set linkedcountries lput 35 linkedcountries
    ask country 35 [set linkedcountries lput 24 linkedcountries]
  ]

  ask country 27 [;United Kingdom
    create-borderpipe-with country 28 ;Norway
    set linkedcountries lput 28 linkedcountries
    ask country 28 [set linkedcountries lput 27 linkedcountries]

    create-borderpipe-with country 6 ;Ireland
    set linkedcountries lput 6 linkedcountries
    ask country 6 [set linkedcountries lput 27 linkedcountries]
  ]

  ask country 28 [;Norway
    create-borderpipe-with country 0 ;Belgium
    set linkedcountries lput 0 linkedcountries
    ask country 0 [set linkedcountries lput 28 linkedcountries]

    create-borderpipe-with country 3 ;Denmark
    set linkedcountries lput 3 linkedcountries
    ask country 3 [set linkedcountries lput 28 linkedcountries]

    create-borderpipe-with country 4 ;Germany
    set linkedcountries lput 4 linkedcountries
    ask country 4 [set linkedcountries lput 28 linkedcountries]

    create-borderpipe-with country 9 ;France
    set linkedcountries lput 9 linkedcountries
    ask country 9 [set linkedcountries lput 28 linkedcountries]
  ]

  ask country 31 [;Turkey & Georgia
    create-borderpipe-with country 7 ;Greece
    set linkedcountries lput 7 linkedcountries
    ask country 7 [set linkedcountries lput 31 linkedcountries]
  ]

  ask country 34 [;Russia
    create-borderpipe-with country 4 ;Germany
    set linkedcountries lput 4 linkedcountries
    ask country 4 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 5 ;Estonia
    set linkedcountries lput 5 linkedcountries
    ask country 5 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 25 ;Finland
    set linkedcountries lput 25 linkedcountries
    ask country 25 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 31 ;Turkey & Georgia
    set linkedcountries lput 31 linkedcountries
    ask country 31 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 35 ;Ukraine
    set linkedcountries lput 35 linkedcountries
    ask country 31 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 36 ;Belarus
    set linkedcountries lput 36 linkedcountries
    ask country 36 [set linkedcountries lput 34 linkedcountries]

    create-borderpipe-with country 37 ;other CIS
    set linkedcountries lput 37 linkedcountries
    ask country 37 [set linkedcountries lput 34 linkedcountries]
  ]

  ask country 35 [;Ukraine
    create-borderpipe-with country 20 ;Poland
    set linkedcountries lput 20 linkedcountries
    ask country 20 [set linkedcountries lput 35 linkedcountries]

    create-borderpipe-with country 22 ;Romania
    set linkedcountries lput 22 linkedcountries
    ask country 22 [set linkedcountries lput 35 linkedcountries]
  ]

  ask country 36 [;Belarus
    create-borderpipe-with country 20 ;Poland
    set linkedcountries lput 20 linkedcountries
    ask country 20 [set linkedcountries lput 36 linkedcountries]
  ]

  ask country 37 [;other CIS
    create-borderpipe-with country 30 ; Non-EU Balkan
    set linkedcountries lput 30 linkedcountries
    ask country 30 [set linkedcountries lput 37 linkedcountries]

    create-borderpipe-with country 31 ; Turkey and Georgia
    set linkedcountries lput 31 linkedcountries
    ask country 31 [set linkedcountries lput 37 linkedcountries]

    create-borderpipe-with country 38 ;Middle East
    set linkedcountries lput 38 linkedcountries
    ask country 38 [set linkedcountries lput 37 linkedcountries]

    create-borderpipe-with country 40 ;Asia-Pacific
    set linkedcountries lput 40 linkedcountries
    ask country 40 [set linkedcountries lput 37 linkedcountries]
  ]

  ask country 38 [;Middle East
    create-borderpipe-with country 31 ;Turkey & Georgia
    set linkedcountries lput 31 linkedcountries
    ask country 31 [set linkedcountries lput 38 linkedcountries]
  ]

  ask country 39 [;Africa
    create-borderpipe-with country 8 ;Spain
    set linkedcountries lput 8 linkedcountries
    ask country 8 [set linkedcountries lput 39 linkedcountries]

    create-borderpipe-with country 11 ;Italy
    set linkedcountries lput 11 linkedcountries
    ask country 11 [set linkedcountries lput 39 linkedcountries]
  ]

  ask borderpipe 0 4 [set capacity 1275825]
  ask borderpipe 0 9 [set capacity 936309]
  ask borderpipe 0 15 [set capacity 277984]
  ask borderpipe 0 18 [set capacity 2671461]
  ask borderpipe 0 27 [set capacity 16856]
  ask borderpipe 1 7 [set capacity 5767]
  ask borderpipe 1 22 [set capacity 61525]
  ask borderpipe 1 30 [set capacity 1424779]
  ask borderpipe 1 31 [set capacity 6839]
  ask borderpipe 2 4 [set capacity 796914]
  ask borderpipe 2 19 [set capacity 22623]
  ask borderpipe 2 20 [set capacity 906678]
  ask borderpipe 2 24 [set capacity 265527]
  ask borderpipe 3 4 [set capacity 964964]
  ask borderpipe 3 18 [set capacity 3739483]
  ask borderpipe 3 26 [set capacity 9714]
  ask borderpipe 4 9 [set capacity 323813]
  ask borderpipe 4 15 [set capacity 1194871]
  ask borderpipe 4 18 [set capacity 1589924]
  ask borderpipe 4 19 [set capacity 2522506]
  ask borderpipe 4 20 [set capacity 292319]
  ask borderpipe 8 9 [set capacity 1186872]
  ask borderpipe 8 21 [set capacity 575102]
  ask borderpipe 9 29 [set capacity 391814]
  ask borderpipe 10 11 [set capacity 255813]
  ask borderpipe 11 19 [set capacity 420957]
  ask borderpipe 11 23 [set capacity 226743]
  ask borderpipe 11 29 [set capacity 257143]
  ask borderpipe 13 5 [set capacity 136002]
  ask borderpipe 13 14 [set capacity 61525]
  ask borderpipe 13 34 [set capacity 2104787]
  ask borderpipe 14 34 [set capacity 248109]
  ask borderpipe 14 36 [set capacity 2930511]
  ask borderpipe 16 19 [set capacity 631436]
  ask borderpipe 16 22 [set capacity 890487]
  ask borderpipe 16 24 [set capacity 570407]
  ask borderpipe 16 30 [set capacity 54856]
  ask borderpipe 16 35 [set capacity 178097]
  ask borderpipe 18 27 [set capacity 416536]
  ask borderpipe 18 28 [set capacity 441103]
  ask borderpipe 19 23 [set capacity 777152]
  ask borderpipe 19 24 [set capacity 323813]
  ask borderpipe 19 29 [set capacity 145716]
  ask borderpipe 20 35 [set capacity 7134]
  ask borderpipe 23 10 [set capacity 61525]
  ask borderpipe 24 35 [set capacity 207448]
  ask borderpipe 27 28 [set capacity 1664238]
  ask borderpipe 27 6 [set capacity 400157.2036] ; based on poster
  ask borderpipe 28 0 [set capacity 445687]
  ask borderpipe 28 3 [set capacity 388576]
  ask borderpipe 28 4 [set capacity 734864]
  ask borderpipe 28 9 [set capacity 527816]
  ask borderpipe 31 7 [set capacity 59883]
  ask borderpipe 34 4 [set capacity 384917]
  ask borderpipe 34 5 [set capacity 224503]
  ask borderpipe 34 25 [set capacity 731818]
  ask borderpipe 34 31 [set capacity 1262872]
  ask borderpipe 34 35 [set capacity 657959] ;assumed to be the same as other CIS
  ask borderpipe 34 36 [set capacity 657959]
  ask borderpipe 34 37 [set capacity 694923]
  ask borderpipe 35 20 [set capacity 165145]
  ask borderpipe 35 22 [set capacity 242860]
  ask borderpipe 36 20 [set capacity 773197]
  ask borderpipe 37 30 [set capacity 77624]
  ask borderpipe 37 31 [set capacity 232873]
  ask borderpipe 37 38 [set capacity 85017]
  ask borderpipe 37 40 [set capacity 1338097]
  ask borderpipe 38 31 [set capacity 328980]
  ask borderpipe 39 8 [set capacity 82949]
  ask borderpipe 39 11 [set capacity 1398874]

end

to go
;  show("Go")
  setglobals
  setprices

  set potentialdeals 1
  set LNGexportingcountries []
  set LNGimportingcountries []

  resetlinks
  resettradevalues

  ask borderpipes [set capacityavailable capacity]

  let loopcount 0
  let prevpotentialdeals 0
  while [potentialdeals > 0] [
    tick

    set potentialdeals 0
    ask transferroutes [die]
    ask LNGroutes [die]
    checkborderpipes

;    createLNGroutes
    checkTH

    createTH

    createtransferroutes
    createLNGroutes

    ask transferroutes [findroute]
    ask transferroutes [checkroutecapacity]

    updatelinks

    setroutetype
    ask links [
      set Deal 0
      set W2TR 0
      set W2TS 0
      set Roffer 0
      set Soffer 0
      determineprice
    ]

;    show("check8")
    ask countries [if TH = 0 [proposedeals]]
;    show("check9")
    ask links [compareproposals]
;    show("check10")
    ask countries [updateneeds]
;    show("check11")

    ifelse prevpotentialdeals = potentialdeals [
      set loopcount loopcount + 1
;      show("loopcount")
;      show(loopcount)

      if loopcount > 30 [set potentialdeals 0]
    ]
    [
      set loopcount 0
    ]
    set prevpotentialdeals potentialdeals
  ]
;  show("checka")
  coaltrade
  oiltrade
  biofueltrade
  updateoutput

   ask borderpipes [
    ifelse planningtoexpand = 0 [needtoexpand]
    [readytoexpand
      set planningtoexpand 0
;    show("expand")
    ]
  ]

  ask countries [
    ifelse planningtoexpandLNGim = 0 [needtoexpandLNGim]
    [readytoexpandLNGim
      set planningtoexpandLNGim 0
;      show("expand")
    ]
    ifelse planningtoexpandLNGex = 0 [needtoexpandLNGex]
    [readytoexpandLNGex
      set planningtoexpandLNGex 0
;      show("expand")
    ]
  ]

;  show("Done")
end

to setglobals
  ask country 0 [
    set transferprice inputtransferprice
    set LNGprice inputLNGprice
    set powerfactor inputpowerfactor
    set price1 inputprice1
    set price2 inputprice2
    set price3 inputprice3
    set price4 inputprice4
    set price5 inputprice5
    set price6 inputprice6
    set price7 inputprice7
    set energyunion inputenergyunion
    set Time inputTime
    Set Capincrease inputCapincrease
    set Capincreasetime inputCapincreasetime
    set LNGCapincrease inputLNGCapincrease
    set LNGCapincreasetime inputLNGCapincreasetime
  ]
end

to setprices
  ask countries [
    if region = 1 [set regionalgasprice price1]
    if region = 2 [set regionalgasprice price2]
    if region = 3 [set regionalgasprice price3]
    if region = 4 [set regionalgasprice price4]
    if region = 5 [set regionalgasprice price5]
    if region = 6 [set regionalgasprice price6]
    if region = 7 [set regionalgasprice price7]
  ]
end

to resettradevalues
  ask countries [
    set eugasimport 0
    set totalimport 0
    set totalexport 0
    set russiangas 0
    set gasimportcosts 0
    set LNGimportavailable LNGimportcapacity
    set LNGexportavailable LNGexportcapacity
  ]
end

to checkborderpipes
  ask borderpipes [
    if capacityavailable = 0 [die]]

  ask countries [set linkedcountries []]

  ask countries [
    let a who
    ask link-neighbors [
      if link-neighbor? country a = TRUE [
        set linkedcountries lput a linkedcountries]]
  ]
end

to createLNGroutes
  set LNGimportingcountries []
  set LNGexportingcountries []
  ask countries [
;    set LNGimportavailable LNGimportcapacity
;    set LNGexportavailable LNGexportcapacity



    if LNGimportavailable > 0 [
      set LNGimportingcountries lput who LNGimportingcountries]
    if LNGexportavailable > 0[
      set LNGexportingcountries lput who LNGexportingcountries]
  ]

  foreach LNGimportingcountries [n ->
    foreach LNGexportingcountries [m ->
      ask country n [
        if n != m and link-neighbor? country m = FALSE [
          create-LNGroute-with country m
;          set linkedcountries lput m linkedcountries ;changed
;          ask country m [set linkedcountries lput n linkedcountries]
        ]
      ]
    ]
  ]

  ask LNGroutes [
    set capacity12 min list [LNGexportavailable] of end1 [LNGimportavailable] of end2
    set capacity21 min list [LNGexportavailable] of end2 [LNGimportavailable] of end1
    set transfercount 0

;    set capacity12 max list capacity12 0
;    set capacity21 max list capacity21 0
;    show("capacity12 21")
;    show(capacity12)
;    show(capacity21)
  ]
end

to checkTH
  ask countries [
    ;  if abs GS < 10 [set GS 0]

    ifelse GS = 0
    [set TH 1]
    [set TH 0]
  ]
end

to updatelinks
  ask countries [set TRUElinkedcountries []]

  ask countries [
    let a who
    ask link-neighbors [
      if link-neighbor? country a = TRUE [
        set TRUElinkedcountries lput a TRUElinkedcountries]]
  ]
end

to createTH

  set EUthcheck 0
  ask countries [
    if eu = 1 [
      if TH = 0 [
        set EUthcheck 1
      ]
    ]
  ]

  ask countries [
    if TH = 1 [
      let countrycheck linkedcountries
      let recheck 1
      set linkedTH []
      set linkedHUB []

      set linkedTH lput who linkedTH

      while [recheck = 1] [
        set recheck 0

        foreach countrycheck [n ->
          if [TH] of country n = 1 and member? n linkedTH = False [
            set linkedTH lput n linkedTH
            foreach [linkedcountries] of country n [a ->
              if member? a countrycheck = False [set countrycheck lput a countrycheck]]
            set recheck 1
          ]
        ]
      ]

      foreach countrycheck [n ->
        if [TH] of country n = 0 [
          set linkedHUB lput n linkedHUB]]
    ]
  ]
end

to createtransferroutes
  ask countries [
    if TH = 1 [
      foreach linkedHUB [n ->
        foreach linkedHUB [m ->
          let newlink 0
          ask country n [
            if n != m and link-neighbor? country m = FALSE [
              if [GS] of country n > 0 and [GS] of country m < 0 [
                ifelse energyunion = 1 [
                  ifelse euthcheck = 1 [
                    if [EU] of country m = 1 [
                      create-transferroute-with country m
                      set newlink 1]
                  ]
                  [
                    create-transferroute-with country m
                    set newlink 1]
                ]
                [
                  create-transferroute-with country m
                  set newlink 1]
              ]
            ]
          ]
        ]
      ]
    ]
  ]
end

to setroutetype
  ask borderpipes [set transfertype 0]
  ask transferroutes [set transfertype 1]
  ask LNGroutes [set transfertype 2]
end

to findroute
  let n1 0
  let n2 0
  ifelse [GS] of end1 > 0 [
    set n1 [who] of end1
    set n2 [who] of end2]
  [if [GS] of end2 > 0 [
    set n1 [who] of end2
    set n2 [who] of end1]]

  let countrylist []
  let irray []

  set countrylist lput n1 countrylist
  set irray lput 0 irray

  ask countries [
    if who != n1 and who != n2 [
      set countrylist lput who countrylist
      set irray lput 0 irray
    ]
  ]

  set countrylist lput n2 countrylist
  set irray lput 0 irray

  let x 0

  (foreach countrylist irray [[c i] ->
    if c != n2 [
      ask country c [
        ifelse borderpipe-neighbor? country n1 = TRUE [
          if [capacityavailable] of borderpipe c n1 > 0 [
            if TH = 1 or c = n2 [
              if i = 0 [set irray replace-item x irray 1]
            ]
          ]
        ]
        [
          if LNGroute-neighbor? country n1 = TRUE [
            if [end1] of LNGroute c n1 = country n1 [
              if [capacity12] of LNGroute c n1 > 0 [
                if TH = 1 or c = n2 [
                  if i = 0 [
                    set irray replace-item x irray 1
;                    ask transferroute n1 n2 [set LNG 1
;                    show("LNG")]
                  ]
                ]
              ]
            ]
            if [end2] of LNGroute c n1 = country n1 [
              if [capacity21] of LNGroute c n1 > 0 [
                if TH = 1 or c = n2 [
                  if i = 0 [
                    set irray replace-item x irray 1
;                    ask transferroute n1 n2 [set LNG 1] ;changed
                  ]
                ]
              ]
            ]
          ]
        ]
    ]]
    set x x + 1
  ])

  let done 0
  let n 1

  let sumirray 5
  let prevsumirray 100000

  while [done = 0][
    let nextset []

    (foreach countrylist irray [[c i] ->
      if i = n [
        set nextset lput c nextset
      ]
    ])

    let nnext 0
    foreach nextset [a ->
      set x 0
      (foreach countrylist irray [[c i] ->
        ask country c [
          ifelse borderpipe-neighbor? country a = TRUE [
            if [capacityavailable] of borderpipe c a > 0 [
              if TH = 1 or c = n2 [
                set nnext n + 1
                if i = 0 [set irray replace-item x irray nnext]
              ]
            ]
          ]
          [
;            if LNGroute-neighbor? country a = TRUE [
;              if [end1] of LNGroute c a = country a [
;                if [capacity12] of LNGroute c a > 0 [
;                  if TH = 1 or c = n2 [
;                    set nnext n + 1
;                    if i = 0 [
;                      set irray replace-item x irray 1
;;                      ask transferroute n1 n2 [set LNG 1] ;changed
;                    ]
;                  ]
;                ]
;              ]
;              if [end2] of LNGroute c a = country a [
;                if [capacity21] of LNGroute c a > 0 [
;                  if TH = 1 or c = n2 [
;                    set nnext n + 1
;                    if i = 0 [
;                      set irray replace-item x irray 1
;;                      ask transferroute n1 n2 [set LNG 1]
;                    ]
;                  ]
;                ]
;              ]
;            ]
          ]
        ]
        set x x + 1
      ])
    ]

    set n n + 1

    set sumirray sum irray
    if sumirray = prevsumirray [
      set done 1
      die]
    set prevsumirray sumirray

    (foreach countrylist irray [[c i] ->
      if c = n2 [
        if i != 0 [
          set done 1
          set n i
        ]
      ]
    ])
  ]

  set route []
  set route fput n2 route
  set n n - 1
  let prevcountry n2



  while [n > 0] [
    (foreach countrylist irray [[c i] ->
      ask country c [
        ifelse borderpipe-neighbor? country prevcountry = TRUE [ ;changed
          if i = n [set prevcountry c]
        ]
        [
          if [LNG] of transferroute n1 n2 = 0 [
          if LNGroute-neighbor? country prevcountry = TRUE [
          if i = n [
            ask LNGroute c prevcountry [set transfercount transfercount + 1]
            set prevcountry c
            ask transferroute n1 n2 [set LNG 1]

          ]
        ]]]
      ]
    ])

    set route fput prevcountry route
    set n n - 1
  ]

  set route fput n1 route

;  if LNG = 1 [
;  show("countrylist irray route")
;  show(countrylist)
;    show(irray)
;  show(route)
;]
;  checkroutecapacity
end

to checkroutecapacity

  set capacityroute []

  let i 0
  let j 1

  let y length route - 1
  let a 0

  while [i < y][

    let c1 item i route
    let c2 item j route
    ask country c1 [
      ifelse borderpipe-neighbor? country c2 = TRUE [
        set a [capacityavailable] of borderpipe c1 c2
      ]
      [if LNGroute-neighbor? country c2 = TRUE [
        ask LNGroute c1 c2 [
          if end1 = country c1 [set a capacity12]
          if end2 = country c1 [set a capacity21]
        ]
        if [transfercount] of LNGroute c1 c2 > 0 [
;          show("a1")
;          show(a)
          set a a / [transfercount] of LNGroute c1 c2
;          show("a2")
;          show(a)
        ]
        ]
      ]
    ]

    set capacityroute lput a capacityroute

    set i i + 1
    set j j + 1
  ]

  set capacity min capacityroute
;  show("route and cap")
;  show(route)
;  show(capacityroute)

  if LNG = 1 [set transfertype 3

;  show("route capacity LNG")
;  show(route)
;  show(capacity)
;  show(LNG)
  ]
end

to determineprice
  ifelse [GS] of end1 > 0 and [GS] of end2 < 0 [
    set PPS [PP] of end1
    set PPR [PP] of end2
    set P4T 1]
  [ifelse [GS] of end1 < 0 and [GS] of end2 > 0 [
    set PPS [PP] of end2
    set PPR [PP] of end1
    set P4T 1]
    [set P4T 0]]

  let gasprice1 [regionalgasprice] of end1
  let gasprice2 [regionalgasprice] of end2
  set gasprice (gasprice1 + gasprice2) / 2

  if P4T = 1 [
    set pipelineprice gasprice * ((PPS - PPR) / powerfactor + 1)

    if transfertype = 0 [
      set pipelinepriceR pipelineprice
      set pipelinepriceS pipelineprice]

    if transfertype = 1 [
      let passingcountries length route - 2
      set pipelinepriceR pipelineprice + (transferprice * passingcountries)
      set pipelinepriceS pipelineprice - (transferprice * passingcountries)]

    if transfertype = 2 [
      set pipelinepriceR pipelineprice + LNGprice
      set pipelinepriceS pipelineprice - LNGprice
      if pipelinepriceS < 1 [ set pipelinepriceS 1]]

    if transfertype = 3 [
      let passingcountries length route - 2
      set pipelinepriceR pipelineprice + (transferprice * passingcountries) + LNGprice
      set pipelinepriceS pipelineprice - LNGprice
      if pipelinepriceS < 1 [set pipelinepriceS 1]]

    if EnergyUnion = 1 [
      if [eu] of end1 = 1 and [eu] of end2 = 1 [
        set pipelinepriceS pipelinepriceS * 100000
        set pipelinepriceR 0
      ]
    ]
  ]
end

to proposedeals
  let pricelist []
  let demandlist []
  let tplist []
  let TD abs GS

  if empty? TRUElinkedcountries = False [

  let LNGcapfreetopropose 0

    if GS > 0 [
      foreach TRUElinkedcountries [n ->
        set pricelist lput [pipelinepriceS] of link-with country n pricelist
        set demandlist lput [GS] of country n demandlist
        set tplist lput [P4T] of link-with country n tplist
      ]
      if LNGexportavailable > 0 [set LNGcapfreetopropose LNGexportavailable]
    ]
    if GS < 0 [
      foreach TRUElinkedcountries [n ->
        set pricelist lput [pipelinepriceR] of link-with country n pricelist
        set demandlist lput [GS] of country n demandlist
        set tplist lput [P4T] of link-with country n tplist
      ]
      if LNGimportavailable > 0 [set LNGcapfreetopropose LNGimportavailable]
    ]

;    if who = 33 [
;      show("LNGcapfreetopropose1")
;      show(LNGcapfreetopropose)
;      show("TD")
;      show(TD)]

    let maxprice 0
    let minprice 1000000000000

    if GS > 0 [
      while [TD > 0 and max tplist > 0] [
        set maxprice 0

        let maxpricecount 0
        (foreach tplist pricelist [[a c] ->
          if a = 1 [
            ifelse c > maxprice [
              set maxprice c
              set maxpricecount 1]
            [
              if c = maxprice [set maxpricecount maxpricecount + 1]
            ]
        ]])


        let i 0

        let TTD 0
        ifelse TD > 10 [
          set TTD TD / maxpricecount
        ]
        [set TTD TD]

        (foreach tplist demandlist pricelist TRUElinkedcountries [[a b c n] ->

          if a = 1 [
            if c = maxprice [
              let offer min list TTD abs b
              let id who
              ask link-with country n [
                if transfertype = 0 [
                  if capacityavailable > 0 [
                    set offer min list offer capacityavailable
;                    set W2TS 1
                  ]
                ]

                if transfertype = 1 [
;                  if capacity > 0 [
                    set offer min list offer capacity
;                    set W2TS 1
;                  ]
                ]

                if transfertype = 2 [
                  if [GS] of end1 > 0 [set capacity capacity12]
                  if [GS] of end1 < 0 [set capacity capacity21]

                  set capacity min list capacity LNGcapfreetopropose

;                  if capacity > 0 [
                    set offer min list offer capacity
;                    set W2TS 1
                    set LNGcapfreetopropose LNGcapfreetopropose - offer
;                  ]

                ]
                set W2TS 1
                set Soffer offer
              ]
              set TD TD - offer
;              if who = 33 [
;                show("LNGcapfreetopropose112")
;                show(LNGcapfreetopropose)
;                show("TD")
;                show(TD)]
              set tplist replace-item i tplist 0
            ]
          ]
          set i i + 1
        ])
      ]
    ]

    if GS < 0 [

      while [TD > 0 and max tplist > 0] [

        set minprice 1000000000000
        let minpricecount 0

        (foreach tplist pricelist [[a c] ->
          if a = 1 [
            ifelse c < minprice [
              set minprice c
              set minpricecount 1]
            [
              if c = minprice [set minpricecount minpricecount + 1]
            ]
        ]])

        let i 0

        let TTD 0
        ifelse TD > 10 [
          set TTD TD / minpricecount
        ]
        [set TTD TD]

        (foreach tplist demandlist pricelist TRUElinkedcountries [[a b c n] ->

          if a = 1 [
            if c = minprice [
              let offer min list TTD abs b

              ask link-with country n [
                if transfertype = 0 [
                  if capacityavailable > 0 [
                    set offer min list offer capacityavailable
;                    set W2TR 1
                  ]
                ]

                if transfertype = 1 [
;                  if capacity > 0 [
                    set offer min list offer capacity
;                    set W2TR 1
;                  ]
                ]

                if transfertype = 2 [
                  if [GS] of end1 > 0 [set capacity capacity12]
                  if [GS] of end1 < 0 [set capacity capacity21]

                  set capacity min list capacity LNGcapfreetopropose

;                  if capacity > 0 [
;                    show("GS end1, cap12, cap21, cap")
;                    show([GS] of end1)
;                    show(capacity12)
;                    show(capacity21)
;                    show(capcity)
                    set offer min list offer capacity
;                    set W2TR 1
                    set LNGcapfreetopropose LNGcapfreetopropose - offer
;                  ]
                ]
                set W2TR 1
                set Roffer offer
              ]
              set TD TD - offer
              set tplist replace-item i tplist 0
            ]
          ]
          set i i + 1
        ])
      ]
    ]


;  if who = 33 [
;      show("LNGcapfreetopropose2")
;      show(LNGcapfreetopropose)
;    show("TD")
;    show(TD)]

]

end

to compareproposals
  if W2TR = 1 and W2TS = 1 [
    let minoffer min list Soffer Roffer
    if minoffer < mindealsize [set minoffer mindealsize]

    set Deal Deal + minoffer
    set potentialdeals potentialdeals + 1

    if transfertype = 0 [
      set capacityavailable capacityavailable - Deal
    ]

    if transfertype = 1 or transfertype = 3 [
      let y length route - 1
      let a 0
      let i 0
      let j 1

;      if transfertype = 3 [
;        show("deal and capacity")
;        show(deal)
;        show(capacity);]
      set deal min list deal capacity

      while [i < y][
        let c1 item i route
        let c2 item j route
        let madedeal deal
        ask country c1 [
          ifelse borderpipe-neighbor? country c2 = TRUE [
            ask borderpipe c1 c2 [set capacityavailable capacityavailable - madedeal]
          ]
          [if LNGroute-neighbor? country c2 = TRUE [
            set LNGexportavailable LNGexportavailable - madedeal
            ask country c2 [set LNGimportavailable LNGimportavailable - madedeal]
            ]
          ]
          set i i + 1
          set j j + 1
        ]
      ]
    ]
    if transfertype = 3 [
      ask transferroutes [ if transfertype = 3 [checkroutecapacity
;      show("check")
      ] ]
    ]
  ]
end

to updateneeds
  foreach TRUElinkedcountries [n ->
    if GS > 0 [set GS GS - [deal] of link-with country n
      set totalexport totalexport + [deal] of link-with country n
      if [transfertype] of link-with country n = 2 [
        set LNGexportavailable LNGexportavailable - [deal] of link-with country n]
    ]
    if GS < 0 [set GS GS + [deal] of link-with country n
      set totalimport totalimport + [deal] of link-with country n

      if n > 27 [
;        Leaving out transfercosts in order to better compare to energy union option
        let price [pipelineprice] of link-with country n
        if [transfertype] of link-with country n = 2 or [transfertype] of link-with country n = 3 [
          set price price + LNGprice]

        let totalcosts [deal] of link-with country n * [pipelinepriceR] of link-with country n
        set gasimportcosts gasimportcosts + totalcosts

        set EUgasimport EUgasimport + [deal] of link-with country n
      ]

      if n = 34 [
        set russiangas russiangas + [deal] of link-with country n
      ]
      if [transfertype] of link-with country n = 2 [
        set LNGimportavailable LNGimportavailable - [deal] of link-with country n]
    ]
  ]
end

to coaltrade
  let totalcoalsupply 0
  let totalcoaldemand 0
  let supplysurplus 0
  let supplyshortage 0
  let percentage 1

  ask countries [
    set coalexport 0
    set coalimport 0
  ]

  ask countries [
    ifelse coalsurplus > 0 [
      set totalcoalsupply totalcoalsupply + coalsurplus]
    [set totalcoaldemand totalcoaldemand - coalsurplus]
  ]

  if totalcoalsupply = totalcoaldemand [
    ask countries [
      ifelse coalsurplus > 0 [
        set coalexport coalsurplus]
      [set coalimport abs(coalsurplus)]
    ]
  ]

  if totalcoalsupply > totalcoaldemand [
    set supplysurplus totalcoalsupply - totalcoaldemand
    set percentage supplysurplus / totalcoalsupply
    set percentage 1 - percentage

    ask countries [
      ifelse coalsurplus > 0 [
        set coalexport coalsurplus * percentage]
      [set coalimport abs(coalsurplus)]
    ]
  ]

  if totalcoalsupply < totalcoaldemand [
    set supplyshortage totalcoaldemand - totalcoalsupply
    set percentage supplyshortage / totalcoaldemand
    set percentage 1 - percentage

    ask countries [
      ifelse coalsurplus > 0 [
        set coalexport coalsurplus
      ]
      [set coalimport abs(coalsurplus) * percentage]
    ]
  ]
end

to oiltrade
  let totaloilsupply 0
  let totaloildemand 0
  let supplysurplus 0
  let supplyshortage 0
  let percentage 1

  ask countries[
    set oilimport 0
    set oilexport 0
  ]

  ask countries [
    ifelse oilsurplus > 0 [
      set totaloilsupply totaloilsupply + oilsurplus]
    [set totaloildemand totaloildemand - oilsurplus]
  ]

  if totaloilsupply = totaloildemand [
    ask countries [
      ifelse oilsurplus > 0 [
        set oilexport oilsurplus]
      [set oilimport abs(oilsurplus)]
    ]
  ]

  if totaloilsupply > totaloildemand [
    set supplysurplus totaloilsupply - totaloildemand
    set percentage supplysurplus / totaloilsupply
    set percentage 1 - percentage

    ask countries [
      ifelse oilsurplus > 0 [
        set oilexport oilsurplus * percentage]
      [set oilimport abs(oilsurplus)]
    ]
  ]

  if totaloilsupply < totaloildemand [
    set supplyshortage totaloildemand - totaloilsupply
    set percentage supplyshortage / totaloildemand
    set percentage 1 - percentage

    ask countries [
      ifelse oilsurplus > 0 [
        set oilexport oilsurplus
]
      [set oilimport abs(oilsurplus) * percentage]
    ]
  ]
end

to Biofueltrade
  let totalbiofuelsupply 0
  let totalbiofueldemand 0
  let supplysurplus 0
  let supplyshortage 0
  let percentage 1

  ask countries [
    set biofuelexport 0
    set biofuelimport 0
  ]

  ask countries [
    ifelse biofuelsurplus > 0 [
      set totalbiofuelsupply totalbiofuelsupply + biofuelsurplus]
    [set totalbiofueldemand totalbiofueldemand - biofuelsurplus]
  ]

  if totalbiofuelsupply = totalbiofueldemand [
    ask countries [
      ifelse biofuelsurplus > 0 [
        set biofuelexport biofuelsurplus]
      [set biofuelimport abs(biofuelsurplus)]
    ]
  ]

  if totalbiofuelsupply > totalbiofueldemand [
    set supplysurplus totalbiofuelsupply - totalbiofueldemand
    set percentage supplysurplus / totalbiofuelsupply
    set percentage 1 - percentage

    ask countries [
      ifelse biofuelsurplus > 0 [
        set biofuelexport biofuelsurplus * percentage]
      [set biofuelimport abs(biofuelsurplus)]
    ]
  ]

  if totalbiofuelsupply < totalbiofueldemand [
    set supplyshortage totalbiofueldemand - totalbiofuelsupply
    set percentage supplyshortage / totalbiofueldemand
    set percentage 1 - percentage

    ask countries [
      ifelse biofuelsurplus > 0 [
        set biofuelexport biofuelsurplus
      ]
      [set biofuelimport abs(biofuelsurplus) * percentage]
    ]
  ]
end

to updateoutput
  set gasimportlist []
  set gasexportlist []
  set coalimportlist []
  set coalexportlist []
  set oilimportlist []
  set oilexportlist []
  set biofuelimportlist []
  set biofuelexportlist []
  set russiangaslist []
  set gasimportcostslist []
  set eugasimportlist []

  let allcountries range 41
  foreach allcountries [x ->
    ask country x [
      set gasimportlist lput totalimport gasimportlist
      set gasexportlist lput totalexport gasexportlist
      set coalimportlist lput coalimport coalimportlist
      set coalexportlist lput coalexport coalexportlist
      set oilimportlist lput oilimport oilimportlist
      set oilexportlist lput oilexport oilexportlist
      set biofuelimportlist lput biofuelimport biofuelimportlist
      set biofuelexportlist lput biofuelexport biofuelexportlist
      set russiangaslist lput russiangas russiangaslist
      set gasimportcostslist lput gasimportcosts gasimportcostslist
      set eugasimportlist lput EUgasimport eugasimportlist
    ]
  ]
end

to needtoexpand
  if capacityavailable = 0 [
    set planningtoexpand 1
    set endtime Time + Capincreasetime
  ]
end

to readytoexpand
  if Time > endtime [
    set capacity capacity + Capincrease
  ]
end

to needtoexpandLNGim
  if LNGimportavailable = 0 and LNGimportcapacity > 0 [
    set planningtoexpandLNGim 1
    set endtimeLNGim Time + LNGCapincreasetime
  ]
end

to readytoexpandLNGim
  if Time > endtimeLNGim [
    set LNGimportcapacity LNGimportcapacity + LNGCapincrease
  ]
end

to needtoexpandLNGex
  if LNGexportavailable = 0 and LNGexportcapacity > 0 [
    set planningtoexpandLNGex 1
    set endtimeLNGex Time + LNGCapincreasetime
  ]
end

to readytoexpandLNGex
  if Time > endtimeLNGex [
    set LNGexportcapacity LNGexportcapacity + LNGCapincrease
  ]
end


to createcountriestest
  create-countries 1 [ ;Belgium 0
    set xcor 3;4.44699
    set ycor 29;50.5039
    set region 1
    set EU 1
    set PP 6
    set GS -4.692494e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 336765.936
    set LNGexportcapacity 0
    set coalsurplus -5.395574e+05
    set oilsurplus -9.024094e+05
    set biofuelsurplus -4.072203e+04	

    set inputpowerfactor 10
    set inputLNGprice 4
    set inputtransferprice 2
    set inputprice1 16410.30439
    set inputprice2 6393.348973
    set inputprice3 11715.344345
    set inputprice4 33883.706575
    set inputprice5 10613.933531
    set inputprice5 11289.083963
    set inputprice6 13323.449326
  ]

  create-countries 1 [ ;Denmark 1 (3)
    set xcor 8;9.5018
    set ycor 36;56.2639
    set region 1
    set EU 1
    set PP 6
    set GS -1.954537e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -524110.41609387967
    set oilsurplus -496100.07116708386
    set biofuelsurplus -4280.410156741714
  ]

  create-countries 1 [ ;Germany 2 (4)
    set xcor 9;10.4515
    set ycor 30;51.1657
    set region 1
    set EU 1
    set PP 6
    set GS  -2.376071e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -1599113.8516704757
    set oilsurplus -4468495.553703555
    set biofuelsurplus 81960.9733448585
  ]

  create-countries 1 [ ;Ireland 3 (6)
    set xcor -11;7.6921
    set ycor 32;53.1424
    set region 1
    set EU 1
    set PP 6
    set GS -3.202831e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus -486854.1055260821
    set oilsurplus -741930.5693385106
    set biofuelsurplus -3966.5970953970136
  ]

  create-countries 1 [ ;Netherlands 4 (18)
    set xcor 4;5.2913
    set ycor 30;52.1326
    set region 1
    set EU 1
    set PP 7
    set GS 5.315481e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 35619.474
    set LNGexportcapacity 0
    set coalsurplus -469266.57684962347
    set oilsurplus -1448199.98229737
    set biofuelsurplus 57188.97767446631
  ]

  create-countries 1 [ ;United Kingdom 5 (27)
    set xcor -3;-3.4360
    set ycor 30;55.3781
    set region 1
    set EU 1
    set PP 7
    set GS -6.389594e+05
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 1217538.384
    set LNGexportcapacity 939058.86
    set coalsurplus -932893.1018341928
    set oilsurplus -1070252.810895356
    set biofuelsurplus -8416.719674838208
  ]

  create-countries 1 [ ;Norway 6 (28)
    set xcor 7;8.4689
    set ycor 43;60.4720
    set region 1
    set EU 0
    set PP 8
    set GS 3.741346e+06
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 281717.658
    set coalsurplus -52626.325010836976
    set oilsurplus 3344438.7168786833
    set biofuelsurplus -4725.721013791823
  ]

  create-countries 1 [ ;Russia 7 (34)
    set xcor 34;60
    set ycor 36;61.524
    set region 4
    set EU 0
    set PP 10
    set GS 1.358815e+07
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 572957.5
    set coalsurplus 4063557.9444440943
    set oilsurplus 16742813.901453026
    set biofuelsurplus -54077.01123753053
  ]
end

to resetlinkstest
  ask transferroutes [die]
  ask LNGroutes [die]
;  ask countries [set linkedcountries []]

;  ask country 0 [;Belgium
;    create-borderpipe-with country 2 ;Germany
;;    set linkedcountries lput 2 linkedcountries
;;    ask country 2 [set linkedcountries lput 0 linkedcountries]
;
;    create-borderpipe-with country 4 ;Netherlands
;;    set linkedcountries lput 4 linkedcountries
;;    ask country 4 [set linkedcountries lput 0 linkedcountries]
;
;    create-borderpipe-with country 5 ;United Kingdom
;;    set linkedcountries lput 5 linkedcountries
;;    ask country 5 [set linkedcountries lput 0 linkedcountries]
;  ]
;
;  ask country 1 [ ;Denmark
;    create-borderpipe-with country 2 ;Germany
;;    set linkedcountries lput 2 linkedcountries
;;    ask country 2 [set linkedcountries lput 3 linkedcountries]
;
;    create-borderpipe-with country 4 ;Netherlands
;;    set linkedcountries lput 4 linkedcountries
;;    ask country 4 [set linkedcountries lput 3 linkedcountries]
;  ]
;
;  ask country 2 [;Germany
;    create-borderpipe-with country 4 ;Netherlands
;;    set linkedcountries lput 4 linkedcountries
;;    ask country 4 [set linkedcountries lput 2 linkedcountries]
;  ]
;
;  ask country 4 [;Netherlands
;    create-borderpipe-with country 5 ;United Kingdom
;;    set linkedcountries lput 5 linkedcountries
;;    ask country 5 [set linkedcountries lput 4 linkedcountries]
;
;    create-borderpipe-with country 6 ;Norway
;;    set linkedcountries lput 6 linkedcountries
;;    ask country 6 [set linkedcountries lput 4 linkedcountries]
;  ]
;
;  ask country 5 [;United Kingdom
;    create-borderpipe-with country 6 ;Norway
;;    set linkedcountries lput 6 linkedcountries
;;    ask country 6 [set linkedcountries lput 5 linkedcountries]
;
;    create-borderpipe-with country 3 ;Ireland
;;    set linkedcountries lput 3 linkedcountries
;;    ask country 3 [set linkedcountries lput 5 linkedcountries]
;  ]
;
;  ask country 6 [;Norway
;    create-borderpipe-with country 0 ;Belgium
;;    set linkedcountries lput 0 linkedcountries
;;    ask country 0 [set linkedcountries lput 6 linkedcountries]
;
;    create-borderpipe-with country 1 ;Denmark
;;    set linkedcountries lput 1 linkedcountries
;;    ask country 1 [set linkedcountries lput 6 linkedcountries]
;
;    create-borderpipe-with country 2 ;Germany
;;    set linkedcountries lput 2 linkedcountries
;;    ask country 2 [set linkedcountries lput 6 linkedcountries]
;  ]
;
;  ask country 7 [;Russia
;    create-borderpipe-with country 2 ;Germany
;;    set linkedcountries lput 2 linkedcountries
;;    ask country 2 [set linkedcountries lput 7 linkedcountries]
;  ]
;
;  ask borderpipe 0 2 [set capacity 1275825]
;  ask borderpipe 0 4 [set capacity 2671461]
;  ask borderpipe 0 5 [set capacity 16856]
;  ask borderpipe 1 2 [set capacity 964964]
;  ask borderpipe 1 4 [set capacity 3739483]
;  ask borderpipe 2 4 [set capacity 1589924]
;  ask borderpipe 4 5 [set capacity 416536]
;  ask borderpipe 4 6 [set capacity 441103]
;  ask borderpipe 5 6 [set capacity 1664238]
;  ask borderpipe 5 3 [set capacity 400157.2036] ; based on poster
;  ask borderpipe 6 0 [set capacity 445687]
;  ask borderpipe 6 1 [set capacity 388576]
;  ask borderpipe 6 2 [set capacity 734864]
;  ask borderpipe 7 2 [set capacity 384917]


end
@#$#@#$#@
GRAPHICS-WINDOW
70
10
890
590
-1
-1
8.0423
1
10
1
1
1
0
1
1
1
-30
70
0
70
1
1
1
ticks
30.0

BUTTON
3
171
66
204
NIL
setup
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
1

BUTTON
3
211
66
244
NIL
go
NIL
1
T
OBSERVER
NIL
NIL
NIL
NIL
0

@#$#@#$#@
## WHAT IS IT?

(a general understanding of what the model is trying to show or explain)

## HOW IT WORKS

(what rules the agents use to create the overall behavior of the model)

## HOW TO USE IT

(how to use the model, including a description of each of the items in the Interface tab)

## THINGS TO NOTICE

(suggested things for the user to notice while running the model)

## THINGS TO TRY

(suggested things for the user to try to do (move sliders, switches, etc.) with the model)

## EXTENDING THE MODEL

(suggested things to add or change in the Code tab to make the model more complicated, detailed, accurate, etc.)

## NETLOGO FEATURES

(interesting or unusual features of NetLogo that the model uses, particularly in the Code tab; or where workarounds were needed for missing features)

## RELATED MODELS

(models in the NetLogo Models Library and elsewhere which are of related interest)

## CREDITS AND REFERENCES

(a reference to the model's URL on the web if it has one, as well as any other necessary credits, citations, and links)
@#$#@#$#@
default
true
0
Polygon -7500403 true true 150 5 40 250 150 205 260 250

airplane
true
0
Polygon -7500403 true true 150 0 135 15 120 60 120 105 15 165 15 195 120 180 135 240 105 270 120 285 150 270 180 285 210 270 165 240 180 180 285 195 285 165 180 105 180 60 165 15

arrow
true
0
Polygon -7500403 true true 150 0 0 150 105 150 105 293 195 293 195 150 300 150

box
false
0
Polygon -7500403 true true 150 285 285 225 285 75 150 135
Polygon -7500403 true true 150 135 15 75 150 15 285 75
Polygon -7500403 true true 15 75 15 225 150 285 150 135
Line -16777216 false 150 285 150 135
Line -16777216 false 150 135 15 75
Line -16777216 false 150 135 285 75

bug
true
0
Circle -7500403 true true 96 182 108
Circle -7500403 true true 110 127 80
Circle -7500403 true true 110 75 80
Line -7500403 true 150 100 80 30
Line -7500403 true 150 100 220 30

butterfly
true
0
Polygon -7500403 true true 150 165 209 199 225 225 225 255 195 270 165 255 150 240
Polygon -7500403 true true 150 165 89 198 75 225 75 255 105 270 135 255 150 240
Polygon -7500403 true true 139 148 100 105 55 90 25 90 10 105 10 135 25 180 40 195 85 194 139 163
Polygon -7500403 true true 162 150 200 105 245 90 275 90 290 105 290 135 275 180 260 195 215 195 162 165
Polygon -16777216 true false 150 255 135 225 120 150 135 120 150 105 165 120 180 150 165 225
Circle -16777216 true false 135 90 30
Line -16777216 false 150 105 195 60
Line -16777216 false 150 105 105 60

car
false
0
Polygon -7500403 true true 300 180 279 164 261 144 240 135 226 132 213 106 203 84 185 63 159 50 135 50 75 60 0 150 0 165 0 225 300 225 300 180
Circle -16777216 true false 180 180 90
Circle -16777216 true false 30 180 90
Polygon -16777216 true false 162 80 132 78 134 135 209 135 194 105 189 96 180 89
Circle -7500403 true true 47 195 58
Circle -7500403 true true 195 195 58

circle
false
0
Circle -7500403 true true 0 0 300

circle 2
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240

cow
false
0
Polygon -7500403 true true 200 193 197 249 179 249 177 196 166 187 140 189 93 191 78 179 72 211 49 209 48 181 37 149 25 120 25 89 45 72 103 84 179 75 198 76 252 64 272 81 293 103 285 121 255 121 242 118 224 167
Polygon -7500403 true true 73 210 86 251 62 249 48 208
Polygon -7500403 true true 25 114 16 195 9 204 23 213 25 200 39 123

cylinder
false
0
Circle -7500403 true true 0 0 300

dot
false
0
Circle -7500403 true true 90 90 120

face happy
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 255 90 239 62 213 47 191 67 179 90 203 109 218 150 225 192 218 210 203 227 181 251 194 236 217 212 240

face neutral
false
0
Circle -7500403 true true 8 7 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Rectangle -16777216 true false 60 195 240 225

face sad
false
0
Circle -7500403 true true 8 8 285
Circle -16777216 true false 60 75 60
Circle -16777216 true false 180 75 60
Polygon -16777216 true false 150 168 90 184 62 210 47 232 67 244 90 220 109 205 150 198 192 205 210 220 227 242 251 229 236 206 212 183

fish
false
0
Polygon -1 true false 44 131 21 87 15 86 0 120 15 150 0 180 13 214 20 212 45 166
Polygon -1 true false 135 195 119 235 95 218 76 210 46 204 60 165
Polygon -1 true false 75 45 83 77 71 103 86 114 166 78 135 60
Polygon -7500403 true true 30 136 151 77 226 81 280 119 292 146 292 160 287 170 270 195 195 210 151 212 30 166
Circle -16777216 true false 215 106 30

flag
false
0
Rectangle -7500403 true true 60 15 75 300
Polygon -7500403 true true 90 150 270 90 90 30
Line -7500403 true 75 135 90 135
Line -7500403 true 75 45 90 45

flower
false
0
Polygon -10899396 true false 135 120 165 165 180 210 180 240 150 300 165 300 195 240 195 195 165 135
Circle -7500403 true true 85 132 38
Circle -7500403 true true 130 147 38
Circle -7500403 true true 192 85 38
Circle -7500403 true true 85 40 38
Circle -7500403 true true 177 40 38
Circle -7500403 true true 177 132 38
Circle -7500403 true true 70 85 38
Circle -7500403 true true 130 25 38
Circle -7500403 true true 96 51 108
Circle -16777216 true false 113 68 74
Polygon -10899396 true false 189 233 219 188 249 173 279 188 234 218
Polygon -10899396 true false 180 255 150 210 105 210 75 240 135 240

house
false
0
Rectangle -7500403 true true 45 120 255 285
Rectangle -16777216 true false 120 210 180 285
Polygon -7500403 true true 15 120 150 15 285 120
Line -16777216 false 30 120 270 120

leaf
false
0
Polygon -7500403 true true 150 210 135 195 120 210 60 210 30 195 60 180 60 165 15 135 30 120 15 105 40 104 45 90 60 90 90 105 105 120 120 120 105 60 120 60 135 30 150 15 165 30 180 60 195 60 180 120 195 120 210 105 240 90 255 90 263 104 285 105 270 120 285 135 240 165 240 180 270 195 240 210 180 210 165 195
Polygon -7500403 true true 135 195 135 240 120 255 105 255 105 285 135 285 165 240 165 195

line
true
0
Line -7500403 true 150 0 150 300

line half
true
0
Line -7500403 true 150 0 150 150

pentagon
false
0
Polygon -7500403 true true 150 15 15 120 60 285 240 285 285 120

person
false
0
Circle -7500403 true true 110 5 80
Polygon -7500403 true true 105 90 120 195 90 285 105 300 135 300 150 225 165 300 195 300 210 285 180 195 195 90
Rectangle -7500403 true true 127 79 172 94
Polygon -7500403 true true 195 90 240 150 225 180 165 105
Polygon -7500403 true true 105 90 60 150 75 180 135 105

plant
false
0
Rectangle -7500403 true true 135 90 165 300
Polygon -7500403 true true 135 255 90 210 45 195 75 255 135 285
Polygon -7500403 true true 165 255 210 210 255 195 225 255 165 285
Polygon -7500403 true true 135 180 90 135 45 120 75 180 135 210
Polygon -7500403 true true 165 180 165 210 225 180 255 120 210 135
Polygon -7500403 true true 135 105 90 60 45 45 75 105 135 135
Polygon -7500403 true true 165 105 165 135 225 105 255 45 210 60
Polygon -7500403 true true 135 90 120 45 150 15 180 45 165 90

sheep
false
15
Circle -1 true true 203 65 88
Circle -1 true true 70 65 162
Circle -1 true true 150 105 120
Polygon -7500403 true false 218 120 240 165 255 165 278 120
Circle -7500403 true false 214 72 67
Rectangle -1 true true 164 223 179 298
Polygon -1 true true 45 285 30 285 30 240 15 195 45 210
Circle -1 true true 3 83 150
Rectangle -1 true true 65 221 80 296
Polygon -1 true true 195 285 210 285 210 240 240 210 195 210
Polygon -7500403 true false 276 85 285 105 302 99 294 83
Polygon -7500403 true false 219 85 210 105 193 99 201 83

square
false
0
Rectangle -7500403 true true 30 30 270 270

square 2
false
0
Rectangle -7500403 true true 30 30 270 270
Rectangle -16777216 true false 60 60 240 240

star
false
0
Polygon -7500403 true true 151 1 185 108 298 108 207 175 242 282 151 216 59 282 94 175 3 108 116 108

target
false
0
Circle -7500403 true true 0 0 300
Circle -16777216 true false 30 30 240
Circle -7500403 true true 60 60 180
Circle -16777216 true false 90 90 120
Circle -7500403 true true 120 120 60

tree
false
0
Circle -7500403 true true 118 3 94
Rectangle -6459832 true false 120 195 180 300
Circle -7500403 true true 65 21 108
Circle -7500403 true true 116 41 127
Circle -7500403 true true 45 90 120
Circle -7500403 true true 104 74 152

triangle
false
0
Polygon -7500403 true true 150 30 15 255 285 255

triangle 2
false
0
Polygon -7500403 true true 150 30 15 255 285 255
Polygon -16777216 true false 151 99 225 223 75 224

truck
false
0
Rectangle -7500403 true true 4 45 195 187
Polygon -7500403 true true 296 193 296 150 259 134 244 104 208 104 207 194
Rectangle -1 true false 195 60 195 105
Polygon -16777216 true false 238 112 252 141 219 141 218 112
Circle -16777216 true false 234 174 42
Rectangle -7500403 true true 181 185 214 194
Circle -16777216 true false 144 174 42
Circle -16777216 true false 24 174 42
Circle -7500403 false true 24 174 42
Circle -7500403 false true 144 174 42
Circle -7500403 false true 234 174 42

turtle
true
0
Polygon -10899396 true false 215 204 240 233 246 254 228 266 215 252 193 210
Polygon -10899396 true false 195 90 225 75 245 75 260 89 269 108 261 124 240 105 225 105 210 105
Polygon -10899396 true false 105 90 75 75 55 75 40 89 31 108 39 124 60 105 75 105 90 105
Polygon -10899396 true false 132 85 134 64 107 51 108 17 150 2 192 18 192 52 169 65 172 87
Polygon -10899396 true false 85 204 60 233 54 254 72 266 85 252 107 210
Polygon -7500403 true true 119 75 179 75 209 101 224 135 220 225 175 261 128 261 81 224 74 135 88 99

wheel
false
0
Circle -7500403 true true 3 3 294
Circle -16777216 true false 30 30 240
Line -7500403 true 150 285 150 15
Line -7500403 true 15 150 285 150
Circle -7500403 true true 120 120 60
Line -7500403 true 216 40 79 269
Line -7500403 true 40 84 269 221
Line -7500403 true 40 216 269 79
Line -7500403 true 84 40 221 269

wolf
false
0
Polygon -16777216 true false 253 133 245 131 245 133
Polygon -7500403 true true 2 194 13 197 30 191 38 193 38 205 20 226 20 257 27 265 38 266 40 260 31 253 31 230 60 206 68 198 75 209 66 228 65 243 82 261 84 268 100 267 103 261 77 239 79 231 100 207 98 196 119 201 143 202 160 195 166 210 172 213 173 238 167 251 160 248 154 265 169 264 178 247 186 240 198 260 200 271 217 271 219 262 207 258 195 230 192 198 210 184 227 164 242 144 259 145 284 151 277 141 293 140 299 134 297 127 273 119 270 105
Polygon -7500403 true true -1 195 14 180 36 166 40 153 53 140 82 131 134 133 159 126 188 115 227 108 236 102 238 98 268 86 269 92 281 87 269 103 269 113

x
false
0
Polygon -7500403 true true 270 75 225 30 30 225 75 270
Polygon -7500403 true true 30 75 75 30 270 225 225 270
@#$#@#$#@
NetLogo 6.0.3
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
@#$#@#$#@
default
0.0
-0.2 0 0.0 1.0
0.0 1 1.0 0.0
0.2 0 0.0 1.0
link direction
true
0
Line -7500403 true 150 150 90 180
Line -7500403 true 150 150 210 180
@#$#@#$#@
0
@#$#@#$#@
