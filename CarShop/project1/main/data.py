
isLogin = False
isAdmin = False

category = 'All'
user = None

categoryes = [
    'All',
    'Electric',
    'Suvs',
    'Sedans',
    'BMW M'
]

users = [
    {
        'login': 'kostya',
        'password': 'k.1254',
        'img': 'https://vsememy.ru/wp-content/uploads/2022/10/01578386557887983de68d99c7c52b1d-300x300.jpg',
        'isAdmin': False
    },
    {
        'login': 'admin',
        'password': 'admin',
        'img': 'https://media.istockphoto.com/id/967305262/ru/%D0%B2%D0%B5%D0%BA%D1%82%D0%BE%D1%80%D0%BD%D0%B0%D1%8F/%D0%BF%D0%BE%D0%BB%D0%B8%D1%86%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-%D0%B7%D0%BD%D0%B0%D1%87%D0%BE%D0%BA-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80%D0%B0-%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD-%D0%BF%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BD%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BA%D0%BE%D0%BD%D0%B0.jpg?s=612x612&w=0&k=20&c=0tMk6g-J1SWFUtyOx_SOEwrY472z-96fuAMf2IuL0Hs=',
        'isAdmin': True
    }
]

cars = [
    {
        'name': 'iX Sports Activity Vehicle',
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBI&vehicle=23II&client=byo&paint=P0C1M&fabric=FSBJG&sa=S01LD,S0248,S0319,S0322,S0330,S0407,S0420,S0494,S04AA,S04NB,S05AC,S05AS,S05AZ,S05DM,S06AC,S06AK,S06C4,S06NX,S06U7,S09T8&date=20220705&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 84.100 ,
        'comments': [
            {
                'user': users[0],
                'raiting': 8,
                'comment': 'Interesting model',
            }
        ],
        'about': 'The all-electric SAV setting standards for aerodynamics, technology, and luxury. ',
        'category': 'Electric'
    },
    {
        'name': 'i4 Gran Coupe ',
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=23DD&client=byo&paint=P0C4E&fabric=FKHSW&sa=S01CB,S0255,S0302,S0319,S0322,S03AG,S03DE,S03FF,S0403,S0430,S0431,S0459,S0493,S04AT,S0508,S0534,S0544,S05AC,S05AS,S0676,S06AC,S06AK,S06C4,S06U2,S06WC,S0760,S0775&date=20221102&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 51.400,
        'comments': [
            {
                'user': users[0],
                'raiting': 7,
                'comment': 'Good for everyday driving',
            }
        ],
        'about': 'Cutting-edge all-electric performance in a luxurious four-door sports car. ',
        'category': 'Electric'
    },
    {
        'name': 'i7 Sedan',
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=237Q&client=byo&paint=P0300&fabric=FVCSW&sa=S01F7,S0302,S0319,S0407,S0416,S043D,S0465,S046A,S04A2,S04FL,S04FM,S04NR,S04V1,S05AS,S05DM,S06AC,S06AK,S06C4,S06NX,S06U3,S06U7,S0775,S07M7&date=20220702&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 119.300 ,
        'comments': [
            {
                'user': users[0],
                'raiting': 5,
                'comment': 'price is so big :(',
            }
        ],
        'about': 'The all-electric luxury sedan with executive style. ',
        'category': 'Electric'
    },
    {
        'name': 'X1 Sports Activity Vehicle ',
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=23XB&client=byo&paint=P0C5Y&fabric=FKHSW&sa=S01EG,S02TF,S0302,S03AT,S03MB,S0420,S0459,S04AT,S04NW,S05A4,S05AC,S05AS,S05DM,S06AC,S06AK,S06C4,S06CP,S06WC,S0775,S07HW,S09T5&date=20220705&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 38.600 ,
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'My the best choise!',
            }
        ],
        'about': 'The all-new, rugged SAV that is always ready for adventure. ',
        'category': 'Suvs'
    },
    {
        'name': "X3 Sports Activity Vehicle ",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=23XQ&client=byo&paint=P0A90&fabric=FKHG7&sa=S01X8,S0255,S02TB,S0302,S0319,S03AG,S0420,S0423,S0430,S0431,S0459,S0481,S0493,S04K1,S04U0,S04UR,S0508,S0534,S0552,S05AC,S05AS,S05AV,S0676,S06AC,S06AK,S06C4,S06U2,S06WB,S0775&date=20220802&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 45.400,
        'comments': [
            {
                'user': users[0],
                'raiting': 9,
                'comment': 'Love this car',
            }
        ],
        'about': 'The versatile four-door SAV perfect for active lifestyles. ',
        'category': 'Suvs'
    },
    {
        'name': "X4 Sports Activity Coupe ",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=23XR&client=byo&paint=P0C3C&fabric=FKHSW&sa=S01X8,S0225,S02TB,S0302,S0319,S03AG,S0402,S0420,S0423,S0430,S0459,S0481,S0493,S04K1,S04U0,S04UR,S0534,S0552,S05AC,S05AS,S05AV,S0676,S06AC,S06AK,S06C4,S06U3,S0775&date=20220802&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 53.400,
        'comments': [
            {
                'user': users[0],
                'raiting': 5,
                'comment': 'So-so',
            }
        ],
        'about': 'The coupe-inspired adventurer of the X family. ',
        'category': 'Suvs'
    },
    {
        'name': "3 Series Sedan",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=233Y&client=byo&paint=P0C4P&fabric=FKHG7&sa=S01CB,S01PL,S0248,S02TB,S0302,S0319,S0322,S032X,S0337,S03AG,S03DZ,S0403,S0430,S0431,S0459,S0465,S0481,S0493,S04LN,S04UR,S0508,S0534,S0544,S05AC,S05AS,S0676,S06AC,S06AK,S06C4,S06NS,S06U3,S0704,S0710,S0715,S0754,S0760,S0775&date=20220705&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 42.300,
        'comments': [
            {
                'user': users[0],
                'raiting': 4,
                'comment': 'Not surprised',
            }
        ],
        'about': 'The four-door sports sedan that started it all. ',
        'category': 'Sedans'
    },
    {
        'name': "4 Series Coupe ",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=234B&client=byo&paint=P0C31&fabric=FKHKC&sa=S01CB,S01PU,S02TB,S0302,S0319,S0322,S0337,S033B,S03BE,S03DZ,S03M2,S03MF,S0403,S0430,S0431,S0459,S0493,S04KL,S04UR,S0508,S0534,S0544,S05A1,S05AC,S05AS,S05AV,S0676,S06AC,S06AK,S06C4,S06U2,S06WB,S0704,S0710,S0715,S0754,S0760,S0775,S07M9&date=20220705&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 47.400 ,
        'comments': [
            {
                'user': users[0],
                'raiting': 6,
                'comment': 'a little disappointed',
            }
        ],
        'about': 'An edgy, sleek reimagining of the two-door coupe. ',
        'category': 'Sedans'
    },
    {
        'name': "M2 Coupe",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=232R&client=byo&paint=P0C6E&fabric=FMANL&sa=S01E6,S01MB,S02MA,S02VF,S0302,S0319,S0322,S03MF,S0403,S0430,S0431,S043A,S0459,S0493,S0494,S04AT,S04GQ,S04UR,S0508,S0534,S0544,S0552,S05AC,S05AS,S05DC,S0688,S06AC,S06AK,S06C4,S06CP,S06U2,S06WC,S0712,S0760,S0775,S07M9&date=20221206&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 62.200,
        'comments': [
            {
                'user': users[0],
                'raiting': 10,
                'comment': 'Perfect classic!',
            }
        ],
        'about': 'A high-performance version of the already sporty two-door coupe. ',
        'category': 'BMW M'
    },
    {
        'name': "M3 Sedan",
        'img': 'https://cache.bmwusa.com/cosy.arox?pov=walkaround&brand=WBBM&vehicle=23TN&client=byo&paint=P0C4G&fabric=FLKSW&sa=S01T8,S0302,S0319,S0322,S03MQ,S0430,S0431,S0459,S0493,S0494,S04LN,S0508,S0534,S0544,S05AC,S05AS,S0688,S06AC,S06AK,S06C4,S06U2,S06WC,S0712,S0760,S0775&date=20220705&angle=40&quality=65&sharp=100&resp=png&BKGND=TRANSPARENT&width=2000',
        'price': 72.800,
        'comments': [
            {
                'user': users[0],
                'raiting': 9,
                'comment': 'Greate speed',
            }
        ],
        'about': 'The ultimate M-tuned version of the iconic 3 Series sports sedan. ',
        'category': 'BMW M'
    },
]

def GetCarByName(name: str):
    for car in cars:
        if(car['name'] == name):
            return car
    return None
