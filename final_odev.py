import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as karar

yorumyazandinlemesayisi = karar.Antecedent(np.arange(0, 11, 1), 'yorumu yazacak kisinin sarkiyi dinleme sayisi')
toplamdinlemesayisi = karar.Antecedent(np.arange(0, 101, 1), 'sarki toplam kac kere dinlendi')
lyricdegerlendirme = karar.Antecedent(np.arange(0, 11, 1), 'sozlerin iceriğinin degerlendirilmesi')
reviewpuan = karar.Consequent(np.arange(0, 11, 1), 'toplam puan')

yorumyazandinlemesayisi['yetersiz'] = fuzz.trimf(yorumyazandinlemesayisi.universe, [0, 0, 5])
yorumyazandinlemesayisi['orta'] = fuzz.trimf(yorumyazandinlemesayisi.universe, [0, 5, 10])
yorumyazandinlemesayisi['yorum yapabilir'] = fuzz.trimf(yorumyazandinlemesayisi.universe, [5, 10, 10])

toplamdinlemesayisi['kesfedilmemis'] = fuzz.trimf(toplamdinlemesayisi.universe, [0, 0, 30])
toplamdinlemesayisi['arada radyoda caliyor'] = fuzz.trimf(toplamdinlemesayisi.universe, [10, 30, 60])
toplamdinlemesayisi['global hit'] = fuzz.trimf(toplamdinlemesayisi.universe, [60, 100, 100])

lyricdegerlendirme['manasiz'] = fuzz.trimf(lyricdegerlendirme.universe, [0, 0, 5])
lyricdegerlendirme['siradan anlam'] = fuzz.trimf(lyricdegerlendirme.universe, [5, 5, 7])
lyricdegerlendirme['derin anlam'] = fuzz.trimf(lyricdegerlendirme.universe, [7, 10, 10])

reviewpuan['vasat'] = fuzz.trimf(reviewpuan.universe, [0, 0, 6])
reviewpuan['orta duzey'] = fuzz.trimf(reviewpuan.universe, [0, 4, 7])
reviewpuan['efsanevi'] = fuzz.trimf(reviewpuan.universe, [6, 10, 10])

kural1 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['vasat'] )
kural2 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['vasat'] )
kural3 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['global hit'], reviewpuan['vasat'] )
kural4 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['vasat'] )
kural5 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['orta duzey'] )
kural6 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['orta duzey'] )
kural7 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['orta duzey'] )
kural8 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['orta duzey'] )
kural9 = karar.Rule(yorumyazandinlemesayisi['yetersiz'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['efsanevi'] )
kural10= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['global hit'], reviewpuan['vasat'])
kural11= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['vasat'])
kural12= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['vasat'])
kural13= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['efsanevi'])
kural14= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['orta duzey'])
kural15= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['orta duzey'])
kural16= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['efsanevi'])
kural17= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['efsanevi'])
kural18= karar.Rule(yorumyazandinlemesayisi['yorum yapabilir'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['efsanevi'])
kural19 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['vasat'])
kural20 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['vasat'])
kural21 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['manasiz'] & toplamdinlemesayisi['global hit'], reviewpuan['vasat'])
kural22 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['orta duzey'])
kural23 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['orta duzey'])
kural24 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['siradan anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['efsanevi'])
kural25 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['arada radyoda caliyor'], reviewpuan['efsanevi'])
kural26 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['kesfedilmemis'], reviewpuan['orta duzey'])
kural27 = karar.Rule(yorumyazandinlemesayisi['orta'] & lyricdegerlendirme['derin anlam'] & toplamdinlemesayisi['global hit'], reviewpuan['efsanevi'])

puan_olustur = karar.ControlSystem([kural1, kural2, kural3,kural4,kural5,kural6,kural7,kural8,kural9,kural10,kural11,kural12,kural13,kural14,kural15,kural16,kural17,kural18,kural19,kural20,
kural21,kural22,kural23,kural24,kural25,kural26,kural27])

puan_ = karar.ControlSystemSimulation(puan_olustur)

puan_.input['sarki toplam kac kere dinlendi'] = 55
puan_.input['yorumu yazacak kisinin sarkiyi dinleme sayisi'] = 8
puan_.input['sozlerin iceriğinin degerlendirilmesi'] = 3


puan_.compute()

print(puan_.output['toplam puan'])