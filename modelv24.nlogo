breed [countries country]
undirected-link-breed [borderpipes borderpipe]
undirected-link-breed [transferpipes transferpipe]
undirected-link-breed [LNGroutes LNGroute]
breed [inputs input]

globals [
  gasprice
  transferprice
  LNGprice
  debug
  potentialdeals
  dealsmade

  THcheck
;  THcountries

  LNGexportingcountries
  LNGimportingcountries

  Time
  Capincrease
  Capincreasetime
  LNGCapincrease
  LNGCapincreasetime

  importA
  exportA
  importB
  exportB
  importC
  exportC
  importD
  exportD
  importE
  exportE
  importF
  exportF
  importlist
  exportlist
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

  inputgasprice
  inputtransferprice
  inputLNGprice
  inputdebug
  inputpotentialdeals
  inputTime
  inputCapincrease
  inputCapincreasetime
  inputLNGCapincrease
  inputLNGCapincreasetime

  Coalsurplus
  Oilsurplus
  Biofuelsurplus

  Coalimport
  Coalexport
  Oilimport
  Oilexport
  Biofuelimport
  Biofuelexport
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

]

transferpipes-own [
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
]

;inputs-own [
;  inputgasprice
;  inputtransferprice
;  inputLNGprice
;  inputdebug
;  inputpotentialdeals
;  inputTime
;  inputCapincrease
;  inputCapincreasetime
;  inputLNGCapincrease
;  inputLNGCapincreasetime
;]

to setup
  clear-all

  set debug 0

;  create-inputs 1 []

;  ask input 0 [
;    set gasprice inputgasprice
;    set transferprice inputtransferprice
;    set LNGprice inputLNGprice
;    set debug inputdebug
;    set potentialdeals inputpotentialdeals
;    set Time inputTime
;    set Capincrease inputCapincrease
;    set Capincreasetime inputCapincreasetime
;    set LNGCapincrease inputLNGCapincrease
;    set LNGCapincreasetime inputLNGCapincreasetime
;  ]

  set-default-shape turtles "circle"
  show ("NEW SETUP")

  create-countries 1 [
    set xcor -5
    set ycor 5
    set PP 9
    set GS 10;28570377.4246;7
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 10
    set oilsurplus -5
    set biofuelsurplus 10
  ]

  create-countries 1 [
    set xcor 0
    set ycor 5
    set PP 5
    set GS -10;-1265662.54576;-4
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 10
    set oilsurplus 10
    set biofuelsurplus -10
  ]

  create-countries 1 [
    set xcor -5
    set ycor 0
    set PP 5;9
    set GS -10;-3387982.57684;-4
    set linkedcountries []
    set totalimport 0
    set totalexport 0
    set LNGimportcapacity 0
    set LNGexportcapacity 0
    set coalsurplus 10
    set oilsurplus 10
    set biofuelsurplus 20
  ]

;  create-countries 1 [
;    set xcor 0
;    set ycor 0
;    set PP 10
;    set GS -705315490.184;10
;    set linkedcountries []
;    set totalimport 0
;    set totalexport 0
;    set LNGimportcapacity 0
;    set LNGexportcapacity 0
;    set coalsurplus -10
;    set oilsurplus -10
;    set biofuelsurplus 10
;  ]
;
;  create-countries 1 [
;    set xcor 5
;    set ycor 5
;    set PP 4
;    set GS 27105406.4276;3
;    set linkedcountries []
;    set totalimport 0
;    set totalexport 0
;    set LNGimportcapacity 0
;    set LNGexportcapacity 0
;    set coalsurplus -10
;    set oilsurplus -10
;    set biofuelsurplus -5
;  ]
;
;  create-countries 1 [
;    set xcor 5
;    set ycor 0
;    set PP 6
;    set GS -817803335.094;-6
;    set linkedcountries []
;    set totalimport 0
;    set totalexport 0
;    set LNGimportcapacity 0
;    set LNGexportcapacity 0
;    set coalsurplus 20
;    set oilsurplus 50
;    set biofuelsurplus 0
;  ]

  resetlinks

  set gasprice 5
  set transferprice 1
  set LNGprice 2
  set THcheck 0
  ask countries [set TH 0]

  ask borderpipes [set planningtoexpand 0]
  ask countries [
    set planningtoexpandLNGim 0
    set planningtoexpandLNGex 0

  ]

  set Time 2010
  set Capincrease 5000
  set Capincreasetime 5
  set LNGCapincrease 5000
  set LNGCapincreasetime 5

  reset-ticks
