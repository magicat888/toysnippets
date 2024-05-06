import random

# Example dictionary of restaurants
restaurants = {
    'McDonald': {'address': '皇后大道中37號余道生大廈地庫', 'cuisine': '快餐店'},
    '永樂園': {'address': '中環昭隆街19號地舖', 'cuisine': '茶餐廳'},
    '郁鍵快餐': {'address': '上環太平山街6號寶雲樓地下A號舖', 'cuisine': '茶餐廳'},
    '牛車水海南雞專門店': {'address': '中環機利文新街30號地舖', 'cuisine': '中餐'},
    '四季常餐': {'address': '中環德輔道中88號地舖', 'cuisine': '茶餐廳'},
    '九頭鳥米線': {'address': '中環域多利皇后街4號利隆大廈地舖', 'cuisine': '滇菜(雲南)'},
    '鐵牛台灣牛肉麵': {'address': '中環蘇豪威靈頓街98號翡翠中心2樓A及B號舖', 'cuisine': '台灣菜'},
    '健康食品拉麵': {'address': '中環皇后大道中139號The L. Place 10樓', 'cuisine': '日本餐'},
    '水記': {'address': '中環吉士笠街2號牌檔', 'cuisine': '港式粉麵'},
    '三多麵食': {'address': '中環威靈頓街85-89號群英商業大廈地下A1號舖', 'cuisine': '港式粉麵'},
    '筷子記': {'address': '中環皇后大道中139號The L. Place 10樓', 'cuisine': '港式粉麵'},
    '九記牛腩': {'address': '中環歌賦街21號地舖', 'cuisine': '港式粉麵'},
    'Five Guys': {'address': '中環皇后大道中38-48號萬年大廈地庫', 'cuisine': '快餐店'},
    '蘭芳園': {'address': '中環結志街2號地舖', 'cuisine': '港式粉麵'},    
    '一樂燒鵝': {'address': '中環士丹利街34-38號地舖', 'cuisine': '茶餐廳'},    
    '盛記': {'address': '中環士丹利街82號地舖', 'cuisine': '大牌檔'},    
    '亞參雞飯': {'address': '中環威靈頓街174-178號地下低層C號舖', 'cuisine': '新加坡菜'},    
    '羅富記粥麵專家': {'address': '中環德輔道中140號地舖', 'cuisine': '港式粉麵'},    
    '快樂蜂': {'address': '中環干諾道中13號歐陸貿易中心地舖', 'cuisine': '快餐店'},    
    'Délifrance': {'address': '中環德輔道中19號環球大廈1樓174號舖', 'cuisine': '法國菜'},    
    '權記雲吞麵': {'address': '中環卑利街2號地舖', 'cuisine': '港式粉麵'},    
    '珍姐海鮮火鍋飯店': {'address': '中環和安里9號地舖', 'cuisine': '茶餐廳'},    
    '和順記': {'address': '中環威靈頓街112-114號新威大廈地下A號舖', 'cuisine': '茶餐廳'},    
    '新興美食': {'address': '中環昭隆街9號地下B號舖', 'cuisine': '茶餐廳'},    
    '美華茶餐廳 ': {'address': '中環鴨巴甸街10號地舖', 'cuisine': '茶餐廳'},    
    '忠記粥品': {'address': '中環機利文新街32-34號A號舖', 'cuisine': '港式粥品'},    
    '餃掂手工餃子雲吞專門店': {'address': '中環威靈頓街55號地舖', 'cuisine': '港式粉麵'},    
    '上環市政大廈熟食中心': {'address': '上環熟食中心', 'cuisine': '茶餐廳'},    
    '雞功房': {'address': '上環禧利街17-19號普益商業大廈地舖', 'cuisine': '茶餐廳'},    
    '生記粥品專家 ': {'address': '上環畢街7-9號地舖', 'cuisine': '港式粥品'},    
    '老上海餛飩舖': {'address': '上環禧利街16號地舖', 'cuisine': '滬菜上海粉麵'},    
    '勝香園': {'address': '中環美輪街2號排檔', 'cuisine': '大牌檔'},    
    '○de▽ 鯛白湯らーめん': {'address': '中環鴨巴甸街13號地舖', 'cuisine': '日本餐'},    
    '新森林焗之專門店 ': {'address': '中環威靈頓街99號威基商業大廈地下D號舖', 'cuisine': '茶餐廳'},   
    'X': {'address': 'X', 'cuisine': 'X'},    

    # Add more restaurants as needed
}

# Function to choose a random restaurant from a dictionary
def choose_random_restaurant(restaurant_dict):
    return random.choice(list(restaurant_dict.keys()))

# Main code
if __name__ == "__main__":
    chosen_restaurant = choose_random_restaurant(restaurants)
    details = restaurants[chosen_restaurant]
    print(f"Today's restaurant choice is: {chosen_restaurant}")
    print(f"Address: {details['address']}")
    print(f"Cuisine: {details['cuisine']}")
