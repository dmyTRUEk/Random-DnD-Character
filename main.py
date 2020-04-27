#
# Random DnD NPC:
#

import sys

import random as rnd





from inspect import getframeinfo, stack

def todo (s):
    print(
        '[TODO] at line',
        getframeinfo(stack()[1][0]).lineno,
        ':', s
    )



races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Dragonborn', 'Gnome', 'Halfelf', 'Halfork', 'Tiefling']

classes = ['Bard', 'Barbarian', 'Warrior', 'Wizard', 'Druid', 'Priest', 'Warlock', 'Monk', 'Paladin', 'Rogue', 'Ranger', 'Magician']

names_dwarf = ['Adrick', 'Alberih', 'Barend', 'Baern', 'Brottor', 'Bruenor', 'Vondal', 'Vate', 'Gardain', 'Dain', 'Darrack', 'Delg', 'Kildrak', 'Morgan', 'Orsick', 'Oscar', 'Ranhrim', 'Rurick', 'Taklinn', 'Toradin', 'Tordeck', 'Torinn', 'Travok', 'Traubon', 'Ulfgar', 'Fargrim', 'Flint', 'Harbeck', 'Eberck', 'Einkil\'',
    'Artin', 'Bardrin', 'Vistra', 'Gunnolda', 'Gudris', 'Dangal', 'Diessa', 'Ilde', 'Katra', 'Kristid', 'Liftrassa', 'Mardred', 'Odlhild', 'Risvin', 'Sannl', 'Torbera', 'Torgga', 'Falkrunn', 'Finellen', 'Heldja', 'Hlin', 'Eldet', 'Ember']
    
names_elf = ['Ara', 'Brin', 'Val\'', 'Del\'', 'Innil', 'Lael\'', 'Mella', 'Nail\'', 'Naeris', 'Rael\'', 'Rinn', 'Si', 'Sillin', 'Tia', 'Fann', 'Faen', 'Arin',
    'Adran', 'Aramil\'', 'Arannis', 'Aust', 'Aelar', 'Bairo', 'Berrian', 'Varis', 'Galinndan', 'Ivellos', 'Immeral\'', 'Karrick', 'Kuarion', 'Lausian', 'Mindratis', 'Paelias', 'Peren', 'Riardon', 'Rolen', 'Soveliss', 'Tamiorn', 'Tarivol', 'Teren', 'Hadaray', 'Himo', 'Hayan', 'Enialis', 'Erdan', 'Erevan',
    'Adriye', 'Altea', 'Anastrianna', 'Andraste', 'Antinua', 'Betrinna', 'Birel\'', 'Vadania', 'Valante', 'Jelenett', 'Drusillia', 'Yelenia', 'Kaelinn', 'Kvelenna', 'Kvilasi', 'Keylet', 'Ksanafia', 'Leshanna', 'Lia', 'Mialli', 'Meriel\'', 'Naivara', 'Sariel\'', 'Silakvi', 'Teirastra', 'Tia', 'Felosial\'', 'Shava', 'Shanayra', 'Enna',
    'Amakiir (sparkling flower)', 'Amastasia (star flower)', 'Galanodel\' (lunar whisp)', 'Il\'felkir (blazing bud)', 'Ksilosent (golden petal)', 'Liadon (silver leaf)', 'Nailo (nighty breeze)', 'Sianodel\' (lunar stream)', 'Holimion (Diamond dew)']

names_halfling = ['Al\'ton', 'Ander', 'Garret', 'Keid', 'Korrin', 'Lail', 'Lindal', 'Mailo', 'Merrik', 'Osborn', 'Perrin', 'Reed', 'Rosko', 'Uellby', 'Finnan', 'Eldon', 'Errih',
    'Bri', 'Vani', 'Verna', 'Jillian', 'Kitri', 'Kora', 'Kelly', 'Lavinia', 'Lidda', 'Merla', 'Nedda', 'Paela', 'Portia', 'Serafina', 'Trim', 'Shaena', 'Endry', 'Ufermia']

todo('add human other names')
names_human = ['Ivor', 'Bor', 'Gler', 'Grigor', 'Igan', 'Kozef', 'Mival\'', 'Orel', 'Pavel', 'Sergor', 'Fodel\'',
    'Aletra', 'Zora', 'Kara', 'Katerin', 'Mara', 'Natali', 'Ol\'ma', 'Tana',
    'Bersk', 'Dotsk', 'Kulenov', 'Marsk', 'Nemeck', 'Starag', 'Chernin', 'Shemov']