end

;to setglobals
;  ask Country 0 [
;    set gasprice inputgasprice
;    set transferprice inputtransferprice
;    set LNGprice inputLNGprice
;    set debug inputdebug
;    set potentialdeals inputpotentialdeals
;    set Time inputTime
;    set Capincrease inputCapincrease
;    set Capincreasetime inputCapincreasetime
;    set LNGCapincrease inputLNGCapincrease
;    set LNGCapincreasetime inputLNGCapincreasetime
;  ]
;end

to go
;  setglobals
  set potentialdeals 1
  set LNGexportingcountries []
  set LNGimportingcountries []
  resetlinks ;FIXME
  resettradevalues
  setLNGcapacity
  createLNGlinks
  ask borderpipes [set capacityavailable capacity]

  while [potentialdeals > 0] [
    tick
    if debug > 0 [
      show("new round")]
    ask transferpipes [die]
    set THcheck 0
    set potentialdeals 0

    ask countries [
      checkTH
      set linkedHUB []
      set TRUElinkedcountries []
    ]

    ask countries [
      let a who
      ask link-neighbors [
        if link-neighbor? country a = TRUE [
          set TRUElinkedcountries lput a TRUElinkedcountries]]]

    ask countries [
      if TH = 1 [createTH]]

    ask countries [
      if TH = 1 [
        createTHlinks
        if debug > 0 [show("test")]]
    ]

    ask borderpipes [set transfertype 0]
    ask transferpipes [set transfertype 1]
    ask LNGroutes [set transfertype 2]

    ask transferpipes [
      findroute
      if LNG = 1 [
        set transfertype 3
      ]
    ]


    ask transferpipes [updatelinklist]

    ask transferpipes [
      if LNG = 1 [set transfertype 3]
    ]

    ask links [
      set Deal 0
      set W2TR 0
      set W2TS 0
      set Roffer 0
      set Soffer 0
      determineprice
      if debug > 0 [
        show("base price")
        show(pipelineprice)
        show("Price S")
        show(pipelinepriceS)
        show("Price R")
        show(pipelinepriceR)]
    ]

    ask LNGroutes [
      set capacity12 min list [LNGexportavailable] of end1 [LNGimportavailable] of end2
      set capacity21 min list [LNGexportavailable] of end2 [LNGimportavailable] of end1
    ]

    ask countries [if TH = 0 [proposedeals]]

    ask links [compareproposals]

    ask countries [updateneeds]

    if debug > 0 [
      show("end of round")
      ask countries [show(GS)]
    ]

  ]

  coaltrade
  oiltrade
  biofueltrade

  updateoutput ;all outputs of the model should be set in the correctly labeled variables within this function

  ask borderpipes [
    if planningtoexpand = 0 [needtoexpand]
    if planningtoexpand = 1 [readytoexpand]
  ]

  ask countries [
    if planningtoexpandLNGim = 0 [needtoexpandLNGim]
    if planningtoexpandLNGim = 1 [readytoexpandLNGim]
    if planningtoexpandLNGex = 0 [needtoexpandLNGex]
    if planningtoexpandLNGex = 1 [readytoexpandLNGex]
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
  if LNGimportavailable = 0 [
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
  if LNGexportavailable = 0 [
    set planningtoexpandLNGex 1
    set endtimeLNGex Time + LNGCapincreasetime
  ]
end

to readytoexpandLNGex
  if Time > endtimeLNGex [
    set LNGexportcapacity LNGexportcapacity + LNGCapincrease
  ]
end

to findroute ;transferpipe perspective
  let n1 [who] of end1
  let n2 [who] of end2

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

  if debug > 0 [
    show (countrylist)
    show (irray)
  ]

  let x 0
  (foreach countrylist irray [[c i] ->
    ask country c [
;      show (c)
      ifelse borderpipe-neighbor? country n1 = TRUE [
        if debug > 0 [
          show ("availalbe capacity")
          show ([capacityavailable] of borderpipe c n1)]
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
                  set LNG 1
                ]
              ]
            ]
          ]
          if [end2] of LNGroute c n1 = country n1 [
            if [capacity21] of LNGroute c n1 > 0 [
              if TH = 1 or c = n2 [
                if i = 0 [
                  set irray replace-item x irray 1
                  set LNG 1
                ]
              ]
            ]
          ]
        ]
      ]
    ]
    set x x + 1
  ])

  let done 0
  let n 1

  let sumirray 5
  let prevsumirray 10

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
            if debug > 0 [
              show ("availalbe capacity")
              show ([capacityavailable] of borderpipe c a)]
            if [capacityavailable] of borderpipe c a > 0 [
              if TH = 1 or c = n2 [
                set nnext n + 1
                if i = 0 [set irray replace-item x irray nnext]
              ]
            ]
          ]
          [
            if LNGroute-neighbor? country a = TRUE [
              if [end1] of LNGroute c n1 = country a [
            if [capacity12] of LNGroute c a > 0 [
              if TH = 1 or c = n2 [
                if i = 0 [
                      set irray replace-item x irray 1
                      set LNG 1
                    ]
              ]
            ]
          ]
          if [end2] of LNGroute c a = country a [
            if [capacity21] of LNGroute c a > 0 [
              if TH = 1 or c = n2 [
                if i = 0 [
                      set irray replace-item x irray 1
                      set LNG 1
                    ]
              ]
            ]
          ]
        ]
          ]
        ]
        set x x + 1
      ])
    ]

    set n n + 1

    if debug > 1 [
      show("sum irray")
      show(sum irray)
    ]
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
    if debug > 1 [
      show("in loop")
      show("countrylist")
      show(countrylist)
      show("irray")
      show(irray)
    ]
  ]
  if debug > 1 [
    show("out of loop")
    show (countrylist)
    show (irray)
    show (done)]

  ;;;;;;;;;;;;Register Route;;;;;;;;;;;;;;

  set route []

  set route fput n2 route

  set n n - 1

  let prevcountry n2

  while [n > 0] [

    (foreach countrylist irray [[c i] ->
      ask country c [
        if borderpipe-neighbor? country prevcountry = TRUE [
          if i = n [set prevcountry c]
        ]
      ]
    ])

    set route fput prevcountry route
    set n n - 1
]

  set route fput n1 route

  if debug > 0 [
    show ("route")
    show (route)]

  ;;;;;;;;;;;;;;;;Calculate capacity route;;;;;;;;;;;;;;;;;;;;;;

  set capacityroute []

  let i 0
  let j 1

  if debug > 0 [
    show (length route)]
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
        ]
      ]
    ]

    set capacityroute lput a capacityroute


    set i i + 1
    set j j + 1

  ]


  set capacity min capacityroute

  if debug > 0 [
    show (capacityroute)
    show (capacity)]

