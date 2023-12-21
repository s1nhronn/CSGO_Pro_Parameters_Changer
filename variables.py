# coding=windows-1251
"""
Файл с переменными
"""

description_en = ['Maximum number of ammo',
                  'How long it takes for the weapon to fully restore accuracy. This only works after you '
                  'release the LMB (while sitting).',
                  'How long it takes for the weapon to fully restore accuracy. This only works after you '
                  'release the LMB (while sitting).',
                  'How long it takes for the weapon to fully restore accuracy. This only works after you '
                  'release the LMB (in a stationary position).',
                  'How long it takes so that the weapon fully restores accuracy. This works after you '
                  'release'
                  ' the LMB (In a stationary position).',
                  'Initial inaccuracy of jump shooting. The lower the number, the more accurate the shot.',
                  'Inaccuracy of shooting while jumping. The lower the number, the more accurate the '
                  'shot.',
                  'Maximum player speed (max 250).',
                  'Automatic shooting (0 means not automatic shooting).',
                  'The cost of the weapon.',
                  'Armor ratio is how effective a weapon is against armored opponents. Numbers equal to '
                  'or '
                  'greater than 2 completely ignore armor, and numbers less than 1 first remove armor, '
                  'and '
                  'then HP.',
                  'Damage.', 'Shot range.',
                  'Number of bullets fired (max 9).', 'Fire rate.',
                  'The number of inaccuracies of the weapon as a whole. The lower the number, the more '
                  'accurate the shot.',
                  'Inaccuracy of shooting while sitting. The lower the number, the more accurate the '
                  'shot.',
                  'Inaccuracy of shooting in a stationary position. The lower the number, the more '
                  'accurate '
                  'the shot.',
                  'Inaccuracy of shooting on the ground. The lower the number, the more accurate the '
                  'shot.',
                  'Inaccurate shooting on the stairs. The lower the number, the more accurate the shot.',
                  'Inaccurate shooting. The lower the number, the more accurate the shot.',
                  'Inaccuracy of shooting while moving. The lower the number, the more accurate the shot.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Number of rounds in the clip.',
                  'Inaccuracy of shooting while sitting. The lower the number, the more accurate the '
                  'shot.',
                  'Inaccurate shooting. The lower the number, the more accurate the shot.',
                  'Inaccurate shooting while jumping. The lower the number, the more accurate the shot.',
                  'Inaccuracy of shooting on the stairs. The lower the number, the more accurate the '
                  'shot.',
                  'Inaccuracy of shooting on the ground. The lower the number, the more accurate the '
                  'shot.',
                  'Inaccuracy of shooting while moving. The lower the number, the more accurate the shot.',
                  'Inaccuracy of shooting in a stationary position. The lower the number, the more '
                  'accurate '
                  'the shot.',
                  'Maximum player speed (max 250).',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.',
                  'Recoil. The number "0" removes recoil.', ]

description_ru = ['Максимальное количество патронов.',
                  'Сколько времени требуется, чтобы оружие полностью восстановило точность. Это работает '
                  'только после того, как вы отпустите Лкм. -Ha Ctrl.',
                  'Сколько времени требуется, чтобы оружие полностью восстановило точность. Это работает '
                  'только после того, как вы отпустите Лкм. -Ha Ctrl.',
                  'Сколько времени требуется, чтобы оружие полностью восстановило точность. Это работает '
                  'только после того, как вы отпустите Лкм -В неподвижном положении.',
                  'Сколько времени требуется, чтобы оружие полностью восстановило точность. Это работает '
                  'после того, как вы отпустите Лкм - В неподвижном положении.',
                  'Первоначальная неточность стрельбы в прыжке. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в прыжке. Чем меньше число, тем точнее выстрел.',
                  'Максимальная скорость игрока (max 250).',
                  'Автоматическая стрельба (0 - не автоматическая, 1 - автоматическая).',
                  'Стоимость оружия.',
                  'Коэффициент брони - это то, насколько эффективно оружие против бронированных '
                  'противников. Числа, равные или больше 2, полностью игнорируют броню, а числа меньше 1 '
                  'сначала снимают броню, а потом HP.',
                  'Урон.',
                  'Дальность выстрела.',
                  'Кол-во выстреливаемых пуль (Max9).',
                  'Скорость стрельбы.',
                  'Число неточности оружия в целом. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы на Ctrl. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в неподвижном положении. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы на земле. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы на лестнице. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в движении. Чем меньше число, тем точнее выстрел.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Кол-во патронов в обойме.',
                  'Неточность стрельбы на Ctrl. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в прыжке. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы на лестнице. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы на земле. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в движении. Чем меньше число, тем точнее выстрел.',
                  'Неточность стрельбы в неподвижном положении. Чем меньше число, тем точнее выстрел.',
                  'Максимальная скорость игрока. (max 250).',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.',
                  'Отдача. Число "0" убирает отдачу.']

