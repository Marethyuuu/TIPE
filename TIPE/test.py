
import matplotlib.pyplot as plt
import numpy as np; np.random.seed(0)
import seaborn as sns; sns.set_theme()
ecranx=720
taillecarre=6
listeposcontact = [[230.0, 545.0], [235.0, 565.0], [608.0, 332.0], [39.0, 212.0], [37.0, 432.0], [36.0, 430.5], [32.0, 434.0], [591.5, 321.0], [605.0, 332.0], [603.5, 329.0], [608.0, 332.0], [605.0, 150.0], [579.0, 327.0], [240.0, 154.0], [33.0, 227.0], [62.0, 424.0], [56.0, 424.0], [47.0, 430.0], [232.0, 557.0], [608.0, 335.0], [591.0, 321.0], [38.0, 213.0], [36.0, 218.0], [603.0, 329.0], [606.0, 331.0], [586.5, 321.0], [228.5, 539.5], [225.0, 541.0], [120.5, 422.0], [51.5, 207.5], [50.0, 222.5], [48.0, 213.0], [49.5, 215.0], [51.0, 233.0], [46.0, 220.5], [615.0, 140.0], [44.0, 228.0], [708.0, 394.0], [706.0, 385.0], [706.0, 378.0], [47.0, 210.0], [52.5, 228.0], [43.5, 215.5], [37.0, 225.0], [240.0, 151.0], [39.0, 218.0], [242.0, 550.0], [238.5, 551.5], [252.0, 562.0], [428.0, 550.0], [444.5, 546.0], [459.0, 553.0], [691.5, 383.5], [689.5, 378.5], [691.0, 393.0], [163.5, 229.0], [230.5, 547.5], [227.0, 549.0], [233.0, 550.0], [229.0, 557.0], [246.0, 152.0], [608.0, 333.0], [427.5, 542.5], [421.0, 535.0], [700.0, 383.0], [460.0, 521.0], [461.0, 533.0], [130.5, 229.0], [674.0, 365.5], [232.0, 540.0], [228.5, 541.5], [244.0, 534.0], [232.0, 542.0], [114.5, 229.0], [44.5, 205.5], [41.0, 211.0], [36.5, 213.5], [34.0, 209.0], [455.5, 523.5], [456.5, 535.5], [452.0, 538.0], [161.5, 232.0], [663.5, 322.5], [634.5, 322.5], [631.5, 325.0], [468.0, 494.0], [217.0, 313.5], [470.0, 498.0], [145.5, 232.0], [78.0, 228.0], [76.5, 211.0], [72.5, 218.5], [74.5, 229.0], [233.5, 329.0], [459.5, 502.5], [470.0, 498.0], [74.5, 229.0], [78.0, 229.0], [244.0, 525.0], [169.5, 240.5], [62.5, 230.5], [66.0, 230.5], [145.5, 232.0], [609.0, 322.5], [618.5, 326.0], [67.5, 238.0], [244.0, 466.5], [460.0, 521.0], [469.5, 504.5], [256.0, 495.5], [459.5, 515.5], [457.0, 505.0], [458.0, 517.0], [469.5, 498.5], [75.0, 229.0], [78.5, 229.0], [67.0, 232.5], [70.5, 232.5], [145.5, 232.0], [72.5, 238.0], [244.0, 462.5], [460.0, 521.0], [471.5, 502.5], [622.0, 321.0], [256.0, 491.5], [238.5, 335.5], [52.0, 227.5], [199.5, 284.5], [35.0, 435.0], [421.0, 549.0], [430.5, 532.5], [111.5, 238.0], [46.5, 227.0], [448.5, 520.0], [430.0, 533.0], [78.5, 229.0], [88.5, 238.0], [111.5, 238.0], [464.5, 510.0], [263.5, 478.0], [614.0, 321.0], [510.0, 458.0], [490.0, 484.0], [217.5, 296.5], [223.5, 302.5], [209.5, 281.5], [223.0, 297.0], [226.0, 303.0], [78.5, 229.0], [57.0, 229.0], [237.5, 531.0], [510.0, 458.0], [116.5, 238.0], [105.5, 238.0], [99.0, 238.0], [145.5, 232.0], [118.0, 238.0], [111.5, 238.0], [484.5, 489.5], [497.5, 476.5], [275.5, 467.5], [594.5, 320.5], [492.5, 487.5], [568.5, 300.5], [225.5, 297.0], [228.5, 303.0], [59.0, 229.0], [510.0, 458.0], [119.0, 238.0], [110.5, 238.0], [102.0, 238.0], [145.5, 232.0], [112.0, 238.0], [103.5, 238.0], [489.5, 484.5], [500.0, 474.0], [280.5, 466.0], [590.0, 318.5], [494.5, 485.5], [59.0, 229.0], [510.0, 458.0], [104.0, 238.0], [113.0, 238.0], [105.5, 238.0], [500.0, 474.0], [280.5, 466.0], [494.5, 485.5], [49.0, 219.0], [53.0, 228.0], [220.0, 317.0], [46.0, 220.5], [51.0, 229.5], [41.0, 219.5], [468.0, 503.0], [172.5, 240.5], [170.0, 238.0], [233.0, 296.5], [224.0, 317.5], [510.0, 458.0], [126.5, 238.0], [126.0, 238.0], [117.5, 238.0], [145.5, 232.0], [119.5, 238.0], [500.0, 474.0], [280.5, 466.0], [494.5, 485.5], [470.5, 500.5], [53.0, 228.0], [51.5, 225.5], [41.5, 215.5], [149.0, 214.0], [700.5, 377.5], [704.0, 373.0], [245.0, 139.0], [481.0, 484.0], [146.5, 237.0], [489.0, 482.0], [155.0, 218.0], [144.5, 236.0], [145.5, 232.0], [319.5, 280.0], [332.5, 468.0], [48.0, 427.0], [416.0, 548.0], [498.0, 435.5], [246.0, 155.5], [248.0, 140.0], [238.5, 440.5], [236.0, 547.0], [493.0, 447.0], [580.0, 228.5], [601.0, 336.0], [189.0, 264.0], [188.0, 263.0], [55.0, 422.5], [46.0, 427.0], [181.0, 256.0], [107.5, 211.0], [308.5, 355.5], [235.0, 207.5], [210.0, 210.0], [238.0, 213.5], [432.5, 542.5], [449.0, 537.0], [284.5, 466.0], [217.0, 211.5], [208.0, 184.0], [165.0, 238.0], [546.0, 428.5], [159.0, 243.0], [376.5, 280.0], [220.5, 160.5], [233.0, 149.0], [541.5, 427.0], [217.0, 188.5], [470.0, 507.0], [611.0, 336.0], [78.5, 229.0], [220.0, 195.0], [228.0, 171.5], [234.0, 543.0], [530.5, 432.5], [232.0, 173.5], [176.5, 421.0], [218.0, 287.0], [142.5, 214.5], [419.5, 310.0], [251.0, 248.0], [609.0, 332.0], [602.0, 336.0], [455.0, 556.0], [484.0, 487.0], [60.5, 219.0], [235.0, 174.5], [433.5, 550.0], [243.0, 274.0], [407.0, 533.0], [491.0, 486.0], [506.0, 456.0], [615.5, 326.5], [603.5, 331.0], [615.0, 335.0], [238.0, 262.5], [423.0, 534.0], [408.5, 295.0], [513.0, 446.0], [696.0, 377.0], [228.5, 152.5], [231.5, 158.5], [234.5, 149.5], [231.0, 142.0], [148.5, 421.0], [171.5, 208.0], [394.0, 520.0], [251.0, 499.0], [509.0, 459.0], [506.0, 459.0], [259.0, 270.5], [568.0, 380.0], [419.5, 310.0], [229.0, 160.0], [232.0, 155.5], [232.0, 151.5], [225.0, 176.0], [235.0, 161.5], [235.0, 157.5], [235.0, 250.0], [241.0, 248.5], [228.0, 171.5], [110.5, 217.0], [259.0, 270.5], [514.0, 448.0], [509.0, 459.0], [510.5, 457.5], [511.0, 436.5], [506.5, 458.5], [246.5, 325.0], [238.0, 316.5], [246.5, 318.5], [238.0, 262.5], [510.0, 464.0], [507.5, 463.5], [250.0, 499.0], [410.5, 535.0], [423.0, 532.5], [148.5, 421.0], [506.5, 473.5], [502.5, 474.5], [394.0, 520.0], [504.0, 473.0], [53.0, 228.0], [171.5, 208.0], [128.5, 427.0], [412.5, 529.5], [238.0, 153.0], [624.0, 315.0], [254.0, 531.0], [600.5, 313.0], [79.5, 232.0], [566.5, 304.0], [407.0, 518.0], [137.5, 430.0], [161.0, 440.0], [215.5, 267.0], [235.0, 346.5], [225.0, 173.0], [235.0, 158.5], [235.0, 157.5], [235.0, 247.0], [241.0, 248.5], [228.0, 171.5], [104.5, 217.0], [235.0, 346.5], [217.0, 370.0], [256.0, 267.5], [514.0, 448.0], [509.0, 459.0], [510.5, 457.5], [505.0, 439.5], [506.5, 458.5], [252.5, 324.5], [238.0, 259.5], [516.0, 458.0], [517.5, 456.5], [513.5, 457.5], [250.0, 499.0], [410.5, 532.0], [423.0, 529.5], [148.5, 421.0], [159.0, 439.0], [138.0, 430.0], [512.5, 467.5], [394.0, 520.0], [406.5, 517.5], [510.0, 467.0], [53.0, 228.0], [562.0, 306.5], [171.5, 208.0], [134.5, 427.0], [406.5, 523.5], [238.0, 156.0], [630.0, 315.0], [256.0, 524.5], [244.5, 550.5], [626.0, 326.0], [618.0, 320.5], [613.0, 331.0], [228.0, 171.5], [54.0, 230.0], [44.0, 220.0], [45.0, 222.0], [625.0, 326.5], [617.5, 320.0], [246.0, 547.5], [234.0, 556.5], [612.5, 329.0], [609.0, 330.0], [236.0, 557.0], [156.0, 434.5], [504.5, 447.0], [144.5, 442.5], [235.0, 155.5], [235.0, 157.5], [241.0, 248.5], [228.0, 171.5], [228.0, 173.5], [506.5, 458.5], [519.5, 451.5], [250.0, 499.0], [148.5, 421.0], [153.0, 436.0], [138.0, 430.0], [514.5, 462.5], [394.0, 520.0], [406.5, 517.5], [516.0, 461.0], [504.5, 446.0], [54.5, 232.0], [556.0, 310.0], [44.5, 222.0], [171.5, 208.0], [624.5, 436.0], [155.5, 433.0], [140.5, 427.0], [400.5, 517.5], [145.0, 442.0], [238.0, 159.0], [636.0, 318.0], [630.0, 325.5], [627.0, 329.5], [256.0, 521.5], [622.0, 317.5], [619.0, 321.5], [244.0, 544.0], [247.0, 544.5], [235.0, 553.5], [613.0, 329.0], [64.5, 226.5], [248.5, 250.5], [420.0, 531.0], [242.5, 339.5], [372.0, 314.5], [38.5, 216.5], [43.0, 223.5], [34.0, 215.0], [62.0, 230.5], [55.5, 236.5], [45.5, 226.5], [51.5, 235.0], [41.5, 225.0], [48.0, 235.0], [565.5, 338.5], [49.5, 227.0], [39.0, 435.0], [202.0, 194.0], [564.5, 340.5], [250.0, 506.5], [55.5, 222.0], [362.0, 488.0], [568.0, 350.0], [561.5, 340.5], [235.0, 231.0], [205.0, 194.0], [228.0, 171.5], [228.0, 182.5], [229.0, 346.0], [244.0, 259.0], [372.0, 313.0], [362.0, 488.0], [65.5, 232.0], [55.5, 225.0], [62.0, 232.0], [276.5, 348.5], [541.5, 432.5], [537.5, 433.5], [250.0, 499.0], [250.0, 503.5], [434.5, 535.0], [135.0, 427.0], [536.5, 443.5], [534.0, 443.0], [53.0, 228.0], [63.5, 238.0], [53.5, 231.0], [60.0, 238.0], [561.5, 338.5], [538.0, 328.0], [53.5, 228.0], [43.5, 221.0], [50.0, 228.0], [155.5, 419.5], [158.5, 422.5], [382.5, 499.5], [145.0, 433.0], [238.0, 168.0], [636.0, 318.0], [634.5, 318.0], [630.0, 321.5], [256.0, 512.5], [626.5, 310.0], [622.0, 313.5], [251.5, 527.5], [251.5, 526.0], [247.0, 536.5], [620.5, 313.5], [60.5, 238.0], [50.5, 231.0], [375.0, 486.0], [538.0, 405.0], [78.5, 223.0], [238.0, 203.5], [77.5, 223.0], [220.0, 318.0], [75.5, 223.0], [235.0, 206.5], [217.5, 211.5], [221.0, 195.0], [250.0, 506.5], [228.0, 200.5], [64.5, 207.5], [222.0, 206.0], [492.0, 331.5], [225.0, 202.5], [570.5, 428.5], [68.5, 223.0], [589.5, 169.0], [250.0, 506.5], [566.5, 427.5], [231.5, 214.5], [238.0, 304.5], [596.0, 154.5], [591.0, 146.0], [247.0, 310.5], [228.0, 171.5], [82.5, 421.0], [30.0, 427.0], [107.0, 226.0], [55.5, 421.5], [37.0, 427.0], [42.0, 425.0], [106.0, 226.0], [568.0, 317.5], [238.0, 204.0], [225.0, 194.0], [221.5, 182.5], [228.0, 199.0], [64.5, 205.0], [69.0, 223.0], [245.0, 314.0], [238.0, 304.5], [225.0, 216.0], [452.5, 522.0], [295.0, 380.5], [228.5, 190.5], [235.0, 207.0], [568.0, 401.0], [565.0, 401.0], [250.0, 499.0], [250.0, 487.0], [250.0, 499.0], [250.0, 496.0], [434.5, 535.0], [102.5, 427.0], [82.5, 421.0], [569.0, 419.0], [569.0, 419.0], [566.0, 419.0], [105.5, 226.0], [94.5, 238.0], [84.5, 238.0], [91.0, 238.0], [251.0, 310.5], [231.5, 168.0], [231.5, 195.5], [566.0, 419.0], [356.0, 467.0], [107.0, 226.0], [636.0, 318.0], [651.0, 333.0], [645.5, 327.5], [256.0, 496.0], [256.0, 496.0], [256.0, 505.0], [652.5, 334.5], [582.0, 183.5], [82.5, 238.0], [56.5, 421.0], [584.5, 161.5], [38.0, 427.0], [104.0, 226.0], [238.0, 174.5], [549.5, 423.0], [54.0, 426.0], [269.0, 297.0], [208.0, 352.5], [86.5, 424.0], [97.0, 226.0], [235.0, 174.5], [92.5, 208.0], [234.0, 544.5], [242.0, 551.0], [235.0, 183.0], [238.0, 168.5], [238.0, 196.0], [215.0, 203.0], [228.0, 175.0], [228.0, 171.5], [228.0, 199.0], [225.0, 216.0], [212.5, 352.5], [292.0, 396.5], [235.0, 175.0], [235.0, 171.5], [235.0, 199.0], [568.0, 386.0], [568.0, 385.5], [250.0, 499.0], [251.5, 479.5], [250.0, 488.5], [269.0, 287.0], [94.5, 427.0], [82.5, 421.0], [597.0, 430.0], [105.5, 226.0], [110.0, 238.0], [100.0, 238.0], [106.5, 238.0], [92.5, 208.0], [238.0, 160.5], [538.0, 429.5], [561.5, 410.0], [340.5, 451.5], [107.5, 226.0], [97.5, 226.0], [104.0, 226.0], [646.5, 328.5], [663.5, 345.5], [658.5, 340.5], [257.5, 481.0], [256.0, 490.0], [668.0, 350.0], [98.5, 238.0], [59.0, 430.0], [63.0, 418.0], [74.5, 424.0], [40.5, 436.0], [44.0, 424.0], [29.0, 430.0], [77.5, 421.0], [243.5, 520.5], [688.0, 373.0], [586.5, 303.0], [235.0, 179.0], [238.0, 168.0], [229.5, 171.5], [229.5, 171.5], [238.0, 304.5], [225.0, 216.0], [412.0, 529.0], [214.5, 352.5], [290.5, 400.5], [235.0, 171.0], [235.0, 197.0], [568.0, 381.5], [568.0, 383.0], [253.5, 477.5], [250.0, 486.5], [434.5, 535.0], [92.5, 427.0], [82.5, 421.0], [77.5, 421.0], [597.0, 430.0], [114.0, 238.0], [104.0, 238.0], [110.5, 238.0], [238.0, 160.0], [561.5, 410.0], [336.0, 447.0], [107.5, 226.0], [97.5, 226.0], [104.0, 226.0], [75.0, 424.0], [650.5, 332.5], [667.5, 349.5], [662.5, 344.5], [256.0, 498.5], [243.5, 520.5], [259.5, 477.0], [256.0, 486.0], [688.0, 373.0], [102.5, 238.0], [61.0, 430.0], [40.0, 435.5], [44.0, 423.5], [71.5, 436.0], [250.0, 524.5], [683.0, 368.0], [238.0, 168.5], [214.5, 352.5], [235.0, 171.5], [235.0, 194.5], [568.0, 380.5], [250.0, 499.0], [250.0, 484.0], [90.0, 427.0], [82.5, 421.0], [77.5, 421.0], [568.0, 392.0], [596.5, 430.0], [106.0, 226.0], [119.5, 238.0], [107.0, 238.0], [93.0, 208.0], [561.5, 410.0], [331.0, 442.0], [95.0, 226.0], [101.5, 226.0], [71.5, 436.0], [72.5, 424.0], [656.0, 338.0], [673.0, 355.0], [668.0, 350.0], [256.0, 496.0], [246.0, 518.0], [250.0, 523.5], [262.0, 472.0], [262.0, 469.0], [688.0, 373.0], [683.0, 368.0], [102.5, 238.0], [64.0, 430.0], [43.0, 435.5], [444.5, 313.0], [241.5, 507.5], [226.5, 493.5], [78.5, 431.0], [250.0, 481.0], [82.5, 421.0], [79.0, 430.5], [109.5, 238.0], [92.0, 226.0], [71.5, 433.5], [248.5, 515.5], [256.0, 475.0], [680.0, 365.0], [66.5, 427.5], [45.5, 433.0], [78.5, 238.0], [74.0, 226.0], [282.0, 437.0], [675.0, 360.0], [229.0, 511.0], [572.5, 427.0], [233.0, 554.0], [247.5, 534.5], [251.0, 540.0], [240.5, 546.0], [240.5, 557.0], [249.0, 551.0], [310.5, 427.5], [238.0, 194.5], [296.0, 440.0], [671.0, 356.0], [225.0, 522.5], [239.5, 229.5], [284.5, 428.5], [692.0, 373.0], [704.0, 378.0], [225.0, 232.0], [238.5, 508.5], [540.5, 413.5], [686.5, 364.5], [239.5, 516.5], [303.0, 419.5], [231.5, 526.5], [91.5, 238.0], [573.5, 413.0], [682.5, 360.5], [247.0, 523.5], [242.5, 153.5], [242.5, 171.5], [223.0, 230.0], [444.0, 310.0], [425.0, 538.0], [217.0, 352.0], [294.5, 426.5], [310.0, 429.5], [296.0, 437.0], [235.0, 171.0], [568.0, 356.0], [233.5, 500.5], [250.0, 499.0], [254.5, 478.0], [250.0, 506.0], [434.5, 535.0], [236.0, 226.0], [79.5, 427.0], [82.5, 421.0], [86.5, 430.0], [77.5, 421.0], [568.0, 381.5], [301.5, 421.0], [287.5, 428.5], [140.0, 238.0], [123.5, 238.0], [541.0, 415.5], [566.5, 427.0], [310.5, 424.0], [296.5, 431.5], [84.5, 226.0], [74.5, 226.0], [71.0, 433.0], [62.0, 424.0], [239.5, 509.5], [239.5, 509.5], [224.0, 521.0], [230.5, 525.0], [573.0, 413.0], [666.5, 348.5], [668.5, 353.5], [256.0, 508.0], [256.0, 515.0], [247.0, 523.5], [670.5, 352.5], [671.0, 356.0], [682.5, 360.5], [268.0, 461.5], [672.5, 357.5], [684.0, 362.0], [86.0, 238.0], [92.5, 238.0], [74.0, 427.0], [247.0, 523.5], [247.0, 530.5], [231.5, 535.0], [45.5, 429.5], [289.5, 445.5], [678.0, 357.0], [556.5, 347.5], [589.0, 253.5], [217.5, 226.5], [444.0, 310.0], [430.0, 538.0], [220.0, 352.5], [301.0, 433.0], [303.5, 433.0], [310.0, 433.0], [294.0, 446.0], [568.0, 349.5], [233.5, 501.5], [232.5, 224.5], [82.5, 421.0], [90.0, 430.0], [77.5, 421.0], [568.0, 378.5], [301.0, 424.0], [294.0, 428.0], [146.5, 238.0], [543.5, 419.0], [303.5, 424.0], [296.5, 428.0], [74.0, 226.0], [64.0, 424.0], [59.0, 424.0], [43.0, 429.5], [239.5, 508.5], [220.5, 517.5], [227.5, 521.5], [569.5, 411.5], [666.5, 348.5], [668.5, 353.5], [676.5, 355.5], [256.0, 503.5], [256.0, 514.0], [244.0, 519.0], [670.5, 352.5], [671.0, 356.0], [679.0, 358.0], [275.0, 458.0], [672.5, 357.5], [680.5, 359.5], [89.0, 238.0], [95.5, 238.0], [77.5, 427.0], [244.0, 527.0], [245.5, 536.5], [225.0, 528.0], [226.5, 537.5], [239.0, 548.0], [556.5, 335.5], [243.5, 151.0], [238.0, 304.5], [444.5, 310.0], [220.5, 352.5], [310.0, 433.0], [294.5, 445.5], [568.0, 349.0], [233.5, 502.0], [250.0, 499.0], [250.0, 496.5], [250.0, 507.5], [232.0, 224.5], [82.5, 421.0], [90.5, 430.0], [77.5, 421.0], [294.5, 424.5], [301.5, 424.5], [295.0, 428.0], [286.0, 437.0], [147.5, 238.0], [589.0, 254.0], [543.5, 419.5], [562.5, 425.0], [303.0, 424.0], [296.5, 427.5], [287.5, 436.5], [74.0, 226.0], [63.5, 424.0], [58.5, 424.0], [239.5, 508.0], [569.0, 411.0], [668.5, 353.5], [256.0, 502.5], [256.0, 513.5], [670.5, 352.5], [671.0, 356.0], [678.5, 357.5], [276.0, 457.5], [672.5, 357.5], [680.0, 359.0], [89.5, 238.0], [96.0, 238.0], [78.0, 427.0], [244.0, 527.0], [246.0, 536.0], [224.5, 527.5], [240.0, 547.0], [233.5, 325.5], [556.5, 334.5], [244.0, 150.5], [238.0, 304.5], [233.5, 325.5], [303.0, 434.0], [305.0, 437.0], [296.0, 446.0], [568.0, 348.0], [250.0, 499.0], [250.0, 496.5], [250.0, 508.5], [82.5, 421.0], [77.5, 421.0], [301.5, 425.5], [287.5, 437.5], [149.5, 238.0], [561.5, 410.0], [543.5, 420.5], [301.0, 424.0], [296.0, 427.0], [74.5, 226.0], [62.5, 424.0], [71.5, 433.0], [57.5, 424.0], [41.5, 429.5], [239.5, 507.0], [568.0, 410.0], [238.0, 207.5], [668.5, 353.5], [256.0, 500.5], [670.5, 352.5], [671.0, 356.0], [678.0, 357.0], [277.0, 457.0], [672.5, 357.5], [679.5, 358.5], [90.5, 238.0], [97.0, 238.0], [79.0, 427.0], [250.5, 532.5], [243.0, 526.0], [247.0, 535.0], [680.0, 362.0], [222.5, 525.5], [241.5, 545.5], [294.0, 435.5], [230.5, 213.0], [236.0, 512.0], [230.5, 527.0], [556.5, 332.5], [556.5, 347.5], [238.0, 304.5], [444.5, 312.5], [307.5, 439.5], [310.0, 436.0], [309.5, 436.5], [300.5, 445.5], [568.0, 346.0], [250.0, 499.0], [250.0, 496.5], [250.0, 510.5], [235.0, 512.5], [229.0, 213.0], [82.5, 421.0], [93.5, 430.0], [77.5, 421.0], [301.5, 427.5], [292.0, 437.0], [153.5, 238.5], [561.5, 410.0], [543.5, 422.5], [297.0, 423.0], [296.5, 423.5], [60.5, 424.0], [55.5, 424.0], [39.5, 429.5], [239.5, 505.0], [239.5, 516.5], [230.5, 527.0], [668.5, 353.5], [256.0, 496.5], [294.5, 433.5], [670.5, 352.5], [671.0, 356.0], [675.5, 354.5], [282.0, 454.5], [672.5, 357.5], [92.5, 238.0], [99.0, 238.0], [81.0, 427.0], [241.0, 524.0], [247.0, 532.5], [218.5, 521.5], [244.0, 540.5], [232.0, 534.5], [268.0, 479.0], [247.5, 519.5], [243.0, 318.5], [241.0, 520.5], [294.5, 451.5], [585.5, 326.5], [247.0, 469.5], [176.0, 232.0], [121.5, 430.0], [247.0, 469.5], [583.0, 323.0], [233.5, 511.5], [250.0, 499.0], [250.0, 496.5], [250.0, 519.0], [245.0, 521.0], [559.0, 272.5], [223.0, 213.5], [100.0, 430.0], [301.5, 433.5], [314.0, 434.0], [166.5, 245.0], [538.5, 429.0], [553.0, 424.0], [54.0, 424.0], [49.0, 424.0], [33.0, 433.0], [218.0, 512.0], [234.5, 520.5], [666.5, 348.5], [668.5, 353.5], [536.5, 429.0], [294.5, 426.5], [670.5, 352.5], [671.0, 356.0], [672.5, 357.5], [102.5, 238.0], [105.5, 238.0], [251.0, 526.0], [28.0, 432.5], [210.5, 508.5], [239.5, 518.0], [44.0, 426.0], [682.0, 375.5], [562.5, 266.5], [163.5, 211.0], [122.0, 430.0], [247.0, 472.0], [247.0, 469.5], [583.5, 314.0], [233.5, 516.0], [250.0, 518.5], [564.0, 277.0], [564.0, 268.0], [104.5, 430.0], [323.5, 439.0], [176.0, 254.0], [561.5, 410.0], [548.5, 424.0], [274.5, 415.5], [239.5, 513.5], [239.5, 515.5], [668.5, 353.5], [527.5, 433.5], [294.0, 418.5], [671.0, 356.0], [102.5, 238.0], [110.5, 238.0], [44.0, 421.5], [256.0, 521.0], [666.5, 348.5], [678.0, 371.5], [28.0, 427.0], [207.5, 499.0], [668.0, 393.0], [345.5, 424.0], [246.0, 536.5], [252.0, 535.5], [252.0, 531.5], [671.0, 362.0], [574.5, 323.5], [52.5, 418.0], [232.0, 526.5], [247.0, 492.5], [222.5, 486.0], [247.0, 493.5], [230.5, 495.0], [577.0, 286.5], [574.0, 320.5], [562.5, 308.0], [262.0, 482.5], [144.5, 229.0], [271.5, 435.5], [241.0, 283.5], [280.5, 430.5], [373.5, 295.0], [87.5, 421.0], [151.5, 424.5], [232.0, 509.5], [618.0, 318.0], [571.0, 274.5], [562.5, 308.0], [562.5, 308.0], [567.0, 307.5], [97.5, 424.0], [85.0, 421.0], [238.0, 304.5], [163.5, 211.0], [145.0, 229.0], [247.0, 492.0], [247.0, 494.0], [230.0, 509.0], [251.5, 422.5], [151.5, 426.5], [358.5, 478.5], [618.0, 318.0], [568.5, 278.5], [572.0, 273.0], [577.0, 262.5], [77.5, 421.0], [562.5, 307.5], [567.0, 307.0], [339.5, 468.0], [672.0, 362.0], [686.5, 376.5], [667.5, 366.5], [204.0, 276.0], [274.5, 415.5], [276.5, 430.5], [225.0, 519.0], [656.5, 341.5], [659.5, 350.5], [282.5, 454.5], [268.0, 477.0], [283.0, 428.0], [660.5, 345.5], [102.5, 238.0], [124.5, 238.0], [62.5, 418.0], [565.0, 285.0], [570.0, 274.5], [57.5, 418.0], [256.0, 504.5], [239.0, 519.5], [640.5, 322.5], [652.0, 346.0], [41.5, 423.5], [182.5, 470.5], [220.5, 274.5], [565.5, 275.5], [220.5, 294.5], [77.5, 421.0], [77.5, 421.0], [48.5, 223.5], [562.5, 308.0], [567.0, 307.5], [82.0, 421.0], [77.0, 421.0], [77.5, 421.0], [238.0, 304.5], [247.0, 506.5], [247.0, 492.0], [227.0, 509.0], [151.5, 429.5], [572.0, 270.0], [562.5, 304.5], [567.0, 304.0], [692.5, 378.5], [210.0, 282.0], [245.0, 516.5], [225.0, 519.0], [653.5, 338.5], [656.5, 347.5], [288.5, 451.5], [271.0, 474.0], [286.0, 425.0], [660.5, 351.5], [102.5, 238.0], [124.5, 238.0], [65.5, 418.0], [565.0, 285.0], [570.0, 277.5], [256.0, 498.5], [634.5, 316.5], [44.5, 423.5], [616.5, 315.5], [624.5, 329.5], [589.0, 189.5], [226.0, 273.0], [160.5, 441.5], [585.5, 325.0], [586.0, 320.0], [165.5, 453.5], [696.5, 378.5], [703.0, 381.0], [707.0, 381.0], [562.5, 308.0], [567.0, 307.5], [583.0, 322.0], [78.0, 421.0], [73.0, 421.0], [78.0, 421.0], [235.0, 298.0], [145.0, 229.0], [247.0, 506.0], [223.0, 509.0], [152.0, 437.5], [155.5, 441.0], [572.0, 265.5], [82.5, 421.0], [565.5, 300.5], [569.0, 295.0], [570.0, 300.0], [586.0, 314.5], [354.0, 475.0], [692.5, 378.5], [695.5, 379.0], [589.0, 189.5], [283.5, 423.5], [249.5, 516.5], [652.0, 343.0], [290.0, 421.0], [702.0, 381.5], [102.5, 238.0], [124.5, 238.0], [70.0, 418.0], [57.5, 427.0], [565.0, 285.0], [570.0, 282.0], [164.5, 452.5], [52.5, 427.0], [256.0, 490.0], [625.5, 307.5], [36.5, 432.5], [607.5, 306.0], [57.5, 427.0], [241.0, 283.5], [245.0, 458.0], [244.0, 460.0], [154.5, 442.5], [63.5, 427.0], [699.5, 379.0], [706.0, 381.5], [705.0, 382.0], [713.0, 382.0], [397.0, 526.0], [404.0, 542.0], [683.0, 368.0], [576.5, 296.5], [576.0, 293.0], [687.5, 363.0], [388.0, 517.0], [607.5, 301.0], [56.5, 425.0], [58.0, 422.0], [54.0, 422.0], [37.0, 426.5], [50.0, 422.0], [46.0, 426.0], [271.5, 435.5], [107.5, 424.0], [45.5, 423.0], [679.0, 355.0], [271.5, 435.5], [562.5, 308.0], [559.0, 311.5], [567.0, 307.5], [572.0, 309.5], [65.5, 421.0], [77.5, 421.0], [57.5, 421.0], [53.5, 425.0], [238.0, 304.5], [235.0, 302.5], [145.0, 229.0], [558.5, 363.5], [130.5, 428.5], [108.0, 424.0], [396.5, 525.5], [577.0, 219.5], [135.0, 226.0], [94.5, 421.0], [578.0, 282.5], [592.0, 276.5], [584.0, 289.5], [388.0, 517.0], [679.0, 365.0], [682.5, 386.5], [283.0, 421.0], [311.0, 424.0], [271.5, 435.5], [679.0, 355.0], [689.0, 389.0], [696.5, 372.5], [683.0, 359.0], [561.5, 290.5], [104.5, 238.0], [125.5, 238.0], [82.0, 418.0], [62.0, 418.0], [58.0, 422.0], [565.0, 285.0], [570.0, 287.0], [558.0, 294.0], [563.0, 296.0], [61.0, 418.0], [57.0, 422.0], [265.5, 465.5], [41.0, 419.0], [37.0, 423.0], [584.0, 281.0], [50.0, 422.0], [287.0, 438.0], [434.5, 528.5], [378.0, 507.0], [426.0, 522.0], [280.5, 430.5], [116.5, 421.0], [48.5, 234.5], [58.5, 234.5], [582.5, 243.5], [459.0, 556.0], [71.5, 421.0], [92.5, 424.0], [585.5, 323.5], [442.5, 538.0], [437.5, 544.5], [568.0, 333.5], [562.5, 308.0], [584.5, 323.5], [567.0, 307.5], [62.5, 421.0], [50.0, 421.0], [46.0, 425.0], [133.0, 217.0], [145.0, 229.0], [565.5, 356.5], [244.0, 493.5], [97.0, 427.0], [94.5, 424.0], [115.5, 427.0], [123.0, 425.5], [108.0, 424.0], [425.5, 532.0], [437.0, 544.0], [579.0, 242.0], [577.0, 231.5], [577.0, 219.5], [120.5, 226.0], [128.0, 226.0], [579.0, 280.0], [577.0, 275.0], [388.0, 517.0], [682.5, 362.5], [283.0, 421.0], [289.5, 418.5], [311.0, 424.0], [294.0, 431.0], [232.0, 332.0], [279.0, 428.0], [229.0, 318.0], [671.5, 347.5], [441.5, 538.0], [285.5, 425.5], [229.0, 330.0], [377.5, 506.5], [675.5, 351.5], [118.5, 238.0], [94.0, 418.0], [66.5, 418.0], [62.5, 422.0], [565.0, 285.0], [563.0, 280.0], [277.5, 450.5], [47.0, 418.0], [43.0, 422.0], [116.5, 421.0], [570.0, 269.0], [564.0, 285.0], [58.0, 238.0], [68.0, 238.0], [50.0, 422.0], [214.5, 483.5], [583.0, 253.5], [566.0, 276.0], [63.5, 425.0], [398.0, 527.5], [433.5, 429.0], [567.0, 305.0], [46.5, 421.0], [107.5, 427.0], [437.5, 539.5], [577.0, 235.5], [577.0, 219.5], [66.0, 421.0], [62.0, 425.0], [583.0, 264.5], [667.0, 343.0], [437.5, 537.5], [286.5, 418.5], [378.0, 507.0], [563.5, 281.0], [559.5, 292.5], [553.0, 287.5], [105.5, 238.0], [103.0, 418.0], [565.0, 285.0], [558.5, 280.0], [103.5, 421.0], [104.5, 418.0], [311.0, 427.0], [51.5, 418.0], [47.5, 422.0], [117.0, 421.0], [66.5, 238.0], [76.5, 238.0], [50.0, 422.0], [429.0, 533.5], [690.0, 375.0], [696.5, 377.5], [684.0, 365.0], [680.0, 361.0], [353.0, 482.0], [559.0, 313.5], [568.0, 322.5], [558.5, 307.5], [567.0, 303.0], [145.0, 229.0], [244.0, 493.5], [84.0, 427.0], [93.0, 424.0], [432.0, 538.0], [437.5, 537.5], [577.0, 219.5], [114.0, 226.0], [98.5, 226.0], [64.0, 421.0], [60.0, 425.0], [583.0, 253.5], [429.0, 531.5], [681.0, 367.0], [283.0, 413.5], [311.0, 424.0], [214.0, 343.0], [398.0, 530.0], [241.0, 331.0], [229.0, 331.0], [667.5, 343.5], [680.0, 361.0], [435.5, 537.5], [695.0, 376.0], [433.5, 430.0], [683.5, 364.5], [557.5, 294.5], [549.0, 289.5], [131.5, 238.0], [109.5, 238.0], [105.0, 418.0], [565.0, 285.0], [569.0, 265.0], [105.5, 421.0], [315.0, 424.5], [53.5, 418.0], [49.5, 422.0], [305.0, 424.5], [80.5, 238.0], [50.0, 422.0], [89.0, 226.0], [686.5, 368.5], [572.5, 293.5], [85.0, 226.0], [559.0, 307.0], [573.0, 293.0], [570.0, 300.0], [145.0, 229.0], [223.0, 500.5], [93.0, 424.0], [94.5, 424.0], [102.5, 427.0], [437.5, 535.0], [577.0, 219.5], [85.0, 226.0], [57.5, 425.0], [429.0, 529.0], [685.5, 370.5], [278.0, 411.0], [398.0, 532.5], [232.0, 350.0], [229.0, 336.0], [667.5, 343.5], [679.5, 360.5], [353.0, 482.0], [690.5, 372.5], [433.5, 430.0], [229.0, 348.0], [683.5, 364.5], [555.0, 297.0], [136.5, 238.0], [115.0, 238.0], [141.5, 238.0], [107.5, 418.0], [565.0, 285.0], [569.0, 267.5], [108.0, 421.0], [320.0, 424.0], [52.0, 422.0], [76.0, 238.0], [86.0, 238.0], [419.0, 527.0], [581.5, 280.5], [592.0, 321.0], [583.0, 228.5], [251.0, 374.0], [566.0, 297.5], [600.0, 320.0], [229.0, 512.5], [93.0, 424.0], [65.5, 424.0], [437.5, 529.0], [85.0, 226.0], [51.5, 425.0], [286.5, 428.5], [679.5, 361.5], [147.5, 238.5], [565.0, 285.0], [569.0, 273.5], [576.5, 275.5], [548.0, 280.0], [332.0, 424.0], [58.0, 422.0], [631.5, 323.5], [581.0, 311.0], [602.0, 320.0], [230.5, 515.5], [64.5, 427.0], [64.5, 424.0], [586.0, 232.0], [85.0, 226.0], [50.0, 425.0], [583.0, 253.5], [583.0, 225.5], [214.0, 355.5], [454.0, 430.0], [565.5, 295.0], [570.0, 300.0], [679.0, 361.0], [359.0, 482.0], [433.5, 430.0], [229.0, 348.0], [150.0, 240.0], [560.5, 280.0], [565.0, 285.0], [569.0, 274.5], [546.5, 280.0], [334.0, 424.0], [59.5, 422.0], [571.5, 274.0], [543.0, 280.0], [50.0, 422.0], [631.0, 322.0], [131.5, 426.5], [130.5, 229.0], [514.5, 333.5], [583.0, 311.0], [578.0, 302.0], [145.0, 229.0], [131.0, 229.0], [231.5, 517.0], [85.0, 226.0], [63.5, 421.0], [49.0, 425.0], [583.0, 224.5], [454.0, 430.0], [566.0, 294.0], [571.0, 299.0], [679.5, 360.5], [360.0, 482.0], [432.5, 430.0], [418.5, 526.5], [514.0, 333.0], [152.0, 241.0], [560.0, 280.0], [565.0, 285.0], [569.0, 275.5], [131.5, 426.0], [336.0, 424.0], [60.5, 422.0], [570.5, 273.5], [102.0, 238.0], [130.0, 426.0], [575.5, 289.5], [95.5, 421.0], [586.5, 310.5], [145.0, 229.0], [130.5, 229.0], [74.0, 424.0], [577.0, 219.5], [85.0, 226.0], [63.5, 421.0], [47.5, 425.0], [213.0, 358.0], [245.0, 374.0], [241.0, 358.0], [572.0, 292.0], [573.0, 297.0], [229.0, 346.0], [361.5, 481.5], [431.0, 430.0], [424.5, 430.0], [418.5, 525.0], [510.5, 332.5], [155.5, 241.0], [558.0, 280.0], [565.0, 285.0], [569.0, 277.0], [120.5, 418.0], [131.0, 424.0], [340.0, 424.0], [95.5, 421.0], [133.5, 238.0], [105.5, 238.0], [146.5, 229.0], [145.0, 229.0], [131.0, 229.0], [234.0, 522.0], [74.0, 424.0], [85.0, 226.0], [583.0, 222.0], [212.0, 359.0], [454.0, 430.0], [573.5, 296.5], [362.0, 482.0], [241.0, 361.0], [430.0, 430.0], [418.5, 524.0], [509.0, 333.0], [157.0, 241.0], [557.0, 280.0], [565.0, 285.0], [568.0, 278.0], [572.0, 271.0], [122.5, 418.0], [340.0, 424.0], [96.0, 421.0], [558.0, 285.0], [107.5, 238.0], [580.5, 282.5], [600.5, 308.0], [120.5, 229.0], [394.0, 502.0], [607.5, 319.5], [146.0, 230.0], [236.0, 526.5], [85.0, 226.0], [242.0, 374.0], [232.0, 363.0], [575.0, 289.0], [576.0, 294.0], [580.5, 282.5], [601.0, 307.0], [239.0, 360.0], [393.5, 501.5], [239.0, 359.0], [162.5, 243.5], [125.0, 418.0], [555.0, 280.0], [565.0, 285.0], [566.0, 280.0], [126.5, 418.0], [131.0, 421.0], [340.0, 424.0], [318.5, 424.0], [333.0, 424.0], [556.0, 285.0], [111.5, 238.0], [116.5, 229.0], [610.5, 294.5], [342.5, 441.5], [130.5, 229.0], [117.0, 229.0], [241.5, 536.5], [42.0, 427.0], [49.0, 428.0], [583.0, 214.0], [188.5, 383.5], [454.0, 430.0], [242.0, 374.0], [581.5, 288.5], [583.5, 282.5], [610.5, 290.5], [239.0, 365.5], [393.5, 501.5], [239.0, 359.0], [173.5, 251.5], [549.5, 280.0], [565.0, 285.0], [560.0, 280.0], [132.0, 418.0], [131.0, 421.0], [342.0, 439.5], [550.5, 285.0], [122.5, 238.0], [260.5, 408.5], [254.5, 382.5], [574.0, 195.5], [117.0, 229.0], [244.0, 536.0], [50.5, 424.0], [586.0, 216.0], [250.5, 386.5], [454.0, 430.0], [242.0, 374.0], [610.5, 281.5], [239.0, 370.5], [238.0, 357.5], [393.5, 501.5], [173.5, 251.5], [565.0, 285.0], [137.0, 418.0], [131.0, 421.0], [574.0, 198.0], [161.0, 407.5], [117.5, 229.0], [43.0, 424.0], [586.0, 214.0], [577.0, 219.5], [583.0, 207.5], [583.0, 194.5], [163.5, 407.5], [454.0, 430.0], [463.0, 430.0], [242.0, 374.0], [238.0, 361.0], [173.5, 251.5], [158.5, 241.5], [565.0, 285.0], [139.0, 418.0], [131.0, 421.0], [95.5, 421.0], [345.5, 424.0], [574.0, 200.0], [220.5, 372.0], [149.5, 241.5], [117.0, 229.0], [43.0, 424.0], [577.0, 219.5], [583.0, 194.5], [506.0, 280.0], [232.0, 365.0], [211.5, 361.5], [173.5, 251.5], [149.5, 241.5], [159.5, 241.5], [137.5, 418.0], [142.5, 421.0], [565.0, 285.0], [559.5, 280.0], [253.5, 531.0], [140.0, 418.0], [131.0, 421.0], [96.0, 421.0], [574.0, 201.0], [369.5, 424.0], [221.5, 360.0], [577.0, 208.5], [117.0, 229.0], [577.0, 219.5], [577.0, 208.5], [164.0, 409.5], [492.0, 280.0], [232.0, 366.5], [369.5, 424.0], [173.5, 251.5], [151.0, 241.5], [160.5, 241.5], [139.0, 418.0], [144.0, 421.0], [565.0, 285.0], [141.0, 418.0], [131.0, 421.0], [340.0, 424.0], [95.5, 421.0], [574.0, 202.0], [46.0, 224.0], [57.5, 427.0], [149.5, 241.5], [577.0, 219.5], [577.0, 216.0], [166.5, 411.5], [505.5, 280.0], [523.5, 280.0], [454.0, 430.0], [242.0, 374.0], [241.0, 372.0], [238.0, 380.0], [362.0, 424.0], [173.5, 251.5], [158.0, 241.5], [168.0, 246.0], [154.5, 241.5], [151.0, 418.0], [131.0, 421.0], [340.0, 424.0], [57.5, 427.0], [513.0, 280.0], [574.0, 209.5], [76.5, 229.0], [519.5, 280.0], [165.5, 248.0], [574.5, 294.5], [366.0, 441.5], [77.0, 229.0], [577.0, 219.5], [577.0, 220.0], [145.0, 421.0], [166.5, 411.5], [506.0, 280.0], [516.5, 280.0], [454.0, 430.0], [476.5, 430.0], [174.5, 410.5], [596.5, 249.5], [238.0, 388.0], [361.0, 439.0], [162.5, 243.5], [172.5, 250.5], [169.0, 250.0], [546.5, 280.0], [571.0, 291.0], [131.0, 421.0], [340.0, 424.0], [57.5, 427.0], [574.0, 213.5], [595.0, 235.5], [345.5, 424.0], [108.5, 418.0], [165.5, 248.0], [153.5, 421.0], [581.5, 280.5], [59.5, 433.0], [76.5, 229.0], [156.0, 424.0], [136.0, 424.0], [517.0, 280.0], [454.0, 430.0], [242.0, 374.0], [439.5, 310.0], [453.0, 295.0], [174.5, 406.5], [176.5, 404.5], [595.0, 241.5], [238.0, 396.0], [203.5, 389.5], [166.5, 244.5], [176.0, 254.0], [169.0, 250.0], [581.5, 280.5], [567.0, 287.0], [131.0, 421.0], [340.0, 424.0], [78.5, 421.0], [57.5, 427.0], [59.5, 433.0], [574.0, 217.5], [57.5, 217.5], [548.0, 284.5], [54.5, 228.5], [549.0, 285.0], [422.5, 427.0], [217.0, 412.5], [255.5, 401.5], [50.0, 437.5], [256.5, 388.5], [222.5, 372.5], [654.0, 410.0], [226.5, 372.5], [653.5, 410.5], [57.5, 427.0], [54.0, 430.0], [564.5, 265.0], [610.0, 191.5], [228.0, 374.0], [595.0, 214.0], [580.0, 217.5], [121.0, 424.0], [122.0, 424.0], [205.5, 424.0], [454.0, 430.0], [238.5, 374.0], [228.5, 374.0], [250.0, 385.5], [132.0, 418.0], [124.0, 418.0], [610.0, 192.0], [238.0, 426.0], [225.0, 363.0], [247.0, 401.0], [434.0, 430.0], [527.5, 425.0], [173.5, 251.5], [131.0, 421.0], [340.0, 424.0], [57.5, 427.0], [60.5, 421.0], [60.0, 427.0], [92.5, 427.0], [198.0, 280.5], [595.0, 195.5], [595.0, 198.5], [592.0, 220.0], [114.5, 424.0], [89.0, 427.0], [571.0, 272.5], [454.0, 430.0], [452.5, 430.0], [244.0, 386.0], [124.5, 418.0], [610.0, 192.5], [442.5, 430.0], [131.0, 421.0], [340.0, 424.0], [57.5, 427.0], [66.5, 421.0], [595.0, 195.5], [142.5, 421.0], [199.5, 284.5], [195.0, 272.0], [80.5, 424.0], [307.5, 466.0], [598.0, 213.0], [90.5, 418.0], [123.5, 430.0], [34.0, 431.0], [144.0, 431.0], [583.0, 191.0], [592.0, 188.0], [135.5, 421.0], [152.0, 424.0], [308.0, 466.0], [91.0, 418.0], [474.0, 430.0], [244.5, 312.5], [146.0, 418.0], [156.5, 412.0], [340.0, 424.0], [57.5, 427.0], [82.5, 421.0], [232.5, 544.0], [598.0, 234.0], [170.0, 248.0], [50.5, 424.0], [51.5, 430.0], [39.5, 430.0], [57.5, 426.5], [57.5, 421.0], [118.5, 424.0], [61.5, 418.0], [592.0, 180.0], [65.5, 427.0], [51.0, 424.0], [48.0, 425.0], [598.0, 234.0], [118.5, 424.0], [91.0, 418.0], [238.0, 486.0], [216.5, 312.5], [260.5, 312.5], [481.0, 280.0], [145.0, 427.0], [208.0, 345.5], [90.5, 421.0], [60.5, 421.0], [57.5, 422.0], [40.0, 425.0], [36.5, 431.5], [37.5, 425.5], [150.5, 239.0], [214.0, 500.5], [300.5, 287.0], [260.5, 459.0], [110.0, 424.0], [118.0, 424.0], [247.0, 518.0], [214.0, 499.5], [468.0, 280.0], [208.0, 323.5], [63.0, 421.0], [148.0, 235.0], [45.5, 424.0], [40.0, 436.0], [55.0, 418.0], [45.5, 430.0], [109.5, 421.0], [58.5, 427.0], [307.5, 283.5], [238.0, 500.0], [247.0, 518.0], [467.0, 280.0], [176.5, 398.5], [63.5, 421.0], [40.0, 436.0], [133.5, 427.0], [187.0, 397.0], [554.0, 310.5], [247.0, 505.5], [59.5, 433.0], [583.0, 192.5], [467.5, 280.0], [321.0, 280.0], [260.5, 459.0], [62.0, 421.0], [238.0, 514.0], [247.0, 506.0], [270.0, 342.0], [178.0, 398.5], [199.5, 391.0], [180.0, 393.5], [57.5, 427.0], [70.0, 421.0], [386.5, 280.0], [454.5, 280.0], [47.0, 436.0], [84.5, 421.0], [290.0, 350.0], [205.0, 291.5], [79.0, 434.0], [87.5, 424.0], [84.5, 424.0], [329.5, 280.0], [378.5, 424.0], [551.0, 315.0], [247.0, 506.0], [186.5, 388.5], [205.5, 291.5], [57.5, 427.0], [78.5, 421.0], [446.0, 280.0], [88.5, 424.0], [247.0, 506.0], [79.0, 421.0], [75.0, 421.0], [514.5, 354.5], [247.5, 344.0], [83.5, 427.0], [392.0, 424.0], [378.5, 424.0], [229.0, 515.5], [294.5, 359.5], [184.5, 390.5], [208.0, 296.5], [80.5, 421.0], [76.0, 421.0], [70.5, 430.0], [247.0, 505.5], [294.5, 360.5], [76.5, 421.0], [184.0, 472.0], [596.5, 298.5], [250.0, 469.5], [345.5, 280.0], [354.5, 280.0], [124.5, 421.0], [66.0, 427.0], [305.5, 362.0], [345.0, 280.0], [352.0, 280.0], [175.5, 402.5], [199.5, 391.0], [124.5, 421.0], [77.0, 430.0], [354.0, 280.0], [119.5, 421.0], [117.5, 424.0], [187.5, 409.5], [114.5, 430.0], [57.0, 427.0], [396.0, 280.0], [395.0, 280.0], [172.5, 244.5], [183.0, 412.0], [229.0, 548.0], [303.5, 363.5], [171.5, 406.5], [199.5, 391.0], [124.0, 421.0], [120.0, 421.0], [138.5, 433.0], [48.0, 427.0], [259.5, 473.5], [184.0, 409.0], [176.5, 416.5], [168.5, 432.5], [305.5, 363.5], [533.0, 405.0], [124.5, 421.0], [120.0, 421.0], [114.5, 430.0], [151.0, 435.0], [136.0, 432.0], [82.5, 421.0], [519.0, 378.5], [583.0, 191.0], [109.0, 424.0], [124.0, 421.0], [134.0, 431.0], [120.0, 421.0], [114.5, 430.0], [519.5, 379.5], [583.0, 191.0], [106.0, 424.0], [396.0, 280.0], [241.0, 490.5], [167.5, 421.0], [377.5, 280.0], [173.5, 245.5], [124.5, 421.0], [127.5, 427.5], [120.5, 421.0], [138.5, 424.0], [520.0, 386.5], [128.0, 421.0], [148.5, 421.0], [93.0, 421.0], [153.0, 421.0], [99.0, 421.0], [128.0, 421.0], [583.0, 191.0], [152.5, 421.0], [341.0, 325.0], [378.0, 280.0], [277.5, 274.5], [148.0, 427.5], [526.5, 400.0], [584.0, 166.0], [583.0, 191.0], [583.5, 166.5], [106.0, 424.0], [378.5, 424.0], [128.0, 421.0], [127.5, 427.5], [125.0, 430.0], [378.5, 280.0], [529.0, 406.5], [148.0, 427.5], [129.5, 424.0], [585.0, 161.5], [123.5, 421.0], [583.0, 173.0], [577.0, 166.0], [112.0, 223.0], [369.5, 313.5], [137.5, 224.5], [95.5, 430.0], [148.0, 427.5], [583.0, 170.5], [96.0, 424.0], [142.0, 424.0], [409.5, 280.0], [137.0, 223.5], [127.5, 427.5], [272.5, 274.0], [148.0, 427.5], [95.5, 424.0], [87.0, 427.0], [378.5, 424.0], [121.0, 424.0], [124.0, 421.0], [494.5, 430.0], [372.0, 313.0], [503.5, 439.0], [127.5, 427.5], [94.5, 424.0], [85.5, 427.0], [120.5, 424.0], [496.0, 430.0], [344.0, 280.0], [127.5, 427.5], [148.5, 421.0], [515.0, 425.5], [78.5, 427.0], [515.0, 426.0], [99.5, 427.0], [127.5, 427.5], [404.5, 310.0], [259.0, 240.5], [164.0, 410.5], [90.5, 430.0], [180.0, 398.0], [148.5, 421.0], [467.5, 280.0], [533.0, 423.0], [396.5, 310.0], [186.5, 391.5], [148.5, 421.0], [480.5, 280.0], [91.0, 430.0], [479.5, 280.0], [241.5, 227.5], [235.0, 210.0], [235.0, 220.5], [454.5, 295.0], [278.0, 276.0], [157.5, 437.0], [480.5, 280.0], [52.5, 424.0], [456.0, 295.0], [380.5, 500.5], [436.5, 310.0], [251.0, 254.0], [462.5, 502.5], [244.0, 253.5], [240.0, 246.0], [243.5, 254.0], [506.0, 280.0], [238.5, 244.5], [271.5, 321.5], [242.5, 254.0], [506.5, 280.0], [568.0, 353.5], [421.5, 524.5], [35.0, 421.0], [242.0, 254.0], [380.5, 313.0], [235.0, 238.5], [229.0, 147.0], [225.5, 231.5], [221.0, 227.0], [253.0, 332.0], [74.5, 430.0], [553.5, 291.0], [406.5, 310.0], [444.5, 535.5], [575.0, 292.5], [570.5, 295.5], [636.5, 421.0], [534.5, 291.0], [451.5, 525.5], [346.5, 481.0], [395.5, 515.5], [522.5, 280.0], [538.5, 295.0], [421.5, 524.5], [540.0, 280.0], [459.5, 315.0], [74.5, 430.0], [413.0, 541.0], [504.5, 280.0], [560.0, 275.5], [417.5, 533.0], [128.0, 226.0], [534.5, 292.5], [392.5, 310.0], [421.5, 524.5], [426.5, 310.0], [110.5, 430.0], [443.0, 310.0], [426.5, 310.0], [445.5, 295.0], [583.0, 247.0], [443.5, 310.0], [451.0, 295.0], [412.0, 310.0], [583.0, 234.5], [564.5, 303.5], [563.0, 303.5], [580.0, 206.5], [577.0, 424.5], [472.0, 319.5], [483.0, 325.5], [386.5, 295.0], [231.0, 524.0], [550.5, 331.0], [217.5, 520.5], [502.0, 344.0], [80.5, 424.0], [577.5, 303.5], [564.5, 297.0], [291.0, 280.0], [673.0, 397.0], [580.5, 310.0], [279.0, 280.0], [583.0, 222.5], [257.5, 263.5], [251.5, 257.5], [583.0, 211.5], [625.5, 426.5], [626.0, 425.5], [568.0, 369.5], [610.0, 430.0], [251.5, 522.0], [639.0, 419.0], [253.0, 522.0], [178.0, 220.0], [643.0, 415.0], [652.0, 406.0], [653.5, 404.5], [656.0, 402.0], [148.0, 214.0], [130.0, 214.0], [111.0, 214.0], [604.0, 302.5], [564.0, 296.0], [580.5, 276.5], [62.5, 214.0], [55.5, 214.0], [604.0, 211.0], [604.0, 201.5], [505.5, 280.0], [589.0, 189.0], [589.0, 182.5], [277.5, 392.5], [589.0, 165.5], [260.5, 392.5], [259.5, 392.5], [589.0, 250.0], [641.0, 429.0], [267.5, 273.5], [580.0, 253.5], [117.5, 424.0], [49.5, 225.0], [171.0, 413.0], [211.0, 346.5], [282.0, 283.0], [58.5, 233.0], [67.0, 235.0], [58.5, 235.0], [584.5, 322.5], [588.0, 312.0], [588.0, 312.0], [606.0, 228.5], [214.0, 496.5], [63.5, 433.0], [240.5, 173.0], [228.0, 169.5], [227.5, 169.5], [473.0, 492.0], [592.0, 171.5], [586.0, 294.0], [77.0, 229.0], [459.5, 313.0], [568.0, 297.5], [597.0, 321.0], [597.0, 321.0], [241.0, 241.5], [238.0, 230.0], [564.0, 295.5], [238.0, 179.5]]



matrice = np.zeros((ecranx // taillecarre, ecranx // taillecarre))
for i in range(len(listeposcontact)):
    matrice[int(listeposcontact[i][1] // taillecarre), int(listeposcontact[i][0] // taillecarre)] += 200


ax = sns.heatmap(matrice)
plt.show()