end


to createLNGlinks
  ask countries [
    if LNGimportcapacity > 0 [
      set LNGimportingcountries lput who LNGimportingcountries]
    if LNGexportcapacity > 0[
      set LNGexportingcountries lput who LNGexportingcountries]
  ]

  foreach LNGimportingcountries [n ->
    foreach LNGexportingcountries [m ->
      ask country n [
        if n != m and link-neighbor? country m = FALSE [
          create-LNGroute-with country m
          set linkedcountries lput m linkedcountries
          ask country m [set linkedcountries lput n linkedcountries]
        ]
      ]
    ]
  ]
end

to setLNGcapacity
  ask countries [
    set LNGimportavailable LNGimportcapacity
    set LNGexportavailable LNGexportcapacity
  ]
end

to resettradevalues
  ask countries [
    set totalimport 0
    set totalexport 0
  ]
end

to resetlinks
  ask transferpipes [die]
  ask countries [set linkedcountries []]

   ask country 0 [
    create-borderpipe-with country 1
    set linkedcountries lput 1 linkedcountries
    ask country 1 [set linkedcountries lput 0 linkedcountries]

    create-borderpipe-with country 2
    set linkedcountries lput 2 linkedcountries
    ask country 2 [set linkedcountries lput 0 linkedcountries]
  ]

;  ask country 1 [
;    create-borderpipe-with country 3
;    set linkedcountries lput 3 linkedcountries
;    ask country 3 [set linkedcountries lput 1 linkedcountries]
;
;    create-borderpipe-with country 4
;    set linkedcountries lput 4 linkedcountries
;    ask country 4 [set linkedcountries lput 1 linkedcountries]
;  ]
;
;  ask country 2 [
;    create-borderpipe-with country 3
;    set linkedcountries lput 3 linkedcountries
;    ask country 3 [set linkedcountries lput 2 linkedcountries]
;  ]
;
;  ask country 3 [
;    create-borderpipe-with country 5
;    set linkedcountries lput 5 linkedcountries
;    ask country 5 [set linkedcountries lput 3 linkedcountries]
;  ]
;
;  ask country 4 [
;    create-borderpipe-with country 5
;    set linkedcountries lput 5 linkedcountries
;    ask country 5 [set linkedcountries lput 4 linkedcountries]
;  ]

  ask borderpipe 0 1 [set capacity 7000000]
  ask borderpipe 0 2 [set capacity 7000000]