# noinspection SpellCheckingInspection
weapons_format = {'P2000': 'weapon_hkp2000_prefab',
                  'USP-S': 'weapon_usp_silencer_prefab',
                  'GLOCK-18': 'weapon_glock_prefab',
                  'DUAL BERETTAS': 'weapon_elite_prefab',
                  'P250': 'weapon_p250_prefab',
                  'FIVE-SEVEN': 'weapon_fiveseven_prefab',
                  'TEC-9': 'weapon_tec9_prefab',
                  'CZ75-AUTO': 'weapon_cz75a_prefab',
                  'DESERT EAGLE': 'weapon_deagle_prefab',
                  'REVOLVER R8': 'weapon_revolver_prefab',
                  'NOVA': 'weapon_nova_prefab',
                  'XM1014': 'weapon_xm1014_prefab',
                  'MAG-7': 'weapon_mag7_prefab',
                  'SAWED-OFF': 'weapon_sawedoff_prefab',
                  'M249': 'weapon_m249_prefab',
                  'NEGEV': 'weapon_negev_prefab',
                  'MAC-10': 'weapon_mac10_prefab',
                  'MP9': 'weapon_mp9_prefab',
                  'MP7': 'weapon_mp7_prefab',
                  'MP5-SD': 'weapon_mp5sd_prefab',
                  'UMP-45': 'weapon_ump45_prefab',
                  'P90': 'weapon_p90_prefab',
                  'PP-19 BISON': 'weapon_bizon_prefab',
                  'FAMAS': 'weapon_famas_prefab',
                  'AUTOMATIC "GALIL"': 'weapon_galilar_prefab',
                  'M4A1-S': 'weapon_m4a1_silencer_prefab',
                  'AK-47': 'weapon_ak47_prefab',
                  'M4A4': 'weapon_m4a1_prefab',
                  'AUG': 'weapon_aug_prefab',
                  'SG 553': 'weapon_sg556_prefab',
                  'SSG 08': 'weapon_ssg08_prefab',
                  'AWP': 'weapon_awp_prefab',
                  'SCAR-20': 'weapon_scar20_prefab',
                  'G3SG1': 'weapon_g3sg1_prefab'
                  }