todo('add dragonborn other names')
names_dragonborn = ['Ardjhan', 'Balazar', 'Bharash', 'Ghesh', 'Donnar', 'Kriv', 'Medrash', 'Mehen', 'Nadarr', 'Pandjed', 'Patrin', 'Rhogar', 'Tarhun', 'Torrinn', 'Heskan', 'Shamash', 'Shedinn',
    'Akra', 'Biri', 'Daar', 'Djheri', 'Kawa', 'Korinn', 'Mis-hann (not sh but s-h)', 'Nala', 'Perra', 'Rayann', 'Sora', 'Surina', 'Thava', 'Uadjitt', 'Faride', 'Havilar', 'Harann']

todo('add gnome other names')
names_gnome = ['Alvin', 'Alston', 'Boddinok', 'Brok', 'Burgel', 'Varrin', 'Vrenn', 'Gerbo', 'Gimbl', 'Glim', 'Jebeddo', 'Dimbl', 'Zuk', 'Kellen', 'Namfuld', 'Orrin', 'Rundar', 'Sibo', 'Sindri', 'Fonkin', 'Frug', 'Eldon', 'Erki',
    'Bimpnottin', 'Brina', 'Veyouket', 'Donella', 'Duvamil', 'Zanna', 'Karamip', 'Karlin', 'Lilli', 'Lorilla', 'Lupmottin', 'Madnab', 'Nix', 'Nissa', 'Oda', 'Orla', 'Royvin', 'Tana', 'Shamil', 'Elevik', 'Elijobell', 'Ella']
    
names_halfelf = names_elf + names_human

names_halfork = ['Gel', 'Dench', 'Imsh', 'Ket', 'Krask', 'Murret', 'Ront', 'Tokk', 'Feng', 'Henk', 'Holg', 'Shamp',
    'Evalda', 'Kansif', 'Mev', 'Higa', 'Ovak', 'Ounka', 'Suta', 'Shauta', 'Emen', 'Engong']
    
todo('add tiefling other names')
names_tiefling = ['Akmenos', 'Ammon', 'Barakas', 'Damakos', 'Yados', 'Kayron', 'Lucis', 'Meleh', 'Morday', 'Mortos', 'Pelayos', 'Skamos', 'Teray', 'Ekemon',
    'Akta', 'Anakis', 'Briseis', 'Damaya', 'Kallista', 'Kriella', 'Lerissa', 'Makaria', 'Nemeya', 'Orianna', 'Rieta', 'Felaya', 'Ea']



aligments = ['Lawful good', 'Neutral good', 'Chaotic good', 'Lawful neutral', 'True neutral', 'Chaotic neutral', 'Lawful evil', 'Neutral evil', 'Chaotic evil']

heights = ['Very small', 'Small', 'A bit small', 'Avarage', 'A bit high', 'High', 'Very high']

body_types = ['Very thick', 'Thick', 'A bit thick', 'Avarage', 'A bit thin', 'Thin', 'Very thin']

clothes = ['Very rich', 'Rich', 'Richer than avarage', 'Avarage', 'Less rich than avarage', 'Poor', 'Very poor']

clothes_color = \
'''
Mellow yellow, Cyber yellow, Royal yellow, Banana yellow, Tuscany yellow, Lemon yellow, Bumblebee yellow, Cream yellow, Peach yellow, Laguna yellow, Mustard yellow, Corn yellow, Pineapple yellow, Flaxen yellow, Eggnog yellow, Trombone yellow, Flax yellow, Ecru yellow, Sepia yellow,

Gold orange, Goldenrod orange, Pumpkin orange, Fire orange, Ochre orange, Burnt orange, Dijon orange, Tangerine orange, Tiger orange, Honey orange, Carrot orange, Amber orange, Apricot orange, Bronze orange, Cider orange, Clay orange, Rust orange, Amber orange, Spice orange,

Salmon red, Scarlet red, Barn red, Imperial red, Indian red, Chili red, Fire brick Red, Maroon red, Redwood red, Raspberry red, Candy apple red, Ferrari red, Persian red, US Flag red, Carmine red, Burgundy red, Crimson red, Sangria red, Mahogany red,

Ruby pink, Ultra pink, Thulian pink, Magenta, Rose pink, Lavender pink, Creamy pink, FuchsIa, French rose, Cerise pink, Carnation pink, Brick pink, Amaranth pink, Taffy pink,Bubble Gum pink, Hot Pink, Punch pink, Lemonade pink, Flamingo pink,

Hibiscus violet, Mauve violet, Fandango violet,

Lavender violet, Orchid violet, Lilac violet, Electric violet, African violet, Grape violet, Amethyst violet, Byzantine violet, Helio Violet, Floral violet, Thistle violet, Orchid violet, Plum violet, Eggplant violet, Lollipop violet, Royal violet, Mulberry violet,

Yale blue, Pigeon blue, Sky blue, Independence blue, Air force blue, Baby blue, Navy blue, Steel blue, Carolina blue, Turkish blue, Maybe blue, Cornflower blue, Olympic blue, Sapphire blue, Azure blue, Egyptian blue, Denim blue, Prussian blue, Space blue,

Forest green, Sage green, Olive green, Lime green, Hunter green, Jade green, Artichoke green, Fern green, Jungle green, Laurel green, Moss green, Mint green, Pine green, Tea green, Army green, Emerald green, Kelly green, Sacramento green, Sea green,

Cedar brown, Cinnamon brown, Brunette brown, Mocha brown, Umber brown, Tortilla brown, Chocolate brown, Syrup brown, Gingerbread brown, Caramel brown, Walnut brown, Pecan brown, Wood brown, Hickory brown, Espresso brown, Peanut brown, Tawny brown, Coffee brown, Russet brown,

Fossil gray, Mink gray, Pearl gray, Abalone gray, Harbor gray, Smoke gray, Thunder gray, Pewter gray, Steel gray, Stone gray, Iron gray, Rhino gray, Trout gray, Seal gray, Lava gray, Shadow gray, Ash gray, Anchor gray, Charcoal gray
'''.replace('\n', ' ') \
    .replace('  ', ' ') \
    .replace(', ', ',') \
    .split(',')





