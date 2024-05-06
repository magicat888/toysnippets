import random

# Example dictionary of restaurants
restaurants = {
    'McDonald': {'address': '皇后大道中37號余道生大廈地庫', 'cuisine': '快餐店', 'weight': 1},
    '永樂園': {'address': '中環昭隆街19號地舖', 'cuisine': '茶餐廳', 'weight': 1},
    '郁鍵快餐': {'address': '上環太平山街6號寶雲樓地下A號舖', 'cuisine': '茶餐廳', 'weight': 1},
    '牛車水海南雞專門店': {'address': '中環機利文新街30號地舖', 'cuisine': '中餐', 'weight': 1},
    '四季常餐': {'address': '中環德輔道中88號地舖', 'cuisine': '茶餐廳', 'weight': 1},
    '九頭鳥米線': {'address': '中環域多利皇后街4號利隆大廈地舖', 'cuisine': '滇菜(雲南)', 'weight': 1},
    '鐵牛台灣牛肉麵': {'address': '中環蘇豪威靈頓街98號翡翠中心2樓A及B號舖', 'cuisine': '台灣菜', 'weight': 1},
    '大戶屋': {'address': '中環皇后大道中139號The L. Place 10樓', 'cuisine': '日本餐', 'weight': 3},
    '健康食品拉麵': {'address': '中環威靈頓街97號威利大廈地下B,C,D號舖', 'cuisine': '日本餐', 'weight': 1},
    '水記': {'address': '中環吉士笠街2號牌檔', 'cuisine': '港式粉麵', 'weight': 1},
    '三多麵食': {'address': '中環威靈頓街85-89號群英商業大廈地下A1號舖', 'cuisine': '港式粉麵', 'weight': 1},
    '筷子記': {'address': '中環皇后大道中139號The L. Place 10樓', 'cuisine': '港式粉麵', 'weight': 0},
    '九記牛腩': {'address': '中環歌賦街21號地舖', 'cuisine': '港式粉麵', 'weight': 1},
    'Five Guys': {'address': '中環皇后大道中38-48號萬年大廈地庫', 'cuisine': '快餐店', 'weight': 1},
    '蘭芳園': {'address': '中環結志街2號地舖', 'cuisine': '港式粉麵', 'weight': 1},    
    '一樂燒鵝': {'address': '中環士丹利街34-38號地舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '盛記': {'address': '中環士丹利街82號地舖', 'cuisine': '大牌檔', 'weight': 1},    
    '亞參雞飯': {'address': '中環威靈頓街174-178號地下低層C號舖', 'cuisine': '新加坡菜', 'weight': 0},    
    '羅富記粥麵專家': {'address': '中環德輔道中140號地舖', 'cuisine': '港式粉麵', 'weight': 1},    
    '快樂蜂': {'address': '中環干諾道中13號歐陸貿易中心地舖', 'cuisine': '快餐店', 'weight': 1},    
    'Délifrance': {'address': '中環德輔道中19號環球大廈1樓174號舖', 'cuisine': '法國菜', 'weight': 1},    
    '權記雲吞麵': {'address': '中環卑利街2號地舖', 'cuisine': '港式粉麵', 'weight': 1},    
    '珍姐海鮮火鍋飯店': {'address': '中環和安里9號地舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '和順記': {'address': '中環威靈頓街112-114號新威大廈地下A號舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '新興美食': {'address': '中環昭隆街9號地下B號舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '美華茶餐廳 ': {'address': '中環鴨巴甸街10號地舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '忠記粥品': {'address': '中環機利文新街32-34號A號舖', 'cuisine': '港式粥品', 'weight': 1},    
    '餃掂手工餃子雲吞專門店': {'address': '中環威靈頓街55號地舖', 'cuisine': '港式粉麵', 'weight': 1},    
    '上環市政大廈熟食中心': {'address': '上環熟食中心', 'cuisine': '茶餐廳', 'weight': 1},    
    '雞功房': {'address': '上環禧利街17-19號普益商業大廈地舖', 'cuisine': '茶餐廳', 'weight': 1},    
    '生記粥品專家 ': {'address': '上環畢街7-9號地舖', 'cuisine': '港式粥品', 'weight': 1},    
    '老上海餛飩舖': {'address': '上環禧利街16號地舖', 'cuisine': '滬菜上海粉麵', 'weight': 1},    
    '勝香園': {'address': '中環美輪街2號排檔', 'cuisine': '大牌檔', 'weight': 1},    
    '○de▽ 鯛白湯らーめん': {'address': '中環鴨巴甸街13號地舖', 'cuisine': '日本餐', 'weight': 1},    
    '新森林焗之專門店 ': {'address': '中環威靈頓街99號威基商業大廈地下D號舖', 'cuisine': '茶餐廳', 'weight': 1},   
    'X': {'address': 'X', 'cuisine': 'X', 'weight': 0},    

    # Add more restaurants as needed
}

def choose_random_restaurants(restaurant_dict, num_choices=30):
    restaurant_names = list(restaurant_dict.keys())
    weights = [restaurant_dict[name]['weight'] for name in restaurant_names]
    selected_restaurants = random.choices(restaurant_names, weights=weights, k=num_choices)
    return selected_restaurants

# Main code
if __name__ == "__main__":
    chosen_restaurants = choose_random_restaurants(restaurants)
    for restaurant_name in chosen_restaurants:
        details = restaurants[restaurant_name]
        print(f"Restaurant: {restaurant_name}")
        print(f"Address: {details['address']}")
        print(f"Cuisine: {details['cuisine']}")
        print("-" * 30)
