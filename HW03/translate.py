from googletrans import Translator

# print(Translator) -> <class 'googletrans.client.Translator'>
# sentence = "좋은 아침이에요"

translator = Translator()

sentence = input("문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요: ")
result = translator.translate(sentence, dest) # 번역되는 언어(fr, ar, vi, de, es, mn, zh-CN, hi)
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang,":",sentence)
print(result.dest,":",result.text)
print("=================================")

'''
sentence = input("번역을 원하는 문장을 입력하세요 : ")
result = Translator.translate(sentence, dest="en")
detect = Translator.detect(sentence)

print("\n============= 번역 결과 ============\n")
print(detect.lang,":", result.origin)
print(result.dest,":", result.text)
print("\n====================================\n")
'''