# noinspection SpellCheckingInspection
csgo_russian = {
    'P2000': ['\t\t"SFUI_WPNHUD_HKP2000"\t\t"P2000"\n'],
    'USP-S': ['\t\t"SFUI_WPNHUD_USP_SILENCER"\t"USP-S"\n'],
    'Glock-18': ['\t\t"SFUI_WPNHUD_Glock18"\t\t"Glock-18"\n'],
    'Dual Berettas': ['\t\t"SFUI_WPNHUD_Elites"\t\t"Dual Berettas"\n',
                      '\t\t"SFUI_WPNHUD_Elite"\t\t\t"Dual Berettas"\n'],
    'P250': ['\t\t"SFUI_WPNHUD_P250"\t\t\t"P250"\n'],
    'Five-SeveN': ['\t\t"SFUI_WPNHUD_FiveSeven"\t\t"Five-SeveN"\n'],
    'Tec-9': ['\t\t"SFUI_WPNHUD_Tec9"\t\t\t"Tec-9"\n'],
    'CZ75-Auto': ['\t\t"SFUI_WPNHUD_CZ75"\t\t\t"CZ75-Auto"\n'],
    'Desert Eagle': ['\t\t"SFUI_WPNHUD_DesertEagle"\t"Desert Eagle"\n',
                     '\t\t"SFUI_WPNHUD_Deagle"\t\t"Desert Eagle"\n'],
    'Revolver R8': ['\t\t"SFUI_WPNHUD_REVOLVER"\t\t"Револьвер R8"\n'],
    'Nova': ['\t\t"SFUI_WPNHUD_Nova"\t\t\t"Nova"\n'],
    'XM1014': ['\t\t"SFUI_WPNHUD_xm1014"\t\t"XM1014"\n'],
    'MAG-7': ['\t\t"SFUI_WPNHUD_Mag7"\t\t\t"MAG-7"\n'],
    'Sawed-Off': ['\t\t"SFUI_WPNHUD_Sawedoff"\t\t"Sawed-Off"\n'],
    'M249': ['\t\t"SFUI_WPNHUD_M249"\t\t\t"M249"\n'],
    'Negev': ['\t\t"SFUI_WPNHUD_Negev"\t\t\t"Негев"\n'],
    'MAC-10': ['\t\t"SFUI_WPNHUD_MAC10"\t\t\t"MAC-10"\n'],
    'MP9': ['\t\t"SFUI_WPNHUD_MP9"\t\t\t"MP9"\n'],
    'MP7': ['\t\t"SFUI_WPNHUD_MP7"\t\t\t"MP7"\n'],
    'MP5-SD': ['\t\t"SFUI_WPNHUD_MP5SD"\t\t\t"MP5-SD"\n'],
    'UMP-45': ['\t\t"SFUI_WPNHUD_UMP45"\t\t\t"UMP-45"\n'],
    'P90': ['\t\t"SFUI_WPNHUD_P90"\t\t\t"P90"\n'],
    'PP-19 Bison': ['\t\t"SFUI_WPNHUD_Bizon"\t\t\t"ПП-19 «Бизон»"\n'],
    'FAMAS': ['\t\t"SFUI_WPNHUD_Famas"\t\t\t"FAMAS"\n'],
    'Automatic "Galil"': ['\t\t"SFUI_WPNHUD_GalilAR"\t\t"Автомат «Галиль»"\n'],
    'M4A1-S': ['\t\t"SFUI_WPNHUD_M4_SILENCER"\t"M4A1-S"\n', '\t\t"SFUI_WPNHUD_M4A1_silencer"\t"M4A1-S"\n'],
    'AK-47': ['\t\t"SFUI_WPNHUD_AK47"\t\t\t"AK-47"\n'],
    'M4A4': ['\t\t"SFUI_WPNHUD_M4A1"\t\t\t"M4A4"\n'],
    'AUG': ['\t\t"SFUI_WPNHUD_Aug"\t\t\t"AUG"\n'],
    'SG 553': ['\t\t"SFUI_WPNHUD_SG556"\t\t\t"SG 553"\n'],
    'SSG 08': ['\t\t"SFUI_WPNHUD_SSG08"\t\t\t"SSG 08"\n'],
    'AWP': ['\t\t"SFUI_WPNHUD_AWP"\t\t\t"AWP"\n'],
    'SCAR-20': ['\t\t"SFUI_WPNHUD_SCAR20"\t\t"SCAR-20"\n'],
    'G3SG1': ['\t\t"SFUI_WPNHUD_G3SG1"\t\t\t"G3SG1"\n'],
}

