from dataclasses import dataclass

@dataclass
class MandarinWord:
    hanzi: str
    pinyin: str
    meaning: str

dictionary = [
    MandarinWord("的","de","of; possessive particle"),
    MandarinWord("一", "yī", "one"),
    MandarinWord("是", "shì", "to be"),
    MandarinWord("不", "bù", "no, not"),
    MandarinWord("了", "le", "completed action marker"),
    MandarinWord("人", "rén", "person"),
    MandarinWord("我", "wǒ", "I, me"),
    MandarinWord("在", "zài", "at, exist"),
    MandarinWord("有", "yǒu", "to have"),
    MandarinWord("他", "tā", "he, him"),
    MandarinWord("这", "zhè", "this"),
    MandarinWord("中", "zhōng", "middle, center"),
    MandarinWord("大", "dà", "big"),
    MandarinWord("来", "lái", "to come"),
    MandarinWord("上", "shàng", "above, up"),
    MandarinWord("国", "guó", "country"),
    MandarinWord("个", "gè", "general classifier"),
    MandarinWord("到", "dào", "to arrive"),
    MandarinWord("说", "shuō", "to speak, say"),
    MandarinWord("们", "men", "plural marker for pronouns"),
    MandarinWord("为", "wèi", "for, on behalf of"),
    MandarinWord("子", "zǐ", "child, son"),
    MandarinWord("和", "hé", "and"),
    MandarinWord("你", "nǐ", "you"),
    MandarinWord("地", "de", "earth; -ly adverb marker"),
    MandarinWord("出", "chū", "to go out"),
    MandarinWord("道", "dào", "way, path"),
    MandarinWord("也", "yě", "also"),
    MandarinWord("时", "shí", "time"),
    MandarinWord("年", "nián", "year"),
    MandarinWord("得", "dé", "to get, obtain"),
    MandarinWord("就", "jiù", "just, simply"),
    MandarinWord("那", "nà", "that"),
    MandarinWord("要", "yào", "to want, need"),
    MandarinWord("下", "xià", "down, below"),
    MandarinWord("以", "yǐ", "with, by means of"),
    MandarinWord("生", "shēng", "to be born, life"),
    MandarinWord("会", "huì", "can, able to"),
    MandarinWord("自", "zì", "self"),
    MandarinWord("着", "zhe", "continuing progress or state"),
    MandarinWord("去", "qù", "to go"),
    MandarinWord("之", "zhī", "literary equivalent of '的'"),
    MandarinWord("过", "guò", "to pass"),
    MandarinWord("家", "jiā", "home, family"),
    MandarinWord("学", "xué", "to study, learn"),
    MandarinWord("对", "duì", "correct; to, toward"),
    MandarinWord("可", "kě", "can, may"),
    MandarinWord("她", "tā", "she, her"),
    MandarinWord("里", "lǐ", "inside"),
    MandarinWord("后", "hòu", "after, behind"),
    MandarinWord("小", "xiǎo", "small"),
    MandarinWord("么", "me", "interrogative suffix"),
    MandarinWord("心", "xīn", "heart, mind"),
    MandarinWord("多", "duō", "many, much"),
    MandarinWord("天", "tiān", "sky, heaven, day"),
    MandarinWord("而", "ér", "and, yet"),
    MandarinWord("能", "néng", "can, be able to"),
    MandarinWord("好", "hǎo", "good"),
    MandarinWord("都", "dōu", "all, both"),
    MandarinWord("然", "rán", "correct; so, like that"),
    MandarinWord("没", "méi", "not, have not"),
    MandarinWord("日", "rì", "sun, day"),
    MandarinWord("于", "yú", "in, at, to"),
    MandarinWord("起", "qǐ", "to rise, to start"),
    MandarinWord("还", "hái", "still, also"),
    MandarinWord("发", "fā", "to send, to emit"),
    MandarinWord("成", "chéng", "to become"),
    MandarinWord("事", "shì", "thing, matter"),
    MandarinWord("只", "zhǐ", "only"),
    MandarinWord("作", "zuò", "to do, to make"),
    MandarinWord("当", "dāng", "to be, to act as"),
    MandarinWord("想", "xiǎng", "to think"),
    MandarinWord("看", "kàn", "to look"),
    MandarinWord("文", "wén", "language, culture"),
    MandarinWord("无", "wú", "without, none"),
    MandarinWord("开", "kāi", "to open"),
    MandarinWord("手", "shǒu", "hand"),
    MandarinWord("十", "shí", "ten"),
    MandarinWord("用", "yòng", "to use"),
    MandarinWord("主", "zhǔ", "main, primary"),
    MandarinWord("行", "xíng", "to go, to travel"),
    MandarinWord("方", "fāng", "direction, method"),
    MandarinWord("又", "yòu", "again"),
    MandarinWord("如", "rú", "like, as"),
    MandarinWord("前", "qián", "front, before"),
    MandarinWord("所", "suǒ", "place; (used before verb)"),
    MandarinWord("本", "běn", "origin, book"),
    MandarinWord("见", "jiàn", "to see"),
    MandarinWord("经", "jīng", "to pass through"),
    MandarinWord("头", "tóu", "head"),
    MandarinWord("面", "miàn", "face, surface"),
    MandarinWord("公", "gōng", "public"),
    MandarinWord("同", "tóng", "same, together"),
    MandarinWord("三", "sān", "three"),
    MandarinWord("已", "yǐ", "already"),
    MandarinWord("老", "lǎo", "old"),
    MandarinWord("从", "cóng", "from, to follow"),
    MandarinWord("动", "dòng", "to move"),
    MandarinWord("两", "liǎng", "two (used before classifier)"),
    MandarinWord("长", "cháng", "long"),
    MandarinWord("知", "zhī", "to know"),
    MandarinWord("民", "mín", "people"),
    MandarinWord("样", "yàng", "appearance, kind"),
    MandarinWord("现", "xiàn", "to appear, current"),
    MandarinWord("分", "fēn", "to divide, minute"),
    MandarinWord("生", "shēng", "life, to be born"),
    MandarinWord("经", "jīng", "already; classic"),
]

def gbk_encoding(array):
    encoded = {}
    for word in array:
        gbk_bytes = word.hanzi.encode('gbk')
        if len(gbk_bytes) == 1:
            val = gbk_bytes[0]
        else:
            val = (gbk_bytes[0] << 8) | gbk_bytes[1]
        encoded[val] = word
    return encoded

hash_table = gbk_encoding(dictionary)

print("Mandarin-English Dictionary")
target=input("Input a Han Zi (to end program input no) : ")

while (target!="no"):
    target_gbk=target.encode('gbk')
    target_val = (target_gbk[0] << 8) | target_gbk[1]
    if target_val in hash_table:
        result = hash_table[target_val]
        print(f"Pin Yin : {result.pinyin}")
        print(f"Meaning : {result.meaning}\n")
    else:
        print(target,"Not found\n")

    target=input("Input a Han Zi (to end program input no) : ")