"""

translator='bing' - TOP !!!
translator='yandex' - через время (ограниченно по запросам в *минуту
google it's shiiit
alibaba медленный и ошибочный
itranslate медленный, но рабочий, есть просечки


import translators as ts


class BDog(object):
    def transla(self, text, a1='bing', a2='en', a3='ru'):
        try:
            tx = ts.translate_text(text, translator=a1, from_language=a2, to_language=a3)
            return tx
        except:
            return "Переводчик оказался пидором"
asd = BDog()

print(asd.transla("Fuck you asshole"))
"""