# noinspection SpellCheckingInspection
csgo_english = {
    'P2000': ['\t\t"SFUI_WPNHUD_HKP2000"\t\t"P2000"\n'],
    'USP-S': ['\t\t"SFUI_WPNHUD_USP_SILENCER"\t"USP-S"\n'],
    'Glock-18': ['\t\t"SFUI_WPNHUD_Glock18"\t\t"Glock-18"\n'],
    'Dual Berettas': ['\t\t"SFUI_WPNHUD_Elites"\t\t"Dual Berettas"\n',
                      '\t\t"SFUI_WPNHUD_Elite"\t\t\t"Dual Berettas"\n'],
    'P250': ['\t\t"SFUI_WPNHUD_P250"\t\t\t"P250"\n'],
    'Five-SeveN': ['\t\t"SFUI_WPNHUD_FiveSeven"\t\t"Five-SeveN"\n'],
    'Tec-9': ['\t\t"SFUI_WPNHUD_Tec9"\t\t\t"Tec-9"\n'],
    'CZ75-Auto': ['\t\t"SFUI_WPNHUD_CZ75"\t\t\t"CZ75-Auto"\n'],
    'Desert Eagle': ['\t\t"SFUI_WPNHUD_DesertEagle"\t"Desert Eagle"\n',
                     '\t\t"SFUI_WPNHUD_Deagle"\t\t"Desert Eagle"\n'],
    'Revolver R8': ['\t\t"SFUI_WPNHUD_REVOLVER"\t\t"R8 Revolver"\n'],
    'Nova': ['\t\t"SFUI_WPNHUD_Nova"\t\t\t"Nova"\n'],
    'XM1014': ['\t\t"SFUI_WPNHUD_xm1014"\t\t"XM1014"\n'],
    'MAG-7': ['\t\t"SFUI_WPNHUD_Mag7"\t\t\t"MAG-7"\n'],
    'Sawed-Off': ['\t\t"SFUI_WPNHUD_Sawedoff"\t\t"Sawed-Off"\n'],
    'M249': ['\t\t"SFUI_WPNHUD_M249"\t\t\t"M249"\n'],
    'Negev': ['\t\t"SFUI_WPNHUD_Negev"\t\t\t"Negev"\n'],
    'MAC-10': ['\t\t"SFUI_WPNHUD_MAC10"\t\t\t"MAC-10"\n'],
    'MP9': ['\t\t"SFUI_WPNHUD_MP9"\t\t\t"MP9"\n'],
    'MP7': ['\t\t"SFUI_WPNHUD_MP7"\t\t\t"MP7"\n'],
    'MP5-SD': ['\t\t"SFUI_WPNHUD_MP5SD"\t\t\t"MP5-SD"\n'],
    'UMP-45': ['\t\t"SFUI_WPNHUD_UMP45"\t\t\t"UMP-45"\n'],
    'P90': ['\t\t"SFUI_WPNHUD_P90"\t\t\t"P90"\n'],
    'PP-19 Bison': ['\t\t"SFUI_WPNHUD_Bizon"\t\t\t"PP-Bizon"\n'],
    'FAMAS': ['\t\t"SFUI_WPNHUD_Famas"\t\t\t"FAMAS"\n'],
    'Automatic "Galil"': ['\t\t"SFUI_WPNHUD_GalilAR"\t\t"Galil AR"\n'],
    'M4A1-S': ['\t\t"SFUI_WPNHUD_M4_SILENCER"\t"M4A1-S"\n',
               '\t\t"SFUI_WPNHUD_M4A1_silencer"\t"M4A1-S"\n'],
    'AK-47': ['\t\t"SFUI_WPNHUD_AK47"\t\t\t"AK-47"\n'],
    'M4A4': ['\t\t"SFUI_WPNHUD_M4A1"\t\t\t"M4A4"\n'],
    'AUG': ['\t\t"SFUI_WPNHUD_Aug"\t\t\t"AUG"\n'],
    'SG 553': ['\t\t"SFUI_WPNHUD_SG556"\t\t\t"SG 553"\n'],
    'SSG 08': ['\t\t"SFUI_WPNHUD_SSG08"\t\t\t"SSG 08"\n'],
    'AWP': ['\t\t"SFUI_WPNHUD_AWP"\t\t\t"AWP"\n'],
    'SCAR-20': ['\t\t"SFUI_WPNHUD_SCAR20"\t\t"SCAR-20"\n'],
    'G3SG1': ['\t\t"SFUI_WPNHUD_G3SG1"\t\t\t"G3SG1"\n'],
}