;  ask borderpipe 1 3 [set capacity 7000000]
;  ask borderpipe 1 4 [set capacity 7000000]
;  ask borderpipe 2 3 [set capacity 7000000]
;  ask borderpipe 3 5 [set capacity 7000000]
;  ask borderpipe 5 4 [set capacity 7000000]
end

to updatelinklist
  let n [who] of end1
  let m [who] of end2
  ask country n [set TRUElinkedcountries lput m TRUElinkedcountries]
  ask country m [set TRUElinkedcountries lput n TRUElinkedcountries]
end

to checkTH
  ifelse GS = 0
  [set TH 1]
  [set TH 0]
end

to createTH
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
end

to createTHlinks
  foreach linkedHUB [n ->
    foreach linkedHUB [m ->
      let newlink 0
      ask country n [
        if n != m and link-neighbor? country m = FALSE [
          create-transferpipe-with country m
          set newlink 1
        ]
      ]
    ]
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

  if P4T = 1 [
    set pipelineprice gasprice * ((PPS - PPR) / 10 + 1)
    if transfertype = 0 [
      set pipelinepriceR pipelineprice
      set pipelinepriceS pipelineprice]
    if transfertype = 1 [
      set pipelinepriceR pipelineprice + transferprice]
    if transfertype = 2 [
      set pipelinepriceR pipelineprice + LNGprice
      set pipelinepriceS pipelineprice - LNGprice]
    if transfertype = 3 [
      set pipelinepriceR pipelineprice + transferprice + LNGprice
      set pipelinepriceS pipelineprice - LNGprice]
  ]
end

to proposedeals
  let pricelist []
  let demandlist []
  let tplist []
  let TD abs GS

  if GS > 0 [
    foreach TRUElinkedcountries [n ->
      set pricelist lput [pipelinepriceS] of link-with country n pricelist
      set demandlist lput [GS] of country n demandlist
      set tplist lput [P4T] of link-with country n tplist
      ask country n [set color blue]
    ]
  ]
  if GS < 0 [
    foreach TRUElinkedcountries [n ->
      set pricelist lput [pipelinepriceR] of link-with country n pricelist
      set demandlist lput [GS] of country n demandlist
      set tplist lput [P4T] of link-with country n tplist
      ask country n [set color blue]
    ]
  ]

  if debug = 1 [
    show("TRUE linked countries")
    show(TRUElinkedcountries)
    show("tplist")
    show(tplist)
  ]
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
      show("# max priced countries:")
      show(maxpricecount)

      let i 0

      let TTD TD / maxpricecount

      (foreach tplist demandlist pricelist TRUElinkedcountries [[a b c n] ->

        if a = 1 [
          show(n)
          show(TD)
          if c = maxprice [
            let offer min list TTD abs b
;            set offer offer / maxpricecount ;has to be done earlier.. devide TD instead?
            let id who
            ask link-with country n [
              ;set W2TS 1 ;changes here! v21

              if transfertype = 0 [
                if capacityavailable > 0 [
                  set offer min list offer capacityavailable
                  set W2TS 1
                  show("offer")
                  show(offer)
                ]
              ]

              if transfertype = 1 [
                if capacity > 0 [
                  set offer min list offer capacity
                  set W2TS 1
                ]
              ]

              if transfertype = 2 [
                if [GS] of end1 > 0 [set capacity capacity12]
                if [GS] of end1 < 0 [set capacity capacity21]
                if capacity > 0 [
                  set offer min list offer capacity
                  set W2TS 1
                ]
              ]

              set Soffer offer
            ]
            set TD TD - offer
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

      let TTD TD / minpricecount

      (foreach tplist demandlist pricelist TRUElinkedcountries [[a b c n] ->

        if a = 1 [
          if c = minprice [

            let offer min list TTD abs b
            ask link-with country n [
;              set W2TR 1

              if transfertype = 0 [
                if capacityavailable > 0 [
                  set offer min list offer capacityavailable
                  set W2TR 1
                ]
              ]

              if transfertype = 1 [
                if capacity > 0 [
                  set offer min list offer capacity
                  set W2TR 1
                ]
              ]

              if transfertype = 2 [
                if [GS] of end1 > 0 [set capacity capacity12]
                if [GS] of end1 < 0 [set capacity capacity21]
                if capacity > 0 [
                  set offer min list offer capacity
                  set W2TR 1
                ]
              ]

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

end

to compareproposals
  if W2TR = 1 and W2TS = 1 [
    let minoffer min list Soffer Roffer
    set Deal Deal + minoffer
    set potentialdeals potentialdeals + 1
    if debug > 0 [show("Deal:")
      show(Deal)]
    if transfertype = 0 [
      set capacityavailable capacityavailable - Deal
    ]

    if transfertype = 1 or transfertype = 3 [
      let y length route - 1
      let a 0

      let i 0
      let j 1

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
            ask country c2[ set LNGimportavailable LNGimportavailable - madedeal]
            ]
          ]
          set i i + 1
          set j j + 1
        ]
      ]

   ; LNG capacity is being updated within updateneeds
    ]
  ]

  if debug = 1 [
    show ("Transfertype")
    show (transfertype)
    show("P4T")
    show(P4T)
    show("W2TR")
    show(W2TR)
    show("W2TS")
    show(W2TS)
    show("Soffer")
    show(Soffer)
    show("Roffer")
    show(Roffer)
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
    if debug > 4 [show(coalsurplus)]
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
          set coalexport coalsurplus]
        [set coalimport abs(coalsurplus) * percentage]
      ]
    ]

  if debug > 4 [
    ask countries [
      show("coal import:")
      show(coalimport)
      show("coal export:")
      show(coalexport)
    ]
    show("totalcoalsupply:")
    show(totalcoalsupply)
    show("totalcoaldemand:")
    show(totalcoaldemand)
  ]
end

to oiltrade
  let totaloilsupply 0
  let totaloildemand 0
  let supplysurplus 0
  let supplyshortage 0
  let percentage 1

  ask countries [
    if debug > 4 [show(oilsurplus)]
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
          set oilexport oilsurplus]
        [set oilimport abs(oilsurplus) * percentage]
      ]
    ]

  if debug > 4 [
    ask countries [
      show("oil import:")
      show(oilimport)
      show("oil export:")
      show(oilexport)
    ]
    show("totaloilsupply:")
    show(totaloilsupply)
    show("totaloildemand:")
    show(totaloildemand)
  ]
end

to Biofueltrade
  let totalbiofuelsupply 0
  let totalbiofueldemand 0
  let supplysurplus 0
  let supplyshortage 0
  let percentage 1

  ask countries [
    if debug > 4 [show(biofuelsurplus)]
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
          set biofuelexport biofuelsurplus]
        [set biofuelimport abs(biofuelsurplus) * percentage]
      ]
    ]

  if debug > 4 [
    ask countries [
      show("biofuel import:")
      show(biofuelimport)
      show("biofuel export:")
      show(biofuelexport)
    ]
    show("totalbiofuelsupply:")
    show(totalbiofuelsupply)
    show("totalbiofueldemand:")
    show(totalbiofueldemand)
  ]
