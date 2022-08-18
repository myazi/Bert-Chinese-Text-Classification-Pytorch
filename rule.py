# coding: UTF-8
import sys
import re
def rule(predic,title_tag, index2hangye):
	othor_index = len(index2hangye) - 1
	title_ch = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", title_tag)
	if len(title_ch) < 10 or len(title_ch) > 300 :
		#print(str(title_ch) + "\t" + "title_tag is fail")
		return othor_index
	return {
		"房产家居/房产中介": predic
		,"房产家居/装潢装修" : predic
		,"房产家居/家具家居" : predic
		,"教育培训/早教" : predic
		,"教育培训/K12教育/学前教育" : predic
		,"教育培训/K12教育/小初高" : predic
		,"教育培训/学历教育/专科" : predic
		,"教育培训/学历教育/本科" : predic
		,"教育培训/学历教育/研究生" : predic
		,"教育培训/职业培训/司法考试培训" : predic if "培训" in title_tag else othor_index 
		,"教育培训/职业培训/会计培训" : predic
		,"教育培训/职业培训/美容美发培训" : predic
		,"教育培训/职业培训/时装设计培训" : predic
		,"教育培训/职业培训/公务员考试培训" : predic
		,"教育培训/语言培训/英语培训" : predic
		,"教育培训/语言培训/小语种培训" : predic
		,"教育培训/出国留学" : predic
		,"教育培训/国际学校" : predic
		,"教育培训/兴趣培训/书法培训" : predic
		,"教育培训/兴趣培训/美术培训" : predic
		,"教育培训/兴趣培训/艺考" : predic
		,"教育培训/兴趣培训/健身培训" : predic
		,"教育培训/兴趣培训/武术培训" : predic
		,"教育培训/兴趣培训/茶艺培训" : predic
		,"教育培训/兴趣培训/舞蹈培训" : predic
		,"教育培训/兴趣培训/音乐培训" : predic
		,"教育培训/兴趣培训/花艺培训" : predic
		,"教育培训/特殊教育" : predic
		,"教育培训/教育培训综合" : predic
		,"教育培训/教育培训-其他" : predic
		,"交通出行/摩托车" : predic
		,"交通出行/电动车" : predic
		,"交通出行/航铁船" : predic
		,"交通出行/非机动车" : predic
		,"交通出行/便民出行" : predic
		,"交通出行/车辆平台" : predic
		,"交通出行-其他" : predic
		,"交通出行/汽车厂商" : predic
		,"交通出行/汽车经销商" : predic
		,"交通出行/汽配及服务" : predic
		,"游戏/页游端游" : predic
		,"游戏/手机游戏" : predic
		,"游戏/休闲益智" : predic
		,"游戏/游戏平台" : predic
		,"游戏/游戏周边" : predic
		,"游戏/开发服务" : predic
		,"游戏/游戏-其他" : predic
		,"农林牧渔/农业" : predic
		,"农林牧渔/林业" : predic
		,"农林牧渔/渔业" : predic
		,"农林牧渔/畜牧业" : predic
		,"农林牧渔/化肥及农药" : predic
		,"农林牧渔/农林牧渔-其他" : predic
		,"机械设备/通用机械设备" : predic
		,"机械设备/建筑工程机械" : predic
		,"机械设备/清洁及通风设备" : predic
		,"机械设备/机床机械" : predic
		,"机械设备/物流设备" : predic
		,"机械设备/食品机械" : predic
		,"机械设备/机械设备-其他" : predic
		,"机械设备/五金配件" : predic
		,"机械设备/机械设备信息平台" : predic
		,"整形美容/整形美容综合" : predic
		,"整形美容/整形修复外科" : predic
		,"整形美容/皮肤美容" : predic
		,"整形美容/面部整形" : predic
		,"整形美容/美体塑形" : predic
		,"整形美容/纹身" : predici
		,"整形美容/植发" : predic
		,"整形美容/口腔美容" : predic
		,"整形美容/眼科美容" : predic
		,"整形美容/医美服务平台" : predic
		,"整形美容/整形美容-其他" : predic
		,"商务服务/咨询调查" : predic
		,"商务服务/商业检修" : predic
		,"商务服务/检测认证" : predic
		,"商务服务/法律服务" : predic
		,"商务服务/技术服务" : predic
		,"商务服务/拍卖" : predic
		,"商务服务/代理代办" : predic
		,"商务服务/出国移民" : predic
		,"商务服务/签证服务" : predic
		,"商务服务/招聘/人才中介" : predic
		,"商务服务/包装印刷" : predic
		,"商务服务/广告服务" : predic
		,"商务服务/安全安保" : predic
		,"商务服务/商务服务-综合平台" : predic
		,"商务服务/团建拓展" : predic
		,"商务服务/商务服务-其他" : predic
		,"生活服务/开锁配钥" : predic
		,"生活服务/刻章办证" : predic
		,"生活服务/便民回收" : predic
		,"生活服务/便民充值" : predic
		,"生活服务/家政服务" : predic
		,"生活服务/月子中心" : predic
		,"生活服务/居民维修" : predic
		,"生活服务/摄影婚庆" : predic
		,"生活服务/餐饮/小吃培训" : predic
		,"生活服务/餐饮/探店" : predic
		,"生活服务/宠物医院" : predic
		,"生活服务/宠物周边" : predic
		,"生活服务/婚恋相亲" : predic
		,"生活服务/室内娱乐" : predic
		,"生活服务/户外娱乐" : predic
		,"生活服务/体育演出场馆" : predic
		,"生活服务/生活美容" : predic
		,"生活服务/养生保健" : predic
		,"生活服务/文玩收藏" : predic
		,"生活服务心理援助" : predic
		,"生活服务/彩票" : predic
		,"生活服务/生活服务-综合平台" : predic
		,"生活服务/生活服务-其他" : predic
		,"日用消费品/礼品" : predic
		,"日用消费品/日化用品" : predic
		,"日用消费品/一般化妆品" : predic
		,"日用消费品/特殊用途化妆品" : predic
		,"日用消费品/成人用品" : predic
		,"日用消费品/日用消费品-其他" : predic
		,"母婴用品/奶粉" : predic
		,"母婴用品/辅食" : predic
		,"母婴用品/婴儿用品" : predic
		,"母婴用品/孕妇用品" : predic
		,"母婴用品/母婴服饰" : predic
		,"母婴用品/母婴用品综合" : predic
		,"母婴用品/母婴用品-其他" : predic
		,"IT/消费电子/手机数码" : predic
		,"IT/消费电子/电脑办公" : predic
		,"IT/消费电子/电器" : predic
		,"IT/消费电子/IT/消费电子交易" : predic
		,"IT/消费电子/IT/消费电子-其他" : predic
		,"旅游服务/旅游局" : predic
		,"旅游服务/景点" : predic
		,"旅游服务/酒店" : predic
		,"旅游服务/旅行社" : predic
		,"旅游服务/商旅票务" : predic
		,"旅游服务/航空公司" : predic
		,"旅游服务/在线旅游" : predic
		,"旅游服务/旅游服务-其他" : predic
		,"箱包服饰/服装鞋帽" : predic
		,"箱包服饰/珠宝饰品" : predic
		,"箱包服饰/眼镜" : predic if "眼" in title_tag or "镜" in title_tag else other_index 
		,"箱包服饰/钟表" : predic
		,"箱包服饰/箱包皮具" : predic
		,"箱包服饰/奢侈品" : predic
		,"医疗服务/妇产科" : predic
		,"医疗服务/男科" : predic
		,"医疗服务/内科" : predic
		,"医疗服务/皮肤科" : predic
		,"医疗服务/外科" : predic
		,"医疗服务/中医科" : predic
		,"医疗服务/耳鼻咽喉科" : predic
		,"医疗服务/眼科" : predic if "眼" in title_tag else other_index
		,"医疗服务/口腔科" : predic if "口" in title_tag else other_index
		,"医疗服务/儿科" : predic
		,"医疗服务/体检科" : predic
		,"医疗服务/精神科" : predic
		,"医疗服务/生殖医学科" : predic
		,"医疗服务/戒毒科" : predic
		,"医疗服务/康复科" : predic
		,"医疗服务/综合医院" : predic
		,"医疗服务/医疗周边服务" : predic
		,"医疗器械/一类医疗器械" : predic
		,"医疗器械/二类、三类医疗器械" : predic
		,"医疗器械/医疗器械-其他" : predic
		,"保健品/药品/药品" : predic
		,"保健品/药品/药房" : predic
		,"保健品/药品/医药电商平台" : predic
		,"保健品/药品/兽药" : predic
		,"保健品/药品/保健品" : predic
		,"文娱传媒/影音动漫" : predic
		,"文娱传媒/传统媒体" : predic
		,"文娱传媒/文书期刊" : predic
		,"文娱传媒/资讯平台" : predic
		,"文娱传媒/视频平台" : predic
		,"文娱传媒/直播平台" : predic
		,"文娱传媒/小说阅读" : predic
		,"文娱传媒/自媒体" : predic
		,"文娱传媒/文娱票务" : predic
		,"文娱传媒/活动演出" : predic
		,"文娱传媒/文娱传媒-其他" : predic
		,"文体器材/办公设备及器械" : predic
		,"文体器材/文教具" : predic
		,"文体器材/办公文教-其他" : predic
		,"文体器材/体育器械" : predic
		,"文体器材/音乐器械" : predic
		,"文体器材/玩具模型" : predic
		,"文体器材/娱乐器械" : predic
		,"文体器材/户外装备" : predic
		,"物流业/普通运输" : predic
		,"物流业/特殊运输" : predic
		,"物流业/物流业-其他" : predic
		,"食品饮料/粮油米面" : predic
		,"食品饮料/生鲜" : predic
		,"食品饮料/速食" : predic
		,"食品饮料/烟酒" : predic
		,"食品饮料/乳制品及乳制品饮料" : predic
		,"食品饮料/休闲零食" : predic
		,"食品饮料/调味品" : predic
		,"食品饮料/饮料冲调" : predic
		,"食品饮料/营养品" : predic
		,"食品饮料/特殊医学用途配方食品" : predic
		,"食品饮料/食品饮料综合" : predic
		,"食品饮料/食品饮料-其他" : predic
		,"金融服务/银行业" : predic
		,"金融服务/证券业" : predic
		,"金融服务/基金业" : predic
		,"金融服务/保险业" : predic
		,"金融服务/期货业" : predic
		,"金融服务/信托业" : predic
		,"金融服务金融征信" : predic
		,"金融服务/外汇类" : predic
		,"金融服务/小额贷款" : predic
		,"金融服务/典当" : predic
		,"金融服务/担保及保理" : predic
		,"金融服务/租赁业" : predic
		,"金融服务/平台中介" : predic
		,"金融服务/第三方支付" : predic
		,"金融服务/网络借贷服务" : predic
		,"金融服务/金融门户网站" : predic
		,"金融服务/金融服务-其他" : predic
		,"软件/多媒体处理" : predic
		,"软件/社交通讯" : predic
		,"软件/商用软件" : predic
		,"软件/实用工具" : predic
		,"软件/软件平台" : predic
		,"商品交易/电商B2B" : predic
		,"商品交易/电商B2C" : predic
		,"商品交易/二类电商" : predic
		,"商品交易/实体零售" : predic
		,"商品交易/商品信息平台" : predic
		,"电子电工/电子器件" : predic
		,"电子电工/仪器仪表" : predic
		,"电子电工/智能制造" : predic
		,"电子电工/电工电气" : predic
		,"通信/电信运营商" : predic
		,"通信/虚拟运营商" : predic
		,"通信/通信及网络设备" : predic
		,"通信/通信-其他" : predic
		,"网络服务/网站建设" : predic
		,"网络服务/域名空间" : predic
		,"网络服务/云服务" : predic
		,"网络服务/系统集成" : predic
		,"网络服务/网络营销" : predic
		,"网络服务/网络服务-其他" : predic
		,"社会公共/政府政务" : predic
		,"社会公共/社会组织" : predic
		,"社会公共/市政建设" : predic
		,"社会公共宗教" : predic
		,"化工及能源/化工原料" : predic
		,"化工及能源/矿产资源" : predic
		,"化工及能源/矿产及化工制品" : predic
		,"化工及能源/消毒产品" : predic
		,"化工及能源/危险化学品" : predic
		,"化工及能源/能源" : predic
		,"化工及能源/污染处理" : predic
		,"化工及能源/废旧回收" : predic
		,"化工及能源/节能" : predic
		,"化工及能源/化工及能源-其他" : predic
		,"招商加盟/招商-餐饮酒店" : predic
		,"招商加盟/招商-教育培训" : predic
		,"招商加盟/招商-服务类" : predic
		,"招商加盟/招商-家居建材" : predic
		,"招商加盟/招商-服装鞋帽" : predic
		,"招商加盟/招商-礼品饰品" : predic
		,"招商加盟/招商-美容化妆" : predic
		,"招商加盟/招商-休闲娱乐" : predic
		,"招商加盟/招商-生活用品" : predic
		,"招商加盟/招商加盟联展平台" : predic
		,"招商加盟/招商-其他" : predic
		,"其他/其他" : predic

		,"家装/园林设计" : predic 	
		,"家装/别墅设计" : predic	
		,"家装/室内装修" : predic
		,"家装/家具设计" : predic if "家" in title_tag else othor_index  	
		,"家装/办公装修" : predic if "办公室" in title_tag and "装" in title_tag else othor_index
		,"家装/民宿酒店" : predic	
		,"家装/装修知识" : predic
		,"家装/室内设计" : predic	
		,"家装/除甲醛" : predic if "甲醛" in title_tag else othor_index
		,"家装/杀虫灭菌" : predic	
		,"家装/园艺" : predic	
		,"家装/人造草坪" : predic	
		,"家装/家用电器" : predic if "家" in title_tag else othor_index	
		,"健康养生/茶叶" : predic if "茶" in "title_tag" and "茶叶蛋" not in title_tag and "小三" not in title_tag and "爱情" not in title_tag else othor_index
		,"旅游住宿/旅游" : predic	
		,"旅游住宿/酒店" : predic if "美食" not in title_tag else othor_index	
		,"美食/探店" : predic	
		,"美食/小吃培训" : predic	
		,"摄影/商业摄影" : predic if "摄影" in title_tag else othor_index  	
		,"摄影/婚纱摄影" : predic if "婚纱" in title_tag else othor_index 
		,"摄影/艺术摄影" : predic if "摄影" in title_tag or "照" in title_tag else othor_index 	
		,"摄影/庆典摄影" : predic	
		,"生活服务/服装" : predic if "服" in title_tag or "装" in title_tag else othor_index	
		,"房地产/新房买卖" : predic if "房" in title_tag else othor_index	
		,"房地产/二手房买卖" : predic if "房" in title_tag else othor_index
		,"房地产/别墅买卖" : predic if "房" in title_tag else othor_index	
		,"房地产/房屋租赁" : predic if "房" in title_tag else othor_index	
		,"房地产/买卖代理看房办证" : predic if "房" in title_tag else othor_index	
		,"婚庆/礼服婚纱" : predic if "婚" in title_tag else othor_index	
		,"婚庆/婚庆策划" : predic if "婚" in title_tag else othor_index	
		,"婚庆/化妆造型" : predic if "妆" in title_tag or "型" in title_tag else othor_index
		,"医美/植发护发" : predic if "发" in title_tag else othor_index	
		,"教育培训/学前教育" : predic 	
		,"教育培训/小初高辅导" : predic	
		,"教育培训/高考辅导" : predic if "星座" not in title_tag else othor_index	
		,"教育培训/成人自考" : predic if "考" in title_tag else othor_index	
		,"教育培训/艺考辅导" : predic if "艺" in title_tag and "考" in title_tag else othor_index	
		,"教育培训/大专辅导" : predic if ("大专" in title_tag or "专科" in title_tag) and "医院" not in title_tag else othor_index
		,"教育培训/本科辅导" : predic	
		,"教育培训/考研辅导" : predic if "考研" in title_tag else othor_index
		,"教育培训/研究生教育" : predic if "影视" not in title_tag and "综艺" not in title_tag and "娱乐" not in title_tag else othor_index	
		,"教育培训/留学教育" : predic	
		,"教育培训/国际学校" : predic	
		,"教育培训/少儿英语培训" : predic	
		,"教育培训/少儿书法美术培训" : predic if "书法" in title_tag or "字" in title_tag or "美术" in title_tag else othor_index	
		,"教育培训/英语等级考试培训" : predic if "英语" in title_tag and "级" in title_tag else othor_index
		,"教育培训/出国英语培训" : predic	
		,"教育培训/小语种培训" : predic	
		,"教育培训/在线教育" : predic	
		,"教育培训/司法考试培训" : predic	
		,"职业培训/会计培训" : predic	
		,"职业培训/美容美发培训" : predic	
		,"职业培训/时装设计培训" : predic if "装" in title_tag else othor_index	
		,"兴趣培训/美术培训" : predic if "美食" in title_tag else othor_index	
		,"兴趣培训/花艺培训" : predic if "花" in title_tag else othor_index	
		,"兴趣培训/健身培训" : predic #if "欢迎大家点亮爱心" not in title_tag else othor_index #欢迎大家点亮爱心	
		,"兴趣培训/体育培训" : predic if "游泳" not in title_tag or ("游泳" in title_tag and "训" in title_tag) else othor_index	
		,"兴趣培训/青少年儿童体能" : predic if "体" in title_tag else othor_index	
		,"兴趣培训/武术培训" : predic if "皇太极" not in title_tag and (title_tag.count("功夫") != 1) else othor_index	
		,"兴趣培训/茶艺培训" : predic if "茶" in title_tag and "茶叶蛋" not in title_tag else othor_index
		,"兴趣培训/舞蹈培训" : predic 	
		,"兴趣培训/音乐培训" : predic	
		,"游戏" : predic	
		,"交通出行/汽车厂商" : predic	
		,"生活服务/文玩收藏" : predic	
		,"其他" : predic	
	}.get(str(index2hangye[predic]),predic)