# this super class over different races
class Char:
    name = None
    race = None
    class_ = None
    history = None
    aligment = None
    
    money = None
    
    body_type = None
    height = None
    clothes = None
    clothes_color = None
    
    def __init__ (self):
        self.race = rnd.choice(races)
        self.class_ = rnd.choice(classes)
        self.aligment = rnd.choice(aligments)
        
        self.body_type = rnd.choice(body_types)
        self.height = rnd.choice(heights)
        self.clothes = rnd.choice(clothes)
        self.clothes_color = rnd.choice(clothes_color)
        
        names = ['No names for this race']
        if self.race == 'Dwarf':
            names = names_dwarf
        elif self.race == 'Elf':
            names = names_elf
        elif self.race == 'Halfling':
            names = names_halfling
        elif self.race == 'Dragonborn':
            names = names_dragonborn
        elif self.race == 'Gnome':
            names = names_gnome
        elif self.race == 'Halfelf':
            names = names_halfelf
        elif self.race == 'Halfork':
            names = names_halfork
        elif self.race == 'Tiefling':
            names = names_tiefling
        self.name = rnd.choice(names)

        money_dice = '0d4'
        if self.class_ == 'Bard':
            money_dice = '5d4'
        elif self.class_ == 'Barbarian':
            money_dice = '2d4'
        elif self.class_ == 'Warrior':
            money_dice = '5d4'
        elif self.class_ == 'Wizard':
            money_dice = '4d4'
        elif self.class_ == 'Druid':
            money_dice = '2d4'
        elif self.class_ == 'Priest':
            money_dice = '5d4'
        elif self.class_ == 'Warlock':
            money_dice = '4d4'
        elif self.class_ == 'Monk':
            money_dice = '1d2'
        elif self.class_ == 'Paladin':
            money_dice = '5d4'
        elif self.class_ == 'Rogue':
            money_dice = '4d4'
        elif self.class_ == 'Ranger':
            money_dice = '5d4'
        elif self.class_ == 'Magician':
            money_dice = '3d4'
        self.money = 10*roll(money_dice)


    
    def to_str (self):
        res = '''
            name: {}
            race: {}
            class: {}
            aligment: {}
            
            money: {}
            
            height: {}
            body_type: {}
            clothes: {}
            clothes_color: {}
        '''.format(self.name, self.race, self.class_, self.aligment, self.money, self.height, self.body_type, self.clothes, self.clothes_color)
        
        return res





def roll (exp):
    dices, dice_size = exp.split('+')[0].split('d')
    
    roll_bonus = exp.split('+')[1] if '+' in exp else 0
    
    dices = int(dices)
    dice_size = int(dice_size)
    roll_bonus = int(roll_bonus)
    
    #print('dices={}, dice_size={}, roll_bonus={}'.format(dices, dice_size, roll_bonus))
    
    res = 0
    for _ in range(dices):
        res += rnd.randint(1, dice_size)
    
    return res + roll_bonus





def main ():
    dice = '1d20'

    for _ in range(10):
        print(dice, '->', roll(dice))
    
    for _ in range(20):
        print(Char().to_str()+'\n')
        
    # return 0
    
    should_exit = False
    while not should_exit:
        print('What you wanna do?')
        print('    NdX+B -> roll dice: just input 3d6+1 for example')
        print('    c -> create random char')
        print('    exit -> exit program')
        print()
        
        action = input()
        # action = 'exit'
        
        if action == 'exit':
            # todo('exit')
            print('Exiting...')
            sys.exit(0)
        
        elif action == 'c':
            print('Here is random character:')
            print(Char().to_str()+'\n')
            
        else:
            try:
                print(roll(action))
            except:
                print('Sorry, i dont understand what you want')
        
        print('\n')
        




if __name__ == '__main__':
    main()