end

to updateoutput
  ask country 0 [
    set importA totalimport
    set exportA totalexport]
  ask country 1 [
    set importB totalimport
    set exportB totalexport]
  ask country 2 [
    set importC totalimport
    set exportC totalexport]
;  ask country 3 [
;    set importD totalimport
;    set exportD totalexport]
;  ask country 4 [
;    set importE totalimport
;    set exportE totalexport]
;  ask country 5 [
;    set importF totalimport
;    set exportF totalexport]

  set importlist []
  set exportlist []

  ask country 0 [
    set importlist lput totalimport importlist
    set exportlist lput totalexport exportlist]
  ask country 1 [
    set importlist lput totalimport importlist
    set exportlist lput totalexport exportlist]
  ask country 2 [
    set importlist lput totalimport importlist
    set exportlist lput totalexport exportlist]
;  ask country 3 [
;    set importlist lput totalimport importlist
;    set exportlist lput totalexport exportlist]
;  ask country 4 [
;    set importlist lput totalimport importlist
;    set exportlist lput totalexport exportlist]
;  ask country 5 [
;    set importlist lput totalimport importlist
;    set exportlist lput totalexport exportlist]
end
@#$#@#$#@
GRAPHICS-WINDOW
210
10
647
448
-1
-1
13.0
1
10
1
1
1
0
1
1
1
-16
16
-16
16
1
1
1
ticks
30.0

BUTTON
76
71
139
104
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
94
154
157
187
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
